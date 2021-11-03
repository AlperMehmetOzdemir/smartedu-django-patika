from django.shortcuts import render
from django.views.generic.list import ListView
from teachers.models import Teacher


class TeacherListView(ListView):
  model = Teacher
  template_name = "teachers.html"
  
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context["teachers"] = Teacher.objects.all().order_by("name")
    return context
  

# def teacher_list(request):
#   teachers = Teacher.objects.all().order_by("name")

#   context = {
#     "teachers": teachers,
#   }

#   return render(request, "teachers.html", context)
