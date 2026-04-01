from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .models import Tajenka


class TajenkaListView(ListView):
    model = Tajenka
    context_object_name = "tajenky"
    template_name = "tajenky/tajenka_list.html"


class TajenkaDetailView(DetailView):
    model = Tajenka
    context_object_name = "tajenka"
    template_name = "tajenky/tajenka_detail.html"


class TajenkaCreateView(CreateView):
    model = Tajenka
    fields = ["text", "popis"]
    template_name = "tajenky/tajenka_form.html"
    success_url = reverse_lazy("tajenky:list")


class TajenkaUpdateView(UpdateView):
    model = Tajenka
    fields = ["text", "popis"]
    template_name = "tajenky/tajenka_form.html"
    success_url = reverse_lazy("tajenky:list")


class TajenkaDeleteView(DeleteView):
    model = Tajenka
    context_object_name = "tajenka"
    template_name = "tajenky/tajenka_confirm_delete.html"
    success_url = reverse_lazy("tajenky:list")

# Create your views here.
