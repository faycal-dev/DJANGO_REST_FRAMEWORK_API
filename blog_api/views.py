from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from blog.models import Post
from .serializers import PostSerializer
from rest_framework.parsers import MultiPartParser, FormParser, FileUploadParser
from rest_framework.permissions import AllowAny, DjangoModelPermissions, IsAdminUser, BasePermission, IsAuthenticated, SAFE_METHODS

class PostUserWritePermission(BasePermission):
    message = "Editing post is restricted the author only!"
    
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            # SAFE_METHODS is a tuple with get options and head in it
            return True
        return obj.author == request.user

class PostList(generics.ListCreateAPIView):
    permission_classes = [AllowAny] 
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

# we can do get and patch like this 
class PostDetail(generics.RetrieveUpdateDestroyAPIView, PostUserWritePermission):
    permission_classes = [PostUserWritePermission]
    queryset = Post.postobjects.all()
    serializer_class = PostSerializer

# we can do patch like this   
class updatePost(APIView, PostUserWritePermission):
    permission_classes = [AllowAny]
    
    def patch(self, request, id):
        post = Post.objects.get(id=id)
        post.content = request.data.get("content",post.content)
        post.title = request.data.get("title",post.title)
        if post:
            post.save()
            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)

class CreatePostWithImage(APIView):
    permission_classes = [AllowAny]
    parser_classes = [MultiPartParser, FormParser]
    
    def post(self, request, format=None):
        print(request.data)
        request.data["author"] = request.user.id
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)