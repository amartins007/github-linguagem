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
def get_repos(request):
# Preparando o Header para o acesso com a API do GitHub
    username = 'octokit'
    api_url_base = 'https://api.github.com/'
    headers = {'Content-Type': 'application/json',
               'User-Agent': 'Python Student',
               'Accept': 'application/vnd.github.v3+json.raw'}
    api_url = '{}repos/{}/octokit.rb/languages'.format(api_url_base, username)
    response = requests.get(api_url, headers=headers)
#Testando o retorno do acesso Status code = 200 ok
    if response.status_code == 200:
        repositories = json.loads(response.content.decode('utf-8'))
        for k, v in repositories.items():
            v_linguagem = repositories.keys()

#inicio da rotina de Limpeza e Gravaçao das Linguagens no Banco
        #limpo o banco para buscar os daddos mais recentes do GitHub

        linguagens = Linguagem.objects.all().delete()

        v_repos = v_linguagem
        for v_repos in v_repos:
            form = LinguagemForm(request.POST or None, request.FILES or None)
            new_form = form.save(commit=False)
            request.method = "POST"
            new_form.linguagem_name = v_repos
            new_form.fabricante = ' '
            new_form.rank = ' '
            new_form.save()


        if form.is_valid():
            form.save()
            linguagens = Linguagem.objects.order_by('linguagem_name').all()
            return render(request, 'linguagem_list.html', {'linguagens': linguagens})
        else:
            #print('Form is Valido:', form.is_valid())
            #print('Form  do ELse:', form)
            linguagens = Linguagem.objects.order_by('linguagem_name').all()
            return render(request, 'linguagem_list.html', {'linguagens': linguagens})

#fim da Rotina de Gravação

        return render(request, 'list_github_teste.html', {'v_repos': v_linguagem})
        #return render (request, 'list_github_teste.html',{'v_repos': repositories})

    else:
        #print('[!] HTTP {0} calling [{1}]'.forrmat(response.status_code, api_url))
        return render(request,None)


@login_required
def linguagens_github_new(request):
    #v_repos=get_repos.import_data()
    #get_repos()
    v_repos = get_repos.v_linguagem.objects.all()
    form = LinguagemForm(request.POST or None, request.FILES or None)
    new_form = form.save(commit=False)

    for k, v in v_repos:
        request.method = "POST"
        new_form.linguagem_name = v_repos
        new_form.fabricante = 'Microsoft7'
        new_form.rank = '79'
        new_form.save()
    else:
        pass
        #print ('NewForm:', new_form)
    if form.is_valid():
        form.save()
        linguagens = Linguagem.objects.order_by('linguagem_name').all()
        return render(request, 'linguagem_list.html', {'linguagens': linguagens})
    else:
        #print('Form is Valido:', form.is_valid())
        #print('Form  do ELse:', form)
        return render(request, 'index.html')

@login_required
def linguagens_github_new_rodando(request):
    ImportToDatabase.import_data()
    form = LinguagemForm(request.POST or None, request.FILES or None)
    new_form = form.save(commit=False)
    request.method = "POST"
    new_form.linguagem_name = 'SQL2'
    new_form.fabricante = 'Microsoft2'
    new_form.rank = '77'
    new_form.save()

    if form.is_valid():
        form.save()
        linguagens = Linguagem.objects.order_by('linguagem_name').all()
        return render(request, 'linguagem_list.html', {'linguagens': linguagens})
    else:
        return render(request, 'index.html')
