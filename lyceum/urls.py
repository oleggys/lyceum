from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

import lyceum
from lyceum import views

urlpatterns = [
    url(r'^$', lyceum.views.index, name="index"),
    url(r'^collective/$', lyceum.views.team, name="team"),
    url(r'^events/$', lyceum.views.events, name="events"),
    url(r'^incoming/$', lyceum.views.incom, name="incom"),
    url(r'^offer/$', lyceum.views.offers, name="offers"),
    url(r'^documents/$', lyceum.views.documents, name="documents"),
    url(r'^make_offer/$', lyceum.views.make_offer, name="make_offer"),
    url(r'^make_com/$', lyceum.views.make_com, name="make_com"),
    url(r'^send_email/$', lyceum.views.messages, name="message"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)