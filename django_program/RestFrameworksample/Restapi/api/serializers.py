
# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import ItemModel

# Create a model serializer
class ItemSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = ItemModel
        fields = ('name', 'description')