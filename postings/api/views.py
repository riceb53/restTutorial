from rest_framework import generics

from postings.models import BlogPost
from .serializers import BlogPostSerializer

class BlogPostRudView(generics.RetrieveUpdateDestroyAPIView):
    lookup_field = 'pk'
    queryset = BlogPost.objects.all()
    serializer_class = BlogPostSerializer

    def get_queryset(self):
        return BlogPost.objects.all()
    