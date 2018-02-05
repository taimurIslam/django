from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import device
from .serializers import deviceSerializer
import datetime
from django.shortcuts import render
# Create your views here.


class DeviceList(APIView):
    def get(self, request):
        devices = device.objects.all()
        serializer = deviceSerializer(devices, many = True)
        return Response(serializer.data)
    def post(self, request):
        pass

def DeviceMatch (request, id):
    # return HttpResponse("You're looking at device id %s." % id)
    #now_Time = datetime.datetime.now()

    queries = list(device.objects.values())
    #print(queries)
    for number_Of_Devices in range(len(queries)):
        #print(queries[number_Of_Devices]['device_ID'])
        if queries[number_Of_Devices]['device_ID'] == id:
            #time_Difference = queries[number_Of_Devices]['time'] - now_Time
            return HttpResponse("You're looking at token number = '" + str(queries[number_Of_Devices]['token_Number']) + "' for device id = " + str(id)
                                +' last hit in time =   '+ str(queries[number_Of_Devices]['time']))

    else:
        return HttpResponse("Your Device is not registered")

def login(request):
    return render(request, 'login\login.html')

def registration(request):
    return render(request, 'registration\\registration.html')
