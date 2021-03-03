from django.shortcuts import render
# from django.shortcuts import render
# from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import View
# from django.views.generic import TemplateView
from homework.models import Answer


class Login(View):
    def get(self, request):
        pass

    def post(self, request):
        pass
