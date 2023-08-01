from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField

# Create your models here.
class BLog(models.Model):
    # title = models.CharField(max_length=200,null=false)
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="")
    contents = RichTextField(null=False,default="")
    description = models.TextField(default="",max_length=250)
    is_active = models.BooleanField(default=True)
    is_home = models.BooleanField(default=False)
    rated = models.BooleanField(default=False)
    page_type = models.CharField(max_length=200,default="blog/partials/blog_card_2.html")
    slug_field = models.SlugField(null=False,blank=True,unique=True,db_index=True,editable=False)
    def __str__(self):
        return self.title 
    
    def save(self, *args,**kwargs):
        self.slug_field = slugify(self.title)
        super().save(*args,**kwargs)

class Referance(models.Model):
    image = models.ImageField(upload_to="")
    name = models.CharField(max_length=50,default="")
    contact = models.CharField(max_length=250)
    def __str__(self):
        return self.name
    