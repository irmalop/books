from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny

from ..serializers import AuthorSerializer
class  AuthorViewSet(ModelViewSet):
    permission_classes = (AllowAny, )
    class_serializer = AuthorSerializer