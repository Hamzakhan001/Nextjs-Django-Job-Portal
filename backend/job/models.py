from django.db import models



class JobType(models.TextChoices):
    Permanent= 'Permanent'
    Temporary= 'Temporary'
    Internship = 'Internship'
    

class Education(models.TextChoices):
    Bachelors = 'Bachelors'
    Masters = 'Masters'
    Phd = 'Phd'


    

class Job(models.Model):
    title=models.CharField(max_length=200,null=True)
    description=models.TextField(null=True)
    email= models.EmailField(null=True)
    address= models.CharField(max_length=100,null=True)
    jobType=models.CharField(max_length=10, choices= JobType.choices, default= JobType.Permanent)