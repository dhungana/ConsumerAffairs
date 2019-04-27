from django.test import TestCase
from django.contrib.auth.models import User
from django.test import Client
from rest_framework import status
from rest_framework.authtoken.models import Token
import json

class LoginTestCase(TestCase):
	def setUp(self):
		user1 = User.objects.create(username='user1',first_name='User1First',\
		  last_name='User1Last', email='user1@gmail.com')
		user1.set_password('P@ss1234-1')
		user1.save()
		self.user1 = user1

		user2 = User.objects.create(username='user2',first_name='User2First',\
		  last_name='User2Last', email='user2@gmail.com')
		user2.set_password('P@ss1234-2')
		user2.save()
		self.user2 = user2

	def test_users_can_login_to_get_unique_tokens(self):
		'''User can login to get unique tokens'''
		client = Client()
		response = client.post('/login/', {'username': 'user1', 'password': 'P@ss1234-1'}, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		token1 = json.loads(response.content)['token']
		_token1 = Token.objects.get(user=self.user1).key
		self.assertEqual(token1, _token1)

		response = client.post('/login/', {'username': 'user2', 'password': 'P@ss1234-2'}, format='json')
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		token2 = json.loads(response.content)['token']
		_token2 = Token.objects.get(user=self.user2).key
		self.assertEqual(token2, _token2)

		self.assertNotEqual(token1, token2)

	def test_invalid_login_cannot_get_tokens(self):
		'''Invalid loginc cannot get tokens'''
		client = Client()
		response = client.post('/login/', {'username': 'user1', 'password': 'invalidPass'}, format='json')
		self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
