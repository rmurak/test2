from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.

# drugi argument funkcji (month) musi miec dokladnie ta sama nazwe ktora zdefiniowalismy jako <identyfikator> w urls.py


def monthly_challenge(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "January challenge"
    elif month == "february":
        challenge_text = "February challenge"
    elif month == "march":

        challenge_text = "March challenge"
    else:
        return HttpResponseNotFound("Nie znaleziono takiej strony")
    return HttpResponse(challenge_text)
