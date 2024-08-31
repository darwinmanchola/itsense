
from django.urls import path,include
from django.contrib import admin
from inventory_itsense import settings
from rest_framework.authtoken.views import obtain_auth_token
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/inventory/',include('apps.inventory.urls')),

]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
