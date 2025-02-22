from rest_framework.response import Response
from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.views import APIView
from rest_framework import viewsets, status
from rest_framework.exceptions import ValidationError

from tutorial.quickstart.serializers import GroupSerializer, UserSerializer

from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken

from django.contrib.auth.models import Group
from .permissions import MODEL_MAPPING, USER_PERMISSIONS

class CustomTokenObtainPairView(TokenObtainPairView):
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        access_token = response.data.get("access")
        return Response({"access_token": access_token})  # Return access token

class RPCView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        model_type = request.data.get('model_type')
        action = request.data.get('action')
        data = request.data.get('data')

        # Check if the user has the appropriate role to access the model
        if not self.has_permission(request.user, model_type):
            raise ValidationError("You do not have permission to perform this action.")

        # Dynamic model resolution
        model, serializer_class = self.get_model_and_serializer(model_type)

        # Perform action based on the type and action requested
        if action == 'list':
            return self.list_objects(model, serializer_class)
        else:
            raise ValidationError("Invalid action.")
    
    def get_model_and_serializer(self, model_type):
        if model_type in MODEL_MAPPING:
            return MODEL_MAPPING[model_type]['model'], MODEL_MAPPING[model_type]['serializer']
        else:
            raise ValidationError("Invalid model type.")

    def has_permission(self, user, model_type):
        """Check if the user has permission to access the model type."""
        if model_type not in MODEL_MAPPING:
            raise ValidationError("Invalid model type.")
        
        user_groups = user.groups.values_list('name', flat=True)
        
        return any(model_type in USER_PERMISSIONS[user_group] for user_group in user_groups)
        
    def list_objects(self, model, serializer_class):
        objects = model.objects.all()
        serializer = serializer_class(objects, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

