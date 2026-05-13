# 📚 Temario de Estudio: Programación Reactiva con Spring WebFlux

## Módulo 1: Fundamentos de la Programación Reactiva

*Antes de tocar Spring, necesitas entender por qué existe la programación reactiva y qué problemas resuelve.*

1. **Evolución de las arquitecturas web:**
  - Modelo Tradicional (Síncrono/Bloqueante - *Thread per request*).
  - El problema del bloqueo (I/O Blocking) y cuellos de botella.
  - Modelo Asíncrono y No Bloqueante.
2. **El Manifiesto Reactivo:**
  - Sistemas Responsivos, Resilientes, Elásticos y Orientados a Mensajes.
3. **Especificación *Reactive Streams*:**
  - Patrón Observador (Publisher - Subscriber).
  - Concepto vital: **Backpressure** (Contrapresión) - Cómo el consumidor controla la velocidad del productor.
  - Interfaces principales: `Publisher`, `Subscriber`, `Subscription`, `Processor`.

## Módulo 2: Project Reactor (El motor de WebFlux)

*WebFlux está construido sobre Project Reactor. Aquí aprenderás a manejar los flujos de datos.*

1. **Introducción a Project Reactor:**
  - ¿Qué es y cómo implementa *Reactive Streams*?
2. **Tipos de datos reactivos (Fundamentales):**
  - `**Mono<T>*`*: Representa 0 o 1 elemento (Ideal para respuestas HTTP únicas, buscar por ID).
  - `**Flux<T>**`: Representa de 0 a N elementos (Ideal para listas, streams de datos, paginación).
3. **Creación de Monos y Flux:**
  - `just()`, `empty()`, `fromIterable()`, `defer()`, `error()`.
4. **Operadores de Transformación (Lo que más usarás):**
  - `map()` vs `flatMap()` (Diferencia crucial en programación reactiva).
  - `filter()`, `defaultIfEmpty()`, `switchIfEmpty()`.
5. **Operadores de Combinación:**
  - `zip()`, `zipWith()`, `merge()`, `concat()`. (Útil para llamar a varios microservicios a la vez).
6. **Manejo de Errores Reactivo:**
  - `onErrorResume()`, `onErrorMap()`, `onErrorReturn()`, `doOnError()`.
7. **Efectos Secundarios (Side Effects):**
  - `doOnNext()`, `doOnSuccess()`, `doFinally()`. (Perfecto para logs o auditorías).

## Módulo 3: Spring WebFlux (La capa Web)

*Ahora sí, a construir APIs REST no bloqueantes.*

1. **Diferencias entre Spring MVC vs Spring WebFlux:**
  - Tomcat (bloqueante) vs Netty (no bloqueante, event-loop).
2. **Modelo Basado en Anotaciones (El que probablemente usaste):**
  - `@RestController`, `@GetMapping`, `@PostMapping` devolviendo `Mono` y `Flux`.
3. **Modelo Funcional (Router Functions & Handlers) - *Opcional pero recomendado*:**
  - Alternativa a los controladores clásicos usando programación puramente funcional.
4. **Validaciones Reactivas:**
  - Uso de `@Valid` y manejo de excepciones con `@ExceptionHandler` genéricos para WebFlux.
5. **Comunicación entre Microservicios (HTTP No bloqueante):**
  - `**WebClient`**: Configuración y uso (Llamadas GET, POST, manejo de errores de red, timeouts). *Esto lo necesitas para cuando Capacidad llama a Tecnología, por ejemplo.*

## Módulo 4: Persistencia Reactiva (Bases de Datos)

*No sirve de nada WebFlux si tu base de datos bloquea el hilo.*

1. **Spring Data R2DBC (Para MySQL - Microservicios Persona, Bootcamp, Capacidad, Tecnología):**
  - ¿Por qué no usar JDBC/JPA/Hibernate en WebFlux? (Problema del bloqueo).
  - Configuración de R2DBC.
  - Repositorios Reactivos (`ReactiveCrudRepository`, `R2dbcRepository`).
  - Mapeo de entidades (anotaciones `@Table`, `@Id`).
  - Transacciones Reactivas (`@Transactional` en métodos que devuelven `Mono`).
2. **Spring Data Reactive MongoDB (Para Microservicio Reporte):**
  - Configuración del driver reactivo de Mongo.
  - `ReactiveMongoRepository`.
  - Diferencias de rendimiento y uso vs R2DBC.

## Módulo 5: Arquitectura Hexagonal en un Mundo Reactivo

*Adaptando los principios de Clean Architecture a flujos de datos.*

1. **Conceptos básicos de Arquitectura Hexagonal (Puertos y Adaptadores):**
  - Dominio, Casos de Uso (Aplicación) e Infraestructura.
2. **Implementación con WebFlux:**
  - ¿Cómo manejar `Mono` y `Flux` en la capa de Dominio sin acoplarse a Spring?
  - Inyección de dependencias de Puertos (Interfaces) en los Casos de Uso.
  - Adaptadores de Entrada (Controladores WebFlux).
  - Adaptadores de Salida (Repositorios R2DBC/Mongo o llamadas WebClient).

## Módulo 6: Seguridad y Documentación

*Protegiendo y exponiendo tu API.*

1. **Spring Security Reactivo (Para Microservicios Tecnología y Reporte):**
  - Configuración de `SecurityWebFilterChain`.
  - Autenticación y Autorización No Bloqueante.
  - Manejo de JWT en un entorno reactivo (`ReactiveAuthenticationManager`).
  - Obtener el usuario actual en el flujo reactivo (`ReactiveSecurityContextHolder`).
2. **Swagger / OpenAPI en WebFlux:**
  - Integración de `springdoc-openapi-webflux-ui`.
  - Anotaciones de Swagger adaptadas a respuestas `Mono/Flux`.

## Módulo 7: Testing Reactivo (Pruebas Unitarias y de Integración)

*Probar código reactivo es diferente porque el código se ejecuta en el futuro.*

1. **Pruebas de Flujos con `StepVerifier`:**
  - Cómo probar qué emite un `Mono` o `Flux`.
  - Aserciones de elementos, errores y finalización.
2. **Pruebas de Controladores con `WebTestClient`:**
  - Simular llamadas HTTP a tus endpoints de manera no bloqueante.
3. **Mocks en Arquitectura Hexagonal Reactiva:**
  - Uso de Mockito devolviendo `Mono.just()` o `Flux.fromIterable()`.

