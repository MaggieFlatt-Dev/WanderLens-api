
from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from WanderLensapi.views import (
    register_user,
    login_user,
    get_current_user,
    )
from WanderLensapi.views import (
  TripView,
  TripTypeView,
  CategoryView
)

router = routers.DefaultRouter(trailing_slash=False)
router.register(r'api/trips', TripView, 'trip')
router.register(r'api/triptypes', TripTypeView, 'triptype')
router.register(r'api/categories', CategoryView, 'category')

urlpatterns = [
    path('', include(router.urls)),
    path('register', register_user),
    path('login', login_user),
    path('current_user', get_current_user)
]

