from django.urls import include, re_path
from  assignment import views 

urlpatterns = [
    
   re_path(r'^signup/$', views.signup, name='signup'),
]