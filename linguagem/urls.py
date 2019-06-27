from django.urls import path
from .views import linguagens_list
from .views import linguagens_new
from .views import linguagens_update
from .views import linguagens_delete
from .views import get_repos
from .views import linguagens_github_new

urlpatterns = [
    path('list/', linguagens_list, name="linguagem_list"),
    path('new/', linguagens_new, name="linguagem_new"),
    path('update/<int:id>/', linguagens_update, name="linguagens_update"),
    path('delete/<int:id>/', linguagens_delete, name="linguagens_delete"),
    path('getrepos/', get_repos, name="get_repos"),
    path('git/', linguagens_github_new, name="linguagens_github_new"),
]