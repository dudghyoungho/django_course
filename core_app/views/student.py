from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status

from core_app.models import Student
from core_app.serializer.student import StudentSerializer

def get_queryset(self):
    queryset = Student.objects.all()
    return queryset

class StudentListViewAPI(APIView):
    def get_queryset(self):
        queryset = Student.objects.select_related("department").all()
        return queryset

    def get(self, request):
        qs = self.get_queryset()
        serializer = StudentSerializer(qs, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StudentDetailAPIView(APIView):
    def get_queryset(self, pk):
        queryset = Student.objects.select_related("department").all()
        return queryset

    def get(self, request, pk):
        obj = self.get_object(pk)
        serializer = StudentSerializer(obj)
        return Response(serializer.data)

    def get_object(self, pk):
        try:
            obj = get_queryset(self).get(pk=pk)
            return obj
        except Student.DoesNotExist:
            raise Http404

    def put(self, request, pk):
        obj = self.get_object(pk)
        serializer = StudentSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        obj = self.get_object(pk)
        obj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)