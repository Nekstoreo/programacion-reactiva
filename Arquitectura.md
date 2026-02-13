``` mermaid
 flowchart LR
    %% Administrador y Navegador (arriba)
    Admin["<b>Administrador</b><br/>[Person]<br/><br/>Tiene la funcionalidad de<br/>crear bootcamp,<br/>crear versión del bootcamp"]
    Nav["<b>NAVEGADOR</b><br/>[JavaScript, Angular, React etc.]<br/><br/>Front Web o Mobile"]
    
    Admin -->|"Tiene la funcionalidad de<br/>crear bootcamp,<br/>crear versión del bootcamp"| Nav

    %% Contenedor principal Bootcamp (TB)
    subgraph Bootcamp["<b>Bootcamp</b><br/>[Software System]"]
        direction TB
        
        %% Capa 1: Persona (horizontal)
        subgraph Layer1["Microservicio Persona"]
            direction LR
            MSPersona["<b>Microservicio Persona</b><br/>[Container: Webflux, Swagger]<br/><br/>Administra las personas del bootcamp"]
            DBPersonas[("<b>BD Personas</b><br/>[ : Mysql]<br/><br/>basedatos del microservicio Personas")]
            MSPersona -->|TCP/IP| DBPersonas
        end
        
        %% Capa 2: Bootcamp (horizontal)
        subgraph Layer2["Microservicio Bootcamp"]
            direction LR
            MSBootcamp["<b>Microservicio Bootcamp</b><br/>[Container: Webflux, Swagger]<br/><br/>Administra el bootcamp"]
            DBBootcamp[("<b>BD Bootcamp</b><br/>[ : Mysql]<br/><br/>basedatos del microservicio Bootcamp")]
            MSBootcamp -->|TCP/IP| DBBootcamp
        end

        %% Conexiones entre microservicios
        MSCapacidad -->|JSON/HTTP| MSBootcamp
        
        %% Capa 3: Capacidad (horizontal)
        subgraph Layer3["Microservicio Capacidad"]
            direction LR
            MSCapacidad["<b>Microservicio Capacidad</b><br/>[Container: Webflux, Swagger]<br/><br/>Administra las capacidades del bootcamp"]
            DBCapacidad[("<b>BD Capacidad</b><br/>[ : Mysql]<br/><br/>basedatos del microservicio capacidad")]
            MSCapacidad -->|TCP/IP| DBCapacidad
        end
        
        %% Conexiones entre microservicios
        MSCapacidad -->|JSON/HTTP| MSTecnologia
        
        %% Capa 4: Tecnología (horizontal)
        subgraph Layer4["Microservicio Tecnología"]
            direction LR
            MSTecnologia["<b>Microservicio Tecnología</b><br/>[Container: Webflux, SpringSecurity, Swagger]<br/><br/>Administra las tecnologías del sistema"]
            DBTecnologia[("<b>BD Tecnología</b><br/>[ : Mysql]<br/><br/>basedatos del microservicio tecnología")]
            MSTecnologia -->|TCP/IP| DBTecnologia
        end
        
        %% Capa 5: Reporte (horizontal)
        subgraph Layer5["Microservicio Reporte"]
            direction LR
            MSReporte["<b>Microservicio Reporte</b><br/>[Container: Webflux, SpringSecurity, Swagger]<br/><br/>Administra los reportes del sistema"]
            DBReporte[("<b>BD Reporte</b><br/>[ : mongodb]<br/><br/>basedatos del microservicio de reporte")]
            MSReporte -->|TCP/IP| DBReporte
        end 
    end

    %% Para que Persona no quede aislado, lo conectamos a algo (opcional)
    Nav -.->|"futura integración"| MSPersona
    
    %% Conexiones desde el Navegador a los MS relevantes
    Nav -->|JSON/HTTP| MSCapacidad
    Nav -->|JSON/HTTP| MSTecnologia
    Nav -->|JSON/HTTP| MSReporte


    %% Estilos (igual que los tuyos)
    classDef personStyle fill:#4a7ba7,stroke:#2e5c8a,color:#fff
    classDef navigatorStyle fill:#7d8fa0,stroke:#5d6f80,color:#fff
    classDef microserviceStyle fill:#f9b233,stroke:#d99520,color:#000
    classDef databaseStyle fill:#3ca8c8,stroke:#2a88a8,color:#fff
    
    class Admin personStyle
    class Nav navigatorStyle
    class MSPersona,MSBootcamp,MSCapacidad,MSTecnologia,MSReporte microserviceStyle
    class DBPersonas,DBBootcamp,DBCapacidad,DBTecnologia,DBReporte databaseStyle
```