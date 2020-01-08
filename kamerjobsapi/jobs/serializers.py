from rest_framework import serializers
from jobs.models import jobTitle, newJob



class jobTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = jobTitle
        fields = '__all__'

class newJobSerializer(serializers.ModelSerializer):  
    class Meta:
        model = newJob
        fields = '__all__'


