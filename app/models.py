from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.pk})

class Mechanics(models.Model):
    mechanic_name = models.CharField(primary_key=True, max_length=50)
    body = models.TextField(blank=True)

    def __str__(self):
        return self.mechanic_name

class Owners(models.Model):
    name = models.CharField(max_length=50)
    motorcycle = models.CharField(max_length=50)
    body = models.TextField()
    mechanic = models.ForeignKey(Mechanics, on_delete=models.SET_NULL, null=True, blank=True, related_name='owners')

    def __str__(self):
        return self.name

class Category(models.Model):
    brand_name = models.CharField(max_length=50, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()

    def __str__(self):
        return self.brand_name

class ServiceHistory(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    owner = models.ForeignKey(Owners, on_delete=models.CASCADE, related_name='service_histories')

    def __str__(self):
        return self.title

class NextServiceAppointment(models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    body = models.TextField()
    owner = models.ForeignKey(Owners, on_delete=models.CASCADE, related_name='next_service_appointments')
    service_history = models.ForeignKey(ServiceHistory, on_delete=models.CASCADE, related_name='next_service_appointments', null=True, blank=True)

    def __str__(self):
        return self.title

class OwnerProfile(models.Model):
    owner = models.OneToOneField(Owners, on_delete=models.CASCADE, related_name='profile')
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=15)

    def __str__(self):
        return f"{self.owner.name}'s Profile"

class ServiceCategory(models.Model):
    service = models.ForeignKey(ServiceHistory, on_delete=models.CASCADE, related_name='service_categories')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='service_categories')

    def __str__(self):
        return f"{self.service.title} - {self.category.brand_name}"