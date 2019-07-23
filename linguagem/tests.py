from django.test import TestCase
from .models import Linguagem
#from django.linguagem.urlresolvers import reverse
from django.contrib.auth.models import User
import unittest
from django.test.client import Client

# ==> Comentar nas Views #@login_required para rodar os testes
# Create your tests here.


class SimpleTest(unittest.TestCase):
    def setUp(self):
        # Cada teste precisa de um cliente.
        self.client = Client()


    def test_login(self):
            # Faz uma requisição POST.
            response = self.client.post('/login/', {'username': 'Admin2', 'password': 'admin222'})
            self.failUnlessEqual(response.status_code, 200)

            # Verifica se a resposta foi 200 OK.
            self.failUnlessEqual(response.status_code, 200)

    def test_logout(self):
            response = self.client.get('/logout/')

            # Verifica se a resposta foi 200 OK.
            self.failUnlessEqual(response.status_code, 200)

    def test_list(self):
            response = self.client.get('/linguagem/list/')

            # Verifica se a resposta foi 200 OK.
            self.failUnlessEqual(response.status_code, 200)

    def test_baixar(self):
            response = self.client.get('/linguagem/baixar/')

            # Verifica se a resposta foi 200 OK.
            self.failUnlessEqual(response.status_code, 200)

    def test_getrepos(self):
            response = self.client.get('/linguagem/getrepos/')

            # Verifica se a resposta foi 200 OK.
            self.failUnlessEqual(response.status_code, 200)

    def test_new(self):
            response = self.client.get('/linguagem/new/')

            # Verifica se a resposta foi 200 OK.
            self.failUnlessEqual(response.status_code, 200)


    if __name__ == '__main__':
        unittest.main()






