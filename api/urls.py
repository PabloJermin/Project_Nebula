from django.urls import path
from .views import all_students
from .views import create_student 
# from .views import detail
from .views import health
from .views import db_connection, search

urlpatterns = [
    path('students/', all_students, name='students'),
    path('create/', create_student, name='create'),
    # path('student/<int:pk>/', detail, name='details'),
    path('health-check/', health, name='health-check'),
    path('test_db_connection/', db_connection, name='db_connection'),
    path('search/', search, name='search')
]