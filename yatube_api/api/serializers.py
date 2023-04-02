from rest_framework import serializers

from posts.models import Post, Group, Comment


class PostSeriazlier(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Post
        fields = ('id', 'text', 'pub_date', 'author', 'image', 'group')


class GroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = Group
        fields = ('id', 'title', 'slug', 'description')


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )
    post = serializers.SlugRelatedField(
        read_only=True,
        slug_field="pk"
    )

    class Meta:
        model = Comment
        fields = ('id', 'author', 'post', 'text', 'created')
