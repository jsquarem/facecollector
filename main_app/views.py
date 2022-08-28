from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def home(request):
  return render(request, 'index.html')

def about(request):
  return render(request, 'about.html')

def faces_index(request):
  return render(request, 'faces/index.html', { 'faces': faces })


class Face:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, age, hotness, date):
    self.name = name
    self.age = age
    self.hotness = hotness
    self.date = date

faces = [
  Face('Billy', 28, '68%', '2022-05-23'),
  Face('Samantha', 36, '82%', '2022-08-21'),
  Face('Joe', 46, '43%', '2022-07-15')
]