"""bikeunit_api URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from usuarios.urls import router as usuarios_router
from usuarios.views import ChangePasswordView
from grupos.urls import router as grupos_router

router = routers.DefaultRouter()
router.registry.extend(grupos_router.registry)
router.registry.extend(usuarios_router.registry)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/altera-senha/', ChangePasswordView.as_view()),
    path('api-auth', include('rest_framework.urls', namespace='rest_framework'))
]
