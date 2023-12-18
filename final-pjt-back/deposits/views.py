from django.shortcuts import render
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import requests
from collections import defaultdict
from django.db.models import Count, Q
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.conf import settings
import requests
from .models import DepositProducts, DepositOptions
from .serializers import DepositProductSerializer, DepositOptionSerializer

api_KEY = settings.API_KEY
deposit_url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={api_KEY}&topFinGrpNo=020000&pageNo=1'
saving_url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={api_KEY}&topFinGrpNo=020000&pageNo=1'
@api_view(['GET'])
def index(request):
    response_deposit = requests.get(deposit_url).json()
    response_saving = requests.get(saving_url).json()
    save_deposit = [
        response_deposit,
        response_saving
    ]
    return Response(save_deposit)


# 예적금 상품 데이터베이스 저장 
@api_view(['GET'])
def save_deposit(request): 
    response_deposit = requests.get(deposit_url).json()
    response_saving = requests.get(saving_url).json()
    
    # 예금 상품 데이터 저장 ===========================================
    deposit_base_list = response_deposit["result"]['baseList']
    deposit_option_list = response_deposit['result']['optionList']

    base_serializer_data = []

    for li in deposit_base_list:
        fin_prdt_cd = li.get('fin_prdt_cd')
        if not DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            save_data = {
                'fin_prdt_cd' : li.get('fin_prdt_cd'),
                'kor_co_nm' : li.get('kor_co_nm'),
                'fin_prdt_nm' : li.get('fin_prdt_nm'),
                'etc_note' : li.get('etc_note'),
                'join_deny' : li.get('join_deny'),
                'join_member' : li.get('join_member'),
                'join_way' : li.get('join_way'),
                'spcl_cnd' : li.get('spcl_cnd'),
                'product_type' : '예금',
            }
            # 저장하기 위해 데이터를 포장
            base_serializer = DepositProductSerializer(data=save_data)

            if base_serializer.is_valid(raise_exception=True):
                base_serializer.save()
                
    base_serializer_data = DepositProductSerializer(DepositProducts.objects.all(), many=True).data
            
    for li in deposit_option_list:
        fin_prdt_cd = li.get('fin_prdt_cd')
        if DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            save_option = {
                'product' : DepositProducts.objects.get(fin_prdt_cd = li.get('fin_prdt_cd')).pk ,
                'fin_prdt_cd' : li.get('fin_prdt_cd'),
                'intr_rate_type_nm' : li.get('intr_rate_type_nm'),
                'intr_rate' : li.get('intr_rate'),
                'intr_rate2' : li.get('intr_rate2'),
                'save_trm' : li.get('save_trm'),
            }    
            # 저장하기 위해 데이터를 포장
            option_serializer = DepositOptionSerializer(data=save_option)
            if option_serializer.is_valid(raise_exception=True):
                option_serializer.save()
    
    # 적금 상품 데이터 저장 ============================================
    saving_base_list = response_saving["result"]['baseList']
    saving_option_list = response_saving['result']['optionList']

    for li in saving_base_list:
        fin_prdt_cd = li.get('fin_prdt_cd')
        if not DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            save_data = {
                'fin_prdt_cd' : li.get('fin_prdt_cd'),
                'kor_co_nm' : li.get('kor_co_nm'),
                'fin_prdt_nm' : li.get('fin_prdt_nm'),
                'etc_note' : li.get('etc_note'),
                'join_deny' : li.get('join_deny'),
                'join_member' : li.get('join_member'),
                'join_way' : li.get('join_way'),
                'spcl_cnd' : li.get('spcl_cnd'),
                'product_type' : '적금',
            }
            # 저장하기 위해 데이터를 포장
            base_serializer = DepositProductSerializer(data=save_data)

            if base_serializer.is_valid(raise_exception=True):
                base_serializer.save()
    
    base_serializer_data = DepositProductSerializer(DepositProducts.objects.all(), many=True).data

    for li in saving_option_list:
        fin_prdt_cd = li.get('fin_prdt_cd')
        if DepositProducts.objects.filter(fin_prdt_cd=fin_prdt_cd).exists():
            save_option = {
                'product' : DepositProducts.objects.get(fin_prdt_cd = li.get('fin_prdt_cd')).pk ,
                'fin_prdt_cd' : li.get('fin_prdt_cd'),
                'intr_rate_type_nm' : li.get('intr_rate_type_nm'),
                'intr_rate' : li.get('intr_rate'),
                'intr_rate2' : li.get('intr_rate2'),
                'save_trm' : li.get('save_trm'),
            }    
            # 저장하기 위해 데이터를 포장
            option_serializer = DepositOptionSerializer(data=save_option)
            if option_serializer.is_valid(raise_exception=True):
                option_serializer.save()


    return Response(base_serializer_data)


@api_view(['GET'])
def recommend_products_options(request):
    products = DepositOptions.objects.all()
    save_data_list = []
    code_names = set()  # 기존에 나온 회사 이름을 저장할 set
    for product in products:
        if product.fin_prdt_cd in code_names:  # 만약 해당 회사 이름이 이미 나온 적이 있다면 건너뜁니다.
            continue
        save_data = {
            'product_code': product.fin_prdt_cd,
            'period': product.save_trm,
            'interest_type': product.intr_rate_type_nm,
            'interest_rate': product.intr_rate,
        }

        save_data_list.append(save_data)
        code_names.add(product.fin_prdt_cd)
    
        
    return Response(save_data_list)


@api_view(['GET'])
def recommend_products(request):
    products = DepositProducts.objects.all()
    save_data_list = []
    company_names = set()  # 기존에 나온 회사 이름을 저장할 set
    for product in products:
        if product.fin_prdt_nm in company_names:  # 만약 해당 회사 이름이 이미 나온 적이 있다면 건너뜁니다.
            continue
        save_data = {
            'product_code': product.fin_prdt_cd,
            'company_name': product.kor_co_nm,
            'product_name': product.fin_prdt_nm,
            'etc_note': product.etc_note,
            'product_type': product.product_type,
        }


        save_data_list.append(save_data)
        company_names.add(product.kor_co_nm)
        
    return Response(save_data_list)


@api_view(['GET'])
def deposit_detail(request, fin_prdt_cd):
    deposit_info = get_object_or_404(DepositProducts, fin_prdt_cd=fin_prdt_cd)
    deposit_info_serializer = DepositProductSerializer(deposit_info)

    deposit_detail_info = DepositOptions.objects.filter(product_id=deposit_info.id)
    deposit_detail_info_serializer = DepositOptionSerializer(deposit_detail_info, many=True)

    deposit_detail_options_sorted = sorted(deposit_detail_info_serializer.data, key=lambda x: x['intr_rate'], reverse=True)
    highest_interest_option = deposit_detail_options_sorted[0] if deposit_detail_options_sorted else None


    serializer_data = {
        'deposit_detail' : deposit_info_serializer.data,
        'deposit_detail_options' : highest_interest_option
    }

    return Response(serializer_data, status=status.HTTP_200_OK)
