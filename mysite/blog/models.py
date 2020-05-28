from django.db import models
from django.urls import reverse

# Create your models here.
class posts(models.Model):
    title=models.CharField(max_length=200,unique=True)
    author=models.CharField(max_length=200)
    created_on=models.DateField(auto_now_add=True)
    content=models.TextField()
    updated_on=models.DateField(auto_now=True)
    image=models.ImageField(upload_to='images/')
    auth_image=models.ImageField(upload_to='images/')
    abt_auth=models.CharField(max_length=300)
    image2=models.ImageField(upload_to='images/')
    image3=models.ImageField(upload_to='images/')
    content2=models.TextField()
    content3=models.TextField()
    class Meta:
        ordering=['-created_on']
    
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        #Returns the url to access a detail record for this book."""
        return reverse('post_detail', args=[str(self.id)])
    objects = models.Manager()
