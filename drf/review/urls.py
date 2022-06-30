from rest_framework.routers import DefaultRouter

import review.views
from django.urls import path, include

# router = DefaultRouter()
# router.register('review' , review.views.ReviewAPI)

urlpatterns = [
    path('review/',review.views.ReviewList.as_view()),
    path('review/<int:pid>/', review.views.ReviewDetail.as_view()),
    path('review/<int:pid>/<int: rid>', review.views.ReviewDetail.as_view())
    # path('', include(router.urls)),
]