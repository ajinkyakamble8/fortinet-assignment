from archival_api.serializers import ArchivedStudentSerializer, ArchivedTeacherSerializer
from archival_api.models import ArchivedStudent, ArchivedTeacher

MODEL_MAPPING = {
    'ArchivedTeacher': {
        'model': ArchivedTeacher,
        'serializer': ArchivedTeacherSerializer,
        'permissions': ['Teacher', 'Student'],
    },
    'ArchivedStudent': {
        'model': ArchivedStudent,
        'serializer': ArchivedStudentSerializer,
        'permissions': ['Student'],
    },
    # Add more models as needed
}

USER_PERMISSIONS = {
    'Teacher': ['ArchivedTeacher', 'ArchivedStudent'],
    'Student': ['ArchivedStudent']
}
