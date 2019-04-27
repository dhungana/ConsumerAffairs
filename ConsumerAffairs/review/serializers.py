from .models import Review, Company
from rest_framework import serializers
from django.contrib.auth.models import User

class UserSerializer(serializers.ModelSerializer):

	class Meta:
		model = User
		fields = ('id', 'username', 'email', 'first_name', 'last_name')

class CompanySerializer(serializers.ModelSerializer):

	class Meta:
		model = Company
		fields = '__all__'

class ReviewRetrieveSerializer(serializers.ModelSerializer):
	company = CompanySerializer(many=False, read_only=True)
	reviewer = UserSerializer(many=False, read_only=True)

	class Meta:
		model = Review
		fields = '__all__'

class ReviewCreateSerializer(serializers.ModelSerializer):

	class Meta:
		model = Review
		fields = '__all__'
		read_only_fields = ('id', 'ip_address', 'submitted_date', 'reviewer')