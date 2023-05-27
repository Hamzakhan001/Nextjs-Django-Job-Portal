from django.db import models
from django.core.validators import MinValueValidator,MaxValueValidator


class JobType(models.TextChoices):
    Permanent= 'Permanent'
    Temporary= 'Temporary'
    Internship = 'Internship'
    

class Education(models.TextChoices):
    Bachelors = 'Bachelors'
    Masters = 'Masters'
    Phd = 'Phd'

class Industry(models.TextChoices):
    Business = 'Business'
    IT = 'Information Technology'
    Banking = 'Banking'
    Education = 'Education'
    Telecommunication = 'Telecommunication'
    Others = 'Others'
    
class Experience(models.TextChoices):
    NO_EXPERIENCE='No Experience'
    ONE_YEAR='1 Years'
    TWO_YEAR='2 Years'
    THREE_YEAR_PLUS='3 Years above'
    
class Salary(models.TextChoices):
    One_Lac='One_Lac'
    Two_Lac='Two Lac'
    Two_Plus='2+'

class Job(models.Model):
    title=models.CharField(max_length=200,null=True)
    description=models.TextField(null=True)
    email= models.EmailField(null=True)
    address= models.CharField(max_length=100,null=True)
    jobType=models.CharField(max_length=10, choices= JobType.choices, default= JobType.Permanent)
    education =models.CharField(max_length=10, choices= Education.choices, default= Education.Bachelors)
    industry=models.CharField(max_length=10, choices= Industry.choices, default= Industry.IT)
    experience=models.CharField(max_length=10, choices= Experience.choices, default= Experience.ONE_YEAR)
    salary=models.ImageField(default=1, validators=[MinValueValidator(1),MaxValueValidator(100000000)])
    
    