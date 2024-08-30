from flask import Flask, render_template
import requests as requests
import time
import random
from pypokemon.pokemon import Pokemon

<<<<<<< HEAD
# สร้าง Flask application
app = Flask(__name__)

def get_pokemon(url):
    # แสดงเวลาและ URL ที่กำลังเรียก
    print(f"{time.ctime()} - get {url}")
    # ส่ง GET request ไปยัง URL ที่กำหนด
    resp = requests.get(url)
    # แปลง response เป็น JSON
=======

app = Flask(__name__)

def get_pokemon(url):
    print(f"{time.ctime()} - get {url}")
    resp = requests.get(url)
>>>>>>> 4394173d61138a69aedfe37bca8b8d4e2a133a37
    pokemon = resp.json()

    return pokemon

def get_pokemons():
<<<<<<< HEAD
    # สร้างรายการตัวเลขสุ่ม 5 ตัว ในช่วง 1-151
=======
>>>>>>> 4394173d61138a69aedfe37bca8b8d4e2a133a37
    rand_list=[]
    for i in range(5):
        rand_list.append(random.randint(1,151))

<<<<<<< HEAD
    # สร้างรายการ Pokemon objects
    pokemon_data = []
    for number in rand_list:
        # สร้าง URL สำหรับแต่ละ Pokemon
        url = f'https://pokeapi.co/api/v2/pokemon/{number}'
        # เรียกข้อมูล Pokemon จาก API
        pokemon_json = get_pokemon(url)
        # สร้าง Pokemon object จากข้อมูล JSON
        pokemon_object = Pokemon(pokemon_json)
        # เพิ่ม Pokemon object เข้าไปในรายการ
=======
    pokemon_data = []
    for number in rand_list:
        url = f'https://pokeapi.co/api/v2/pokemon/{number}'
        pokemon_json = get_pokemon(url)
        pokemon_object = Pokemon(pokemon_json)
>>>>>>> 4394173d61138a69aedfe37bca8b8d4e2a133a37
        pokemon_data.append(pokemon_object)
    return pokemon_data

@app.route('/')
def index():
<<<<<<< HEAD
    # บันทึกเวลาเริ่มต้น
    start_time = time.perf_counter()
    # ดึงข้อมูล Pokemon
    pokemons = get_pokemons()
    # บันทึกเวลาสิ้นสุด
    end_time = time.perf_counter()
    # แสดงข้อมูลเวลาที่ใช้ในการดึงข้อมูล
    print(f"{time.ctime()} - Get {len(pokemons)} pokemons. Time taken: {end_time-start_time} seconds")
    # แสดงผลหน้า index.html พร้อมส่งข้อมูล Pokemon และเวลา
    return render_template('index.html', pokemons=pokemons, end_time=end_time, start_time=start_time)

# รัน Flask app ในโหมด debug ที่ port 50000
=======
    start_time = time.perf_counter()
    pokemons = get_pokemons()
    end_time = time.perf_counter()
    print(f"{time.ctime()} - Get {len(pokemons)} pokemons. Time taken: {end_time-start_time} seconds")
    return render_template('index.html', pokemons=pokemons, end_time=end_time, start_time=start_time)

>>>>>>> 4394173d61138a69aedfe37bca8b8d4e2a133a37
if __name__ == '__main__':
    app.run(debug=True, port=50000)