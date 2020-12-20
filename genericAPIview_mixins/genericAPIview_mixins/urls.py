from django.contrib import admin
from django.urls import path
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('student/', LCStudentAPIView.as_view()),
    path('student/<int:pk>/', RUDStudentAPIView.as_view()),
]
