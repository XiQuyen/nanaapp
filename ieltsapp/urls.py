# ieltsapp/urls.py
from django.conf.urls import url, include
from django.urls import path
from ieltsapp import views
# post?firstname=Mickey&lastname=Mouse
urlpatterns = [
    url(r'^$', views.HomePageView.as_view()),
    url(r'^about/$', views.AboutPageView, name='AboutPageView'), # Add this /about/ route
	url(r'^speaking/$', views.SpeakingPageView.as_view()),
	url(r'^reading/$', views.ReadingPageView.as_view()),
	url(r'^listening/$', views.ListeningPageView.as_view()),
	url(r'^writing/$', views.WritingPageView.as_view()),
	url(r'^contact/$', views.ContactPageView.as_view()),
	url(r'^listening/(?P<topic>\w{0,50})/$', views.listening, name='listening'),
	url(r'^speaking/(?P<topic>\w{0,50})/$', views.speaking, name='speaking'),
	url(r'^reading/(?P<topic>\w{0,50})/$', views.reading, name='reading'),
	url(r'^writing/(?P<topic>\w{0,50})/$', views.writing, name='writing'),
    url(r'^home/$', views.home, name='home'),
	#url(r'^author/add/$', views.add_author_edit, name='add_author_edit'),
	#url(r'^wiki/add/$', views.add_wiki_edit, name='add_wiki_edit'),
	#url(r'^post/new/$', views.add_post_edit, name='add_post_edit'),
    #url(r'^post/(?P<user_id>\d+)/$', views.post_detail, name='post_detail'),
	#url(r'^vote/(?P<user_id>\d+)/$', views.vote_detail, name='vote_detail'),
	#url(r'^render/(?P<user_id>\d+)/$', views.render_detail, name='render_detail'),
	url(r'^book/(?P<pk>\d+)/detail/$', views.book_detail, name='book_detail'),
	url(r'^book/(?P<pk>\d+)/results/$', views.book_review, name='book_review'),
	url(r'^user/(?P<username>\w{0,50})/$', views.user_profile_page,name='user_profile_page'),
	url("^search/$", views.search, name="search"),
    #url("^json/$", views.search_json, name="search_json"),
	path('<int:question_id>', views.index, name = 'index'),
    path('<int:question_id>/detail', views.view_question, name='view_question'),
    path('<int:question_id>/results/', views.view_results, name='view_results'),
    path('<int:question_id>/vote/', views.view_vote, name='view_vote'),	
	#url(r'^questions/', include('ieltsapp.questions.urls')),
]