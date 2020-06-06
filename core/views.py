from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import CodeSnippet
# from .models import Tag
from .forms import SnippetForm, TagForm

def homepage(request):
    if request.user.is_authenticated:
        return redirect(to='display_snippets')
    return render(request, 'snippets/homepage.html')

@login_required
def display_snippets(request):
    your_snippets = request.user.codesnippets.all()
    return render(request, 'snippets/display_snippets.html',
                {"snippets": your_snippets})

@login_required
def new_snippets(request):
    if request.method == 'POST':
        form = SnippetForm(data=request.POST)
        if form.is_valid():
            snippet = form.save(commit=False)
            snippet.user = request.user
            snippet.save()
        return redirect(to='singular_snippet', snippet_pk=snippet.pk)
    else:
        form = SnippetForm()
    return render(request, 'snippets/new_snippets.html', {"form": form})        

@login_required
def singular_snippet(request, snippet_pk):
    snippet = get_object_or_404(request.user.codesnippets, pk=snippet_pk)
    return render(request, "snippets/singular_snippet.html", {"snippet": snippet})    

@login_required
def delete_snippet(request, snippet_pk):
    snippet = get_object_or_404(request.user.codesnippets, pk=snippet_pk)
    if request.method == "POST":
        snippet.delete()
        return redirect(to='display_snippets')
    return render(request, "snippets/delete_snippet.html", {"snippet": snippet})   

@login_required
def edit_snippet(request, snippet_pk):
    snippet = get_object_or_404(request.user.codesnippets, pk=snippet_pk)
    if request.method == "POST":
        form = SnippetForm(instance=snippet, data=request.POST)
        if form.is_valid():
            snippet = form.save()
            return redirect(to="singular_snippet", snippet_pk=snippet.pk)
    else: 
        form = SnippetForm(instance=snippet)
    return render(request, "snippets/edit_snippet.html", {"form": form, "snippet": snippet})            




