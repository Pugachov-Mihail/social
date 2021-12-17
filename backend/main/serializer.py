from rest_framework import serializers
from .models import UserModel, PhotoFile, Hobbie



class PhotoFileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = PhotoFile
        fields = (
           "title",
            "url",
        )

class HobbieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hobbie
        fields = "__all__"


class UserModelSerialize(serializers.ModelSerializer):
    username = serializers.CharField()
    photo = PhotoFileSerializer(many=True, read_only=True)
    hobbies = HobbieSerializer(many=True, read_only=True)
    def save(self, **kwargs):
        user = UserModel(
            email=self.validated_data['email'],
            username=self.validated_data['username'])
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({password: "Пароли не совпадают"})
        user.set_password(password)
        user.save()
        return user

    class Meta:
        model = UserModel
        fields = (
            'username', "first_name", "last_name", "surname",
             "password", "password2", 'email', "photo", "hobbies"
        )

