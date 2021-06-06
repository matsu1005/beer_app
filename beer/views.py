from beer.models import Beer, Review
from django.shortcuts import render
from django.views import generic
from django.db.models import Avg


class IndexView(generic.ListView):
	model = Beer
	template_name = 'index.html'

	def get_context_data(self, **kwargs):
		beers =Beer.objects.all()
		context = super().get_context_data(**kwargs)
		review_list = []
		for beer in beers:
			review_list.extend(list(beer.review_set.all().order_by('?')[:1].values_list('id', flat=True)))		
		context['review_list'] = Review.objects.filter(pk__in=review_list)
		# print(Beer.objects.random())
		return context


    # def get_queryset(self):
    #     queryset = super().get_queryset()
    #     # カテゴリを、紐づいた記事数と一緒に取得し、その記事数順に並び替え
    #     return queryset.annotate(beer_score=('post')).order_by('-post_count')
