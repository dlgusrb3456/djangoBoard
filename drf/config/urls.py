from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api-auth/', include('rest_framework.urls')),
    path('dj_rest-auth/',include('dj_rest_auth.urls')),
    path('dj_rest-auth/registration/',include('dj_rest_auth.registration.urls')),
    path('',include('product.urls')),
    path('',include('review.urls')),
    path('',include('order.urls')),
]