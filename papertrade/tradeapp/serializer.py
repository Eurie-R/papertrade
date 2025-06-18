from rest_framework import serializers
from . models import *

class ReactSerailizer(serializers.ModelSerializer):
    class Meta:
        model = React
        fields = ['trader']
