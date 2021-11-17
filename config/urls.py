from django.contrib import admin
from django.urls import path
from rest.views import base




urlpatterns = [
    path('admin/', admin.site.urls),


    # My app urls
    path('',base,name='home'),
]


from django.conf import settings
from django.conf.urls.static import static
if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)