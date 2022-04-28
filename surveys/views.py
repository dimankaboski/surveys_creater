from django.shortcuts import render
from django.views.generic import CreateView, TemplateView, ListView, DetailView, View, FormView, UpdateView


class IndexPage(TemplateView):
    template_name = 'surveys/index.html'


class CreateSurvey(TemplateView):
    template_name = 'surveys/create.html'