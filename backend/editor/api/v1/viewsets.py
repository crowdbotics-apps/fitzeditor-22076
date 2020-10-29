from rest_framework import authentication
from editor.models import Editor
from .serializers import EditorSerializer
from rest_framework import viewsets


class EditorViewSet(viewsets.ModelViewSet):
    serializer_class = EditorSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Editor.objects.all()
