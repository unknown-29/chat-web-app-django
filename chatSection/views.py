from django.shortcuts import render,redirect
from django.http import *
from chatDb.models import *
from django.views.decorators.csrf import csrf_exempt
from django.utils import *
from datetime import datetime
# from 
# Create your views here.

def getSenderReceiver(request, user):
    # print(Connections.objects.all().values())
    user['user1']=request.GET['user1']
    user['user2']=request.GET['user2']
    # user['sub']=request.GET.get('sub')
    # request.POST._mutable=True
    # if request.POST.get('hidden') is not None:
        # print(request.POST.get('hidden'))
        # request.POST['hidden']="nothid" # request.POST['hidden']="nothid"
        # post=request.POST.copy()
        # print(post['hidden']+"=>")
        # post['hidden']='nothid'
        # print("**"+request.POST.get('hidden'))
    # if user['sub']=
    # print(user['sub']+"=>")
    # try:
    #     user['sub']=request.GET['sub']
    # except MultiValueDictKeyError:
    #     user['sub']=False
    return

def getConnectionId(request, user):
    # need to check in both ways => l1, l2
    l1=Connections.objects.all().filter(user1=user['user2'],user2=user['user1'])
    l2=Connections.objects.all().filter(user1=user['user1'],user2=user['user2'])
    print(user['user1'])
    print(user['user2'])
    if l1.first():
        print(l1.first().connection_id)
        return l1.values()
    else:
        print(l2.first().connection_id)
        return l2.values()
    # try:
    #     return Connections.objects.all().filter(user1=user['user2']).values()
    # except Connections.DoesNotExist:
    #     try:
    #         return Connections.objects.all().filter(user1=user['user1']).values()
    #     except Connections.DoesNotExist:
    #         return None # connections does not exist
    # if Connections.objects.all().get(user1=user['user2']).connection_id is None:
    #     if Connections.objects.all().get(user1=user['user1']).connection_id is not None:
    #         print(Connections.objects.all().get(user1=user['user1']).connection_id)
    #         # return Connections.objects.all().get(user1=user['user1']).connection_id
    #     else:
    #         print(None)
    #         # return None
    # else:
    #     print(Connections.objects.all().get(user1=user['user2']).connection_id)
    #     # return Connections.objects.all().get(user1=user['user2']).connection_id

@csrf_exempt
def showMessages(request):
    # print("hello")
    # print(request.POST['hidden'])
    user={}
    # user['user1']=request.GET['user1']
    # user['user2']=request.GET['user2']
    getSenderReceiver(request, user)
    # print(user['hid'])
    # user['sub']=False
    # connectionId=list(Connections.objects.only().filter(user1=user['user1'],user2=user['user2']).values_list('connection_id'))
    connectionId=getConnectionId(request, user).first().get("connection_id")
    # print(connectionId.index("0"))
    # print(" ".join(line) for line in connectionId)
    # print(type(connectionId) is list)
    # print(connectionId)
    # print(i for i in co/nnectionId)
    # Messages(connection_id=connectionId,message=)
    user['messages']=Messages.objects.all().filter(connection_id=connectionId).order_by('timestamp')
    arrangeMessagesDetails(user)
    # print(user['messages'][12][0])
    # print(type(Connections.objects.get(connection_id=connectionId)) is Connections)
    # return HttpResponse(request)
    # post=request.POST.copy()
    # post['message']="hjafbabjasbdjchjfdhb"
    return render(request,"chat.html",{'users':user})

# adding csrf_exempt annotation you don't need to specify {% csrf_token %} in your html
@csrf_exempt
def send(request):
    user={}
    getSenderReceiver(request, user)
    # user['sub']=True
    # print(request.POST.get('hidden') if request.POST.get('hidden') is not None else "hey")
    # print(request.POST.get("btn") if request.POST.get("btn") is not None else "hey")
    # if request.POST.get("hidden") is not None and request.POST.get("hidden")=="nothid":
        # user['hidden']="hid"
        # request.POST._mutable=True
        # request.POST['hidden']="hid"
        # message=request.POST['message']
        # print(getConnectionId(request, user).first().get("connection_id"))
        # print(request.POST['message']+" "+request.GET['user1']+" "+request.GET['user2'])
        # print(Connections.objects.only().get(user1=user['user1'],user2=['user2'],connection_id=getConnectionId(request, user).first().get("connection_id")))
    connection_id=getConnectionId(request, user).first().get("connection_id")
    print(connection_id)
    print(user['user1'])
    print(user['user2'])
    if connection_id is not None:
        message=Messages(
            connection_id=Connections.objects.get(connection_id=connection_id),
            sender=User.objects.all().get(username=user['user1']),
            message=request.POST['message'],
        )
        message.save()
        # request.POST['message']=None
        # print(request.POST['message'])
        # user['sub']=False
        return redirect("/chatWebApp/dashboard/chatSection/tmp?user1="+user['user1']+"&user2="+user['user2'])
    else:return HttpResponseBadRequest(request)
    # else:return showMessages(request)
    # else:return showMessages(request)
    # return HttpResponse(request)

