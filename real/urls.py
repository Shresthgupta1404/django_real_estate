from django.contrib import admin
from django.urls import path
from estate.views import signin_form,signin_check, sign_up, create_user,uploadPics,home,about,property,propertysingle,contact,bloggrid,blogsingle,tab2




urlpatterns = [
    path('admin/', admin.site.urls),
    path('uploadFile',uploadPics),
    path('create',create_user),
    path('signin',signin_form),
    path('sign',sign_up),
    path('check',signin_check),
    path('sign/home/',home),
    path('home',home),
    path('blogsingle',blogsingle),
    path('about',about),
    path('property',property),
    path('propertysingle',propertysingle),
    path('contact',contact),
    path('bloggrid',bloggrid),
    path('tab2',tab2),
    path('',signin_form)
]
