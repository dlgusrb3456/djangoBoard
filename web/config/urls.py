from django.conf.urls.static import static

from config import settings
from django.contrib import admin
from django.urls import path, include

import board.views
import accounts.views
import reply2.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', board.views.mainPage),
    path('board', board.views.mainPage),
    path('createWork', board.views.createGet),
    path('listAt/deleteWork/<int:bid>', board.views.deleteGet),
    path('listAt/updateWork/<int:bid>', board.views.updateGet),
    path('listAt/<int:bid>', board.views.atlistGet),
    path('accounts/',include('allauth.urls')),
    path('accounts/profile/',board.views.mainPage),
    path('accounts/logout/',board.views.mainPage),
    #path('accounts/profile',board.views.mainPage),

    path('reply/create/<int:rid>', reply2.views.create),
    path('reply/list', reply2.views.list),
    path('reply/read/<int:rid>', reply2.views.read),
    path('reply/delete/<int:rid>/<int:bid>', reply2.views.delete),
    path('reply/update/<int:rid>/<int:bid>', reply2.views.update),

    path('oauth',accounts.views.getcode),
    path('email2/',accounts.views.func1),
    path('kakaologin/', accounts.views.loginPage),
    path('kakaologout/', accounts.views.logoutPage),
    path('oauth/redirect',accounts.views.getcode),
    #path('kakaologin',accounts.views.getcode),

    path('like/<int:bid>',board.views.like)
]+ static(settings.MEDIA_URL,document_root = settings.MEDIA_ROOT)
