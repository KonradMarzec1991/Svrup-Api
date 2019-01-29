from django.shortcuts import render
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView
)

from .models import Video
from .forms import VideoForm
from .mixins import MemberRequiredMixin, StaffMemberRequiredMixin


class VideoCreateView(StaffMemberRequiredMixin, CreateView):
    model = Video
    form_class = VideoForm


class VideoDetailView(MemberRequiredMixin, DetailView):
    queryset = Video.objects.all()

    # def get_context_data(self, *args, **kwargs):
    #     context = super(VideoDetailView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context


class VideoListView(ListView):
    def get_queryset(self):
        request = self.request
        qs = Video.objects.all()
        query = request.GET.get('q')
        if query:
            qs = qs.filter(title__icontains=query)
        return qs

    # def get_context_data(self, *args, **kwargs):
    #     context = super(VideoListView, self).get_context_data(*args, **kwargs)
    #     print(context)
    #     return context


class VideoUpdateView(StaffMemberRequiredMixin, UpdateView):
    queryset = Video.objects.all()
    form_class = VideoForm


class VideoDeleteView(StaffMemberRequiredMixin, DeleteView):
    queryset = Video.objects.all()
    success_url = '/videos/'
