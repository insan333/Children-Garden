from django.shortcuts import render
from django.views.generic import View
from .models import Educator,Children,Children_Garden

class MainView(View):
    children_garden=Children_Garden.objects.all()
    def get(self, request):
        return render(request, template_name="main/main.html",context={'children_garden':self.children_garden})




class Children_Garden1View(View):
    educator=Educator.objects.filter(children_garden_id=1)
    def get(self, request):
        return render(request, template_name="main/children_gardens1.html",context={'educators':self.educator})
class Children_Garden2View(View):
    educator=Educator.objects.filter(children_garden_id=2)
    def get(self, request):
        return render(request, template_name="main/children_gardens2.html",context={'educators':self.educator})
class Children_Garden3View(View):
    educator=Educator.objects.filter(children_garden_id=3)
    def get(self, request):
        return render(request, template_name="main/children_gardens3.html",context={'educators':self.educator})


class Educator1View(View):
    educator=Children.objects.filter(educator_id=1)
    def get(self, request):
        return render(request, template_name="main/educators1.html",context={'educators':self.educator})
class Educator2View(View):
    educator=Children.objects.filter(educator_id=2)
    def get(self, request):
        return render(request, template_name="main/educators2.html",context={'educators':self.educator})
class Educator3View(View):
    educator=Children.objects.filter(educator_id=3)
    def get(self, request):
        return render(request, template_name="main/educators3.html",context={'educators':self.educator})
class Educator4View(View):
    educator=Children.objects.filter(educator_id=4)
    def get(self, request):
        return render(request, template_name="main/educators4.html",context={'educators':self.educator})
class Educator5View(View):
    educator=Children.objects.filter(educator_id=5)
    def get(self, request):
        return render(request, template_name="main/educators5.html",context={'educators':self.educator})
class Educator6View(View):
    educator=Children.objects.filter(educator_id=6)
    def get(self, request):
        return render(request, template_name="main/educators6.html",context={'educators':self.educator})
class Educator7View(View):
    educator=Children.objects.filter(educator_id=7)
    def get(self, request):
        return render(request, template_name="main/educators7.html",context={'educators':self.educator})
class Educator8View(View):
    educator=Children.objects.filter(educator_id=8)
    def get(self, request):
        return render(request, template_name="main/educators8.html",context={'educators':self.educator})
class Educator9View(View):
    educator=Children.objects.filter(educator_id=9)
    def get(self, request):
        return render(request, template_name="main/educators9.html",context={'educators':self.educator})