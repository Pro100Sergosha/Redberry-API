import re
from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from .models import GeneralInfo, EducationInfo, ExperienceInfo, Resume


class GeneralInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = GeneralInfo
        fields = '__all__'
    
    def validate_email(self, value):
        if not value.endswith('redberry.ge'):
            raise serializers.ValidationError('Email must end with @redberry.ge')
        return value
    
    def validate_number(self, value):
        if not value.startswith('+995'):
            raise serializers.ValidationError('Phone number must start with +995')
        return value
    
    def validate(self, attrs):
        for atr in attrs:
            if attrs[atr] in ['name', 'last_name', 'bio'] and not re.match(r'^[\u10A0-\u10FF\s]+$', attrs[atr]):
                raise serializers.ValidationError('This text must be written in georgian')
        return attrs

class ExperienceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExperienceInfo
        fields = '__all__'
    

class EducationSerializer(serializers.ModelSerializer):
    class Meta:
        model = EducationInfo
        fields = '__all__'

class ResumeSerializer(WritableNestedModelSerializer):
    general = GeneralInfoSerializer(many = True)
    experience = ExperienceSerializer(many = True)
    education = EducationSerializer(many = True)
    class Meta:
        model = Resume
        fields = '__all__'