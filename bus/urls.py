from django.urls import path, re_path

from . import views

urlpatterns = [
	path('', views.index, name='index'),
	re_path(r'^route/(?P<route_number>[\w-]+)/$', views.route, name='route'),
	re_path(r'^route/(?P<route_number>[\w-]+)/(?P<direction>[\w-]+)/$', views.route_stops, name='route_stops'),
	re_path(r'^route/(?P<route_number>[\w-]+)/(?P<direction>[\w-]+)/(?P<stop_id>[\w-]+)/$', views.schedule, name='schedule'),
]