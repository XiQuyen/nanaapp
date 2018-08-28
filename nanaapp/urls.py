"""nanaapp URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import  include,url
from django.contrib import admin

# it is important to have from django.conf.urls import  include,url
# when generate it doesn't have include so I build error
# Add url(r'^', include('ieltsapp.urls')) is important as well
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	#url(r'^questions/', include('ieltsapp.questions.urls')),
    #url(r'^articles/', include('ieltsapp.articles.urls')),
	url(r'^books/', include('booksapp.urls')),
	url(r'^ielts/', include('ieltsapp.urls')),
	url(r'^', include('ieltsapp.urls'))
]
