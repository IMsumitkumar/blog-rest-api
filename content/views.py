from django.shortcuts import render
from rest_framework.response import Response
from .models import Blog
from rest_framework.views import APIView
from rest_framework import generics , request
from .serializers import BlogSerializer

# Create your views here.
class BlogListView(generics.ListCreateAPIView):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


    # def get_queryset(self):
    
    #     req_data = self.request.data

    #     if req_data:
    #         return Blog.objects.filter(title__startswith=req_data.get('title'))

class BlogDetailView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


class BlogView(APIView):
    
    # only works in terminal - Printing in terminal
    def get(self, request):

        req_data = request.data

        if req_data:
            
            query_set = Blog.objects.filter(title__startswith=req_data.get('title'))
            # print("qury",query_set)
        
            serializer = BlogSerializer(query_set, many=True)

            return Response(data=serializer.data)

        else:

            
            return Response(data='sumit')

    # queryset = Blog.objects.all()
    # serializer_class = BlogSerializer

    