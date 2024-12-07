from . import views
from django.urls import path

urlpatterns = [
    path("", views.all_lists, name="home"),
    path("create_list", views.create_list, name="create_list"),
    path("lists/<list_id>", views.view_list, name="view_list"),
]
