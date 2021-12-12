#Main/views.py

from django.shortcuts import render
from django.http import HttpResponse , HttpResponseRedirect ,  HttpRequest 
from .models import Item, ToDoList
from .forms import CreateNewList , CreateTasks
from django.contrib.auth.models import User

# Create your views here.


def profile(response):
    out = {}
    if (response.user):
        if response.user.is_authenticated :
            print("voici !!!!!!",response.user._do_insert)
            uUserName = response.user.username
            uMail = response.user.email
            #uSex = response.user.sex
            uSex = ""
            td=response.user.todolist.all()
            print(td)
            print("user name : " , uUserName)
           
            
            print("email : " , uMail)
            
            out = {"uUserName" : uUserName,"uMail" :uMail , "uSex" : uSex }
            
            print(out)
    else:
        pass
   
    # for td in user.todolist_set 
		
		# td.id
	
	
    
    return render(response,"main/profile.html",out)

def home(response):
    if(response.user.is_active):
        listnumbTab = 0
        ConditionToDleteItems=0
        TdToDel_id = 0
        listnumb=0
        ToDoLists=ToDoList.objects.all()
        
        for td in response.user.todolist.all(): 
            if td.id != None:
                listnumb = listnumb +1 
        
        
        if response.method=="POST":
            
           
            
            
            
            if response.POST.get("save"):
                
                print(response.POST)
                print("###########################") 
                
                for Td in ToDoLists:
                    

                    
                    ConditionToDleteTd = 0 
                    
                    for Item in Td.item_set.all():
                        print("###########################")
                        
                    
                        if response.POST.get("c"+str(Item.id))=="clicked":
                            print("******")
                            
                            #print("task  ' " + str(Item) + " ' of todolist : ' " +str(td.name)+ " ' clicked")
                            Item.complete = True
                            Item.save()
                             
                            
                            
                           
                        else :
                            print("////")
                            #print("task ' " + str(Item) + " '  of todolist ' " +str(td.name)+ " ' unclicked")
                            Item.complete =False 
                            Item.save()
                            
                        
                        
                        
                       
                        
                        if response.POST.get("del"+str(Item.id))=="clicked":
                            
                            #print("task  ' " + str(Item) + " ' of todolist : ' " +str(td.name)+ " ' clicked")
                            Item.delet = True
                        else :
                            Item.delet = False #print("task ' " + str(Item) + " '  of todolist ' " +str(td.name)+ " ' unclicked")
                        
                        Td.save()

                        if Item.delet == True:
                            ConditionToDleteTd = ConditionToDleteTd+1
                            print("*********")
                            
                            print(Item.id)
                            print(Item.delet)
                            
                            #Item_ = ToDo.objects.get(pk = Item.id )
                            print("///////////////////////////")
                            print(str(Td.item_set.get(pk=Item.id)) + "deleted")
                            TdDelete = Td.item_set.get(pk=Item.id)
                            TdDelete.delete()
                        
                    
                    
                    print("Voici la condition DelTd : " + str(ConditionToDleteTd))
                    print("Voici le nombre items de la Td : " + str(Td.item_set.all().count()))
                    Td.save()
                    if ConditionToDleteTd >= 0 and Td.item_set.all().count() == 0:
                            print("je suis la")
                            Td.delete()
                            
                    listnumb=0       
                    for td in ToDoLists: 
                        if td.id != None:
                            listnumb = listnumb +1 
                    
                    # for Td in ToDoLists:
                        # if Td.delet==True:
                            # Td.delete()
     
                        
                        

                            
                    
                    
                    
                        
                     
                    
                    
                    
                    
                
                        
                        
                    
            elif response.POST.get("newItem"):
                print(response.POST.get)
                idFirst=ToDoList.objects.all().first().id
                idLast =ToDoList.objects.all().last().id
                TdClicked_id = response.POST.get('newItem').split(":")[1]
                TdClicked_Ordre = int(TdClicked_id)-idFirst+1
                Text_List = response.POST.getlist('new')
                Text_Task=""
                print("Text_List" , Text_List)
                
                IdList = []
                
                
                
                for Td in response.user.todolist.all():
                    IdList.append(Td.id)
                
                
                print(IdList)
                j=0
                for k in Text_List :
                    
                    if Text_List[j]=="":
                        print(str(j+1) + "emty")
                        Text_Task = k
                        print(k)
                        
                    else:
                        print(str(j+1) + "full")
                        Text_Task = k
                        print(k)
                        if len(Text_Task)>3 :
                            t = response.user.todolist.get(id=IdList[j])
                            t.item_set.create(text=Text_Task, complete=False, delet = False)
                            print ("text correcrt")
                            print("voici la TD : " , response.user.todolist.get(id=IdList[j]))
                            
                        else:
                            print("text non valid")
                    j=j+1
                
                    print(Text_Task)
                
                
                
                
                # print( Text_List[int(TdClicked_Ordre-1)])
                
                
                print("yes")
                # if len(Text_Task) > 3 :
                    # pass
                    # t = ToDoList.objects.get(id=TdClicked_id)
                    # t.item_set.create(text=Text_Task, complete=False, delet = False)
                    # print(t.name)
                # else : 
                    # pass
                    # print("text non valide")

            elif response.POST.get("delItem"):
            
                
                 
                
                TdToDel_id = int(response.POST.get("delItem").split(":")[1])
                t = ToDoList.objects.get(id=TdToDel_id)
                ConditionToDleteItems = 1
                print("want to delete from : ")
                print(t.name)
                for item in t.item_set.all():
                    print("zzzzzzzzzzzzzzzzz")
                    if response.method=="POST":
                        print("yes")
                        print(ConditionToDleteItems)
                        
                listnumb=0       
                for td in ToDoLists: 
                    if td.id != None:
                        listnumb = listnumb +1 
                 
                
                
                
        
            
            else:
                pass
        
        
        
       
        
        #print("ConditionToDleteItems  " + str(ConditionToDleteItems))
        #print("from ID : " + str(TdToDel_id))
    
        return render(response,"main/home.html",{"ToDoLists":ToDoLists,"ConditionToDleteItems":ConditionToDleteItems,"TdToDel_id":TdToDel_id,"listnumb":listnumb,"listnumbTab":listnumbTab} )
    else:
        return render(response,"main/home.html")
    
    
    
    
    
    
    
    
    
def create(response):
    if response.method == "POST":
        print("yes in the post")
        
        if response.POST.get("create"):
            NewNameList = response.POST.get('NewListName')
        
           
            if len(NewNameList) > 3 : 
                #t= ToDoList(name=NewNameList)
                response.user.todolist.create(name=NewNameList)
               
            
            
            else:
                print("text non valid")
            
            return HttpResponseRedirect("/home/")
        
        
        
        elif response.POST.get("cancel"):
            print("yes in the cancel")
            return HttpResponseRedirect("/home/")
        else:
            pass
            
            
    else:
        pass
        # form = CreateNewList()
        # form1 =CreateTasks()
    
    #return render(response,"main/create.html",{"form":form,"form1":form1})
    return render(response,"main/create.html")
    