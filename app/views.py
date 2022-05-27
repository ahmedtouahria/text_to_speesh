from django.shortcuts import render
from .models import Text
# Create your views here.
def home(request):
    if request.method == "GET":
        try:
            sms_words = request.GET.get('sms').split(' ')
        except:
            sms_words=[]
        array_of_objects=[]
        for i in sms_words:
            sms_db = Text.objects.filter(contenu=i)
            if sms_db.count()>0:
                array_of_objects.append(sms_db)
        context={"smss":array_of_objects}
        print(array_of_objects)
    return render(request,"index.html",context)

