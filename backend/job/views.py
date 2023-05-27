from django.shortcuts import render
from rest_framework.decorators import api_view
from .models import Job 
from .serializers import JobSerializer
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework import status
from django.db.models import Min,Max,Avg
from .filters import JobsFilter
# Create your views here.


@api_view(['GET'])
def getAllJobs(request):
    
    filterset=JobsFilter(request.GET, queryset=Job.objects.all().order_by('id'))
    
    # jobs = Job.objects.all()
    serializer = JobSerializer(filterset.qs , many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getJob(request,pk):
    
    # job=Job.objects.filter(id=pk)
    
    #alternate of this is written below
    job=get_object_or_404(Job, id=pk)
    serializer = JobSerializer(job,many= False)
    return Response(serializer.data)

@api_view(['POST'])
def new_job(request):
    data=request.data
    # ** =spread operator here
    job=Job.objects.create(**data)
    serializer = JobSerializer(job, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def update(request , pk):
    job = get_object_or_404(Job, id=pk)
    
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