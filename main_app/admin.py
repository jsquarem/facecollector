from django.contrib import admin

# Register your models here.
from .models import Face, Picture

admin.site.register(Face)
admin.site.register(Picture)