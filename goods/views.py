from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from goods.models import ProductInfo
from goods.serializers import ProductInfoSerializer

@api_view(['GET','POST'])
def goods_list(request):

    if request.method == 'GET':
        infos = ProductInfo.objects.all()
        serializer = ProductInfoSerializer(infos,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductInfoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
    # elif request.method == 'DELETE':
    #     pass


@api_view(['GET','PUT','DELETE'])
def goods_detail(request,pk):
    try:
        info = ProductInfo.objects.get(code = pk)
    except ProductInfo.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductInfoSerializer(info)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = ProductInfoSerializer(info,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        info.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
