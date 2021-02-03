from rest_framework import serializers

from users.models import User
from blog.models import Post


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username',)


class PostSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(source='pk', read_only=True)

    class Meta:
        model = Post
        fields = ('id', 'title', 'body', 'author', 'publish', 'status',)


class ListPostsSerializer(PostSerializer):
    author = UserSerializer(instance='blog_post', read_only=True)
