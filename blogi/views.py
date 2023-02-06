from django.http import HttpResponse
from django.shortcuts import render


def postaukset(request):
    return HttpResponse("Moi!")
