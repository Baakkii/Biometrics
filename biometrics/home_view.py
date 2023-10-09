from django.http import HttpResponse
from django.template.loader import render_to_string
def Home(requset):
    response = render_to_string("biometrics/main.html"),
    return HttpResponse(response)