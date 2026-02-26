from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.views.decorators.csrf import csrf_exempt
import logging
import json

from .models import CarMake, CarModel
from .populate import initiate
from .restapis import get_request, analyze_review_sentiments, post_review

# Logger
logger = logging.getLogger(__name__)

# ============================
# User Authentication APIs
# ============================

@csrf_exempt
def login_user(request):
    data = json.loads(request.body)
    username = data['userName']
    password = data['password']

    user = authenticate(username=username, password=password)
    response_data = {"userName": username}

    if user is not None:
        login(request, user)
        response_data = {
            "userName": username,
            "status": "Authenticated"
        }

    return JsonResponse(response_data)


@csrf_exempt
def logout_request(request):
    logout(request)
    return JsonResponse({"userName": ""})


@csrf_exempt
def registration(request):
    data = json.loads(request.body)

    username = data['userName']
    password = data['password']
    first_name = data['firstName']
    last_name = data['lastName']
    email = data['email']

    try:
        User.objects.get(username=username)
        return JsonResponse({
            "userName": username,
            "error": "Already Registered"
        })
    except:
        user = User.objects.create_user(
            username=username,
            first_name=first_name,
            last_name=last_name,
            password=password,
            email=email
        )

        login(request, user)

        return JsonResponse({
            "userName": username,
            "status": "Authenticated"
        })


# ============================
# Car Models API
# ============================

def get_cars(request):
    if CarMake.objects.count() == 0:
        initiate()

    car_models = CarModel.objects.select_related('car_make')
    cars = []

    for car_model in car_models:
        cars.append({
            "CarModel": car_model.name,
            "CarMake": car_model.car_make.name
        })

    return JsonResponse({"CarModels": cars})


# ============================
# Dealership APIs
# ============================

def get_dealerships(request, state="All"):
    if state == "All":
        endpoint = "/fetchDealers"
    else:
        endpoint = "/fetchDealers/" + state

    dealerships = get_request(endpoint)

    return JsonResponse({
        "status": 200,
        "dealers": dealerships
    })


def get_dealer_details(request, dealer_id):
    endpoint = "/fetchDealer/" + str(dealer_id)
    dealership = get_request(endpoint)

    return JsonResponse({
        "status": 200,
        "dealer": dealership
    })


# ============================
# Dealer Reviews API
# ============================

def get_dealer_reviews(request, dealer_id):
    endpoint = "/fetchReviews/dealer/" + str(dealer_id)
    reviews = get_request(endpoint)

    # Add sentiment analysis
    for review in reviews:
        sentiment_response = analyze_review_sentiments(review['review'])
        review['sentiment'] = sentiment_response['sentiment']

    return JsonResponse({
        "status": 200,
        "reviews": reviews
    })


# ============================
# Add Review API (POST)
# ============================

@csrf_exempt
def add_review(request):
    if request.method == "POST":

        # Only authenticated users can post reviews
        if not request.user.is_anonymous:

            data = json.loads(request.body)

            try:
                response = post_review(data)
                print(response)

                return JsonResponse({
                    "status": 200,
                    "message": "Review posted successfully"
                })

            except:
                return JsonResponse({
                    "status": 500,
                    "message": "Error in posting review"
                })

        else:
            return JsonResponse({
                "status": 403,
                "message": "Unauthorized"
            })

    return JsonResponse({
        "status": 405,
        "message": "Invalid request method"
    })