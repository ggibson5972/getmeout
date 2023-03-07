import json

from django.shortcuts import get_object_or_404, render, redirect
from django.template import loader
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
from urllib.request import urlopen
import re as r
from .google import search_engine
from decouple import config

API_KEY = config('API_KEY')
CSE_ID = config('CSE_ID')


def index(request):
    return render(request, 'index.html')


#  events
class EventList(APIView):

    def get(self, request):
        zipcode = _get_estimated_location()

        query_param: str = request.GET.get('zipcode', zipcode)
        if query_param:
            zipcode = query_param
        assert len(str(zipcode)) == 5, f'Invalid Zipcode: {zipcode}'

        # only get first 10 results
        payload = search_engine(f'salsa dancing events near {zipcode}', API_KEY, CSE_ID)[:10]
        return Response(payload)

    def post(self, request):
        data = request.data
        return render(request, 'events_list.html', data)


# Helper Methods

def _get_estimated_location():
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)
    return str(data['postal'])
