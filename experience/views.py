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


    # # lists all events
    # @api_view(['GET'])
    # def get_hello_world(self, request):
    #     payload = {"body": "Hello world"}
    #     return Response(payload)

    def get(self, request):
        # location = '33403'
        # if request.GET['zipcode']:
        #     location = str(request.GET['zipcode'])
        # elif request.GET['city']:
        #     location = str(request.GET['city'])
        payload = google("salsa dancing events", API_KEY, CSE_ID)
        return Response(payload)


# def events_view(request):
#     location = - request.GET['zipcode']
