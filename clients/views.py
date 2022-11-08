from django.shortcuts import render
from django.db import connections

# Create your views here.
from django.shortcuts import render, redirect  
from clients.forms import ClientForm  
from clients.models import Client  
from django.template import RequestContext
# Create your views here.  
def clnt(request):  
    if request.method == "POST":  
        form = ClientForm(request.POST)  
        if form.is_valid():  
            try:  
                #form.save() 
                cid = request.POST['cid']
                name = request.POST['name']
                email = request.POST['email']
                contact = request.POST['contact']
                cursor = connections['default'].cursor()
                cursor.execute("insert into clients (cid,name,email,contact) VALUES ( %s , %s  , %s  , %s )", [cid,name,email,contact])                
                return redirect('/show')  
            except:  
                pass  
    else:    
        form = ClientForm() 
    return render(request,'index.html',{'form':form})  
def show(request):  
    client = Client.objects.raw('SELECT cid,name,email,contact,id FROM clients')
    #Only first raw 'Client.objects.raw('SELECT * FROM myapp_person')[0]'
    return render(request,"show.html",{'clients':client})  
def edit(request, id):  
    client = Client.objects.get(cid=id)  
    return render(request,'edit.html', {'clients':client})  
def update(request, id):  
    client = Client.objects.get(cid=id)  
    form = ClientForm(request.POST, instance = client)  
    if form.is_valid():  
        #form.save() 
        cid = request.POST['cid']
        name = request.POST['name']
        email = request.POST['email']
        contact = request.POST['contact']
        cursor = connections['default'].cursor()
        cursor.execute("update clients set name = %s, email = %s , contact = %s where cid = %s", [name,email,contact,cid])                    
        return redirect("/show")  
    return render(request, 'edit.html', {'clients':client})  
def error(request):
    return redirect('/error')        
def destroy(request, id):  
    cid = id
    cursor = connections['default'].cursor()
    cursor.execute("delete from clients where cid = %s", [cid]) 
    return redirect("/show")  