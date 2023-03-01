from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .google_search import google


API_KEY = "AIzaSyCsBmUzB-KWShCbWHCWTOKSYbGjHFd8s2M"
CSE_ID = "361ef2027456b4ed6"


#  events


class EventList(APIView):

    def get(self, request):
        zipcode = request.GET.get('zipcode', '')
        assert len(zipcode) == 5, "Invalid Zipcode"
        payload = google(f'salsa dancing events {zipcode}', API_KEY, CSE_ID)
        return Response(payload)


# def events_view(request):
#     location = - request.GET['zipcode']
