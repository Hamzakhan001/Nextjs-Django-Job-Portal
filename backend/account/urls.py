from django.urls import path
from . import views


urlpatterns = [
	path('register/',views.register,name='resigter'),
 	path('me/',views.get_currentUser,name='current_user'),
]