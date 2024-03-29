"""checkers URL Configuration

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
from rest_framework import routers
from checkers.boardREST.views import *
from django.urls import include, path

router = routers.DefaultRouter()
router.register(r'board', BoardViewSet, base_name='board')
router.register(r'tasks', TaskViewSet, base_name='tasks')
# urlpatterns = [ path('', include(router.urls))]
urlpatterns = router.urls
