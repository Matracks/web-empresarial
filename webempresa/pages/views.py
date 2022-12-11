from django.shortcuts import render, get_object_or_404
from .models import Page
from django.urls import reverse_lazy
from django.contrib.admin.views.decorators import   staff_member_required
from django.utils.decorators import method_decorator
from django.views.generic.edit import UpdateView
from django.views.generic.detail import DetailView
from .forms import PageForm

# Create your views here.


# def page(request, page_id, page_slug):
#     page = get_object_or_404(Page, id=page_id)
#     return render(request, 'pages/sample.html', {'page': page})

class PageDetailView(DetailView):
    model = Page


@method_decorator(staff_member_required, name='dispatch')
class PageUpdateView(UpdateView):
    model = Page
    form_class = PageForm
    template_name_suffix = '_update_form'

    def get_success_url(self):
        return reverse_lazy('page:update', args=[self.object.id, self.request.resolver_match.namespace]) + '?ok'