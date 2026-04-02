from django.urls import path

from .views import (
    CrosswordAnswerCreateView,
    CrosswordAnswerDetailView,
    CrosswordAnswerHideView,
    CrosswordAnswerListView,
    CrosswordAnswerRestoreView,
    CrosswordAnswerUpdateView,
    SourceURLCreateView,
    SourceURLHideView,
    SourceURLListView,
    SourceURLRestoreView,
    SourceURLUpdateView,
)

app_name = "krizovky"

urlpatterns = [
    path("", CrosswordAnswerListView.as_view(), name="list"),
    path("nova/", CrosswordAnswerCreateView.as_view(), name="create"),
    path("<int:pk>/", CrosswordAnswerDetailView.as_view(), name="detail"),
    path("<int:pk>/upravit/", CrosswordAnswerUpdateView.as_view(), name="update"),
    path("<int:pk>/skryt/", CrosswordAnswerHideView.as_view(), name="hide"),
    path("<int:pk>/obnovit/", CrosswordAnswerRestoreView.as_view(), name="restore"),
    path("zdroje/", SourceURLListView.as_view(), name="source_url_list"),
    path("zdroje/nova/", SourceURLCreateView.as_view(), name="source_url_create"),
    path("zdroje/<int:pk>/upravit/", SourceURLUpdateView.as_view(), name="source_url_update"),
    path("zdroje/<int:pk>/skryt/", SourceURLHideView.as_view(), name="source_url_hide"),
    path("zdroje/<int:pk>/obnovit/", SourceURLRestoreView.as_view(), name="source_url_restore"),
]
