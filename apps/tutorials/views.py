from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from . import models as myModels
from django.core import serializers
from django.shortcuts import render


def detail(request):
    tutorials = myModels.Tutorial.objects.all()
    # template = loader.get_template("index.html")

    context = {
        "tutorials": tutorials,

    }

    return render(request, "index.html", context)
    # return HttpResponse(template.render(context, request))
