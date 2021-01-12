from django.urls import path

from empapp import views

app_name="empapp"

urlpatterns=[
    # path("index/",views.index,name="index"),
    # path("deluser/",views.deluser,name="deluser"),
    # path("getunpuser/",views.getunpuser,name="getunpuser"),
    # path("unpuser/",views.unpuser,name="unpuser"),
    # path("adduser/",views.adduser,name="adduser"),
    # path("index/", views.UserAPIVIew.as_view()),
    # path("index/<str:id>", views.UserAPIVIew.as_view()),
    path("index/", views.UserGenericsAPIView.as_view()),
    path("index/<str:id>", views.UserGenericsAPIView.as_view()),

    path("login/", views.LoginViewSet.as_view({"post":"longin_count"})),
]