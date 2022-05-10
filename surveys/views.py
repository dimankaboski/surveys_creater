from cgitb import lookup
from django.shortcuts import redirect, render
from django.views.generic import CreateView, TemplateView, ListView, DetailView, View, FormView, UpdateView
from .models import Survey, Element, FilledSurvey, ElementValue


class IndexPage(TemplateView):
    template_name = 'surveys/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['surveys'] = Survey.objects.filter(created_by=self.request.user)
        return context

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('auth:login')
        return super().dispatch(request, *args, **kwargs)

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
                text='',
                survey=survey,
            )
            if element.type == Element.TYPE.ONE_IN_MANY:
                element.text = data.get(f'el_text_{prop}')
            elif element.type == Element.TYPE.MANY_IN_MANY:
                element.text = data.get(f'el_text_{prop}')
            elif element.type == Element.TYPE.RANGE:
                element.range_from = data.get(f'el_range_min_{prop}')
                element.range_to = data.get(f'el_range_max_{prop}')
            if data.get(f'el_required_{prop}') == '1':
                element.required = True
            else:
                element.required = False
            if request.FILES.get(f'el_file_{prop}'):
                element.file = request.FILES.get(f'el_file_{prop}')
            element.save()
            prop += 1
        
        return redirect('surveys:index')

    def dispatch(self, request, *args, **kwargs):
        if not request.user.is_authenticated:
            return redirect('auth:login')
        return super().dispatch(request, *args, **kwargs)

class SurveyPublicOpened(DetailView):
    template_name = 'surveys/public.html'
    model = Survey

    def post(self, request, pk):
        survey = self.get_object()
        user = request.user if request.user.is_authenticated else None
        filled_survey = FilledSurvey.objects.create(
            survey=survey,
            user=user
        )
        data = request.POST
        for prop in survey.element_set.all():
            if data.get(f'prop_{prop.id}'):
                if prop.type == Element.TYPE.MANY_IN_MANY:
                    ElementValue.objects.create(
                        survey=filled_survey,
                        element=prop,
                        value='\n'.join(data.getlist(f'prop_{prop.id}'))
                    )
                else:
                    ElementValue.objects.create(
                        survey=filled_survey,
                        element=prop,
                        value=data.get(f'prop_{prop.id}')
                    )
            else:
                ElementValue.objects.create(
                    survey=filled_survey,
                    element=prop,
                    value=''
                )
        return redirect('surveys:complete')


class SurveyPassingByUrl(DetailView):
    template_name = 'surveys/public.html'
    model = Survey

    def get_object(self, queryset=None):
        return Survey.objects.get(uuid=self.kwargs.get("uuid"))

    def post(self, request, uuid):
        survey = self.get_object()
        user = request.user if request.user.is_authenticated else None
        filled_survey = FilledSurvey.objects.create(
            survey=survey,
            user=user
        )
        data = request.POST
        for prop in survey.element_set.all():
            if data.get(f'prop_{prop.id}'):
                if prop.type == Element.TYPE.MANY_IN_MANY:
                    ElementValue.objects.create(
                        survey=filled_survey,
                        element=prop,
                        value='\n'.join(data.getlist(f'prop_{prop.id}'))
                    )
                else:
                    ElementValue.objects.create(
                        survey=filled_survey,
                        element=prop,
                        value=data.get(f'prop_{prop.id}')
                    )
            else:
                ElementValue.objects.create(
                    survey=filled_survey,
                    element=prop,
                    value=''
                )
        return redirect('surveys:complete')


class SurveyStatistic(DetailView):
    template_name = 'surveys/statistic.html'
    model = Survey

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filled_last'] = self.get_object().filledsurvey_set.last()
        return context


class SurveyStatisticFilled(DetailView):
    template_name = 'surveys/statistic_filled.html'
    model = Survey


class PassedSurveyDetail(DetailView):
    template_name = 'surveys/passed_survey.html'
    model = FilledSurvey


class PassedSurveyComplete(TemplateView):
    template_name = 'surveys/complete.html'