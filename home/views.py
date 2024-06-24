from django.shortcuts import render,redirect
from django.http import HttpResponse

import pandas as pd
from .models import uploadExcel
# Create your views here.
def wellcome(request):
    # return HttpResponse("Wellcome to uplloder")
    
    if request.method == 'POST'and request.FILES.get('excel_file') :
        name = request.POST.get('name')
        excel_file = request.FILES['excel_file']
        
        uploaded_excel = uploadExcel(name=name, excel_file=excel_file)
        # return render (request, "index.html")
        uploaded_excel.save()
        return redirect('display_file', file_id=uploaded_excel.id)
    return render(request, 'index.html')


def display_file(request,file_id):
    try:
        # print("try bloack")
        
        uploaded_excel = uploadExcel.objects.get(id=file_id)
        file_path = uploaded_excel.excel_file.path
        data = pd.read_excel(file_path)
        print(type(data))
        print(data)
        '''
        # this code is not useble in current way that I have code;
        datadict=data.to_dict()# for rendering html data must be in dictionary 
        print(datadict)
        print(type(data))
        print(data)
        # for i in data:
        #     print(i)
        #     print(type(i))
        '''
        message="<h2>This is Excel File</h2>"
        data_html = data.to_html()
        # html_response = f"{message}{data_html}"
        datatohttpresponce=f"{message}{data_html}"
        return HttpResponse(datatohttpresponce)
        # return render (request,'index.html',datadict=datadict)  # if we want to display though render html, but its idoal for predefine data means excel file that have in same format (columns, heading)
    except Exception as e:  
        print("The error is",e)
        return HttpResponse("Error")