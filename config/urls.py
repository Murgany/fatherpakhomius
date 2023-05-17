from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns


# Set up project urls

urlpatterns = i18n_patterns(
    path('admin/', admin.site.urls),
    path('', include('fatherpakhomius.urls')),

    # I had to include this here because I'm using the {% set_language %} tag to switch between languages
    path('i18n/', include('django.conf.urls.i18n')),

    # If no prefix is given, use the default language
    prefix_default_language=False
)

