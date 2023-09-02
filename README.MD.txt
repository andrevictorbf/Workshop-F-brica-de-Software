Primeiro projeto - API - Organizador de itens - Objetos
Tentativa de API simples(versao - 00) focada na organização, localizaçao e classificação de itens através do conceito 'CRUD'

Por meio dos códigos da pasta api\views, é possivel realziar as funções do CRUD. São eles:

from django.shortcuts import render

from rest_framework import generics

from models import Item, Location 

from serializers import ItemSerializer, LocationSerializer

class Itemlistas (generics.ListCreateAPIView): 
    serializer_class = ItemSerializer
    def get_queryset(self):
    queryset = Item.objects.all()
    Location = self.request.query_params.get('location')
        if location is not None:
            queryset = queryset.filter(itemlocal = Location)
        return queryset
    
class ItemDetalhes (generics.RetrieveUpdateDestroyAPIView): #CRUD
    serializer_class = ItemSerializer
    queryset = Item.objects.all()
    
class Listalocal (generics.ListCreateAPIView):
    serializer_class: LocationSerializer
    queryset = Location.objects.all ()
    
class Localizacao (generics.RetrieveUpdateDestroyAPIView):
    serializer_class: LocationSerializer
    queryset = Location.objects.all ()

