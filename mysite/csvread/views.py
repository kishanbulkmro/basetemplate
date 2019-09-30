from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render , render_to_response
import pandas as pd
from django.db import transaction
from .models import UploadFileForm

# Create your controller here.

@transaction.atomic
def index(request):
    if request.method == 'POST':
        csv_file = request.FILES["myFile"]
        file_data = pd.read_csv(csv_file)
        data = pd.DataFrame(file_data).values.tolist()
        for i in data:
            newmodel = UploadFileForm(CompanyName = i[0] , CountryName = i[1] , StandNumber = i[2] , Address = i[3] , Website = i[4] , ProductCatogery =i[5] , Year = i[6] , Email = i[7] , Phone = i[8])
            newmodel.save()
    return render(request,'csvgetter.html')

def response(request):
    data = UploadFileForm.objects.all()

    stu = {
        "all_data": data
    }

    return render_to_response("profile.html", stu)

