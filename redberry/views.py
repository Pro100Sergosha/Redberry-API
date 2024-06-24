from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import GeneralInfo, EducationInfo, ExperienceInfo
from .serializers import GeneralInfoSerializer

class GeneralInfoViewset(viewsets.ModelViewSet):
    queryset = GeneralInfo.objects.all()
    serializer_class = GeneralInfoSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
