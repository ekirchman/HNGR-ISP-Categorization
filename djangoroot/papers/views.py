from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Document
from .forms import DocumentForm
# Create your views here.

def index(request):
    document_list = Document.objects.order_by("-year")[:5]
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

def upload_file(request):
    if request.method == 'POST':
        form = DocumentForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            document = form.save()
            form.save()
            return render(request, 'papers/upload_success.html', {"document": document} )
            #return HttpResponseRedirect("papers/upload_success.html")
            #return render(request, 'papers/upload_success.html')
    else:
        form = DocumentForm()
    return render(request, 'papers/upload.html', {'form': form})

