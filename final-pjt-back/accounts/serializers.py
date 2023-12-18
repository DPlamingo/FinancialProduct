from rest_framework import serializers
from allauth.account import app_settings as allauth_settings
from allauth.account.adapter import get_adapter
from .models import User
from dj_rest_auth.registration.serializers import RegisterSerializer
from accounts.models import User
from django.contrib.auth import get_user_model

User = get_user_model()

class CustomRegisterSerializer(RegisterSerializer):
# 추가할 필드들을 정의합니다.
    nickname = serializers.CharField(
    required=False,
    allow_blank=True,
    max_length=255
    )
    first_name = serializers.CharField(
    max_length=30
    )
    birth_date = serializers.DateField()
    gender = serializers.ChoiceField(choices=[('male', '남성'), ('female', '여성')])
    financial_products = serializers.ListField(child=serializers.IntegerField(), required=False)

    def get_cleaned_data(self):
            return {
        'username': self.validated_data.get('username', ''),
        'password1': self.validated_data.get('password1', ''),
        'email': self.validated_data.get('email', ''),  # 이 줄을 추가하세요.
        'first_name': self.validated_data.get('first_name', ''),
        # 'last_name': self.validated_data.get('last_name', ''),
        'gender': self.validated_data.get('gender', ''),
        'birth_date': self.validated_data.get('birth_date', ''),
        'nickname': self.validated_data.get('nickname', ''),
        'financial_products': self.validated_data.get('financial_products', ''),
        }

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        return user
    

class UserSerializer(serializers.ModelSerializer):
    # gender = serializers.CharField(source='userprofile.gender')
    # birth_date = serializers.DateField(source='userprofile.birth_date')
    gender = serializers.CharField()  # 수정된 부분
    birth_date = serializers.DateField()
    
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'password', 'gender', 'birth_date']
        extra_kwargs = {'password': {'write_only': True}}

    def update(self, instance, validated_data):
        instance.first_name = validated_data.get('first_name', instance.first_name)
        instance.last_name = validated_data.get('last_name', instance.last_name)
        instance.set_password(validated_data.get('password', instance.password))
        instance.birth_date = validated_data.get('birth_date', instance.birth_date)
        instance.gender = validated_data.get('gender', instance.gender)

        instance.save()
        return instance


