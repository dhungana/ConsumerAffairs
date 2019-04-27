from django.test import TestCase
from django.contrib.auth.models import User
from .models import Company, Review
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

		company1 = Company.objects.create(name='Google')
		company1.save()
		self.company1 = company1

	def test_users_can_post_reviews(self):
		'''Users can post reviews with their tokens'''
		client = Client()
		response = client.post('/login/', {'username': 'user1', 'password': 'P@ss1234-1'}, format='json')
		token = json.loads(response.content)['token']

		response = client.post('/reviews/', {'rating': 5, 'company':self.company1.id, 'title':'Google is good', 
			'summary':'Google is a really good company'}, format='json', HTTP_AUTHORIZATION='Token '+token)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)


	def test_invalid_users_cannot_post_reviews(self):
		'''Users cannot post reviews with invalid tokens'''
		client = Client()
		response = client.post('/reviews/', {'rating': 5, 'company':self.company1.id, 'title':'Google is good', 
			'summary':'Google is a really good company'}, format='json', HTTP_AUTHORIZATION='Token fdlsakfjas')
		self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

	def test_users_can_list_their_reviews_only(self):
		'''Users can list their reviews and theirs only'''
		client = Client()
		response = client.post('/login/', {'username': 'user1', 'password': 'P@ss1234-1'}, format='json')
		token1 = json.loads(response.content)['token']

		response = client.post('/login/', {'username': 'user2', 'password': 'P@ss1234-2'}, format='json')
		token2 = json.loads(response.content)['token']

		response = client.get('/reviews/', HTTP_AUTHORIZATION='Token '+token1)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(json.loads(response.content)), 0)

		response = client.post('/reviews/', {'rating': 5, 'company':self.company1.id, 'title':'Google is good', 
			'summary':'Google is a really good company'}, format='json', HTTP_AUTHORIZATION='Token '+token1)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		response = client.get('/reviews/', HTTP_AUTHORIZATION='Token '+token1)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(json.loads(response.content)), 1)

		response = client.get('/reviews/', HTTP_AUTHORIZATION='Token '+token2)
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(len(json.loads(response.content)), 0)

	def test_users_can_retrieve_their_review_only(self):
		'''Users can retrieve their review and theirs only'''
		client = Client()
		response = client.post('/login/', {'username': 'user1', 'password': 'P@ss1234-1'}, format='json')
		token1 = json.loads(response.content)['token']

		response = client.post('/login/', {'username': 'user2', 'password': 'P@ss1234-2'}, format='json')
		token2 = json.loads(response.content)['token']

		response = client.post('/reviews/', {'rating': 5, 'company':self.company1.id, 'title':'Google is good', 
			'summary':'Google is a really good company'}, format='json', HTTP_AUTHORIZATION='Token '+token1)
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)

		review_id = Review.objects.get(reviewer=self.user1.id).id

		response = client.get('/reviews/' + str(review_id) + '/', HTTP_AUTHORIZATION='Token '+token1)
		self.assertEqual(response.status_code, status.HTTP_200_OK)

		response = client.get('/reviews/' + str(review_id) + '/', HTTP_AUTHORIZATION='Token '+token2)
		self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)