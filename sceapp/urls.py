from django.urls import path
from .views import Home,CreatePost,MyPost,ContactView
# from .import views


# app_name = 'sceapp'

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('create/', CreatePost.as_view(), name='create'), 
    path('contact/',ContactView.as_view(), name='contact'),        
    path('mypost/', MyPost.as_view(), name='mypost'), 
]    

