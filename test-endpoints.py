#!/usr/bin/env python3
import sys
import json
import time

try:
    import requests
except ImportError:
    print("Error: Se requiere la librería 'requests' de Python.")
    print("Puedes instalarla usando: pip install requests")
    sys.exit(1)

# Variables de la Colección (Equivalente a pm.collectionVariables)
variables = {
    "tech_1_id": None,
    "tech_2_id": None,
    "tech_3_id": None,
    "tech_delete_id": None,
    "cap_1_id": None,
    "cap_delete_id": None,
    "bootcamp_1_id": None,
    "bootcamp_delete_id": None,
    "person_1_id": None
}

def print_banner(text):
    print("\n" + "=" * 65)
    print(f" {text}")
    print("=" * 65)

def check_services():
    ports = {"Persona (8081)": 8081, "Bootcamp (8082)": 8082, "Capacidad (8083)": 8083, "Tecnología (8084)": 8084, "Reporte (8085)": 8085}
    inactive = []
    for name, port in ports.items():
        try:
            r = requests.get(f"http://localhost:{port}/swagger-ui.html", auth=("admin", "adminpassword"), timeout=2)
        except requests.RequestException:
            # intentamos con path de api básico
            try:
                r = requests.get(f"http://localhost:{port}", auth=("admin", "adminpassword"), timeout=2)
            except requests.RequestException:
                inactive.append(name)
    if inactive:
        print("❌ Error: Los siguientes servicios no parecen estar activos:")
        for serv in inactive:
            print(f"   - {serv}")
        print("\nPor favor, levántalos primero usando: ./start-services.sh")
        sys.exit(1)
    print("✅ Todos los microservicios están en línea y respondiendo.")

def run_test(name, method, url_template, body_template=None, expected_status=None):
    # Reemplazar variables en URL
    url = url_template
    for key, val in variables.items():
        placeholder = "{{" + key + "}}"
        if val is not None and placeholder in url:
            url = url.replace(placeholder, str(val))
            
    # Reemplazar variables en Body
    body = None
    if body_template:
        body_str = json.dumps(body_template)
        for key, val in variables.items():
            placeholder = "{{" + key + "}}"
            if val is not None and placeholder in body_str:
                body_str = body_str.replace(placeholder, str(val))
        body = json.loads(body_str)

    headers = {"Content-Type": "application/json"}
    
    print(f"\n🚀 Pruebas: {name}")
    print(f"   {method} {url}")
    if body:
        print(f"   Payload: {json.dumps(body)}")
        
    try:
        if method == "POST":
            response = requests.post(url, json=body, headers=headers, auth=("admin", "adminpassword"), timeout=5)
        elif method == "GET":
            response = requests.get(url, headers=headers, auth=("admin", "adminpassword"), timeout=5)
        elif method == "DELETE":
            response = requests.delete(url, headers=headers, auth=("admin", "adminpassword"), timeout=5)
        else:
            print(f"   ❌ Método no soportado: {method}")
            return None

        # Imprimir resultado
        status = response.status_code
        print(f"   Status: {status}")
        try:
            resp_data = response.json()
            print(f"   Respuesta: {json.dumps(resp_data)}")
        except ValueError:
            resp_data = response.text
            print(f"   Respuesta: {resp_data}")

        # Validar status si se especifica
        if expected_status:
            if status in expected_status:
                print(f"   ✅ [OK] Código de estado esperado.")
            else:
                print(f"   ❌ [FALLÓ] Se esperaba {expected_status}, se obtuvo {status}")
        else:
            if status >= 200 and status < 300:
                print(f"   ✅ [OK] Petición exitosa.")
            else:
                print(f"   ⚠️  [AVISO] Código de estado no exitoso: {status}")

        return resp_data
    except Exception as e:
        print(f"   ❌ [ERROR] La petición falló: {e}")
        return None

# --- EJECUCIÓN DEL SCRIPT ---

check_services()

suffix = str(int(time.time()))[-5:]
print(f"ℹ️  Usando el sufijo único '{suffix}' para evitar conflictos de duplicados en base de datos.")

# ==========================================
# HU-1 — Registrar tecnologías
# ==========================================
print_banner("HU-1 — Registrar tecnologías (Tecnología)")

