from rest_framework import serializers 
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.name')

    class Meta:
        model = Profile
        fields = [
            'id', 'owner', 'name', 'created_at', 'bio','image'
        ]