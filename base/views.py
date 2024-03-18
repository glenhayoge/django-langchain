from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        query = request.POST.get('query')
        result = {}  # Here, we will get results from embeddings
        return JsonResponse(result)
    # Here, we will create a database if we don't have one as the user loads onto the page
    return render(request, 'base/index.html')