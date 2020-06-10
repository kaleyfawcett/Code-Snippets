from django.db import models
from django.db.models import Q 
from users.models import User 

LANGUAGE_CHOICES = (
    ('HTML', 'HTML'),
    ('CSS', 'CSS'),
    ('JAVASCRIPT', 'JavaScript'),
    ('PYTHON', 'Python'),
)

class Tag(models.Model):
    tag = models.CharField(max_length=100, unique=True) 

    def __str__(self):
        return self.tag 

class CodeSnippet(models.Model): 
    user = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name= 'codesnippets')
    title = models.CharField(max_length=250, blank=True, default= '')
    language = models.CharField(max_length=100, choices=LANGUAGE_CHOICES, default='HTML')
    created_at = models.DateTimeField(auto_now_add=True)
    code_body = models.TextField()
    is_public = models.BooleanField(default=True)
    parent = models.ForeignKey(to ='self', on_delete=models.SET_NULL, related_name='children', null=True, blank =True)
    tags = models.ManyToManyField(to=Tag, related_name='codesnippets')



    def get_tag_names(self):
        tag_names = []
        for tag in self.tags.all():
            tag_names.append(tag.tag)

        return " ".join(tag_names)  

    def set_tag_names(self, tag_names):
        tag_names = tag_names.split()
        tags = []
        for tag_name in tag_names:
            tag = Tag.objects.filter(tag=tag_name).first()
            if tag is None:
                tag = Tag.objects.create(tag=tag_name)
            tags.append(tag)
        self.tags.set(tags)        


    def __str__(self):
        return self.title       

def search_snippets_for_user(user, query):
    return user.codesnippets.filter(
        Q(title__icontains=query)|Q(tags__icontains=query)).distinct()
        