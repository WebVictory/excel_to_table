import pandas
import xlrd as xlrd
from django.shortcuts import render, redirect
import numpy as np
from data.models import Main
import logging


def tables(request):

    return render(request, 'tables.html')

def home(request):
    if request.method == "GET":

        return render(request, 'home.html')

    if request.method=='POST':
        #Обробатываем загруженный файл
        excel_file = request.FILES["excel_file"]
        source = pandas.read_excel(excel_file)
        head =list(source.columns)

        #Работаем с числовыми значенияим
        chec_numerics = ['int16', 'int32', 'int64', 'float16', 'float32', 'float64']
        numerics_head = source.select_dtypes(include=np.number).columns.tolist()
        another_head = set(head) - set(numerics_head)

        # print(numerics_head)
        numerics_data = [(row  **2) for row  in source[numerics_head].to_numpy()]

        # print (numerics_data)
        numerics_data = pandas.DataFrame(numerics_data)
        numerics_data.columns=numerics_head

        #Обновляем данные
        another_data =source[another_head]
        update_result = another_data.join(numerics_data)
        my_head = [
    {
        "title": "num1",
        "field": "num1"
    },
    {
        "title": "num2",
        "field": "num2"
    },
    {
        "title": "num3",
        "field": "num3"
    },
    {
        "title": "num4",
        "field": "num4"
    },
    {
        "title": "num5",
        "field": "num5"
    },
    {
        "title": "num6",
        "field": "num6"
    },
    {
        "title": "num7",
        "field": "num7"
    }
]
        #Работа с моделью
        r, c = source.shape
        obj = Main.objects.create(rows=r,columns = c)
        logger = logging.getLogger(__name__)
        logger.debug("Создан обьект: " +str(obj))

        update_result.to_json('data/static/data/data1.json',orient="records")
        return render(request, 'home.html',{'head':head})
