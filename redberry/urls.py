from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import GeneralInfoViewset

router = DefaultRouter()
router.register(r'general', GeneralInfoViewset)

urlpatterns = [
    path('api/', include(router.urls))
]
