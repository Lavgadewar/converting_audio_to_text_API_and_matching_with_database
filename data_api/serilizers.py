from rest_framework import serializers
from data_api.models import Audio

# Create the serializer class for the Audio model
class AudioSerializer(serializers.ModelSerializer):

     # Declare the audio_file field as a file field
    audio_file = serializers.FileField()
    
    # Specify the model and fields for the serializer
    class Meta:
        model = Audio
        fields = "__all__"