from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import CodeSnippet
from .models import Tag
from .forms import SnippetForm, TagForm

def homepage(request):
    if request.user.is_authenticated:
        return redirect(to='display_snippets')
    return render(request, 'snippets/homepage.html')

@login_required
def display_snippets(request):
    snippets = request.user.snippets.all()
    form = SnippetForm(data=request.POST)
    return render (request, 'snippets/',
                {"snip_form": form,
                "snippets": snippets,})

@login_required
def new_snippets(request):
    if request.method == 'POST':
        form = SnippetForm(data=request.POST)
        if form.is_valid():
            snip = form.save(commit=False)
            snip.save()
            return redirect(to='snippets/', snippet_pk=snippet.pk)
        else:
            form = SnippetForm()
        return render(request, 'new_snippet.html', {"form": form})        
