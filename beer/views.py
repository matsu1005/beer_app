from beer.models import Beer, Review
from django.urls import reverse_lazy
from django.contrib import messages
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import ReviewCreateForm
from django.http import JsonResponse


class IndexView(generic.ListView):
	model = Beer
	template_name = 'index.html'
	paginate_by = 8


	def get_context_data(self, **kwargs):
		beers =Beer.objects.all()
		context = super().get_context_data(**kwargs)
		review_list = []
		for beer in beers:
			review_list.extend(list(beer.review_set.all().order_by('?')[:1].values_list('id', flat=True)))		
		context['review_list'] = Review.objects.filter(pk__in=review_list)
		return context


class ReviewCreateView(LoginRequiredMixin, generic.CreateView):
	model = Review
	template_name = 'review_create.html'
	form_class = ReviewCreateForm
	success_url = reverse_lazy('beer:index')

	def form_valid(self, form):
		print(form)
		review = form.save(commit=False)
		review.user = self.request.user
		review.save()
		messages.success(self.request, 'レビューを投稿しました。')
		return super().form_valid(form)

	def form_invalid(self, form):
		messages.error(self.request, 'レビューの投稿に失敗しました。')
		return super().form_invalid(form)


class DetailView(generic.DetailView):
	model = Beer
	template_name = 'beer_detail.html'
	

def get_beer(request):
	beers = Beer.objects.all().values()
	reviews = []
	for beer in Beer.objects.all():
		reviews.extend(list(beer.review_set.all().order_by('?')[:1].values_list('id', flat=True)))		
	review_list = list(Review.objects.filter(pk__in=reviews).values())
	data_dict = {
		"beers" : list(beers),
		"review": review_list
	}
	return JsonResponse(data_dict, safe=False)