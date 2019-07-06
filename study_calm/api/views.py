from django.http import HttpResponse


def index(request):
    return HttpResponse("<h1>Hello, World!</h1>")

def tester(request):
    return HttpResponse("<h1>TESTER!</h1>")