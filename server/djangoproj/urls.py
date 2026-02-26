"""
djangoproj URL Configuration
"""

from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # Admin
    path('admin/', admin.site.urls),

    # Django API routes
    path('djangoapp/', include('djangoapp.urls')),

    # =========================
    # React SPA Routes
    # =========================

    # Home page (React)
    path('', TemplateView.as_view(template_name="index.html")),

    # Login page (React)
    path('login/', TemplateView.as_view(template_name="index.html")),

    # Register page (React)
    path('register/', TemplateView.as_view(template_name="index.html")),

    # Dealers list page (React)
    path('dealers/', TemplateView.as_view(template_name="index.html")),

    # Dealer details page (React)
    path('dealer/<int:dealer_id>/', TemplateView.as_view(template_name="index.html")),

    # ✅ ADD THIS (Post Review Page)
    path('postreview/<int:dealer_id>/', TemplateView.as_view(template_name="index.html")),

    # =========================
    # Static HTML Pages
    # =========================

    # About page
    path('about/', TemplateView.as_view(template_name="About.html")),

    # Contact page
    path('contact/', TemplateView.as_view(template_name="Contact.html")),
]

# Static files (for production build)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)