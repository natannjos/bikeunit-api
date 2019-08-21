from django.urls import path, include
from rest_framework.routers import DefaultRouter
from grupos import views

router = DefaultRouter()
router.register(r'todos-grupos', views.TodosGruposViewset)
router.register(r'meus-grupos', views.MeusGruposViewset)
router.register(r'todos-pedais', views.TodosPedaisViewset)
router.register(r'meus-pedais', views.MeusPedaisViewset)

urlpatterns = [
    path('', include(router.urls))
]
