from rest_framework import serializers
from . import Task
from checkers.boardREST.board import Board


STATUSES = (
    'New',
    'Ongoing',
    'Done',
)


class TaskSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=256)
    owner = serializers.CharField(max_length=256)
    status = serializers.ChoiceField(choices=STATUSES, default='New')

    def create(self, validated_data):
        return Task(id=None, **validated_data)

    def update(self, instance, validated_data):
        for field, value in validated_data.items():
            setattr(instance, field, value)
        return instance

class BoardSerializer(serializers.Serializer):
    position = serializers.ListField(
        child=serializers.CharField(allow_blank=False, max_length=1, trim_whitespace=False), 
        min_length=32, 
        max_length=32)
    nextboards = serializers.ListField( 
        #child=serializers.ListField( child = serializers.CharField(trim_whitespace=False)),        
        #child=serializers.ListField( child = serializers.IntegerField())
        )

    #def create(self, validated_data):
     #   return None    