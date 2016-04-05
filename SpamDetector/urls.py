from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^api/play_count_by_month', views.play_count_by_month, name='play_count_by_month'),
]