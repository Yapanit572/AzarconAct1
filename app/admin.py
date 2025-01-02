from django.contrib import admin
from .models import Post, Mechanics, Owners, Category, ServiceHistory, NextServiceAppointment, OwnerProfile, ServiceCategory

admin.site.register(Post)
admin.site.register(Mechanics)
admin.site.register(Owners)
admin.site.register(Category)
admin.site.register(ServiceHistory)
admin.site.register(NextServiceAppointment)
admin.site.register(OwnerProfile)
admin.site.register(ServiceCategory)
