from django.urls import path
from . import views

urlpatterns = [
  path('', views.home, name='home'),
  path('about/', views.about, name='about'),
  path('faces/', views.faces_index, name='index'),
  # path('camera_feed', views.camera_feed, name='camera_feed')    
  path('faces/<int:face_id>/', views.faces_detail, name="detail"),
  path('faces/create/', views.FaceCreate.as_view(), name='faces_create'),
  # pk is what the django views is expecting as a param if we need one, which is short for primary key
  # aka the face_id
  path('faces/<int:pk>/update/', views.FaceUpdate.as_view(), name='faces_update'),
  path('faces/<int:pk>/delete/', views.FaceDelete.as_view(), name='faces_delete'),

]