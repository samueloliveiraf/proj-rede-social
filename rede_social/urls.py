from django.urls import path, include
from django.contrib import admin

from apps.accounts import urls as urls_accounts


urlpatterns = [
    path('accounts/', include(urls_accounts)),
    path('admin/', admin.site.urls),
]
