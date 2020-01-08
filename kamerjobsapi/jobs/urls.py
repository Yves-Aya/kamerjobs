from django.urls import path,include
from rest_framework import routers
from jobs.views import jobTitleViewSet, newJobViewSet

router = routers.DefaultRouter()
router.register(r'jobtitle', jobTitleViewSet)
router.register(r'newjob', newJobViewSet)

urlpatterns = [
    path('', include(router.urls)),   

]
