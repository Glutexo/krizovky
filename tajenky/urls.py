from django.urls import path

from .views import (
    TajenkaCreateView,
    TajenkaDeleteView,
    TajenkaDetailView,
    TajenkaListView,
    TajenkaUpdateView,
)

app_name = "tajenky"

urlpatterns = [
    path("", TajenkaListView.as_view(), name="list"),
    path("nova/", TajenkaCreateView.as_view(), name="create"),
    path("<int:pk>/", TajenkaDetailView.as_view(), name="detail"),
    path("<int:pk>/upravit/", TajenkaUpdateView.as_view(), name="update"),
    path("<int:pk>/smazat/", TajenkaDeleteView.as_view(), name="delete"),
]
