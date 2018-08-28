# ieltsapp/urls.py
from django.conf.urls import url, include
from django.urls import path
#from ieltsapp import views
from booksapp import views as book_views
# post?firstname=Mickey&lastname=Mouse
urlpatterns = [
    url(r'^index/$', book_views.index, name='index'),
    #url(r'^check_notifications/(?P<user_id>\d+)/$', views.check_notifications, name='check_notifications'),
	#url(r'^last_notifications/(?P<user_id>\d+)/$', views.last_notifications, name='last_notifications'),
	#url(r'^notifications/(?P<user_id>\d+)/$', views.notifications, name='notifications'),
	#url(r'^book/(?P<pk>\d+)/check_notifications/$', views.check_notifications, name='check_notifications'),
	#url(r'^book/(?P<pk>\d+)/last_notifications/$', views.last_notifications, name='last_notifications'),
	#url(r'^user/(?P<username>\w{0,50})/$', views.notifications,name='notifications')
]