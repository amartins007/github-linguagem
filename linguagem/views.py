from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Linguagem
from .forms import LinguagemForm
from django.http import HttpResponse
import json
import requests




@login_required
def linguagens_list(request):
    linguagens = Linguagem.objects.order_by('linguagem_name').all()
    return render(request, 'linguagem_list.html', {'linguagens': linguagens})

@login_required
def linguagens_new(request):
    form = LinguagemForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('linguagem_list')
    return render(request, 'linguagem_new.html', {'form': form})

@login_required
def linguagens_update(request, id):
    linguagem = get_object_or_404(Linguagem, pk=id)
    form = LinguagemForm(request.POST or None, request.FILES or None, instance=linguagem)

    if form.is_valid():
        form.save()
        return redirect('linguagem_list')

    return render(request, 'linguagem_update.html', {'form': form})


@login_required
def linguagens_delete(request, id):
    linguagem = get_object_or_404(Linguagem, pk=id)
    print('Metodo delete', request.method)

    if request.method == 'POST':
        linguagem.delete()
        return redirect('linguagem_list')

    return render(request, 'linguagem_delete_confirm.html', {'linguagem': linguagem})


@login_required
def get_repos_new(request):
# Preparando o Header para o acesso com a API do GitHub
    username = 'octokit'
    api_url_base = 'https://api.github.com/'
    headers = {'Content-Type': 'application/json',
               'User-Agent': 'Python Student',
               'Accept': 'application/vnd.github.v3+json.raw'}
    api_url = '{}orgs/{}/repos'.format(api_url_base, username)
    response = requests.get(api_url, headers=headers)
#Testando o retorno do acesso Status code = 200 ok
    if response.status_code == 200:
        repositories = json.loads(response.content.decode('utf-8'))
        repo_list = repositories
        v_linguagem = repositories
#Limpo o banco para buscar os daddos mais recentes do GitHub
        linguagens = Linguagem.objects.all().delete()
        j = 0
        while j < 5:
            #print('Lingua:', j, repo_list[j]['language'])
            new_lingua = ( repo_list[j]['language'])
            #print('Forks:',repo_list[j]['forks_count'])
            new_forks = ( repo_list[j]['forks_count'])
            #print('Whatches:', j, repo_list[j]['watches_count'])
            new_watches = (repo_list[j]['watchers_count'])
#Prepara os dados para gravar no banco
            form = LinguagemForm(request.POST or None, request.FILES or None)
            new_form = form.save(commit=False)
            request.method = "POST"
            new_form.linguagem_name = new_lingua
            new_form.forks = new_forks
            new_form.watches = new_watches
            new_form.save()
            j = j + 1
        else:
            pass


#Salvando no Banco de Dados as linguagens e informações dos Diretórios
        if form.is_valid():
            form.save()
            linguagens = Linguagem.objects.order_by('linguagem_name').all()
            return render(request, 'linguagem_baixar.html', {'linguagens': linguagens})
        else:
            linguagens = Linguagem.objects.order_by('linguagem_name').all()
            return render(request, 'linguagem_baixar.html', {'linguagens': linguagens})

#fim da Rotina de Gravação

        return render(request, 'list_github_teste.html', {'v_repos': v_linguagem})
        #return render (request, 'list_github_teste.html',{'v_repos': repositories})

    else:
        #print('[!] HTTP {0} calling [{1}]'.forrmat(response.status_code, api_url))
        return render(request,None)
