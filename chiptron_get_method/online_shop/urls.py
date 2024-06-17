from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.contrib import admin
from django.urls import path,include
from online_kart import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('online_kart.urls')),
    path('accounts/', include('accounts.urls')),
    path('pdf/', include('pdf_convert.urls')),
    path('emailsender/', include('send_email.urls')),
]