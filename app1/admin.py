from django.contrib import admin
from app1.models import student

# Register your models here.
class student_admin(admin.ModelAdmin):
    list_display=['std_name','std_pin']
admin.site.register(student,student_admin)
