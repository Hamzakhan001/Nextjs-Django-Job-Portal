from django.urls import path
from . import views


urlpatterns = [
	path('jobs/',views.getAllJobs,name='jobs'),
 	path('job/new/',views.new_job,name='new_job'),
  	path('job/<str:pk>/',views.getJob,name='job'),
    path('job/<str:pk>/update/',views.update,name='update_job'),
    path('job/<str:pk>/delete/',views.deleteJob,name='delete_job'),
    path('stats/<str:topic>/',views.getTopicStats,name='topic_stats'),
]
