from django.urls import path, include
from rest_framework.routers import DefaultRouter
from usuarios import views

router = DefaultRouter()
router.register(r'perfis', views.ProfileViewset)


urlpatterns = [
    path('', include(router.urls)),
]
