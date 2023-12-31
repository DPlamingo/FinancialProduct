from django.db import models
from django.contrib.auth.models import AbstractUser
from allauth.account.adapter import DefaultAccountAdapter
# from deposits.models import DepositProducts


# # Create your models here.
# class UserProfile(models.Model):
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     birth_date = models.DateField(null=True, blank=True)
#     gender = models.CharField(max_length=10, null=True, blank=True)


class User(AbstractUser):
    username = models.CharField(max_length=30, unique=True)
    nickname = models.CharField(max_length=255, blank=True, null=True)
    # first_name = models.CharField(max_length=30)
    # last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=6, choices=[('male', '남성'), ('female', '여성')], blank=True, null=True)
    birth_date = models.DateField(blank=True, null=True)
    email = models.EmailField(max_length=254, blank=True, null=True)
   
    # 리스트 데이터 저장을 위해 Text 형태로 저장
    financial_products = models.TextField(blank=True, null=True)
    # superuser fields
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    USERNAME_FIELD = 'username'

class CustomAccountAdapter(DefaultAccountAdapter):
    def save_user(self, request, user, form, commit=True):
        """
        Saves a new `User` instance using information provided in the
        signup form.
        """
        from allauth.account.utils import user_email, user_field, user_username
        # 기존 코드를 참고하여 새로운 필드들을 작성해줍니다.
        data = form.cleaned_data
        first_name = data.get("first_name")
        last_name = data.get("last_name")
        email = data.get("email")
        username = data.get("username")
        nickname = data.get("nickname")
        gender = data.get("gender")
        birth_date = data.get("birth_date")
    
        financial_product = data.get("financial_products")
        user_email(user, email)
        user.email = email  # 이 줄을 추가하세요.

        user_username(user, username)
        if first_name:
            user_field(user, "first_name", first_name)
        if last_name:
            user_field(user, "last_name", last_name)
        if nickname:
            user_field(user, "nickname", nickname)
        if gender:
            user_field(user, 'gender', gender)
        if birth_date:
            user_field(user, 'birth_date', birth_date.strftime('%Y-%m-%d'))

    
        if financial_product:
            financial_products = user.financial_products.split(',')
            financial_products.append(financial_product)
            if len(financial_products) > 1:
                financial_products = ','.join(financial_products)
            user_field(user, "financial_products", financial_products)
        if "password1" in data:
            user.set_password(data["password1"])
        else:
            user.set_unusable_password()
        self.populate_username(request, user)
        if commit:
            # Ability not to commit makes it easier to derive from
            # this adapter by adding
            user.save()
        return user
    

# class Like(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     financial_product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True)