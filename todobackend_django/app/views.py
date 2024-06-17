from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Todo
from .serializers import TodoSerializer

# Create your views here.

@api_view(['GET', 'POST'])
def todo_list(request):
    """
    List all todos, or create a new todo
    """
    if request.method == 'GET':
        todos = Todo.objects.all()
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.saved()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.error, status=status.HTTP_400_BAD_REQUEST)
