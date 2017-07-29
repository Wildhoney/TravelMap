from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from api.models import Country
from api.serializers import CountrySerializer

def country_list(request):
    """
    List all of the countries and associated country codes.
    """
    if request.method == 'GET':
        snippets = Country.objects.all()
        serializer = CountrySerializer(snippets, many=True)
        return JsonResponse(serializer.data, safe=False)
