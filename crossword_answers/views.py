from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import CrosswordAnswerForm, SourceURLForm
from .models import CrosswordAnswer, SourceURL


class CrosswordAnswerListView(ListView):
    model = CrosswordAnswer
    context_object_name = "answers"
    template_name = "crossword_answers/answer_list.html"


class CrosswordAnswerDetailView(DetailView):
    model = CrosswordAnswer
    context_object_name = "answer"
    template_name = "crossword_answers/answer_detail.html"


class CrosswordAnswerCreateView(CreateView):
    model = CrosswordAnswer
    form_class = CrosswordAnswerForm
    template_name = "crossword_answers/answer_form.html"
    success_url = reverse_lazy("crossword_answers:list")


class CrosswordAnswerUpdateView(UpdateView):
    model = CrosswordAnswer
    form_class = CrosswordAnswerForm
    template_name = "crossword_answers/answer_form.html"
    success_url = reverse_lazy("crossword_answers:list")


class CrosswordAnswerDeleteView(DeleteView):
    model = CrosswordAnswer
    context_object_name = "answer"
    template_name = "crossword_answers/answer_confirm_delete.html"
    success_url = reverse_lazy("crossword_answers:list")


class SourceURLListView(ListView):
    model = SourceURL
    context_object_name = "source_urls"
    template_name = "crossword_answers/source_url_list.html"


class SourceURLCreateView(CreateView):
    model = SourceURL
    form_class = SourceURLForm
    template_name = "crossword_answers/source_url_form.html"
    success_url = reverse_lazy("crossword_answers:source_url_list")


class SourceURLUpdateView(UpdateView):
    model = SourceURL
    form_class = SourceURLForm
    template_name = "crossword_answers/source_url_form.html"
    success_url = reverse_lazy("crossword_answers:source_url_list")


class SourceURLDeleteView(DeleteView):
    model = SourceURL
    context_object_name = "source_url"
    template_name = "crossword_answers/source_url_confirm_delete.html"
    success_url = reverse_lazy("crossword_answers:source_url_list")
