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
  path('faces/<int:face_id>/add_picture', views.add_picture, name='add_picture'),
  path('faces/<int:pk>/update/', views.FaceUpdate.as_view(), name='faces_update'),
  path('faces/<int:pk>/delete/', views.FaceDelete.as_view(), name='faces_delete'),
  path('faces/<int:face_id>/assoc_tag/<int:tag_id>/', views.assoc_tag, name='assoc_tag'),
  path('tags/', views.TagList.as_view(), name='tags_index'),
  path('tags/<int:pk>/', views.TagDetail.as_view(), name='tags_detail'),
  path('tags/create/', views.TagCreate.as_view(), name='tags_create'),
  path('tags/<int:pk>/update/', views.TagUpdate.as_view(), name='tags_update'),
  path('tags/<int:pk>/delete/', views.TagDelete.as_view(), name='tags_delete'),
  path('faces/<int:face_id>/upload_image', views.upload_picture, name='upload_picture'),
]