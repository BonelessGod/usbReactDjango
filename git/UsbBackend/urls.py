from django.contrib import admin
from django.urls import path, include, re_path
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from rest_framework import routers

from backend.views import EventView, PhotoView

#routers
router = routers.DefaultRouter()
router.register(r'event', EventView, 'event')
router.register(r'photo', PhotoView, 'photo')

def render_react(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),
    path('', TemplateView.as_view(template_name='index.html')),
    #re_path(r"^$", render_react),
    #re_path(r"^(?:.*)/?$", render_react),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()