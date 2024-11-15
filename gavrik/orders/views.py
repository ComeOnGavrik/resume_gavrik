# views.py
from django.http import JsonResponse
from django.shortcuts import render


def basket_adding(request):
    return_dict = dict()
    session_key = request.session.session_key
    print(request.POST)
    print('_____________________________________________________')
    return JsonResponse(return_dict)
