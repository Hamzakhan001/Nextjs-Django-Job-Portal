from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from .models import Job,CandidatesApplied
from .serializers import JobSerializer,CandidatesAppliedSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.db.models import Min,Max,Avg
from .filters import JobsFilter
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import IsAuthenticated
from datetime import *
# Create your views here.


@api_view(['GET'])
def getAllJobs(request):
    
    filterset=JobsFilter(request.GET, queryset=Job.objects.all().order_by('id'))
    # jobs = Job.objects.all()
    
    count=filterset.qs.count()
    
    
    #Pagination
    resPerPage=2
    paginator=PageNumberPagination()
    paginator.page_size=resPerPage
    queryset = paginator.paginate_queryset(filterset.qs,request)
    
    serializer = JobSerializer(queryset, many=True)
    return Response({
        "count":count,
        'resPerPage':resPerPage,
		'jobs':serializer.data
	})
    # return Response(serializer.data)


@api_view(['GET'])
def getJob(request,pk):
    
    # job=Job.objects.filter(id=pk)
    
    #alternate of this is written below
    job=get_object_or_404(Job, id=pk)
    serializer = JobSerializer(job,many= False)
    return Response(serializer.data)

@api_view(['POST'])
def new_job(request):
    request.data['user'] = request.user
    data=request.data
    # ** =spread operator here
    job=Job.objects.create(**data)
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update(request , pk):
    job = get_object_or_404(Job, id=pk)
    
    
    if job.user != request.user:
        return Response({'message':"You can't update this job"},status=status.HTTP_403_FORBIDDEN)
    
    job.title=request.data['title']
    job.description=request.data['description']
    job.email=request.data['email']
    job.address=request.data['address']
    job.jobType=request.data['jobType']
    job.education=request.data['education']
    job.industry=request.data['industry']
    job.experience=request.data['experience']
    
    job.save()
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteJob(request,pk):
    job=get_object_or_404(Job, id=pk)
    
    if job.user != request.user:
        return Response({'message':"You can't delete this job"},status=status.HTTP_403_FORBIDDEN)
    
    job.delete()
    return Response({'message':'Job has been deleted'},status=status.HTTP_200_OK)



@api_view(['GET'])
def getTopicStats(request,topic):
    args={'title_icontains':topic}
    jobs=Job.objects.filter(**args)
    
    if len(jobs) == 0:
        return Response({'message':'No stats found for {format}'.format(topic=topic)})
    
    stats=jobs.aggregate(
		total_jobs = Count('title'),
  		avg = Avg('positions'),
		avg_salary=Avg('salary'),
		min_salary=Min('salary'),
		max_salary=Max('salary')
	)
    
    return Response(stats)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def applyToJob(request,pk):
    
    user=request.user
    job=get_object_or_404(Job,id=pk)
    
    if user.userprofile.resume == " ":
        return Response({'message':'Please upload your resume first'},status=status.HTTP_400_BAD_REQUEST)
    
    if job.lastDate < timezone.now():
        return Response({'message':'Last date is already passed'},status=status.HTTP_400_BAD_REQUEST)
    
    alreadyApplied=job.candidatesapplied_set.filter(user=user).exists()
    if alreadyApplied:
        return Response({'message':'You have already applied to this job'},status=status.HTTP_400_BAD_REQUEST)
    
    jobApplied=CandidatesApplied.objects.create(
        job=job,
        user=user,
        resume=user.userprofile.resume
    )
    
    return Response({
        'applied':True,
        'job_id':jobApplied.id
    },status=status.HTTP_200_OK)
    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def appliedJobs(request):
    args={'user_id':request.user.id}
    jobs= CandidatesApplied.objects.filter(**args)
    
    serializer=CandidatesAppliedSerializer(jobs,many=True)
    
    return Response(serializer.data)