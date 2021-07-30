from django.contrib import admin
from .models import Student, Kelas, Class_Enrollment

# Register your models here.
admin.site.register(Student)
admin.site.register(Kelas)
admin.site.register(Class_Enrollment)
