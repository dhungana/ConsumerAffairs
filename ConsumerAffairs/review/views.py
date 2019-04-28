from rest_framework import viewsets, mixins
from .models import Review
from .serializers import ReviewCreateSerializer, ReviewRetrieveSerializer
from rest_framework.permissions import IsAuthenticated
from ipware import get_client_ip
import datetime

class ReviewViewSet(mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.ListModelMixin, viewsets.GenericViewSet):
	permission_classes = (IsAuthenticated,)

	def perform_create(self, serializer):
		ip_address, is_routable = get_client_ip(self.request)
		if ip_address is None:
			ip_address = ' '
		serializer.save(reviewer=self.request.user, ip_address=ip_address, submitted_date=datetime.date.today())

	def get_queryset(self):
		queryset = Review.objects.filter(reviewer=self.request.user)
		return queryset

	def get_serializer_class(self):
		if self.action == 'create':
			return ReviewCreateSerializer
		else:
			return ReviewRetrieveSerializer
