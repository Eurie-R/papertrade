from django.shortcuts import render
from rest_framework.views import APIView
from . models import *
from rest_framework.response import Response 
from . serializer import *
from rest_framework.decorators import api_view
from . alpaca_client import *
from alpaca.data.requests import CryptoBarsRequest
from alpaca.data.timeframe import TimeFrame
import pandas as pd

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

@api_view(['GET'])
def liveMarket(request):
    request_params = CryptoBarsRequest(
        symbol_or_symbols=['BTC/USD'],
        timeframe=TimeFrame.Day, 
    )
    btc_bars = crypto_client.get_crypto_bars(request_params)
    ctx = {'btc':btc_bars.df}
    return render(request,'livemarket.html', ctx)

def strategyManagement(request):
    return render(request,'strategymanagement.html')

@api_view(['GET'])
def getData(request):
    person = {'name':'Dennis', 'age':28}
    return Response(person)

@api_view(['POST'])
def addItem(request):
    return Response()


