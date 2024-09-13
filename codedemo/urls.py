from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include("mainapp.urls"))
]


#코드 설명
#Server/DoorServer/urls,py에서 url을 호출함
'''
urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include('Server.DoorServer.urls',namespace="DoorServer")),
]
'''
