from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models.aggregates import Avg
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView, ListView

from WellnessNewProject.mixins import HostOnlyMixin
from bookings.models import Booking
from reviews.models import Review
from studio_classes.forms import StudioClassForm, TagsForm, StudioClassDeleteForm
from studio_classes.models import StudioClass, Tag


# Create your views here.
class StudioClassesCreateView(LoginRequiredMixin, HostOnlyMixin, CreateView):
    model = StudioClass
    form_class = StudioClassForm
    template_name = 'studio_classes/create-class.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)

class StudioClassesEditView(LoginRequiredMixin, HostOnlyMixin, UpdateView):
    model = StudioClass
    form_class = StudioClassForm
    template_name = 'studio_classes/edit-class.html'
    success_url = reverse_lazy('manage_page')

class StudioClassesDetailsView(LoginRequiredMixin, DetailView):
    model = StudioClass
    template_name = 'studio_classes/details-class.html'
    context_object_name = 'studio_class'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_booked'] = Booking.objects.filter(
            user=self.request.user,
            booked_class=self.object,
        ).exists()

        avg_rating = self.object.reviews.aggregate(
            Avg('rating')
        )['rating__avg']
        context['avg_rating'] = avg_rating

        return context

class StudioClassesDeleteView(LoginRequiredMixin, HostOnlyMixin, DeleteView):
    model = StudioClass
    form_class = StudioClassDeleteForm
    template_name = 'studio_classes/delete-class.html'
    success_url = reverse_lazy('manage_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = StudioClassDeleteForm(instance=self.object)
        return context

class ClassReviewListView(ListView):
    model = Review
    template_name = 'reviews/class-reviews.html'
    context_object_name = 'reviews'
    paginate_by = 9

    def get_queryset(self):
        self.studio_class = get_object_or_404(StudioClass, pk=self.kwargs['pk'])
        return Review.objects.filter(review_class=self.studio_class).order_by('-created_at')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['studio_class'] = self.studio_class
        return context

class TagsCreateView(LoginRequiredMixin, HostOnlyMixin, CreateView):
    model = Tag
    form_class = TagsForm
    template_name = 'tags/create-tag.html'
    success_url = reverse_lazy('manage_page')

class TagsDeleteView(LoginRequiredMixin, HostOnlyMixin, DeleteView):
    model = Tag
    template_name = 'tags/delete-tag.html'
    success_url = reverse_lazy('manage_page')