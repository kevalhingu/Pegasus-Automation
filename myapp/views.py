from django.shortcuts import render,redirect
from django.conf import settings
from django.core.mail import send_mail
import random
from django.http import JsonResponse
from .forms import SignupForm
from django.contrib.auth import login
from .models import SupportRequest
from django.contrib.auth import logout

# Create your views here.

def index(request):
	return render(request,'index.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to the login page after signup
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


def support(request):
    message = ""
    if request.method == "POST":
        # Get form data
        name = request.POST.get("name")
        email = request.POST.get("email")
        contact = request.POST.get("contact")
        question = request.POST.get("question")

        # Save the form data to the SupportRequest model
        SupportRequest.objects.create(
            name=name,
            email=email,
            contact=contact,
            question=question
        )

        # Set the confirmation message
        message = "The support request is submitted, a technician will get back to you soon."

    return render(request, "support.html", {"message": message})
def custom_logout(request):
    if request.method == 'POST' or request.method == 'GET':
        logout(request)
        return redirect('index')  # Replace with your preferred redirect URL
    return redirect('index')  # Redirect to home or an error page for unsupported methods