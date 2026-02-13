# Planteamiento

## Introducción

On-Class es una iniciativa que brinda oportunidades de crecimiento en carreras tecnológicas a través de bootcamps sincrónicos. Están interesados en contratarte para desarrollar su sitio web, el cual servirá como plataforma de comunicación entre los tutores y los participantes del bootcamp.

El propósito principal del sitio web es facilitar la organización de los bootcamps, que se centran en fortalecer conocimientos en diferentes capacidades tecnológicas. Estas capacidades pueden incluir roles como:

- Desarrollador backend
- Desarrollador frontend
- DevOps
- Cloud Ops
- Analista de calidad
- Entre otros

Cada capacidad tiene asociado un conjunto de tecnologías, como Java, Node.js, Angular, Git, Mockito o JUnit.

## Estructura de los Bootcamps

Inicialmente, se requiere la creación de la estructura de los bootcamps. Un bootcamp tiene:

- Un nombre
- Un conjunto de capacidades que cubrirá

Las capacidades, a su vez, están compuestas por:

- Un nombre
- Una descripción
- Un listado de tecnologías, cada una con su propio nombre y descripción

## Iteraciones de Bootcamps

Una vez establecida la estructura del bootcamp en el sistema, los administradores deben poder crear iteraciones de esos bootcamps. Cada iteración representa:

- La ejecución de un bootcamp en una fecha específica
- Tutores y participantes asignados
- Un listado de entregables que los tutores crearán para evaluar el progreso de los participantes
- Un cupo máximo establecido

Además, se debe permitir la generación de un enlace de invitación para tutores y participantes de cada iteración del bootcamp.

## Funcionalidades por Rol

### Tutores

Los tutores tienen la capacidad de:

- Ver todas las iteraciones en las que participan
- Crear entregables para evaluar el progreso de los participantes
- Revisar las entregas realizadas por estos
- Proporcionar retroalimentación

### Participantes

Los participantes pueden:

- Acceder a la lista de iteraciones de bootcamp en las que están inscritos
- Ver los entregables asignados por los tutores
- Enviar sus entregas
- Recibir feedback de los tutores
- Agregar comentarios públicos sobre las entregas, para formular dudas o responder dudas de otros participantes

### Administradores

La parametrización oficial de los bootcamps debe ser realizada por un usuario administrador del sistema.

## Reglas

| Regla | Front | Back |
|-------|-------|------|
| Cada microservicio es un repositorio aparte. |  | x |
| Cada microservicio debe persistir únicamente su base de datos. |  | x |
| Cada regla de negocio debe tener sus respectivos tests unitarios. | x | x |
| Cada microservicio debe tener su respectiva documentación OpenApi. |  | x |
| Cada microservicio debe estar basado en arquitectura hexagonal. |  | x |
| Cada HU debe estar implementada en su rama única (recomendamos el uso de gitflow). | x | x |

