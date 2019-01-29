from django.shortcuts import render
from django.views.generic import View


class SearchView(View):

    def get(self, request, *args, **kwargs):
        query = request.GET.get('q')
        # qs = None
        # if query:
        #     qs = Course.objects.all().lectures().filter(
        #             title__icontains=query,
        #             category__title__icontains=query,
        #             )
        # c_qs = Category.objects.filter(title__icontains=query)
        return render(request, "search/templates/search/default.html", {"qs": qs, "c_qs": c_qs})
