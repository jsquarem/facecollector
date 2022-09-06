from django.http import HttpResponse, StreamingHttpResponse
from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Face, Tag
from .forms import FaceForm, PictureForm, TagForm
import base64
import json
import time
# from django.views.decorators import gzip
import cv2
# import threading


# Create your views here.

# @gzip.gzip_page
def home(request):
    return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def faces_index(request):
  faces = Face.objects.all()
  return render(request, 'faces/index.html', { 'faces': faces })

def faces_detail(request, face_id):
  face = Face.objects.get(id=face_id)
  picture_form = PictureForm()
  tags_face_doesnt_have = Tag.objects.exclude(id__in = face.tags.all().values_list('id'))

  return render(request, 'faces/detail.html', { 'face': face, 'picture_form': picture_form, 'tags': tags_face_doesnt_have })

def add_picture(request, face_id):
  form = PictureForm(request.POST)
  if form.is_valid():
    new_picture = form.save(commit=False)
    new_picture.face_id = face_id
    new_picture.save()
  return redirect('detail', face_id=face_id)


def upload_picture(request, face_id):
  current_time = time.time()
  file_name = str(face_id) + '-' + str(current_time).replace('.','-')
  full_file_path = f'main_app/static/images/{file_name}.jpeg'
  form = json.loads(request.body)
  print(form['image'],'<-image')
  header, encoded = form['image'].split(",", 1)
  with open(full_file_path, "wb") as fh:
    # fh.write(form)
    fh.write(base64.b64decode(encoded))
  # print(form)
  # if form.is_valid():
  #   new_picture = form.save(commit=False)
  #   new_picture.face_id = face_id
  #   new_picture.save()
  return redirect('detail', face_id=face_id)

def assoc_tag(request, face_id, tag_id):
  Face.objects.get(id=face_id).tags.add(tag_id)
  return redirect('detail', face_id=face_id)

class FaceCreate(CreateView):
    model = Face
    form_class = FaceForm
    # fields = '__all__' 

class FaceUpdate(UpdateView):
    model = Face
    form_class = FaceForm
    # fields = ['age', 'hotness'] 

class FaceDelete(DeleteView):
    model = Face 
    success_url = '/faces/'

class TagList(ListView):
    model = Tag

class TagDetail(DetailView):
    model = Tag

class TagCreate(CreateView):
    model = Tag
    form_class = TagForm

class TagUpdate(UpdateView):
    model = Tag
    form_class = TagForm

class TagDelete(DeleteView):
    model = Tag
    success_url = '/tags/'












# def camera_feed(request):
#   return StreamingHttpResponse(gen(VideoCamera()), content_type="multipart/x-mixed-replace; boundary=frame")

# class VideoCamera(object):
#     def __init__(self):
#         self.video = cv2.VideoCapture(0)
#         (self.grabbed, self.frame) = self.video.read()
#         threading.Thread(target=self.update, args=()).start()

#     def __del__(self):
#         self.video.release()

#     def get_frame(self):
#         image = self.frame
#         _, jpeg = cv2.imencode('.jpg', image)
#         return jpeg.tobytes()

#     def update(self):
#         while True:
#             (self.grabbed, self.frame) = self.video.read()

# def gen(camera):
#     while True:
#         frame = camera.get_frame()
#         yield (b'--frame\r\n'
#               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')