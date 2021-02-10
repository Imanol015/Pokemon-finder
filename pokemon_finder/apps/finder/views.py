from django.shortcuts import render
from .modules.query import make_query
from .modules.suggestion import make_suggestion

def home(request):
    """
        Se encarga de renderizar la pagina principal y obtener los datos de entrada del usuario
    """
    user_entry= request.GET.get("search_bar") if "search_bar" in request.GET else None    #Obtiene la palabra ingresada por el usuario siempre y cudo este en el request
    
    suggestions=make_suggestion(listar=True)    #Obtiene la lista de todos los pokemons
    last_pokemon= request.GET.get("next_button") if "next_button" in request.GET else None  #Obtiene el ultimo pokemon mostrado en la lista inicial
    
    search_result=make_query(user_entry, last_pokemon)  

    return render(request,"home/home.html",{"suggestions": suggestions , "last_pokemon":search_result[-1]["name"] , "search_result":search_result })



def pokemon_profile(request,pokemon_name):
    """
        Se encarga de renderizar el profile del pokemon
    """
    search_result=make_query(pokemon_name,extended_version=True)
    return render(request,"pokemon_profile/pokemon_profile.html",{"search_result":search_result })