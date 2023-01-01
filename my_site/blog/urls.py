from django.urls import path
from . import views
urlpatterns = [
    path("",views.mainPage,name="main"),
    path("index",views.index,name="index"),
    path("<slug:slug>",views.post,name="model_detail")
]
