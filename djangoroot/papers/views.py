from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Document
# Create your views here.

def index(request):
    document_list = Document.objects.order_by("-pub_date")[:5]
    template = loader.get_template("papers/index.html")
    context = { "document_list": document_list  }
    return render(request, "papers/index.html", context)

def detail(request, document_id):
    #return HttpResponse("You're looking at document %s." % document_id)
    try:
        document = Document.objects.get(pk=document_id)
    except Document.DoesNotExist:
        raise Http404("Document does not exist")
    return render(request, "papers/detail.html", {"document": document})

