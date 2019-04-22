from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt 
def index(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        return render(request, 'index.html', {'range': range(int(data['times'])), 'text': data['text']})
    return render(request, 'index.html')