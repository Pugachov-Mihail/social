from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from .serializer import UserModelSerialize
from .models import UserModel
# Create your views here.


class UserList(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerialize(queryset, many=True)
    user = {
        "user": serializer_class.data
    }
    def get(self, request):

        return Response(self.user)

