import re
from rest_framework import serializers
from .models import GeneralInfo, EducationInfo, ExperienceInfo


class GeneralInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInfo
        fields = '__all__'

    def validate_name(self, value):
        if not re.match(r'^[\u10A0-\u10FF\s]+$', value):
            raise serializers.ValidationError('Name must be in georgian')
        return value
    
    def validate_last_name(self, value):
        if not re.match(r'^[\u10A0-\u10FF\s]+$', value):
            raise serializers.ValidationError('Last name must be in georgian')
        return value
    
    def validate_bio(self, value):
        if not re.match(r'^[\u10A0-\u10FF\s]+$', value):
            raise serializers.ValidationError('Bio must be in georgian')
        return value
    
    def validate_email(self, value):
        if not value.endswith('redberry.ge'):
            raise serializers.ValidationError('Email must end with @redberry.ge')
        return value
    
    def validate_number(self, value):
        if not value.startswith('+995'):
            raise serializers.ValidationError('Phone number must start with +995')
        return value