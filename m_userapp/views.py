from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from django.contrib.auth.models import User
from django.core import serializers


@api_view(['GET', 'POST'])
def calc(request):
    try:
        if request.method == "POST":
            num1 = request.data['num1']
            num2 = request.data['num2']
            if num1 - num2 < 0:
                return Response({"result": "Navigate"}, status=status.HTTP_400_BAD_REQUEST)
            return Response({"result": "Positive"}, status=status.HTTP_200_OK)
        return Response({"result": "GET"}, status=status.HTTP_200_OK)
    except KeyError:
        return Response({"result": "Error"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_user(request):
    user_serializer = serializers.UserSerializer(data=request.data)

    if user_serializer.is_valid():
        user_serializer.save()
        return Response({"result": "OK"}, status=status.HTTP_201_CREATED)
    return Response({"result": "Error"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def all_user(request):
    users = User.objects.all()
    json_users = serializers.serialize('json', users)
    return Response(data=json_users, status=status.HTTP_200_OK)

