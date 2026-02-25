from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from datetime import datetime
from django.views.decorators.csrf import csrf_exempt
import logging
import json

# Get an instance of a logger
logger = logging.getLogger(__name__)


# ============================
# Create your views here.
# ============================


# Create a `login_user` view to handle sign in request
@csrf_exempt
def login_user(request):
    # Get username and password from request body
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']

    # Try to authenticate user
    user = authenticate(username=username, password=password)

    data = {"userName": username}

    if user is not None:
        # If authentication successful, log in the user
        login(request, user)
        data = {"userName": username, "status": "Authenticated"}

    return JsonResponse(data)


# Create a `logout_request` view to handle sign out request
@csrf_exempt
def logout_request(request):
    # Terminate user session
    logout(request)

    # Return empty username after logout
    data = {"userName": ""}

    return JsonResponse(data)


# Create a `registration` view to handle sign up request
# @csrf_exempt
# def registration(request):
#     pass


# Update the `get_dealerships` view to render the index page
# def get_dealerships(request):
#     pass


# Create a `get_dealer_reviews` view to render the reviews of a dealer
# def get_dealer_reviews(request, dealer_id):
#     pass


# Create a `get_dealer_details` view to render the dealer details
# def get_dealer_details(request, dealer_id):
#     pass


# Create a `add_review` view to submit a review
# def add_review(request):
#     pass