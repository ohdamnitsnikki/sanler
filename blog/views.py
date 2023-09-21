from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.views import generic, View
from django.urls import reverse
from django.http import HttpResponseRedirect


def index(request):
    # Get all the posts with images from the database
    return render(
        request, 'index.html')