from django.db import models
from django.core.validators import MaxLengthValidator,MinLengthValidator
from django.utils.text import slugify
from django.urls import reverse
# Create your models here.
class Tag(models.Model):
    caption=models.CharField(max_length=50,null=True)

    def __str__(self):
        return f"{self.caption}"
    
class Author(models.Model):
    first_name=models.CharField(max_length=50,validators=[MinLengthValidator(1),])
    last_name=models.CharField(max_length=50,validators=[MinLengthValidator(1),])
    email_address=models.EmailField(max_length=254)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Post(models.Model):
    title=models.CharField(max_length=50,unique=True)
    Excerpt=models.CharField(max_length=50)
    imageName=models.CharField(max_length=512,null=True)
    date=models.DateField(auto_now=True)
    Content=models.TextField()
    author=models.ForeignKey(Author,on_delete=models.CASCADE)
    tag=models.ManyToManyField(Tag)
    slug=models.SlugField(default="",db_index=True,null=False)
    def __str__(self):
        return f"{self.title} {self.author}"
    
    def save(self,*args, **kwargs):
        self.slug=slugify(self.title)
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("model_detail",args=[self.slug])
    