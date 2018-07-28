import django.contrib.auth.urls
from django.conf.urls import url
from django.urls import include, path
from django.views import generic

import project.urls
from buza import views


urlpatterns = [
    path('', generic.RedirectView.as_view(pattern_name='question-list'), name='home'),

    path('questions/', views.QuestionList.as_view(), name='question-list'),
    path('questions/<int:pk>/', views.QuestionDetail.as_view(), name='question-detail'),
    path('questions/ask/', views.QuestionCreate.as_view(), name='question-create'),
    path(
        'questions/<int:pk>/edit/',
        views.QuestionUpdate.as_view(),
        name='question-edit',
    ),

    path(
        'questions/<int:question_pk>/answer/<int:pk>/edit',
        views.AnswerUpdate.as_view(),
        name='answer-edit',
    ),

    path(
        'questions/<int:question_pk>/answer/',
        views.AnswerCreate.as_view(),
        name='answer-create',
    ),
    path('subjects/<int:pk>/', views.SubjectDetail.as_view(), name='subject-detail'),
    path(
        'subjects/my-subjects/<int:pk>/',
        views.UserSubjectList.as_view(),
        name='my-subject-list',
    ),
    path('subjects/', views.SubjectList.as_view(), name='subject-list'),

    url(r'^register/$', views.register, name='register'),
    url(r'^edit/$', views.edit, name='edit'),
    path(r'users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),

    path('auth/', include(django.contrib.auth.urls)),

    # Fall back to older project urls.
    path('', include(project.urls)),  # TODO: Migrate
]