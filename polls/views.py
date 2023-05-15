from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render
from .forms import NumberForm
from .models import Number
from .tasks import send_messages

def add_number(request):
    send_messages.delay(request)
    if request.method == "POST":
        form = NumberForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse("sms"))
    else:
        form = NumberForm()
    return render(request, "number_form.html", {"form": form})


def sms(request):
    return render(request, "number_form_sms.html")