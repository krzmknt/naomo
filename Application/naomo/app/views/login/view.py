from django.http import HttpResponse
from django.http.request import HttpRequest
from django.template import loader


def top(request: HttpRequest):
    template = loader.get_template("login/index.html")
    return HttpResponse(template.render({}, request))

