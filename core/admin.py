from django.contrib import admin
from .models import CodeSnippet, Tag 

# Register your models here.

admin.site.register(CodeSnippet)
admin.site.register(Tag)
