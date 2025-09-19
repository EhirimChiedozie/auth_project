from rest_framework import serializers
from .models import BlogPost, Comments



class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ['id', 'commenter', 'comment', 'date_posted']

class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    author = serializers.SlugRelatedField(read_only=True, slug_field='username')
    class Meta:
        model = BlogPost
        fields = ['title', 'content', 'date_posted', 'author', 'comments']