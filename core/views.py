from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required

from .models import CodeSnippet
from .models import Tag, search_snippets_for_user
from .forms import SnippetForm

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
            snippet.set_tag_names(form.cleaned_data['tag_names'])
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
            snippet.set_tag_names(form.cleaned_data['tag_names'])
            return redirect(to="singular_snippet", snippet_pk=snippet.pk)
    else: 
        form = SnippetForm(instance=snippet, initial={"tag_names": snippet.get_tag_names()})
    return render(request, "snippets/edit_snippet.html", {"form": form, "snippet": snippet})     

@login_required
def view_tag(request, tag_name):
    tag = get_object_or_404(Tag, tag=tag_name)
    snippets = tag.codesnippets.filter(user=request.user)
    return render(request, "snippets/tag_detail.html", {"tag": tag, "snippets": snippets})           


@login_required
def search_snippets(request):
    query = request.GET.get('q')
    if query is not None:
        snippets = search_snippets_for_user(request.user, query)
    else:
        snippets = None 

    return render(request, "snippets/search_snippets.html", {"snippets": snippets, "query": query})

@login_required
def copy_snippet(request, snippet_pk):
    original_snippet = get_object_or_404(CodeSnippet, pk=snippet_pk)
    cloned_snippet = CodeSnippet(
        title=original_snippet.title + " (Copy)",
        code_body=original_snippet.code_body,
        user=request.user,
        original_snippet=original_snippet,
     ) 
    cloned_snippet.save()   
    cloned_snippet.tags.set(original_snippet.tags.all())
    return redirect(to='singular_snippet', snippet_pk=cloned_snippet.pk) 