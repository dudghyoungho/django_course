from rest_framework import serializers
from core_app.models import Course, Department, Professor
from core_app.serializer.department import DepartmentSerializer
from core_app.serializer.professor import ProfessorSerializer


class CourseSerializer(serializers.ModelSerializer):
    department = DepartmentSerializer(read_only=True)
    department_id = serializers.PrimaryKeyRelatedField(queryset=Department.objects.all(),write_only=True)
    professor = ProfessorSerializer(read_only=True)
    professor_id = serializers.PrimaryKeyRelatedField(queryset=Professor.objects.all(),write_only=True)





    class Meta:
        model = Course
        fields = '__all__'
        read_only_fields = ['id']

    def create(self, validated_data):
        department_id = validated_data.pop('department_id')
        professor_id = validated_data.pop('professor_id')
        course = Course.objects.create(department=department_id, professor=professor_id, **validated_data)
        return course

