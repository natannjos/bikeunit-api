from django.urls import path, include
from rest_framework.routers import DefaultRouter
from grupos import views

router = DefaultRouter()
router.register(r'grupos', views.TodosGruposViewset)
router.register(r'meus-grupos', views.MeusGruposViewset,
                basename='meus_grupos')
router.register(r'pedais', views.TodosPedaisViewset)
router.register(r'meus-pedais', views.MeusPedaisViewset,
                basename='meus_pedais')
router.register(r'entra-sai-pedal', views.EntrarESairDePedalViewset,
                basename='entra_sai_pedal')

urlpatterns = [
    path('', include(router.urls))
]
