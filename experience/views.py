from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# events/
class EventList(APIView):
    # lists all events
    def get(self, request):
        payload = {"body": "Hello world"}
        return Response(payload)
