"""mysite URL Configuration

The `urlpatterns` list routes URLs to controller. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function controller
    1. Add an import:  from my_app import controller
    2. Add a URL to urlpatterns:  path('', controller.home, name='home')
Class-based controller
    1. Add an import:  from other_app.controller import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import controller
from rest_framework.authtoken import views

urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('api/v1/books/<int:pk>', controller.get_delete_update_book, name='get_delete_update_puppy'),
    path('api/v1/books/all',controller.post_Books,name='post_Books'),
    path('', controller.BookList.as_view(), name='book_list'),
    path('view/', controller.BookView.as_view(), name='book_list'),
    path('new/', controller.BookCreate.as_view(), name='book_form'),
    path('view/<int:pk>', controller.BookView.as_view(), name='book_details'),
    path('edit/<int:pk>', controller.BookUpdate.as_view(), name='book_form'),
    path('delete/<int:pk>', controller.BookDelete.as_view(), name='book_confirm_delete'),
]



