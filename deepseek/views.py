from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello You're at the deepseek home page.")
def soumya(request):
    return HttpResponse("Hello, world. You're at the soumya  page.")


