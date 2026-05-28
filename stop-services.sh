#!/bin/bash

# Puertos de los microservicios
ports=(8081 8082 8083 8084 8085)

echo "=========================================================="
echo " Deteniendo los 5 Microservicios (Puertos 8081-8085)"
echo "=========================================================="

for port in "${ports[@]}"; do
    # Buscamos el PID ocupando el puerto
    pid=$(lsof -t -i:$port 2>/dev/null)
    if [ ! -z "$pid" ]; then
        echo "-> Puerto $port: Deteniendo proceso PID $pid..."
        kill -9 $pid 2>/dev/null
    else
        echo "-> Puerto $port: Libre (sin procesos activos)"
    fi
done

# Detener demonios de Gradle que consumen memoria residual
echo ""
echo "-> Deteniendo Daemons de Gradle residuales..."
for ms in microservicio-*; do
    if [ -d "$ms" ]; then
        (cd "$ms" && ./gradlew --stop >/dev/null 2>&1)
    fi
done

echo ""
echo "=========================================================="
echo " ¡Todos los microservicios han sido detenidos!"
echo "=========================================================="
