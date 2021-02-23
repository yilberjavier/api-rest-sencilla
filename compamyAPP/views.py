from django.views import View
from .models import Company
from django.http import JsonResponse
from django.forms import model_to_dict

# Create your views here.


# devuelve lista de todos los objetos y (tambien devuelve objetos filtados por el nombre)
class CompanyListView(View):
    def get(self, request):
        if('name' in request.GET):
            List = Company.objects.filter(name__contains=request.GET['name'])
        else:
            List = Company.objects.all()
        return JsonResponse(list(List.values()), safe= False)
        



# devuelve solo el objeto que pides atraves del id
class CompanyDetalView(View):
    def get(self, request, pk):
        company = Company.objects.get(pk=pk)
        return JsonResponse(model_to_dict(company))
        
    