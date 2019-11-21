from django.views.generic.list import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from .models import Bookmark


class BookmarkListView(ListView):
    model = Bookmark
    paginate_by = 6


class BookmarkCreateView(CreateView):
    model = Bookmark
    fields = ['site_name','url']
    success_url = reverse_lazy('list')  # 글쓰기를 완료했을 때 이동할 페이지
    template_name_suffix = '_create'


class BookmarkDetailView(DetailView):
    model = Bookmark


class BookmarkUpdateView(UpdateView):
    model = Bookmark
    fields = ['site_name','url']
    template_name_suffix = '_update' # 템플릿 파일명 접미사 --> bookmark_update.html 템플릿 사용

    # success_url 없으면 모델에 get_absolute_url 이라는 메서드를 통해 결정


class BookmarkDeleteView(DeleteView):
    model = Bookmark
    success_url = reverse_lazy('list')