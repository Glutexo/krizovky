from django.urls import path

from .views import (
    CrosswordAnswerCreateView,
    CrosswordAnswerDeleteView,
    CrosswordAnswerDetailView,
    CrosswordAnswerListView,
    CrosswordAnswerUpdateView,
    SourceURLCreateView,
    SourceURLDeleteView,
    SourceURLListView,
    SourceURLUpdateView,
)

app_name = "crossword_answers"

urlpatterns = [
    path("", CrosswordAnswerListView.as_view(), name="list"),
    path("nova/", CrosswordAnswerCreateView.as_view(), name="create"),
    path("<int:pk>/", CrosswordAnswerDetailView.as_view(), name="detail"),
    path("<int:pk>/upravit/", CrosswordAnswerUpdateView.as_view(), name="update"),
    path("<int:pk>/smazat/", CrosswordAnswerDeleteView.as_view(), name="delete"),
    path("zdroje/", SourceURLListView.as_view(), name="source_url_list"),
    path("zdroje/nova/", SourceURLCreateView.as_view(), name="source_url_create"),
    path("zdroje/<int:pk>/upravit/", SourceURLUpdateView.as_view(), name="source_url_update"),
    path("zdroje/<int:pk>/smazat/", SourceURLDeleteView.as_view(), name="source_url_delete"),
]
