
from . models import Car
from rest_framework import viewsets
from . serializers import CarSerializer
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAdminUser
from . permissions import AllForAdminOtherReadOnly
from rest_framework import filters


class CarViewSet(viewsets.ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = [filters.SearchFilter]
    search_fields = ['brand', 'email','year',]
# Create your views here.
