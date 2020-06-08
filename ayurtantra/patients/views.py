from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied 
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView, DeleteView, CreateView
from django.urls import reverse_lazy

from .models import Patient

# Create your views here.

class PatientListView(LoginRequiredMixin, ListView):
    model = Patient
    template_name = 'patient_list.html'
    login_url = 'login'

class PatientDetailView (LoginRequiredMixin, DetailView):
    model = Patient
    template_name = 'patient_detail.html'
    login_url = 'login'

class PatientUpdateView (LoginRequiredMixin, UpdateView):
    model = Patient
    fields = ('first_name','last_name','dob')
    template_name = 'patient_edit.html'
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.create_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class PatientDeleteView (LoginRequiredMixin, DeleteView):
    model = Patient
    template_name = 'patient_delete.html'
    success_url = reverse_lazy('patient_list')
    login_url = 'login'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.create_by != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

class PatientCreateView (LoginRequiredMixin, CreateView):
    model = Patient
    template_name = 'patient_new.html'
    fields = ('first_name', 'last_name','gender','dob')
    login_url = 'login'

# Following is an in-built form validation method. It is modified to pick create_by automatically.
# Will have to learn such things on our own.

    def form_valid (self, form):
        form.instance.create_by = self.request.user
        return super().form_valid(form)