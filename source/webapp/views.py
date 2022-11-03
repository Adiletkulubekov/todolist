from django.shortcuts import render
from webapp.models import Todolist


# Create your views here.
def todolist_view(request):
    all_todolist = Todolist.objects.all
    return render(request, 'index.html', {'all': all_todolist})
