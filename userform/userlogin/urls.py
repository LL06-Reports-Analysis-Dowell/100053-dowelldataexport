from django.urls import path

from . import views

urlpatterns = [
   
    path('authenticate/login',views.loginform),
    path('questionid/',views.questionid),
    # path('questionid/',views.questionidview),
]
