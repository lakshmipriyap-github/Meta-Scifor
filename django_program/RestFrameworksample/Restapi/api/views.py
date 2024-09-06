# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import ItemSerializer
from .models import ItemModel


# create a viewset
class ItemViewSet(viewsets.ModelViewSet):
    # define queryset
    queryset = ItemModel.objects.all()
    # specify serializer to be used
    serializer_class = ItemSerializer