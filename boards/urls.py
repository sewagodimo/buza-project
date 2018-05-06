from django.conf.urls import url
# from django.contrib.auth import authenticate, login, logout

from . import views

urlpatterns = [
	url(r'^questions/', views.all_questions, name='all_questions'),
	url(r'^all/$', views.all_boards, name='all_boards'),
	url(r'^mine/$', views.my_boards, name='my_boards'),
	url(r'^users/$', views.all_users, name='users'),
	url(r'^(?P<board_name>[\w|\W]+)/', views.board_questions, name='board_questions'),
	url(r'^(?P<board_name>\w+)/', views.board_questions, name='board_questions'),
	# url(r'^question/(?P<id>\d+)/(?P<slug>\d+)/$', views.question_view, name='board_questions'),
]