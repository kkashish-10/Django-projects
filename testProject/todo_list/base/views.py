from django.http import HttpResponse


# Create your views here.
def task_list(request):
    return HttpResponse('To do list')