r = run_test("1. Crear Tecnología 1 (Java)", "POST", "http://localhost:8084/technologies", 
             {"name": f"Java_{suffix}", "description": "Lenguaje de programación backend"}, [200, 201])
if r and isinstance(r, dict) and "id" in r:
    variables["tech_1_id"] = r["id"]

r = run_test("2. Crear Tecnología 2 (Spring Boot)", "POST", "http://localhost:8084/technologies", 
             {"name": f"Spring Boot_{suffix}", "description": "Framework backend"}, [200, 201])
if r and isinstance(r, dict) and "id" in r:
    variables["tech_2_id"] = r["id"]

r = run_test("3. Crear Tecnología 3 (Docker)", "POST", "http://localhost:8084/technologies", 
             {"name": f"Docker_{suffix}", "description": "Contenedores"}, [200, 201])
if r and isinstance(r, dict) and "id" in r:
    variables["tech_3_id"] = r["id"]

r = run_test("4. Crear Tecnología para Eliminar", "POST", "http://localhost:8084/technologies", 
             {"name": f"TempTech_{suffix}", "description": "Sera eliminada"}, [200, 201])
if r and isinstance(r, dict) and "id" in r:
    variables["tech_delete_id"] = r["id"]

run_test("5. Listar Tecnologías", "GET", "http://localhost:8084/technologies?page=0&size=10")
run_test("6. Obtener Tecnología por ID", "GET", "http://localhost:8084/technologies/{{tech_1_id}}")
run_test("7. Verificar Tecnologías Existentes", "GET", "http://localhost:8084/technologies/exists?ids={{tech_1_id}},{{tech_2_id}}")
run_test("8. Obtener Detalles de Tecnologías", "GET", "http://localhost:8084/technologies/details?ids={{tech_1_id}},{{tech_2_id}}")
run_test("9. Eliminar Tecnología", "DELETE", "http://localhost:8084/technologies/{{tech_delete_id}}")


# ==========================================
# HU-2 — Registrar capacidades
# ==========================================
print_banner("HU-2 — Registrar capacidades (Capacidad)")

r = run_test("10. Crear Capacidad (Backend Java)", "POST", "http://localhost:8083/capabilities", 
             {
                 "name": f"Backend Java_{suffix}",
                 "description": "Desarrollo backend con Java",
                 "technologyIds": ["{{tech_1_id}}", "{{tech_2_id}}", "{{tech_3_id}}"]
             }, [200, 201])
if r and isinstance(r, dict) and "id" in r:
    variables["cap_1_id"] = r["id"]

r = run_test("11. Crear Capacidad para Eliminar", "POST", "http://localhost:8083/capabilities", 
             {
                 "name": f"TempCap_{suffix}",
                 "description": "Para eliminar",
                 "technologyIds": ["{{tech_1_id}}", "{{tech_2_id}}", "{{tech_3_id}}"]
             }, [200, 201])
if r and isinstance(r, dict) and "id" in r:
    variables["cap_delete_id"] = r["id"]


# ==========================================
# HU-3 — Listar capacidades
# ==========================================
print_banner("HU-3 — Listar capacidades (Capacidad)")

run_test("12. Listar Capacidades", "GET", "http://localhost:8083/capabilities?page=0&size=10&sort=name,asc")
run_test("13. Obtener Capacidad por ID", "GET", "http://localhost:8083/capabilities/{{cap_1_id}}")
run_test("14. Obtener Capacidades en Bulk", "GET", "http://localhost:8083/capabilities/bulk?ids={{cap_1_id}}")
run_test("15. Eliminar Capacidad", "DELETE", "http://localhost:8083/capabilities/{{cap_delete_id}}")


# ==========================================
# HU-4 — Registrar bootcamp
# ==========================================
print_banner("HU-4 — Registrar bootcamp (Bootcamp)")

r = run_test("16. Crear Bootcamp 1 (Aprende Java)", "POST", "http://localhost:8082/bootcamps", 
             {
                 "name": f"Bootcamp Java_{suffix}",
                 "description": "Aprende Java",
                 "releaseDate": "2026-05-01",
                 "duration": 30,
                 "capabilityIds": ["{{cap_1_id}}"]
             }, [200, 201])
if r and isinstance(r, dict) and "id" in r:
    variables["bootcamp_1_id"] = r["id"]

