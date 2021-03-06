"""gestao_linguagem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.urls import path, include
from linguagem import urls as linguagem_urls
from django.contrib.auth import views as auth_views
from linguagem.views import linguagens_list
from linguagem.views import get_repos_new

urlpatterns = [
       path('list/', linguagens_list, name="linguagem_list"),
       path('baixar/', get_repos_new, name="linguagem_baixar"),
       path('linguagem/', include (linguagem_urls)),
       path('admin/', admin.site.urls),
       path('login/', auth_views.LoginView.as_view(), name='login'),
       path('logout/', auth_views.LoginView.as_view(), name='logout'),
]
