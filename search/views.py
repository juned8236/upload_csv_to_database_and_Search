from django.shortcuts import render
from django.views.generic import ListView
from app.models import Test2

class SearchProductView(ListView):
    template_name = "view.html"

    def get_context_data(self, *args, **kwargs):
        context = super(SearchProductView, self).get_context_data(*args, **kwargs)
        query = self.request.GET.get('q')
        context['query'] = query
        print(context)
        # SearchQuery.objects.create(query=query)
        return context

    def get_queryset(self, *args, **kwargs):
        request = self.request
        method_dict = request.GET
        query = method_dict.get('q', None) # method_dict['q']
        print(query)
        if query is not None:
            return Test2.objects.search(query)
        return Test2.objects.all()
        '''
        __icontains = field contains this
        __iexact = fields is exactly this
        '''

# Create your views here.
