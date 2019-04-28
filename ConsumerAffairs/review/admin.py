from django.contrib import admin
from .models import Company, Review

class CompanyAdmin(admin.ModelAdmin):
	list_display = ('id', 'name', 'url')

class ReviewAdmin(admin.ModelAdmin):
	def reviewer_username(self, obj):
		return obj.reviewer.username

	def company_name(self, obj):
		return obj.company.name

	list_display = ('id', 'rating', 'title', 'ip_address', 'submitted_date', 'company_name', 'reviewer_username')


admin.site.register(Company, CompanyAdmin)
admin.site.register(Review, ReviewAdmin)