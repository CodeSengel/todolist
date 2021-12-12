from main.models import Item, ToDoList
t= ToDoList(name="Mehdi List") #créer une todolist object
t.save()                       #sauvegarder
ToDoList.objects.all()         #afficher tous les objects
ToDoList.objects.get(id=1)     #afficher l'objet dont l'ID = 1
ToDoList.objects.get(name="Mehdi List") #afficher l'objet avec le nom
ToDoList.objects.all().first().id      # renvoyer l'ID du la première ligne 
ToDoList.objects.all().last().id       # renvoyer l'ID du la première ligne 

Td.item_set.all().count()

t.item_set.all()               #afficher les éléments de la liste
t.item_set.create(text="Read book 1 ", complete=False) # crer une tache dans la la todoliste (tant que ce n'est pas réaliser ==> Flase)
t.item_set.create(text=" play foot ", complete=True)
t.item_set.all().first().id
t.item_set.all().last().id
t.delete()
t.objects.filter(name__startswith="M") # filtrer les éléments qui commencent par M


"""
auth_user schema 
id
password
last_login
is_superuser
username
last_name
email
is_staff
is_active
date_joined
first_name


"""




















