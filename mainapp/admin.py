from django.contrib import admin
from .models import *

admin.site.register(CategoryCourse)
admin.site.register(Course)
admin.site.register(Lesson)
admin.site.register(Schedule)
admin.site.register(ContactMessage)