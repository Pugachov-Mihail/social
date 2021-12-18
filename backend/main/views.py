from djangochannelsrestframework import permissions
from rest_framework.generics import ListAPIView, RetrieveAPIView, RetrieveUpdateAPIView, CreateAPIView, \
    RetrieveDestroyAPIView
from rest_framework.response import Response

from .serializer import UserModelSerialize, HobbieSerializer
from .models import UserModel, Hobbie
# Create your views here.


class UserList(ListAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerialize(queryset, many=True)
    user = {
        "user": serializer_class.data
    }
    def get(self, request):
        return Response(self.user)

class CreateUser(CreateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerialize
    #permission_classes = [permissions.AllowAny]

    def post(self, request, *args, **kwargs):
        serializer = UserModelSerialize(data=request.data)
        data = {}
        if serializer.is_valid():
            print(request.data)
            serializer.save(data=request.data)
            data['response'] = True
            return Response(data, status=201)
        else:
            data = serializer.errors
            return Response(data, status=400)


class ProfilUserView(RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerialize

class ProfilUpdateView(RetrieveUpdateAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerialize


#Create and destroy Hobbies

class HobbiesUsersView(RetrieveAPIView):
    queryset = UserModel.objects.all()
    serializer_class = UserModelSerialize


#Сделать завтра создание хобби от пользователя
class HobbiesUsersView(CreateAPIView):
    queryset = Hobbie.objects.all()
    serializer_class = HobbieSerializer

    def get_queryset(self):
        user = self.kwargs['pk']
        print("Ndsadasdasdas", user)
        try:
            return Hobbie.objects.filter(id=user)
        except:
            return Response(status=self.serializer_class.errors)


class HobbiesDestroy(RetrieveDestroyAPIView):
    queryset = Hobbie.objects.all()
    serializer_class = HobbieSerializer

class HobbiesUsersUpdateView(RetrieveUpdateAPIView):
    serializer_class = HobbieSerializer

    def get_queryset(self):
        user = self.kwargs['pk']
        print("Ndsadasdasdas", user)
        try:
            return Hobbie.objects.filter(id=user)
        except:
            return Response(status=self.serializer_class.errors)