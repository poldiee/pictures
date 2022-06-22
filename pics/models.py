from django.db import models

# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()

class Location(models.Model):
    name = models.CharField(max_length=60)

    def __str__(self):
        return self.name

    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()

class Image(models.Model):
    image = models.ImageField(blank=False)
    name = models.CharField(max_length=60)
    description = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey('Category', on_delete=models.DO_NOTHING,)
    location = models.ForeignKey('Location', on_delete=models.DO_NOTHING,)

    def __str__(self):
        return self.image

    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()