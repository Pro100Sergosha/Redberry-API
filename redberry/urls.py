
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GeneralInfoViewset, ExperienceInfoViewset, EducationViewset, ResumeViewset

router = DefaultRouter()
router.register(r'general', GeneralInfoViewset)
router.register(r'experience', ExperienceInfoViewset)
router.register(r'education', EducationViewset)
router.register(r'resume', ResumeViewset)

urlpatterns = [
    path('', include(router.urls))
]
