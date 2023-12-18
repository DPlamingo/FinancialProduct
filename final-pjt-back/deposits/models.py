from django.db import models
# from django.conf import settings


class DepositProducts(models.Model):
    # 금융 상품 코드 
    fin_prdt_cd = models.TextField(unique=True)
    # 금융회사명
    kor_co_nm = models.TextField()
    # 금융 상품명
    fin_prdt_nm = models.TextField()
    # 금융 상품 설명
    etc_note = models.TextField()
    # 가입 제한(1: 제한없음, 2:서민전용, 3:일부제한)
    join_deny = models.IntegerField() 
    # 가입대상
    join_member = models.TextField() 
    # 가입 방법
    join_way = models.TextField() 
    # 우대 조건
    spcl_cnd = models.TextField()
    # 상품 구분(예금, 적금)
    product_type = models.CharField(max_length=10)


class DepositOptions(models.Model):
    # 외래 키(DepositProducts 클래스 참조)
    product = models.ForeignKey(DepositProducts, on_delete=models.CASCADE)
    # 금융 상품 코드
    fin_prdt_cd = models.TextField()  
    # 저축금리 유형명
    intr_rate_type_nm = models.CharField(max_length=100) 
    # 저축금리
    intr_rate = models.FloatField(null=True)  
    # 최고우대금리
    intr_rate2 = models.FloatField(default=-1, null=True) 
    # 저축기간 (단위: 개월)
    save_trm = models.IntegerField() 