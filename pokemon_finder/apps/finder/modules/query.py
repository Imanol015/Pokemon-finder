#Utilities
import requests
import json

#Own
from .suggestion import make_suggestion

def make_query(word=None,last_pokemon=None,extended_version=False):
    """
        Parametros de entrada= word(string) , last_pokemon(string) , extended_version(Boolean).
        Retorna un lista de diccionarios.
        El parametro word(entrada usuario) se utiliza para invocar a la funcion "make_suggestion"(devuelve una lista de nombres de pokemon). Con el resultado de dicha funcion realiza n llamados a "pokeapi"(recibe un dict por cada llamado).
        El parametro last_pokemon representa el ultimo pokemon mostrado en el inicio
        El parametro extended_version se utiliza para mostrar o una version "extendida" de los datos del pokemon. Utilizado en el profile
    """
    suggestions_list=[]

    for option in make_suggestion(word,last_pokemon):
        service_response=requests.get("https://pokeapi.co/api/v2/pokemon/"+option.lower())  #El metodo requiere el nombre en miniscula
        if service_response.status_code == 200:
            json_response=service_response.json()
            
            pokemon_data={}
            pokemon_data["name"]=json_response["name"].capitalize()     #El servicio devuelve los nombre en minuscula
            pokemon_data["sprite"]=json_response["sprites"]["front_default"]    #Imagen usada en la pagina
            
            suggestions_list.append(json_response) if extended_version else  suggestions_list.append(pokemon_data)  #Si

    return suggestions_list