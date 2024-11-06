"""
URL configuration for votingproject project.

The `urlpatterns` list routes URLs to views. For more information, please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from landingPage import views as landing_views
from votingApp import views as voting_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('landingPage.urls')),  # Adjust 'landingPage' to match your actual app name
    path('voting/', include('votingApp.urls')),  # Adjust 'votingApp' to match your actual app name
    path('register/people/', landing_views.register_people, name='register_people'),
    path('register/candidate/', voting_views.register_candidate, name='register_candidate'),
    path('login/people/', landing_views.people_login, name='people_login'),
    path('login/candidates/', voting_views.candidate_login, name='candidate_login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
]
