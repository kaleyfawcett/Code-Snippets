from django.db import models
from users.models import User 

class Tag(models.Model):
    tag = models.CharField(max_length=200, unique=True) 

    def __str__(self):
        return self.tag 

class CodeSnippet(models.Model): 
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name= 'codesnippets')
    title = models.CharField(max_length=250, blank=True, default= '')
    language = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    code_body = models.TextField()
    is_public = models.BooleanField(default=True)
    parent = models.ForeignKey(to ='self', on_delete=models.SET_NULL, related_name='children', null=True, blank =True)
    tags = models.ManyToManyField(to=Tag, related_name='codesnippets')

    def __str__(self):
        return self.title 
