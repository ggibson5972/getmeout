import json

from decouple import config
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from urllib.request import urlopen
import requests
from yelpapi import YelpAPI

from event_aggregator.google import search_engine


API_KEY = config('API_KEY')
CSE_ID = config('CSE_ID')
EVENT_SEARCH_API_URL = config('YELP_EVENTS_API_URL')
YELP_API_KEY = config('YELP_API_KEY')


def index(request):
    return render(request, 'index.html')


def yelp_results(request):
    yelp_results = []
    with YelpAPI(YELP_API_KEY, timeout_s=3.0) as yelp_api:
        yelp_results = yelp_api.search_query(categories='dancestudio', location=zipcode)
    return render(request, 'yelp_results.html', context={'yelp_results': yelp_results})


#  events
class EventList(APIView):

    def get(self, request):
        zipcode = _get_estimated_location()

        query_param: str = request.GET.get('zipcode', zipcode)
        if query_param:
            zipcode = query_param
        assert len(str(zipcode)) == 5, f'Invalid Zipcode: {zipcode}'

        # only get first 10 results
        search_results: list = search_engine(f'salsa dancing events near {zipcode}', API_KEY, CSE_ID)[:10]
        # return Response(yelp_results)
        return render(request, 'events_list.html', context={'search_results': search_results})




# Helper Methods

def _get_estimated_location() -> str:
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)
    return str(data['postal'])
