from django import urls
from django import db
from django.db import router
from django.urls import path
from django.urls.conf import include
from rest_framework import routers
from .views import ArticleViewSet, SymbolViewSet, get_rss_news_feed, post_rss_news_feed
from rest_framework.routers import DefaultRouter

routers = DefaultRouter()
routers.register('articles', ArticleViewSet, basename='articles')
routers.register('symbols', SymbolViewSet, basename='symbols')

urlpatterns = [
    path('rss/get_news_by_symbol/', get_rss_news_feed, name="get_news"),
    path('rss/post_news_by_symbol/', post_rss_news_feed, name="post_news"),
    path('api/', include(routers.urls)),
    path('api/<int:pk>/', include(routers.urls)),
    # path('article/', ArticleAPIView.as_view()),
    # path('article/<int:pk>', ArticleDetail.as_view()),
    # path('generic/article/', GenericAPIView.as_view()),
    # path('generic/article/<int:id>/', GenericAPIView.as_view()),

]
