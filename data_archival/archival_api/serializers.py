from rest_framework import serializers
from archival_api.models import ArchivedStudent, ArchivedTeacher

class ArchivedStudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchivedStudent
        fields = '__all__'

class ArchivedTeacherSerializer(serializers.ModelSerializer):
    class Meta:
        model = ArchivedTeacher
        fields = '__all__'


