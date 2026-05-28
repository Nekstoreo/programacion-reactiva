#!/bin/bash

# Array de directorios de los microservicios
microservices=(
    "microservicio-tecnologia"
    "microservicio-capacidad"
    "microservicio-bootcamp"
    "microservicio-persona"
    "microservicio-reporte"
)

echo "=========================================================="
echo " Deteniendo contenedores Docker de los microservicios"
echo "=========================================================="

for ms in "${microservices[@]}"; do
    if [ -d "$ms" ]; then
        if [ -f "$ms/docker-compose.yml" ]; then
            echo ""
            echo "-> Deteniendo Docker Compose en: $ms"
            echo "----------------------------------------------------"
            (cd "$ms" && docker compose down)
        else
            echo "⚠️  Aviso: No se encontró docker-compose.yml en $ms"
        fi
    else
        echo "⚠️  Aviso: El directorio $ms no existe"
    fi
done

echo ""
echo "=========================================================="
echo " ¡Proceso completado! Los contenedores han sido detenidos."
echo "=========================================================="