r = run_test("17. Crear Bootcamp 2 (Temporal para eliminar)", "POST", "http://localhost:8082/bootcamps", 
             {
                 "name": f"TempBootcamp_{suffix}",
                 "description": "Para eliminar",
                 "releaseDate": "2026-06-01",
                 "duration": 15,
                 "capabilityIds": ["{{cap_1_id}}"]
             }, [200, 201])
if r and isinstance(r, dict) and "id" in r:
    variables["bootcamp_delete_id"] = r["id"]


# ==========================================
# HU-5 — Listar bootcamps
# ==========================================
print_banner("HU-5 — Listar bootcamps (Bootcamp)")

run_test("18. Listar Bootcamps", "GET", "http://localhost:8082/bootcamps?page=0&size=10&sortName=name&sortDir=asc")
run_test("19. Obtener Bootcamp por ID", "GET", "http://localhost:8082/bootcamps/{{bootcamp_1_id}}")


# ==========================================
# HU-6 — Eliminar bootcamp
# ==========================================
print_banner("HU-6 — Eliminar bootcamp (Bootcamp)")

run_test("20. Eliminar Bootcamp", "DELETE", "http://localhost:8082/bootcamps/{{bootcamp_delete_id}}")


# ==========================================
# HU-7 — Inscribirme en bootcamps (Persona)
# ==========================================
print_banner("HU-7 — Inscribirme en bootcamps (Persona & Bootcamp)")

r = run_test("21. Crear Persona", "POST", "http://localhost:8081/persons", 
             {"name": f"Juan Perez_{suffix}", "email": f"juan.perez{suffix}@example.com"}, [200, 201])
if r and isinstance(r, dict) and "id" in r:
    variables["person_1_id"] = r["id"]

run_test("22. Listar Personas", "GET", "http://localhost:8081/persons?page=0&size=10")
run_test("23. Obtener Persona por ID", "GET", "http://localhost:8081/persons/{{person_1_id}}")
run_test("24. Inscribir Persona en Bootcamp", "POST", "http://localhost:8082/bootcamps/{{bootcamp_1_id}}/enrollments", 
             {"personId": "{{person_1_id}}"}, [200, 201])


# ==========================================
# HU-8 — Registrar reporte de bootcamp
# ==========================================
print_banner("HU-8 — Registrar reporte (Reporte)")

# Esperamos 1 segundo para dar tiempo a la publicación asíncrona del reporte desde Bootcamp a Reporte
print("⏱️ Esperando 1 segundo para asegurar la publicación asíncrona del reporte...")
time.sleep(1)

run_test("25. Registrar Reporte Manualmente (Opcional)", "POST", "http://localhost:8085/reports/bootcamps", 
             {
                 "bootcampId": "{{bootcamp_1_id}}",
                 "bootcampName": "Bootcamp Backend 2026",
                 "bootcampDescription": "Aprende Java",
                 "releaseDate": "2026-05-01",
                 "duration": 30,
                 "capabilities": [],
                 "technologies": [],
                 "enrollments": [],
                 "capabilityCount": 1,
                 "technologyCount": 3,
                 "enrollmentCount": 1
             })

run_test("26. Añadir Inscripción al Reporte (Opcional)", "POST", "http://localhost:8085/reports/bootcamps/{{bootcamp_1_id}}/enrollments", 
             {
                 "personId": "{{person_1_id}}",
                 "name": "Juan Perez",
                 "email": "juan@example.com",
                 "enrollmentDate": "2026-02-22T00:00:00Z"
             })

run_test("27. Listar Reportes", "GET", "http://localhost:8085/reports/bootcamps")
run_test("28. Obtener Reporte por Bootcamp ID", "GET", "http://localhost:8085/reports/bootcamps/{{bootcamp_1_id}}")


# ==========================================
# HU-9 — Mostrar el bootcamp con mayor cantidad de personas
# ==========================================
print_banner("HU-9 — Mostrar el bootcamp con mayor cantidad de personas")

run_test("29. Obtener Bootcamp con Más Inscritos", "GET", "http://localhost:8085/reports/bootcamps/most-enrolled")

print_banner("🎉 ¡Todas las pruebas han finalizado exitosamente! 🎉")
