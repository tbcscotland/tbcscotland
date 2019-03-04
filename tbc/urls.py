from django.conf.urls import url
from tbc import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^search/$', views.search, name='search'),
    url(r'^about/', views.about, name='about'),
    url(r'^getstarted/', views.getstarted, name='getstarted'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^login/$', views.user_login, name='login'),
    url(r'^profiles/', views.profiles, name='profiles'),
    url(r'^lendandsell/$', views.lendandsell, name='lendandsell'),
    url(r'^projects/$', views.projects, name='projects'),
    url(r'^services/$', views.services, name='services'),
    url(r'^lendandsell/(?P<lendandsell_name_slug>[\w\-]+)/$', views.show_lendandsell, name='show_lendandsell'),
    url(r'^projects/(?P<project_name_slug>[\w\-]+)/$', views.show_project, name='show_project'),
    url(r'^services/(?P<service_name_slug>[\w\-]+)/$', views.show_service, name='show_service'),        
]
