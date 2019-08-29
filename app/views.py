from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from app.models import Test2
from django.contrib import messages
import csv,io

import request
# Create your views here.
def upload_csv(request,*args,**kwargs):
    template="upload.html"
    prompt={
    'order':"order should be :   "
    }
    if request.method=='GET':
        return render(request,template,prompt)

    csv_file=request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.error(request,'this is not valid')

    data_set = csv_file.read().decode('UTF-8')
    io_string=io.StringIO(data_set)
    next(io_string)
    for column in csv.reader(io_string,delimiter=','):
        print(column)
        _,created=Test2.objects.update_or_create(
        Id =column[0],
        Age =column[1],
        Job  =column[2],
        Marital   =column[3],
        Education  =column[4],
        Default =column[5],
        Balance  =column[6],
        HHInsurance  =column[7],
        CarLoan  =column[8],
        Communication  =column[9],
        LastContactDay   =column[10],
        LastContactMonth   =column[11],
        NoOfContacts    =column[12],
        DaysPassed    =column[13],
        PrevAttempts   =column[14],
        Outcome  =column[15],
        CallStart =column[16],
        CallEnd   =column[17],
        CarInsurance     =column[18])
    context={}
    return render(request,template,context)
    # kjsdklj
