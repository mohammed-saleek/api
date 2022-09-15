from rest_framework import serializers
from django.contrib.auth import get_user_model # If used custom user model

UserModel = get_user_model()

class UserRegistrationSerializer(serializers.ModelSerializer):
    # password = serializers.CharField(write_only=True)
    password2 = serializers.CharField(style={'input_type':'password'},write_only=True)
    class Meta:
        model = UserModel
        fields = ['email', 'username', 'password','password2']
        # fields = ['email', 'username', 'password']
        extra_kwargs = {
            # 'first_name': {'required': True},
            # 'last_name': {'required': True},
            'password':{'write_only':True}
        }
    def save(self):
        user = UserModel.objects.create_user(
            username=self.validated_data['username'],
            password=self.validated_data['password'],
            email = self.validated_data['email'],    
        )
        password = self.validated_data['password']
        password2 = self.validated_data['password2']
        if password != password2:
            raise serializers.ValidationError({'password':'Password Must Match'})
        user.set_password(password)
        user.save()
        return user
 