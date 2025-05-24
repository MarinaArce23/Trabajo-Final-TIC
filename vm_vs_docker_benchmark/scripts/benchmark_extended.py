import requests
import time
import psutil
from statistics import mean

URL = "http://localhost:5000"
IMG_PATH = "../test.jpg"
REPETICIONES = 10

tiempos = []
usos_cpu = []
usos_ram = []

for i in range(REPETICIONES):
    with open(IMG_PATH, 'rb') as img:
        proceso = psutil.Process()
        inicio = time.perf_counter()
        requests.post(URL, files={'image': img})
        fin = time.perf_counter()
        cpu = proceso.cpu_percent(interval=0.1)
        ram = proceso.memory_info().rss / (1024 * 1024)

    tiempos.append((fin - inicio) * 1000)
    usos_cpu.append(cpu)
    usos_ram.append(ram)
    print(f"Intento {i+1}: {tiempos[-1]:.2f} ms, CPU: {cpu:.2f}%, RAM: {ram:.2f} MB")

# Promedios
print("\n📊 Resultados promedio:")
print(f"Tiempo: {mean(tiempos):.2f} ms")
print(f"CPU: {mean(usos_cpu):.2f} %")
print(f"RAM: {mean(usos_ram):.2f} MB")
