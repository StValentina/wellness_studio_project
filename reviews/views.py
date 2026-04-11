from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy

from studio_classes.models import StudioClass
from django.views.generic import CreateView, UpdateView, DeleteView
from reviews.forms import ReviewForm, ReviewDeleteForm
from reviews.models import Review


# Create your views here.

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/create-review.html'

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.review_class = get_object_or_404(StudioClass, pk=self.kwargs['pk'])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('details-class', kwargs={'pk': self.kwargs['pk']})

class ReviewEditView(UpdateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/edit-review.html'

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)

    def get_success_url(self):
        return reverse_lazy('details-class', kwargs={'pk': self.object.review_class.pk})

class ReviewDeleteView(LoginRequiredMixin, DeleteView):
    model = Review
    template_name = 'reviews/delete-review.html'
    context_object_name = 'review'

    def get_queryset(self):
        return Review.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ReviewDeleteForm(instance=self.object)
        return context

    def get_success_url(self):
        return reverse_lazy('details-class', kwargs={'pk': self.object.review_class.pk})