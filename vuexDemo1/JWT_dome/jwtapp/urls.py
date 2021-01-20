from django.urls import path
from rest_framework_jwt import views

urlpatterns = [
    path("login/",views.ObtainJSONWebToken.as_view()),
    path("user/", views.LoginAPIView.as_view()),

]
