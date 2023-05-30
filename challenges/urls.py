from django.urls import path
from . import views


# przechwytujemy dynamicznie url'a i przekazujemy go do funkcji monthly_challenge w views
# w nawiasach ostrych osadzamy <identyfikator> ktory pozniej wykorzystamy w funkcji w
urlpatterns = [
    path("<month>", views.monthly_challenge)
]