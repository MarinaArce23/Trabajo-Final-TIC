# VM vs Docker Performance Benchmark Project

This project compares resource usage and performance metrics between a full virtual machine (VirtualBox) and a Docker container.

## 🔧 Project Structure
- `notebooks/`: Jupyter Notebook for running and plotting benchmarks
- `scripts/`: Setup scripts for VM, Docker, and Dockerfile itself
- `results/`: Placeholder for benchmark results

## 📦 Requirements
- Python 3.8+
- Docker (host or WSL2)
- VirtualBox (with a Linux guest)
- `sysbench`, `jupyter`, `matplotlib`, `psutil`

## 🚀 Quick Start
```bash
# On VM or Docker:
cd scripts
bash vm_setup.sh      # For VirtualBox
bash docker_setup.sh  # For Docker or WSL2
```

## Proyecto explicado 

---

## Estado Actual

### Máquina Virtual Ubuntu

- Máquina virtual creada y configurada en VirtualBox con Ubuntu Server.
- Clonado el repositorio del proyecto dentro de la VM.
- Instalado Python3, pip y creado un entorno virtual (`venv`).
- Instaladas dependencias: Flask, Pillow, etc.
- Aplicación Flask (`app.py`) que recibe imágenes, las convierte a PNG y permite descargarlas.
- Servidor Flask probado y accesible desde el host en la IP de la VM (ejemplo: `http://192.168.0.28:5000`).

### Docker

- Dockerfile preparado para construir la imagen con Python 3.10 slim.
- Dockerfile copia el código fuente y las plantillas.
- Dockerfile instala las dependencias mediante `requirements.txt`.
- Script `docker_setup.sh` creado para construir la imagen y lanzar el contenedor.
- Expuesto el puerto 5000 para acceder a la aplicación desde fuera del contenedor.

---

## Pasos para levantar el proyecto

### En la VM

1. Clonar el repositorio:

    ```bash
    git clone https://github.com/MarinaArce23/Trabajo-Final-TIC.git
    cd Trabajo-Final-TIC/vm_vs_docker_benchmark
    ```

2. Crear y activar entorno virtual:

    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Instalar dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Ejecutar la aplicación Flask:

    ```bash
    python app.py
    ```

5. Acceder desde host en `http://<IP_VM>:5000`.

### En Docker

1. Desde la carpeta del proyecto, ejecutar script para levantar Docker:

    ```bash
    ./vm_vs_docker_benchmark/scripts/docker_setup.sh
    ```

2. Acceder desde host en `http://localhost:5000` (o la IP de la VM si se ejecuta allí).

---

## Próximos pasos

- Completar scripts de configuración para la VM (`vm_setup.sh`).
- Automatizar pruebas de rendimiento entre VM y Docker.
- Análisis y visualización de resultados en `vm_vs_docker_benchmark/notebooks/vm_vs_docker_comparison.ipynb`.

---

## Notas

- La app Flask es un simple conversor de imágenes JPEG a PNG.
- La comparación buscará medir tiempos de ejecución, consumo de recursos y facilidad de despliegue.
- El entorno actual está en desarrollo; cualquier sugerencia o mejora es bienvenida.

---

## Contacto

Creado por Marina Arce  
- Repositorio: [https://github.com/MarinaArce23/Trabajo-Final-TIC](https://github.com/MarinaArce23/Trabajo-Final-TIC)



http://192.168.0.28:5000