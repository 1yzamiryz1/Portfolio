from django.contrib import messages
from django.shortcuts import render

from main.forms import ContactForm
from main.models import Certificate


def index_view(request):
    return render(request, "main/index.html")


def about_view(request):
    certificates = Certificate.objects.all()
    context = {"certificates": certificates}
    return render(request, "main/about.html", context)


def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(
                request, messages.SUCCESS, "your ticket submitted successfully"
            )
        else:
            messages.add_message(
                request, messages.ERROR, "your ticket didn't submitted"
            )
    form = ContactForm()
    context = {"form": form}
    return render(request, "main/contact.html", context)


def maintenance_view(request):
    return render(request, 'maintenance.html')


def handler404(request, *args, **kwargs):
    return render(request, '404.html', status=404)
