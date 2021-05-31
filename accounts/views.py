from django.shortcuts import render
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.models import CustomUser
from .forms import AccountUpdateForm
from django.urls import reverse_lazy
from django.contrib import messages


class MypageView(LoginRequiredMixin, generic.UpdateView):
    model = CustomUser
    template_name = 'mypage.html'
    form_class = AccountUpdateForm

    def get_success_url(self):
        return reverse_lazy('mypage', kwargs={'pk': self.kwargs['pk']})

    def form_valid(self, form):
        messages.success(self.request, 'ユーザー情報を更新しました')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'ユーザー情報を更新に失敗しました。')
        return super().form_invalid(form)