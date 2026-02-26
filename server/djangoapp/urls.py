from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'

urlpatterns = [

    # =========================
    # User Authentication APIs
    # =========================

    path('register', views.registration, name='register'),
    path('login', views.login_user, name='login'),
    path('logout', views.logout_request, name='logout'),

    # =========================
    # Car Models API
    # =========================

    path('get_cars', views.get_cars, name='getcars'),

    # =========================
    # Dealership APIs
    # =========================

    # Get all dealers
    path('get_dealers', views.get_dealerships, name='get_dealers'),

    # Get dealers by state
    path('get_dealers/<str:state>', views.get_dealerships, name='get_dealers_by_state'),

    # Get dealer details
    path('dealer/<int:dealer_id>', views.get_dealer_details, name='dealer_details'),

    # Get dealer reviews with sentiment
    path('reviews/dealer/<int:dealer_id>', views.get_dealer_reviews, name='dealer_reviews'),

    # =========================
    # Add Review API
    # =========================

    path('add_review', views.add_review, name='add_review'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)