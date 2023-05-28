from rest_framework import serializers
from .models import Job,CandidatesApplied





class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields='__all__'
    

class CandidatesAppliedSerializer(serializers.ModelSerializer):
    
    #relearn
    #because we need job where user has applied
    job=JobSerializer()
    
    class Meta:
        model=CandidatesApplied
        fields=('user','resume','applied_At','job')