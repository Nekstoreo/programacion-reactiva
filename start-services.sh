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
echo " Compilando e Iniciando los 5 Microservicios"
echo "=========================================================="

for ms in "${microservices[@]}"; do
    if [ -d "$ms" ]; then
        echo ""
        echo "🔨 Compilando: $ms..."
        (cd "$ms" && ./gradlew bootJar -x test)
        
        if [ $? -eq 0 ]; then
            echo "🚀 Lanzando: $ms (puerto en logs)"
            echo "   Logs en vivo en: $ms/spring-boot-run.log"
            echo "----------------------------------------------------"
            # Iniciamos en segundo plano con nohup y redirigimos logs
            (cd "$ms" && nohup java -jar build/libs/*-0.0.1-SNAPSHOT.jar > spring-boot-run.log 2>&1 &)
            # Un pequeño sleep para no sobrecargar el sistema levantándolos al mismo milisegundo
            sleep 1
        else
            echo "❌ Error al compilar $ms. Cancelando el inicio de este microservicio."
        fi
    else
        echo "⚠️  Aviso: El directorio $ms no existe"
    fi
done

echo ""
echo "=========================================================="
echo " ¡Todos los microservicios han sido lanzados!"
echo " Puedes verificar los logs de cada uno usando:"
echo " tail -f microservicio-{nombre}/spring-boot-run.log"
echo "=========================================================="

