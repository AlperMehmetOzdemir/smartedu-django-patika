from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic import DetailView
from courses.models import Course
from teachers.models import Teacher


class TeacherListView(ListView):
  model = Teacher
  template_name = "teachers.html"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["teachers"] = Teacher.objects.all().order_by("name")
    return context
  
class TeacherDetailView(DetailView):
  model = Teacher
  template_name="teacher.html"
  context_object_name = "teacher"

  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["courses"] = Course.objects.filter(available=True, teacher=self.kwargs["pk"] ).order_by("date")
    return context
