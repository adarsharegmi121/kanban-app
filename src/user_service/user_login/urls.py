from django.urls import path
from user_login.views import UserApiView

urlpatterns = [
    path("api/login/", UserApiView.as_view()),
]
