from django.urls import path, include
from .views import *



urlpatterns = [
    path('api/v1/category', PersonCategoryView.as_view()),
    path('api/v1/services/individual', ServiceForIndividualView.as_view()),
    path('api/v1/services/legal-entity', ServiceForLegalEntityView.as_view()),
]