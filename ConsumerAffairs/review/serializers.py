from .models import Review, Company
from rest_framework import serializers
from django.contrib.auth.models import User

class CompanySerializer(serializers.ModelSerializer):

	class Meta:
		model = Company
		fields = ('id', 'name', 'description', 'url')

class ReviewRetrieveSerializer(serializers.ModelSerializer):
	company = CompanySerializer(many=False, read_only=True)

	class Meta:
		model = Review
		fields = ('id', 'rating', 'title', 'summary', 'submitted_date', 'company')

class ReviewCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Review
		fields = '__all__'
		read_only_fields = ('id', 'ip_address', 'submitted_date', 'reviewer')