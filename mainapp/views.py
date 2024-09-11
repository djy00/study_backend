from django.shortcuts import render

# Create your views here.
# views.py
from django.shortcuts import render

def home(request):
    # 'home.html'이라는 템플릿을 렌더링하고, 추가로 'context' 데이터를 전달합니다.
    return render(request, 'home.html', {'message': 'Hello from the new app!'})
