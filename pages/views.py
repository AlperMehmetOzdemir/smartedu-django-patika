from django.shortcuts import render
from django.http import HttpResponse

def index():
  return HttpResponse("<h1>Index Sayfası</h1>")
