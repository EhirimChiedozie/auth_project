from rest_framework.views import APIView
from rest_framework import generics, status, mixins, viewsets
from rest_framework.response import Response
from .models import BlogPost, Comments
from .serializers import PostSerializer, CommentSerializer
from rest_framework.permissions import IsAuthenticated


class CreatePostView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        title = request.data.get('title')
        content = request.data.get('content')
        data = {
            'title':title,
            'content':content
        }
        serializer = PostSerializer(data=data)
        if serializer.is_valid():
            serializer.save(author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class PostListView(generics.ListCreateAPIView):
#     queryset = BlogPost.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated]


# class PostDetailView(generics.RetrieveDestroyAPIView):
#     queryset = BlogPost.objects.all()
#     serializer_class = PostSerializer
#     permission_classes = [IsAuthenticated]


class PostViewSet(viewsets.ModelViewSet):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer
    #permission_classes = [IsAuthenticated]
    

class UpdateBlogPost(mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DeleteBlogPost(generics.DestroyAPIView):
    queryset = BlogPost.objects.all()
    serializer_class = PostSerializer
    permission_classes = [IsAuthenticated]

#Comments
class CommentList(generics.ListCreateAPIView):
    serializer_class = CommentSerializer

    def get_queryset(self):
        post_id = self.kwargs['post_id']
        return Comments.objects.filter(post_id=post_id)

    def perform_create(self, serializer):
        post_id = self.kwargs['post_id']
        post = BlogPost.objects.get(id=post_id)
        serializer.save(post=post)