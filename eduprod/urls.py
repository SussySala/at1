from django.urls import include, path

urlpatterns = [
    path('', include('at1.urls')),  # Include specific URL patterns from the 'at1' app
    # Other URL patterns for your project
]
