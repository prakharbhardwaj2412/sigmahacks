from django.urls import path, include
from .import views
urlpatterns = [
    path('' ,views.signup , name="register"),
    path('login/' ,views.login, name="login" ),
    path('shop/' , views.shop_signup ,name="shopkeepersignup")
    path('slogin', views)
]