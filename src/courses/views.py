from django.contrib.auth.mixins import LoginRequiredMixin
from django.db.models import Prefetch
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import (
    CreateView,
    DetailView,
    ListView,
    UpdateView,
    DeleteView,
    RedirectView,
    View)

from .models import Course, Lecture, MyCourses
from .forms import CourseForm
from videos.mixins import MemberRequiredMixin, StaffMemberRequiredMixin


class CourseCreateView(StaffMemberRequiredMixin, CreateView):
    model = Course
    form_class = CourseForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()
        return super(CourseCreateView, self).form_valid(form)


class LectureDetailView(View):
    template_name = 'courses/lecture_detail.html'

    def get(self, request, clsug=None, lslug=None, *args, **kwargs):
        obj = None
        qs = Course.objects.filter(slug=clsug).lectures().owned(request.user)
        if not qs.exists():
            raise Http404

        course_ = qs.first()

        lectures_qs = course_.lecture_set.filter(slug=lslug)
        if not lectures_qs.exists():
            raise Http404

        obj = lectures_qs.first()

        context = {
            'object': obj,
            "course": course_,
        }

        if not course_.is_owner and not obj.free:
            return render(request, "courses/must_purchase.html", {'object': course_})

        return render(request, self.template_name, context)


class CourseDetailView(DetailView):
    # queryset = Course.objects.all()

    def get_object(self):
        slug = self.kwargs.get("slug")
        qs = Course.objects.filter(slug=slug).lectures().owned(self.request.user)
        if qs.exists():
            return qs.first()
        raise Http404


class CoursePurchaseView(LoginRequiredMixin, RedirectView):
    permanent = False

    def get_redirect_url(self, slug=None):
        qs = Course.objects.filter(slug=slug).owned(self.request.user)
        if qs.exists():
            user = self.request.user
            if user.is_authenticated():
                my_courses = user.mycourses
                # run transaction
                # if transaction successful:
                my_courses.courses.add(qs.first())
                return qs.first().get_absolute_url()
            return qs.first().get_absolute_url()
        return "/courses/"


class CourseListView(ListView):
    paginate_by = 12

    def get_queryset(self):
        request = self.request
        qs = Course.objects.all()
        query = request.GET.get('q')
        user = self.request.user

        if query:
            qs = qs.filter(title__icontains=query)

        if user.is_authenticated():
            qs = qs.owned(user)
        return qs


class CourseUpdateView(StaffMemberRequiredMixin, UpdateView):
    queryset = Course.objects.all()
    form_class = CourseForm

    def form_valid(self, form):
        obj = form.save(commit=False)
        if not self.request.user.is_staff:
            obj.user = self.request.user
        obj.save()
        return super(CourseUpdateView, self).form_valid(form)


class CourseDeleteView(StaffMemberRequiredMixin, DeleteView):
    queryset = Course.objects.all()
    success_url = '/courses/'
