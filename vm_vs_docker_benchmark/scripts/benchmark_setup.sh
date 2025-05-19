#!/bin/bash

echo "🧪 Iniciando benchmark contra http://localhost:5000"
IMG_PATH="../test.jpg"
URL="http://localhost:5000"
REPETICIONES=10
RESULTS_FILE="../results/resultados_$(date +%s).txt"

# Verificar que el archivo de prueba existe
if [ ! -f "$IMG_PATH" ]; then
  echo "❌ No se encontró $IMG_PATH. Por favor, coloca una imagen llamada test.jpg en la raíz del proyecto."
  exit 1
fi

echo "Repeticiones: $REPETICIONES" > "$RESULTS_FILE"
echo "Archivo de resultados: $RESULTS_FILE"
echo "-------------------------------------"

for i in $(seq 1 $REPETICIONES); do
  START=$(date +%s%N)
  curl -s -o /dev/null -F "image=@$IMG_PATH" "$URL"
  END=$(date +%s%N)
  DURATION_NS=$((END - START))
  DURATION_MS=$((DURATION_NS / 1000000))
  echo "Intento $i: $DURATION_MS ms" | tee -a "$RESULTS_FILE"
done

echo "✅ Benchmark completado. Resultados guardados en $RESULTS_FILE"
