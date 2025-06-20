from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response 
from . serializer import *

class ReactView(APIView):
    def get(self, request):
        output = [{"trader": output.trader
                   for output in React.objects.all()}]
        return Response(output)
    
    def post(self, request):
        serializer = ReactSerailizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

def liveMarket(request):
    return render(request,'livemarket.html')

def strategyManagement(request):
    return render(request,'strategymanagement.html')