from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api.views import *

router=DefaultRouter()
router.register('student',StudentViewSet,basename='student')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api',include(router.urls)),
]
