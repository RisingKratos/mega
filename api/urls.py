from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^api/(?P<email>\w{0,50})/(?P<password>\w{0,50})$', views.login_api_view, name='login_api_view'),
    url(r'^api/(?P<code_id>[0-9]+)$', views.gem_api_view, name='gem_api_view'),
]
