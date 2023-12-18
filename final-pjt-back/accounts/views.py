from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth.hashers import make_password
# from accounts.models import Like
from deposits.models import DepositProducts

# Create your views here.
from accounts.models import User
from rest_framework import status, serializers
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework import permissions
from rest_framework.generics import RetrieveUpdateAPIView
from .serializers import UserSerializer
from django.contrib.auth import get_user_model



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username','first_name', 'nickname', 'password', 'email', 'gender', 'birth_date']

    def update(self, instance, validated_data):
        # 비밀번호가 제공되었을 때, 비밀번호를 암호화해서 저장
        password = validated_data.pop('password', None)
        if password is not None:
            instance.set_password(password)
        return super().update(instance, validated_data)
    

class UserUpdateView(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated,]

    def get_object(self):
        return self.request.user

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)  # partial=True allows partial updates
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)

        if getattr(self, 'swagger_fake_view', False):
            return Response(serializer.data)

        return Response(serializer.data, status=status.HTTP_200_OK)



class DeleteUserView(APIView):
    permission_classes = [IsAuthenticated]

    def delete(self, request):
        user = User.objects.get(username=request.user.username)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

# def UserProfileView(request):
#     user = request.user
#     serializers = UserSerializer(user)
#     return Response(serializers.data)

# class UserUpdateView(RetrieveUpdateAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [permissions.IsAuthenticated,]

#     def get_object(self):
#         return self.request.user

#     def update(self, request, *args, **kwargs):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)  # partial=True allows partial updates
#         serializer.is_valid(raise_exception=True)
#         self.perform_update(serializer)

#         if getattr(self, 'swagger_fake_view', False):
#             return Response(serializer.data)

#         return Response(serializer.data, status=status.HTTP_200_OK)

User = get_user_model()

@api_view(['GET'])
def account_detail(request):

    user = request.user

    serializer = UserSerializer(user)
    data = serializer.data

    if data['gender'] == 'male':
        data['gender'] = '남성'
    elif data['gender'] == 'female':
        data['gender'] = '여성'

    return Response(data)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def account_update(request):
    
    new_password = request.data.get('new_password')

    if new_password is None:
        return Response({"error": "New password is not provided"}, status=status.HTTP_400_BAD_REQUEST)

    # 새 비밀번호를 암호화하여 저장합니다.
    request.user.password = make_password(new_password)
    request.user.save()
    
    return Response({"success": "Password updated successfully"}, status=status.HTTP_200_OK)


# @api_view(['POST', 'DELETE'])
# @permission_classes([IsAuthenticated])
# def likes(request):
#     user = request.user
#     product_code = request.data.get('product_code')

#     if product_code is None:
#         return Response({"error": "Product code is not provided"}, status=status.HTTP_400_BAD_REQUEST)

#     product = DepositProducts.objects.get(code=product_code)

#     if request.method == 'POST':
#         Like.objects.create(user=user, financial_product=product)
#         return Response({"success": "Like created successfully"}, status=status.HTTP_200_OK)
    
#     elif request.method == 'DELETE':
#         Like.objects.filter(user=user, financial_product=product).delete()
#         return Response({"success": "Like deleted successfully"}, status=status.HTTP_200_OK)