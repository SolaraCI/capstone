from . import views
from django.urls import path

urlpatterns = [
    path("", views.OverView.as_view(), name='home'),
    path("create_list", views.CreateListFormView.create_list, name="create_list"),
    path("lists/<list_id>", views.SingleListView.view_list, name="view_list"),
    path("register/", views.RegisterFormView.register, name="register"),
    path("login/", views.LoginFormView.login_page, name="login"),
    path("delete_item/<str:name>/", views.SingleListView.delete_item, name="delete_item"),
]
