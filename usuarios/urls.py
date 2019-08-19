from django.urls import path, include
from rest_framework.routers import DefaultRouter
from usuarios import views

router = DefaultRouter()
router.register(r'perfis', views.ProfileViewset)
#router.register(r'auth/user', views.UserViewSet, 'user-detail')


urlpatterns = [
    path('', include(router.urls)),
]
