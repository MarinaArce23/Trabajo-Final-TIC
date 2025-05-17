# 📊 Servidor de Conversión de Imágenes: Análisis de Rendimiento en Docker y VM

Este proyecto implementa un servidor web usando Flask que permite convertir imágenes JPG a PNG mediante una interfaz sencilla. Además, se realiza un análisis comparativo de rendimiento ejecutando el servidor dentro de un contenedor Docker y en una máquina virtual (VM).

---

## Máquinas Virtuales (VM) y Contenedores: Diferencias y Casos de Uso

Las **máquinas virtuales (VM)** y los **contenedores** son tecnologías de virtualización que permiten ejecutar aplicaciones de forma aislada, optimizando recursos y facilitando su despliegue en distintos entornos. Aunque comparten similitudes, su arquitectura y propósitos varían significativamente.

---

### 1. Máquinas Virtuales (VM)

### ¿Qué es una VM?
Una máquina virtual es una **réplica digital de una máquina física**, que incluye su propio sistema operativo (SO), kernel virtualizado, y recursos asignados (CPU, RAM, almacenamiento). Se ejecuta sobre un **hipervisor** (ej: VMware, Hyper-V) que gestiona el acceso al hardware físico.

### Características clave:
- **Alto aislamiento**: Cada VM es independiente y segura (ideal para entornos críticos).
- **Multi-SO**: Puedes ejecutar Linux en un host Windows o viceversa.
- **Overhead alto**: Consume más recursos porque virtualiza hardware completo.
- **Arranque lento**: Tarda minutos en iniciar (dependiendo del SO).

### Ventajas:
- Mayor seguridad y aislamiento  
- Compatibilidad con cualquier SO  
- Ideal para aplicaciones legacy  

### Desventajas:
- Consumo elevado de recursos  
- Escalabilidad compleja  
- Tiempos de despliegue más largos  

### Ejemplo práctico:
```bash
# Crear una VM con Ubuntu en VirtualBox (host Windows)
VBoxManage createvm --name "Ubuntu-Server" --ostype "Ubuntu_64" --register
```
### ¿Cuándo usar VM?
- Aplicaciones que requieren un SO específico (ej: Windows Server 2008).
- Entornos con requisitos de seguridad estricta (ej: bancos, hospitales).
- Pruebas de software en múltiples SO sin afectar al host.

### 2. Contenedores

### ¿Qué es un Contenedor?
Un contenedor es un paquete ligero que incluye una aplicación, sus dependencias y configuraciones, ejecutándose de forma aislada pero compartiendo el kernel del host. Usa tecnologías como **namespaces** y **cgroups** en Linux.

### Características clave:
- **Eficiencia:** Consume menos recursos que una VM (solo MBs).
- **Portabilidad:** "Funciona en mi máquina" resuelto.
- **Arranque rápido:** Segundos para iniciar/detener.
- **Escalabilidad:** Horizontal fácil con orquestadores (Kubernetes).

### Ventajas:
- Máxima eficiencia de recursos
- Despliegue instantáneo
- Ideal para microservicios

### Desventajas:
- Menor aislamiento que una VM
- Dependencia del kernel del host
- Limitaciones para kernels personalizados  

### Ejemplo práctico:
```bash
# Ejecutar un contenedor con Node.js usando Docker
docker run -d -p 3000:3000 --name my-node-app node:18-alpine
```

### ¿Cuándo usar contenedores?
- Arquitecturas de microservicios (ej: APIs en Kubernetes).
- Pipelines CI/CD (pruebas automatizadas).
- Aplicaciones cloud-nativas (ej: serverless en AWS Lambda).

### Tabla Comparativa: Contenedores vs Máquinas Virtuales

