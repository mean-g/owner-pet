from django.shortcuts import render

# Create your views here.
import json

from django.http import JsonResponse
from django.views import View

from .models import Owner, Dog

class OwnersView(View):
    def post(self, request):
        data      = json.loads(request.body)
        Owner.objects.create(
            name = data['name'],
            email = data['email'],
            age = data['age']
        )
        return JsonResponse({'messasge':'created'}, status=201)
    
    def get(self, request):
        owners = Owner.objects.all()
        results = []

        for owner in owners:

            results.append(
                {
                    'name' : owner.name,
                    'age' : owner.age,
                    'email' : owner.email,
                }
            )
        return JsonResponse({'result' : results}, status=200)


class DogsView(View):
    def post(self, request):
        data      = json.loads(request.body)
        Dog.objects.create(
            name = data['name'],
            age = data['age'],
            owner = Owner.objects.get(name=data['owner'])
        )
        return JsonResponse({'messasge':'created'}, status = 201)

    def get(self, request):
        dogs = Dog.objects.all()
        results = []

        for dog in dogs:

            results.append(
                {
                    'name' : dog.name,
                    'age' : dog.age,
                    'owner': dog.owner.name
                }
            )
        return JsonResponse({'result' : results}, status=200)