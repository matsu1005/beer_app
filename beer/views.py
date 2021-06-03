from beer.models import Beer
from django.shortcuts import render
from django.views import generic


class IndexView(generic.ListView):
	model = Beer
	template_name = 'index.html'

	def get_queryset(self):
		beers = Beer.objects.filter(origin_place = '長野県')
		return beers

