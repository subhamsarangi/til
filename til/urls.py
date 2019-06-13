from django.conf.urls import  include, url
from django.contrib.auth.views import LoginView, LogoutView
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # url(r'^', include('things.urls', namespace="things")),
    url(r'^admin/', admin.site.urls),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