def arrangeMessagesDetails(user):
    user['senderMessages']=list()
    user['receiverMessages']=list()
    for msg in user['messages']:
        # print(msg.timestamp=="2023-03-01 11:40:12.857751+00:00")
        # here msg is a tuple with one element which are actual texts shared between users
        if str(msg.sender)==str(user['user1']):
            user['senderMessages'].append(msg)
        else:
            user['receiverMessages'].append(msg)
            
    # print(user['messages'][0].sender.username==user['user1'])
    return

@csrf_exempt
def deletemsg(request):
    connection_id=request.GET['conid']
    s=request.GET['time'].split('/')
    timestamp=s[0]+" "+s[1]+"."+s[2]
    # print(timestamp)
    # print(datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f"))
    # print(timestamp+"----")
    
    # deleting the message
    Messages.objects.all().filter(connection_id=connection_id,timestamp=datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f")).delete()
    
    return redirect("/chatWebApp/dashboard/chatSection/tmp?user1="+request.GET['user1']+"&user2="+request.GET['user2'])

@csrf_exempt
def tmp(request):
    return showMessages_tmp(request)

def getConnections(user):
    user['con01']=list()
    user['con02']=list()
    user['con1']=Connections.objects.all().filter(user1=user['user1'])
    user['con2']=Connections.objects.all().filter(user2=user['user1'])
    for u in user['con1']:
        print(User.objects.all().get(username=u.user1).username)
        user['con01'].append(User.objects.all().get(username=u.user2))
    for u in user['con2']:
        print(User.objects.all().get(username=u.user1).username)
        user['con02'].append(User.objects.all().get(username=u.user1))
    # print(i for i in user['con01'])
    # print(i.username for i in user['con02'])   
    # user['con1']['last']=Messages.objects.all().get(connection_id=getConnectionId(request, user).first().get("connection_id"),sender=user['user2'])
    # user['con2']['last']=Messages.objects.all().get(connection_id=getConnectionId(request, user).first().get("connection_id"),sender=user['user2'])
    return
    
@csrf_exempt
def showMessages_tmp(request):
    # print("hello")
    # print(request.POST['hidden'])
    user={}
    # user['user1']=request.GET['user1']
    # user['user2']=request.GET['user2']
    getSenderReceiver(request, user)
    # print(user['hid'])
    # user['sub']=False
    # connectionId=list(Connections.objects.only().filter(user1=user['user1'],user2=user['user2']).values_list('connection_id'))
    connectionId=getConnectionId(request, user).first().get("connection_id")
    # print(connectionId.)
    # print(connectionId.index("0"))
    # print(" ".join(line) for line in connectionId)
    # print(type(connectionId) is list)
    # print(connectionId)
    # print(i for i in co/nnectionId)
    # Messages(connection_id=connectionId,message=)
    user['messages']=Messages.objects.all().filter(connection_id=connectionId).order_by('timestamp')
    arrangeMessagesDetails(user)
    getConnections(user)
    # print(user['messages'][12][0])
    # print(type(Connections.objects.get(connection_id=connectionId)) is Connections)
    # return HttpResponse(request)
    # post=request.POST.copy()
    # post['message']="hjafbabjasbdjchjfdhb"
    return render(request,"chat_tmp.html",{'users':user})

@csrf_exempt
def deletechat(request):
    user={}
    getSenderReceiver(request, user)
    
    connection_id=getConnectionId(request, user).first().get("connection_id")
    Messages.objects.all().filter(connection_id=connection_id).delete()
    return showMessages_tmp(request)

@csrf_exempt
def searchUser(request):
    user={}
    getSenderReceiver(request, user)
    search=request.GET['search']
    # print(search+" =====")
    return HttpResponse(search)