from django.urls import path
from htmlApp import views
urlpatterns = [
    path("index/", views.index),
    path("basic_tag/", views.tag),
    path("kts_tag/", views.kts),
    path("main/", views.main),
    path("form_tag/", views.form),
    path("login/", views.login),
    path("table_form/", views.table),
    path("login_form/", views.loginform),
    path("login2/", views.login2),
]