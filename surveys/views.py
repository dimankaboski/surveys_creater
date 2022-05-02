from django.shortcuts import redirect, render
from django.views.generic import CreateView, TemplateView, ListView, DetailView, View, FormView, UpdateView
from .models import Survey, Element


class IndexPage(TemplateView):
    template_name = 'surveys/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['surveys'] = Survey.objects.filter(created_by=self.request.user)
        return context

class CreateSurvey(TemplateView):
    template_name = 'surveys/create.html'

    def post(self, request):
        data = request.POST
        survey = Survey.objects.create(
            name=data.get('name'),
            description=data.get('text'),
            created_by=request.user,
        )
        prop = 0
        # raise Exception
        while data.get(f'el_id_{prop}'):
            element = Element.objects.create(
                type=data.get(f'el_type_{prop}'),
                name=data.get(f'el_name_{prop}'),
                survey=survey,
            )
            if element.type == Element.TYPE.ONE_IN_MANY:
                element.text = data.get(f'el_text_{prop}')
            elif element.type == Element.TYPE.MANY_IN_MANY:
                element.text = data.get(f'el_text_{prop}')
            elif element.type == Element.TYPE.TEXT:
                element.text = data.get(f'el_text_{prop}')
            elif element.type == Element.TYPE.STRING:
                element.text = data.get(f'el_text_{prop}')
            elif element.type == Element.TYPE.RANGE:
                element.range_from = data.get(f'el_range_min_{prop}')
                element.range_to = data.get(f'el_range_max_{prop}')
            element.required = False
            element.save()
            prop += 1
        
        return redirect('surveys:index')

class SurveyPublicOpened(DetailView):
    template_name = 'surveys/public.html'
    model = Survey