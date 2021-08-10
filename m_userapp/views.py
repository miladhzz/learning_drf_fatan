from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view()
def users(request):
    return Response({"test": "test1"})


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