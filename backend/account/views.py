from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.hashers import make_password
from .serializers import UserSerializer,SignUpSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated

#hashers are used to encrypt and save it to db



@api_view(['POST'])
def register(request):
    data=request.data
    user=SignUpSerializer(data=data)
    
    if user.is_valid():
        if not User.objects.filter(username=data['email']).exists():
            user=User.objects.create(
				first_name=data['first_name'],
				last_name=data['last_name'],
				username=data['username'],
    			email=data['email'],
				password=make_password(data['password'])
			)
            return Response({
				'message':'User created' },
				status=status.HTTP_200_OK
				)
        else:
            return Response({
				'error':'User already exists!' },
				status=status.HTTP_400_BAD_REQUEST
				)
    else:
        return Response(user.errors)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_currentUser(request):
    user=request.user
     
    user= UserSerializer(user)
    return Response(user.data)