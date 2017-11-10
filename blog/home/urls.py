from django.conf.urls import url

from blog.home.views import Home


urlpatterns = [
    url(r'^$', Home.as_view(), name='home'),
]
