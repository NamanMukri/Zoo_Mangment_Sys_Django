
from django.http import JsonResponse,HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from animals import models
import datetime

def querytodict(obj_queryset):
    dict1=list(obj_queryset.values())[0]
    return dict1
    
#for Mammals
@csrf_exempt
def mammals(request):
    if request.method=="GET":
        entries=models.Mammal.objects.all()
        data=[]
        for entry in entries:
            data1=[entry.name,entry.species,entry.gender,entry.food]
            data.append(data1)
        return JsonResponse({"data":data})
            
    if request.method=="POST":
        new_mammal=json.loads(request.body)
        models.Mammal.objects.create(name=new_mammal["name"],species=new_mammal["species"],gender=new_mammal["gender"].upper(),food=new_mammal["food"])
        return JsonResponse({"Created":{"name":new_mammal["name"]}})
#for particular mammal
@csrf_exempt
def mammal(request,name):
    obj1= models.Mammal.objects.filter(name=name)
    if obj1:
        data=querytodict(obj1)
        if request.method=="GET":
            res={
                    "name":data["name"],
                    "species":data["species"],
                    "gender":data["gender"],
                    "food":data["food"]
                    
                    }        
            return JsonResponse(res,safe=False)
        if request.method=="POST":
            new_mammal=json.loads(request.body)
            models.Mammal.objects.create(name=new_mammal["name"],species=new_mammal["species"],gender=new_mammal["gender"].upper(),food=new_mammal["food"])
            return JsonResponse({"Created":{"name":new_mammal["name"]}})

        if request.method=="PUT":            
            obj1.update(last_feed_time=datetime.datetime.now())
            return JsonResponse({"Feeded":data["name"]})
    
        if request.method=="DELETE":            
            obj1.delete()
            return JsonResponse({"Deleted ":data["name"]})            
    
    else:
        return HttpResponse(f"{name} is not in zoo,Please enter another name")
            
#for Birds         
@csrf_exempt
def birds(request):
    if request.method=="GET":
        entries=models.Bird.objects.all()
        data=[]
        for entry in entries:
            data1=[entry.name,entry.species,entry.food]
            data.append(data1)
        return JsonResponse({"data":data})
            
    if request.method=="POST":
        new_bird=json.load(request.body)
        models.Bird.objects.create(name=new_bird["name"],species=new_bird["species"],food=new_bird["food"])
        return JsonResponse({"Created":{"name":new_bird["name"]}})
#for particular bird
@csrf_exempt
def bird(request,name):
    obj1= models.Bird.objects.filter(name=name)     
    if obj1:
        data=querytodict(obj1)
        if request.method=="GET":                
            res={
                "name":data["name"],
                "species":data["species"],
                "food":data["food"],
                }        
            return JsonResponse(res,safe=False)           
                      
        if request.method=="POST":
            new_bird=json.loads(request.body)
            models.Bird.objects.create(name=new_bird["name"],species=new_bird["species"],food=new_bird["food"])
            return JsonResponse({"Created":{"name":new_bird["name"]}})

        if request.method=="PUT":                
            obj1.update(last_feed_time=datetime.datetime.now())                
            return JsonResponse({"Feeded":data["name"]})
            
        if request.method=="DELETE":                
            obj1.delete()
            return JsonResponse({"Deleted ":data["name"]})
    else:
        return HttpResponse(f"{name} is not in zoo,Please enter another name")
#for Fishes
@csrf_exempt
def fishes(request):
    if request.method=="GET":
        entries=models.Fish.objects.all()
        data=[]
        for entry in entries:
            data1=[entry.color,entry.species,entry.food,entry.count]
            data.append(data1)
        return JsonResponse({"data":data})
            
    if request.method=="POST":
        new_fish=json.loads(request.body)
        models.Fish.objects.create(color=new_fish["color"],species=new_fish["species"],food=new_fish["food"],count=new_fish["count"])
        return JsonResponse({"Created":{"species":new_fish["species"]}})
#for particular fish
@csrf_exempt
def fish(request,species):
    obj1= models.Fish.objects.filter(species=species)     
    if obj1:
        data=querytodict(obj1)
        if request.method=="GET":        
            res={
                "color":data["color"],
                "species":data["species"],
                "food":data["food"],
                "count":data["count"]
                }        
            return JsonResponse(res,safe=False)            
        
        if request.method=="POST":
            new_fish=json.loads(request.body)
            models.Fish.objects.create(color=new_fish["color"],species=new_fish["species"],food=new_fish["food"],count=new_fish["count"])
            return JsonResponse({"Created":{"species":new_fish["species"]}})

        if request.method=="PUT":            
            obj1.update(last_feed_time=datetime.datetime.now())
            return JsonResponse({"Feeded":data["species"]})
    
        if request.method=="DELETE":            
            obj1.delete()
            return JsonResponse({"Deleted ":data["species"]})
    else:
        return HttpResponse(f"{species} is not in zoo,Please enter another name")
    

