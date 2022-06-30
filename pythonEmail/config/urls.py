
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import accounts.views
import board.views
from config import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('allauth.urls')),
    path('email2/',accounts.views.func1),
    path('oauth/', accounts.views.loginPage),
    path('oauth/redirect',accounts.views.getcode),
    path('board/mainpage', board.views.mainPage),
    path('board/createWork', board.views.createGet),
    path('board/read/<int:bid>', board.views.read),
] + static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
