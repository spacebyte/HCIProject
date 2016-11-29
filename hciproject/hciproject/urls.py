"""hciproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from hciproject import views, settings
from registration.backends.simple.views import RegistrationView

class RegistrationBypass(RegistrationView):
    def get_success_url(self, user):
        return '/add_profile/'

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index, name='index'),
    url(r'^quiz/$', views.quiz, name='quiz'),
    url(r'^quiz_eval/$', views.quiz_eval, name='quiz_eval'),
    url(r'^add_profile/$', views.register_profile, name='profile_registration'),
    url(r'^profile/$', views.profile, name='profile'),
    url(r'^accounts/register/$', RegistrationBypass.as_view(), name='registration_register'),
    url(r'^quiz/send_score/$', views.send_score, name='send_score'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
