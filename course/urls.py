from django.urls import path
from django.conf.urls import url

from . import views

app_name = 'course'
urlpatterns = [
    path('course-list/', views.CourseListView.as_view(), name='course_list'),
    url(r'^course-articles-list/(?P<course_id>\d+)/$', views.CourseArticlesListView.as_view(), name='course_articles_list'),
]
