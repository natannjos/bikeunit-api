from django.urls import path, include
from rest_framework.routers import DefaultRouter
from grupos import views

router = DefaultRouter()
router.register(r'grupos', views.GrupoViewset)
router.register(r'pedais', views.PedalViewset)

urlpatterns = [
    path('', include(router.urls))
]
