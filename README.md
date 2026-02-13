# Programación Reactiva - On-Class

Plataforma de bootcamps para desarrollo de capacidades técnicas.

## Arquitectura

Sistema de 5 microservicios independientes:

| Servicio | Puerto | BD | Descripción |
|----------|--------|----|----|
| [Persona](./microservicio-persona) | 8081 | MySQL | Gestión de usuários |
| [Bootcamp](./microservicio-bootcamp) | 8082 | MySQL | Gestión de bootcamps |
| [Capacidad](./microservicio-capacidad) | 8083 | MySQL | Gestión de capacidades técnicas |
| [Tecnología](./microservicio-tecnologia) | 8084 | MySQL | Gestión de tecnologías |
| [Reporte](./microservicio-reporte) | 8085 | MongoDB | Generación de reportes |

## Requisitos

- Java 25+
- Gradle 9.3.0+
- MySQL 8.0+
- MongoDB 4.0+

## Clonar el proyecto

```bash
git clone --recurse-submodules git@github.com:Nekstoreo/programacion-reactiva.git
cd programacion-reactiva
```

## Levantar servicios

Cada microservicio se inicia de forma independiente:

```bash
cd microservicio-{nombre}
./gradlew bootRun
```

Todos estarán disponibles en `http://localhost:808X` con OpenAPI en `/swagger-ui.html`

## Ramas

- `main` - Código estable, listo para producción
- `develop` - Integración de features (base para ramas de característica)
- `feature/*` - Nuevas funcionalidades

## Documentación

- [Reto](./Reto.md) - Especificación funcional
- [Cronograma](./Cronograma.md) - Backlog de historias de usuario
- [Arquitectura](./Arquitectura.md) - Diagrama de solución
