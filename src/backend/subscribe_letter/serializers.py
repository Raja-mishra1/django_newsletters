from rest_framework import serializers
from .models import Newsletter



class NewsletterSerializer(serializers.ModelSerializer):
    """[Serializer to convert Newsletter model output to json]

    Args:
        serializers ([type]): [django serializers]
    """
    class Meta:
        model = Newsletter
        fields = ('firstname','email','agree','timestamp')