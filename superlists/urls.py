from django.urls import path
from lists import views

urlpatterns = [
    path("", views.home_page, name="home"),
    path("about-me/" , views.about_me, name='about_me'),
]
