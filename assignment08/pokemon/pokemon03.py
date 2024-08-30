from pypokemon.pokemon import Pokemon
import asyncio
import httpx
import time
import random

async def get_pokemon(client, url):
<<<<<<< HEAD
    print(f'{time.ctime()} - get {url}')
    resp = await client.get(url)
    pokemon = resp.json()
    
    return Pokemon(pokemon)

async def get_pokemons():
    async with httpx.AsyncClient() as client:
        tasks = []
        rand_list = []
        for i in range(5):
            rand_list.append(random.randint(1, 151))
            
        for number in rand_list:
            url = f'https://pokeapi.co/api/v2/pokemon/{number}'
            tasks.append(asyncio.create_task(get_pokemon(client, url)))
            
        pokemons = await asyncio.gather(*tasks)
        return pokemons
=======
    pass

async def get_pokemons():
    async with httpx.AsyncClient() as client:
        pass
>>>>>>> 4394173d61138a69aedfe37bca8b8d4e2a133a37

async def index():
    start_time = time.perf_counter()
    pokemons = await get_pokemons()
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Asynchronous get {len(pokemons)} pokemons. Time taken: {end_time-start_time} seconds")

if __name__ == '__main__':
   asyncio.run(index())