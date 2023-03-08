from django.shortcuts import render
from django.http import *
from chatDb.models import *
# Create your views here.

def showDashboard(request):
    content={}
    content['username']=request.GET['username']
    chatList1=Connections.objects.all().filter(user1=content['username'])
    chatList2=Connections.objects.all().filter(user2=content['username'])
    # chatList1.append(chatList2)
    content['chatList1']=chatList1
    content['chatList2']=chatList2
    # print(type(chatList1))
    # print(type(chatList2))
    # print(chatList[0].user2)
    # print(chatList2)
    # for userList in chatList1 :
    #     for userT in userList :
    #         content['chatList']+=list(userT)    
            # for user in userT :
            #     content['chatList']+=user+"\n"        
    # print(content['chatList'])
    # for i in content['chatList']:
    #     print(i)
    # content['chatList']=(" ".join(line) for line in chatList1)
    # print(type(chatList1))
    # content['chatList']=" ".join(list(chatList1))
    # return HttpResponse(request)
    return render(request, "dashboard.html",{'user':content})