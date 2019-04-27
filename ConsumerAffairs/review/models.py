from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator

class Company(models.Model):
	name = models.CharField(max_length=128)
	description = models.TextField(max_length=10000, blank=True)
	url = models.URLField(blank=True)

	def __str__(self):
		return self.name

	class Meta:
		ordering = ['id']

class Review(models.Model):
	rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
	title = models.CharField(max_length=64)
	summary = models.TextField(max_length=10000)
	ip_address = models.CharField(max_length=45)
	submitted_date = models.DateField()
	company = models.ForeignKey(Company, on_delete=models.CASCADE)
	reviewer = models.ForeignKey(User, on_delete=models.CASCADE)

	def __str__(self):
		return self.title
		
	class Meta:
		ordering = ['id']

