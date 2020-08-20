from django.conf.urls import url

from aldryn_newsblog.feeds import CategoryFeed, LatestArticlesFeed, TagFeed
from aldryn_newsblog.views import (
    ArticleDetail, ArticleList, ArticleSearchResultsList, AuthorArticleList,
    CategoryArticleList, DayArticleList, MonthArticleList, TagArticleList,
    YearArticleList,
)


urlpatterns = [
    url(r'^$', ArticleList.as_view(), name='article-list'),

    url(r'^feed/$', LatestArticlesFeed(), name='article-list-feed'),

    url(r'^search/$',
        ArticleSearchResultsList.as_view(), name='article-search'),

    url(r'^author/(?P<author>\w[-\w]*)/$',
        AuthorArticleList.as_view(), name='article-list-by-author'),

    url(r'^category/(?P<category>\w[-\w]*)/feed/$',
        CategoryFeed(), name='article-list-by-category-feed'),
    url(r'^category/(?P<category>\w[-\w]*)/$',
        CategoryArticleList.as_view(), name='article-list-by-category'),

    url(r'^tag/(?P<tag>\w[-\w]*)/feed/$',
        TagFeed(), name='article-list-by-tag-feed'),
    url(r'^tag/(?P<tag>\w[-\w]*)/$',
        TagArticleList.as_view(), name='article-list-by-tag'),

    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/$',
        DayArticleList.as_view(), name='article-list-by-day'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/$',
        MonthArticleList.as_view(), name='article-list-by-month'),
    url(r'^(?P<year>\d{4})/$',
        YearArticleList.as_view(), name='article-list-by-year'),

    # Various permalink styles that we support
    # ----------------------------------------
    # This supports permalinks with <article_pk>
    # NOTE: We cannot support /year/month/pk, /year/pk, or /pk, since these
    # patterns collide with the list/archive views, which we'd prefer to
    # continue to support.
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<pk>\d+)/$',
        ArticleDetail.as_view(), name='article-detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<day>\d{1,2})/(?P<slug>\w[-\w]*)/$',  # flake8: noqa
        ArticleDetail.as_view(), name='article-detail'),
    url(r'^(?P<year>\d{4})/(?P<month>\d{1,2})/(?P<slug>\w[-\w]*)/$',
        ArticleDetail.as_view(), name='article-detail'),
    url(r'^(?P<year>\d{4})/(?P<slug>\w[-\w]*)/$',
        ArticleDetail.as_view(), name='article-detail'),

    # These support permalinks with <article_slug>
    url(r'^(?P<slug>\w[-\w]*)/$',
        ArticleDetail.as_view(), name='article-detail'),
]
