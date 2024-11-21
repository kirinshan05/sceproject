from django.urls import path
from .import views

app_name = 'sceapp'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('sce-detail<int:pk>/',
        views.SceDetail.as_view(),
        name='sce-detail'
    ),
    path(
        'hobby-list/',
        views.HobbyViews.as_view(),
        name='hobby_list'
    ),
    path(
        'study-list/',
        views.StudyViews.as_view(),
        name='study_list'
    ),
    path(
        'other-list/',
        views.OtherViews.as_view(),
        name='other_list'
    ),
    path(
        'contact/',
        views.ContactView.as_view(),
        name='contact'
    ),
    
    

]
