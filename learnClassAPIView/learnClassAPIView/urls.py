from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', StudentAPIView.as_view()),
    path('student/<int:id>/', StudentAPIView.as_view()),
]
