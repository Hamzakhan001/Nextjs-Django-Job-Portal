from django.urls import path
from . import views


urlpatterns = [
	path('jobs/',views.getAllJobs,name='jobs'),
 	path('job/new/',views.new_job,name='new_job'),
  	path('job/<str:pk>/',views.getJob,name='job'),
    path('job/<str:pk>/update/',views.update,name='update_job'),
    path('job/<str:pk>/delete/',views.deleteJob,name='delete_job'),
    path('stats/<str:topic>/',views.getTopicStats,name='topic_stats'),
    path('jobs/<str:id>/apply/',views.applyToJob,name='apply_job'),
    path('me/jobs/applied/',views.appliedJobs,name='applied_jobs'),
    path('jobs/<str:pk>/check/',views.isApplied,name='is_applied_to_job'),
    path('me/jobs/',views.getCurrentUserJobs,name='get_current_user_jobs'),
]