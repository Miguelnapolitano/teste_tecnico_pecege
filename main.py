import pokebase
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import matplotlib.pyplot as plt

def get_first_hundred():
    """
    With a parallel execution, goes to PokeAPI and get data of first
    hundred pokemons

    """
    first_hundred_list = []

    with ThreadPoolExecutor(max_workers=16) as executor:
        futures = [executor.submit(get_pokemon_type, i) for i in range(1, 101)]
        for future in futures:
            try:
                pokemon_type = future.result()
                first_hundred_list.append(pokemon_type)
            except Exception as e:
                print(e)
    
    create_poke_type_chart(first_hundred_list)


def get_pokemon_type(id):
    """
    Through Pokebase library does a request to get pokemon
    info by id from PokeAPI database.

    Params:
        id: PokemonAPI position number of pokemons.
    """

    pokemon = pokebase.pokemon(id)
    pokemon_info = {
        "name": pokemon.name,
        "weight": pokemon.weight,
        "heigh": pokemon.height,
        "dominant_type": pokemon.types[0].type.name
    }
    return pokemon_info


def create_poke_type_chart(first_hundred_list):  
    """
    With the received list of first hundred Pokemons, creates a 
    dataframe to feed a bar chart with the count of dominant types 
    occurrences using matplotlib library.

    Params:
        first_hundred_list: A list with first hundred pokemons info.

    """

    dominant_types_list = [x["dominant_type"] for x in first_hundred_list]
    df = pd.DataFrame(data={"Dominant Type": dominant_types_list})
    counts = df["Dominant Type"].value_counts()
    result_df = pd.DataFrame({'Dominant Type': counts.index, 'count': counts.values})
    bars = plt.bar(result_df["Dominant Type"], result_df["count"])
    plt.title("Dominant Types of PokeAPI's First 100 Pokemon")
    plt.ylabel("Ocurrences")
    plt.xlabel("Types")
    plt.bar_label(bars)
    plt.show()


if __name__ == "__main__":
    get_first_hundred()

