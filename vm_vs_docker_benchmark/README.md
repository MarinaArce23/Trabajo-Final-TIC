# VM vs Docker Performance Benchmark Project

Este proyecto compara el rendimiento y el uso de recursos entre una máquina virtual (VirtualBox con Ubuntu) y un contenedor Docker, a través de una aplicación Flask que convierte imágenes JPEG a PNG y un análisis automatizado mediante Jupyter Notebook.

---

## 📁 Estructura del Proyecto

- `app.py`: Servidor Flask que convierte imágenes JPG a PNG.
- `notebooks/vm_vs_docker_comparison.ipynb`: Notebook que realiza comparativas de rendimiento.
- `scripts/`: Scripts para configurar VM y Docker.
- `results/`: Archivos generados con métricas (tiempo, CPU, RAM).
- `requirements.txt`: Dependencias necesarias.

---

## ⚙️ Requisitos

- Python 3.10+
- Docker
- VirtualBox (con una VM Ubuntu instalada)
- Paquetes: `flask`, `pillow`, `psutil`, `jupyter`, `matplotlib`, `pandas`

---

## 🚀 Instrucciones rápidas

### En la Máquina Virtual

```bash
git clone https://github.com/MarinaArce23/Trabajo-Final-TIC.git
cd Trabajo-Final-TIC/vm_vs_docker_benchmark
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python app.py
```

Accede desde el navegador en `http://<IP_VM>:5000`.

### En Docker

```bash
cd Trabajo-Final-TIC/vm_vs_docker_benchmark/scripts
bash docker_setup.sh
```

Accede desde `http://localhost:5000` o desde la IP de la VM si ejecutas Docker dentro de ella.

---

## 📊 Comparativa de rendimiento

Desde el directorio `notebooks`, abre y ejecuta el Jupyter Notebook:

```bash
jupyter notebook
```

El archivo `vm_vs_docker_comparison.ipynb`:

- Detecta automáticamente si estás en Docker o VM.
- Ejecuta una serie de conversiones de imágenes y mide:
  - Tiempo de ejecución promedio
  - Uso medio de CPU (%)
  - Uso medio de RAM (MB)
  - Métricas también con concurrencia (multi-threading)
- Guarda los resultados en JSON dentro de `results/`.
- Si detecta ambos entornos, genera automáticamente una gráfica comparativa.

---

## 📈 Resultados

Los archivos generados se encuentran en `results/`:

- `resultados_vm.json`
- `resultados_docker.json`
- `benchmark_completo.csv`
- `grafica_comparativa.png`

---

## 🧪 Carga concurrente

Durante las pruebas, se simula una carga con múltiples hilos para observar cómo afecta la concurrencia en la conversión de imágenes.

---

## 💡 Observaciones

- No es necesario modificar el notebook al cambiar de entorno.
- Solo tienes que ejecutarlo en VM y luego en Docker: todo se guarda y se fusiona automáticamente.
- El entorno Docker debe montarse con el volumen compartido (`-v $(pwd):/app`) para que los resultados se guarden correctamente.

---

## 👩‍💻 Autoría

Creado por **Marina Arce**  
Repositorio: [https://github.com/MarinaArce23/Trabajo-Final-TIC]