from django.contrib.auth.models import User
from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.contrib.messages.views import SuccessMessageMixin

from pages.forms import ContactForm
from courses.models import Course
from teachers.models import Teacher

class IndexView(TemplateView):
  template_name = "index.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["courses"] = Course.objects.filter(available=True).order_by("-date")[:2]
    context["total_courses"] = Course.objects.filter(available=True).count()
    context["total_users"] = User.objects.count()
    context["total_teachers"] = Teacher.objects.count()

    return context

class AboutView(TemplateView):
  template_name = "about.html"

class ContactView(SuccessMessageMixin, FormView):
  template_name = "contact.html"
  form_class = ContactForm
  success_url = reverse_lazy("contact")
  success_message = "We recieved your request"

  def form_valid(self, form) :
    form.save()
    return super().form_valid(form)
