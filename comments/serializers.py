from rest_framework import serializers 
from .models import Comments

class CommentsSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    is_owner = serializers.SerializerMethodField()
    profile_id = serializers.ReadOnlyField(source='owner.profile.id')
    profile_image = serializers.ReadOnlyField(source='owner.profile.image.url')

    def get_is_owner(self, obj):
        request = self.context['request']
        return request.user == obj.owner

    class Meta:
        model = Comments
        fields = [
            'id', 'owner', 'is_owner', 'profile_id',
            'profile_image', 'created_at','content'
            'is_owner', 'updated_at'
        ]

class CommentsDetailSerializer(CommentsSerializer):
    post = serializers.ReadOnlyField(source='post.id')