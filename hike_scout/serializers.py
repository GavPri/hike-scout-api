from dj_rest_auth.serializers import UserDetailSerializer
from rest_framework import serializer

class CurrentUserSerializer(UserDetailSerializer):
    profile_id = serializers.ReadOnlyField(source='profile.id')
    profile_image = serializers.ReadOnlyField(source='profile.image.url')

    class Meta(UserDetailSerializer.Meta):
        fields = UserDetailSerializer.Meta.fields + (
            'profile_id', 'profile_image'
        )
