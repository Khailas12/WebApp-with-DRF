from .models import User
from rest_framework import serializers
from phonenumber_field.serializerfields import PhoneNumberField


class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(max_length=25)
    email = serializers.EmailField(max_length=50)
    phone_number = PhoneNumberField(allow_null=False, allow_blank=False)
    password = serializers.CharField(min_length=8)
    
    
    class Meta:
        model = User
        fields = [
            'username',
            'email',
            'password',
            'phone_number',
        ]
        
    def validate(self, attrs):
        username_exists = User.objects.filter(username=attrs['username']).exists()
        email_exists = User.objects.filter(username=attrs['email']).exists()
        phonenumber_exists = User.objects.filter(username=attrs['phone_number']).exists()
        password_exists = User.objects.filter(username=attrs['password']).exists()
        
        if username_exists or email_exists or phonenumber_exists or password_exists:
            raise serializers.ValidationError(detail='User already exists')
        
        return super().validate(attrs)