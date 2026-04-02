from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView

from .forms import CrosswordAnswerForm, SourceImportForm, SourceURLForm
from .models import CrosswordAnswer, SourceURL
from .source_import import SourceImportError, import_answers_from_source_url


class HideView(DeleteView):
    def form_valid(self, form):
        self.object = self.get_object()
        self.object.hide()
        return HttpResponseRedirect(self.get_success_url())


class CrosswordAnswerListView(ListView):
    context_object_name = "answers"
    template_name = "krizovky/answer_list.html"

    def get_queryset(self):
        queryset = CrosswordAnswer.all_objects.all() if self.show_hidden else CrosswordAnswer.objects.all()
        return queryset.order_by("text")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["show_hidden"] = self.show_hidden
        context["import_form"] = kwargs.get("import_form", SourceImportForm())
        return context

    def post(self, request, *args, **kwargs):
        form = SourceImportForm(request.POST)
        self.object_list = self.get_queryset()

        if form.is_valid():
            source_url = form.cleaned_data["url"]

            try:
                result = import_answers_from_source_url(source_url)
            except SourceImportError as exc:
                form.add_error("url", str(exc))
            else:
                parts = [f"uloženo {result.created_count}"]
                if result.restored_count:
                    parts.append(f"obnoveno {result.restored_count}")
                if result.skipped_count:
                    parts.append(f"přeskočeno {result.skipped_count}")

                messages.success(
                    request,
                    f"Import ze zdroje {result.source_url.url} dokončen: {', '.join(parts)} tajenek.",
                )
                return HttpResponseRedirect(reverse("krizovky:list"))

        context = self.get_context_data(import_form=form)
        return self.render_to_response(context)

    @property
    def show_hidden(self) -> bool:
        return self.request.GET.get("show_hidden") == "1"


class CrosswordAnswerDetailView(DetailView):
    queryset = CrosswordAnswer.all_objects.all()
    context_object_name = "answer"
    template_name = "krizovky/answer_detail.html"


class CrosswordAnswerCreateView(CreateView):
    model = CrosswordAnswer
    form_class = CrosswordAnswerForm
    template_name = "krizovky/answer_form.html"
    success_url = reverse_lazy("krizovky:list")


class CrosswordAnswerUpdateView(UpdateView):
    queryset = CrosswordAnswer.all_objects.all()
    form_class = CrosswordAnswerForm
    template_name = "krizovky/answer_form.html"
    success_url = reverse_lazy("krizovky:list")


class CrosswordAnswerHideView(HideView):
    queryset = CrosswordAnswer.all_objects.all()
    context_object_name = "answer"
    template_name = "krizovky/answer_confirm_hide.html"
    success_url = reverse_lazy("krizovky:list")


class CrosswordAnswerRestoreView(View):
    def post(self, request, pk):
        answer = CrosswordAnswer.all_objects.get(pk=pk)
        answer.restore()
        return HttpResponseRedirect(f"{reverse('krizovky:list')}?show_hidden=1")


class SourceURLListView(ListView):
    context_object_name = "source_urls"
    template_name = "krizovky/source_url_list.html"

    def get_queryset(self):
        queryset = SourceURL.all_objects.all() if self.show_hidden else SourceURL.objects.all()
        return queryset.order_by("url")

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["show_hidden"] = self.show_hidden
        return context

    @property
    def show_hidden(self) -> bool:
        return self.request.GET.get("show_hidden") == "1"


class SourceURLCreateView(CreateView):
    model = SourceURL
    form_class = SourceURLForm
    template_name = "krizovky/source_url_form.html"
    success_url = reverse_lazy("krizovky:source_url_list")


class SourceURLUpdateView(UpdateView):
    queryset = SourceURL.all_objects.all()
    form_class = SourceURLForm
    template_name = "krizovky/source_url_form.html"
    success_url = reverse_lazy("krizovky:source_url_list")


class SourceURLHideView(HideView):
    queryset = SourceURL.all_objects.all()
    context_object_name = "source_url"
    template_name = "krizovky/source_url_confirm_hide.html"
    success_url = reverse_lazy("krizovky:source_url_list")


class SourceURLRestoreView(View):
    def post(self, request, pk):
        source_url = SourceURL.all_objects.get(pk=pk)
        source_url.restore()
        return HttpResponseRedirect(f"{reverse('krizovky:source_url_list')}?show_hidden=1")
