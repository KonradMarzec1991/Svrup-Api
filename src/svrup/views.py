from django.shortcuts import render
from django.views import View

from courses.models import Course


class Home(View):
    template_name = 'home.html'

    def get(self, request):
        qs = Course.objects.all().featured().lectures().owned(request.user).distinct().order_by("?")[:6]

        context = {
            'qs': qs
        }

        return render(request, self.template_name, context)
