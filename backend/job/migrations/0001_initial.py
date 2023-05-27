# Generated by Django 4.1.5 on 2023-05-27 12:32

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import job.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, null=True)),
                ('description', models.TextField(null=True)),
                ('email', models.EmailField(max_length=254, null=True)),
                ('address', models.CharField(max_length=100, null=True)),
                ('jobType', models.CharField(choices=[('Permanent', 'Permanent'), ('Temporary', 'Temporary'), ('Internship', 'Internship')], default='Permanent', max_length=50)),
                ('education', models.CharField(choices=[('Bachelors', 'Bachelors'), ('Masters', 'Masters'), ('Phd', 'Phd')], default='Bachelors', max_length=50)),
                ('industry', models.CharField(choices=[('Business', 'Business'), ('Information Technology', 'It'), ('Banking', 'Banking'), ('Education', 'Education'), ('Telecommunication', 'Telecommunication'), ('Others', 'Others')], default='Information Technology', max_length=50)),
                ('experience', models.CharField(choices=[('No Experience', 'No Experience'), ('1 Years', 'One Year'), ('2 Years', 'Two Year'), ('3 Years above', 'Three Year Plus')], default='1 Years', max_length=50)),
                ('salary', models.ImageField(default=1, upload_to='', validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100000000)])),
                ('company', models.CharField(max_length=100, null=True)),
                ('positions', models.IntegerField(default=1)),
                ('lastDate', models.DateTimeField(default=job.models.return_date_time_field)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]