from django.urls import path, include
from rest_framework.routers import DefaultRouter
from grupos import views

router = DefaultRouter()
router.register(r'todos-grupos', views.TodosGruposViewset)
router.register(r'meus-grupos', views.MeusGruposViewset)
router.register(r'pedais', views.PedalViewset)

urlpatterns = [
    path('', include(router.urls))
]
