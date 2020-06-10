"""djangoscratch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from core import views as snippet_views 

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('registration.backends.simple.urls')),
    path('', snippet_views.homepage, name='homepage'),
    path('snippet/', snippet_views.display_snippets, name='display_snippets'),
    path('snippet/new/', snippet_views.new_snippets, name='new_snippets'),
    path('snippet/<int:snippet_pk>/', snippet_views.singular_snippet, name='singular_snippet'),
    path('snippet/<int:snippet_pk>/delete/', snippet_views.delete_snippet, name='delete_snippet'),
    path('snippet/<int:snippet_pk>/edit/', snippet_views.edit_snippet, name='edit_snippet'),
    path('snippet/<int:snippet_pk>/copy/', snippet_views.copy_snippet, name='copy_snippet'),
    path('snippet/search/', snippet_views.search_snippets, name='search_snippets'),
    path('snippet/<str:tag_name>/', snippet_views.view_tag, name='view_tag'),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),

        # For django versions before 2.0:
        # url(r'^__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
