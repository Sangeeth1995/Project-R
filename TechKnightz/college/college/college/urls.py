"""college URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from Students.views import login_user,project_add_view,project_view,user_register,profile_view,about_view,department_view,contact_view
from django.contrib.auth.decorators import login_required


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', login_user, name="login"),
    url(r'^project/add/$', login_required(project_add_view), name='project_add'),
    url(r'^projects/$', login_required(project_view),name='project'),
    url(r'^register/$', user_register,name='register'),
    url(r'^profile/$', login_required(profile_view),name='profile'),
    url(r'^about/', about_view, name="about"),
    url(r'^department/', department_view, name="department"),
    url(r'^contact/', contact_view, name="contact"),

]
