from django.shortcuts import render
from .models import Url, ParsingInfo
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import UrlSerialize
from django.http import HttpResponse
from django.views.generic import TemplateView
from .parser import Parser
import json
# Create your views here.


class UrlView(APIView):
    def get(self, request):
        urls = Url.objects.all()
        serializer = UrlSerialize(urls, many=True)
        return Response({"urls":serializer.data})

    def post(self, request):
        url = request.data
        serializer = UrlSerialize(data=url)
        if serializer.is_valid(raise_exception=True):
            url_save = serializer.save()
            return Response({"Success":"Done, you add: {}".format(url_save.url)})


def get_tittle(request):
    parser = Parser()
    db = ParsingInfo()
    if len(list(ParsingInfo.objects.all())) == 0:
        parser.parse_urls()
        status = "Готово к обработке. Обновите страницу"
        return render(request, "index.html", context={"parsing_info": "Здесь пока ничего нет :)", "parsing_status":status})
    else:
        data = list(ParsingInfo.objects.all())
        status = "Все URL отработаны успешно"
        #back = ParsingInfo.objects.all()
        #delete_all = back.delete()
        return render(request, "index.html", context={"parsing_info":data, "parsing_status":status})


    #b = parser.parse_urls()
    #data = {"parsing_info": b}
    #return render(request, "index.html", context=data)