| **Característica**       | **Contenedores**                          | **Máquinas Virtuales**                  |
|--------------------------|------------------------------------------|-----------------------------------------|
| **Nivel de virtualización** | A nivel de SO (comparten kernel)       | A nivel de hardware (hipervisor)        |
| **Tamaño típico**        | MBs (solo app + dependencias)           | GBs (incluye SO completo)               |
| **Tiempo de inicio**     | Segundos                                 | Minutos                                 |
| **Consumo de recursos**  | Mínimo (comparte kernel)                | Alto (SO completo virtualizado)         |
| **Aislamiento**          | Procesos (namespaces/cgroups)           | Hardware completo                       |
| **Portabilidad**         | Alta (misma imagen en cualquier host)   | Media (depende del hipervisor)          |
| **Seguridad**           | Depende del kernel host                 | Mayor (aislamiento completo)            |
| **Escalabilidad**       | Alta (ideal para microservicios)        | Limitada (mayor overhead)              |
| **Sistemas operativos** | Solo el mismo tipo que el host          | Cualquier SO independiente             |
| **Casos de uso típicos**| Microservicios, CI/CD, aplicaciones cloud | Legacy apps, entornos seguros, multi-SO |
| **Herramientas populares**| Docker, Podman, Kubernetes             | VMware, VirtualBox, Hyper-V            |

---

## Objetivo del Proyecto
Desarrollar un servidor Flask para convertir imágenes JPG a PNG.

Medir y comparar el rendimiento del servidor en un contenedor Docker vs una VM.

Analizar métricas como tiempo de conversión, consumo de CPU y memoria.

Proporcionar una solución multiplataforma fácil de usar y desplegar.

---

## Entorno de Pruebas

- **Host**: Intel Core i3 9100F, 16 GB RAM, Windows 10
- **Virtual Machine (Guest)**: Ubuntu 20.04, 4 GB RAM, 2 vCPU, VirtualBox 7
- **Docker**: Imagen base `python:3.10-slim`, 2 CPUs asignadas
- **Red y conexión**: Ambas plataformas usan red NAT para conectarse al host.

El servidor Flask se expone en localhost:5000 para acceder desde el navegador

---

## Estructura actual del proyecto

``` cpp
.
├── README.md
├── generar_proyecto.py
└── vm_vs_docker_benchmark/
    ├── .gitignore
    ├── results/
    ├── notebooks/
    │   └── vm_vs_docker_comparison.ipynb
    ├── scripts/
    │   ├── docker_setup.sh
    │   ├── vm_setup.sh
    │   └── Dockerfile
    │   
```

---

## Bibliografía y Recursos

Este proyecto se ha apoyado en documentación oficial y recursos técnicos para comparar el rendimiento entre contenedores Docker y máquinas virtuales.

- [Docker - Documentación oficial](https://docs.docker.com/get-started/)
- [VirtualBox Manual](https://www.virtualbox.org/manual/)
- [Flask - Microframework para Python](https://flask.palletsprojects.com/)
- [Red Hat - Contenedores vs Máquinas Virtuales](https://www.redhat.com/es/topics/containers/containers-vs-vms)
- [IBM Developer - ¿Qué son los contenedores?](https://developer.ibm.com/articles/what-are-containers/)

---

## Requisitos

- **Python 3.8+** – Lenguaje base del proyecto.
- **Flask** – Microframework web para construir la interfaz de usuario y el servidor.
- **Pillow (PIL)** – Librería de procesamiento de imágenes para manejar la conversión JPG → PNG.
- **Docker** – Para ejecutar el proyecto en contenedores y comparar el rendimiento.
- **VirtualBox / Máquina Virtual (Ubuntu 20.04 recomendado)** – Para pruebas comparativas fuera de Docker.
- **Git/GitHub** – Control de versiones y almacenamiento del código fuente.
- **Navegador web** – Para usar la interfaz de carga de imágenes (`localhost:5000`).
- **Editor de código (Visual Studio Code, PyCharm, etc.)** – Para desarrollo y pruebas.

---

## Formas fáciles de ejecutar el proyecto

### 1. Ejecutar localmente sin Docker
Si solo quieres probar rápido el servidor Flask, sigue estos pasos:

```bash
pip install -r requirements.txt
python app.py
```
Luego abre en el navegador: `http://localhost:5000`

### 2. Ejecutar con Docker 
Construye y corre el contenedor con un solo comando:

```bash
docker build -t jpg-to-png-converter .
docker run -p 5000:5000 jpg-to-png-converter
```
Luego abre en el navegador: `http://localhost:5000`

### 3. Entorno virtual para mantener todo limpio
```bash
python -m venv venv
source venv/bin/activate      # En Windows: venv\Scripts\activate
pip install -r requirements.txt
python app.py
```