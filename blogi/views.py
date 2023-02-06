from django.shortcuts import render

from .models import Postaus


def postaukset(request):
    postaukset = Postaus.objects.all()
    context = {"postaukset": postaukset}
    return render(
        request,
        "blogi/postauslista.html",
        context,
    )

def nayta_postaus(request, id):
    return render(request, "blogi/postaus.html")
