from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from core_app.models import Department
from core_app.serializer.department import DepartmentSerializer

def get_queryset(self):
    queryset = Department.objects.all()
    return queryset

class DepartmentListViewAPI(APIView):
    def get_queryset(self):
        queryset =  Department.objects.all()
        return queryset

    def get(self, request):
        qs = self.get_queryset()
        serializer = DepartmentSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = DepartmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DepartmentDetailAPIView(APIView):
    def get_queryset(self):
        queryset = Department.objects.all()
        return queryset

    def get_object(self, pk):
        try:
            obj = self.get_queryset().get(pk=pk)
            return obj
        except Department.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        obj = self.get_object(pk)
        serializer = DepartmentSerializer(obj)
        return Response(serializer.data)

    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = DepartmentSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

