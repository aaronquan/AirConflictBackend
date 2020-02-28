"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest

from rest_framework import generics
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer

from flightapi.models import Airport
from flightapi.serializers import AirportSerializer

import flightapi.views as apiviews

class AirportListDetail(generics.ListAPIView):
    queryset = Airport.objects.all()
    serializer_class = AirportSerializer
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, request, *args, **kwargs):
        airports = self.get_queryset()
        return Response({'airports': airports, 'user':'asd'}, template_name='app/airports.html')

class AirportDetail(generics.RetrieveAPIView):
    queryset = Airport.objects.all()
    renderer_classes = [TemplateHTMLRenderer]
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        return Response({'airports': self.object, 'user': 'qwe'}, template_name='app/airport.html')

def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Home Page',
            'year':datetime.now().year,
        }
    )

def data(request):
    """Data page"""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/data.html',
        {
        }
    )

def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Contact',
            'message':'Your contact page.',
            'year':datetime.now().year,
        }
    )

def about(request):
    """Renders the about page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/about.html',
        {
            'title':'About',
            'message':'Your application description page.',
            'year':datetime.now().year,
        }
    )