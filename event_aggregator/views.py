import json

from decouple import config
from django.shortcuts import render
from rest_framework.views import APIView
from urllib.request import urlopen

from event_aggregator.google import search_engine


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
        search_results: list = search_engine(f'salsa dancing events near {zipcode}', API_KEY, CSE_ID)[:10]
        # for image, ['pagemap']['cse_thumbnail'][0]['src']
        # return Response(search_results)
        return render(request, 'events_list.html', context={'search_results': search_results})


# Helper Methods

def _get_estimated_location() -> str:
    url = 'http://ipinfo.io/json'
    response = urlopen(url)
    data = json.load(response)
    return str(data['postal'])
