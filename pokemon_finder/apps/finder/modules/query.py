#Utilities
import requests
import json

#Own
from .suggestion import make_suggestion

def make_query(word=None,last_pokemon=None):
    """
        Parametro de entrada= string.
        Retorna un lista de diccionarios.
        Utiliza el string(entrada usuario) para llamar a la funcion "make_suggestion"(devuelve una lista de nombres de pokemon). Con el resultado de dicha funcion realiza n llamados a "pokeapi"(recibe un dict por cada llamado). 
    """
    suggestions_list=[]

    for option in make_suggestion(word,last_pokemon):
        service_response=requests.get("https://pokeapi.co/api/v2/pokemon/"+option.lower())  #El metodo requiere el nombre en miniscula
        if service_response.status_code == 200:
            json_response=service_response.json()

            pokemon_data={}
            pokemon_data["name"]=json_response["name"].capitalize()     #El servicio devuelve los nombre en minuscula
            pokemon_data["sprite"]=json_response["sprites"]["front_default"]    #Imagen usada en la pagina
            suggestions_list.append(pokemon_data)

    return suggestions_list