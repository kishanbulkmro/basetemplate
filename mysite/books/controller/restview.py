from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from ..models import Book
from ..serializers import BookSerializer

@api_view(['GET', 'DELETE', 'PUT' ])
def get_delete_update_book(request, pk):
    puppy = Book.objects.get(pk=pk)
    print(puppy)
    # get details of a single puppy
    if request.method == 'GET':
        serializer =  BookSerializer(puppy)
        return Response(serializer.data)

    # update details of a single puppy
    if request.method == 'PUT':
        serializer = BookSerializer(puppy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # delete a single puppy
    if request.method == 'DELETE':
        puppy.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)



@api_view(['GET' , 'POST'])
def post_Books(request,queryset=None):
    puppy = Book.objects.all()

    # get details of a single puppy
    if request.method == 'GET':
        serializer =  BookSerializer(puppy,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = BookSerializer(puppy, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

