from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .forms import NumberForm
from .tasks import send_messages


def add_number(request):
    if request.method == "POST":
        form = NumberForm(request.POST)
        if form.is_valid():
            form.save()
            message = form.cleaned_data["number"]

            send_messages.delay(message)

            return HttpResponseRedirect(reverse("sms"))
    else:
        form = NumberForm()
    return render(request, "number_form.html", {"form": form})


def sms(request):
    return render(request, "number_form_sms.html")
