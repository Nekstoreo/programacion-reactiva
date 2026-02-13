# Cronograma - Backlog ✅
---

### HU-1 — Registrar tecnologías  
**Rol:** admin  
**Descripción:** Yo como admin necesito registrar las tecnologías que serán usadas próximamente por las capacidades para saber el bootcamp a qué tecnologías le está apuntando y agrupar de mejor manera.

**Criterios de aceptación:**
- [ ] Cada tecnología tiene 3 campos: `id`, `nombre` y `descripción`.
- [ ] El `nombre` de la tecnología no se puede repetir.
- [ ] Todas las tecnologías deben tener una `descripción`.
- [ ] Tamaño máximo del `nombre`: 50 caracteres.
- [ ] Tamaño máximo de la `descripción`: 90 caracteres.

---

### HU-2 — Registrar capacidades  
**Rol:** admin  
**Descripción:** Yo como admin necesito registrar las capacidades para agrupar tecnologías.

**Criterios de aceptación:**
- [ ] Cada capacidad tiene 3 campos: `id`, `nombre` y `descripción`.
- [ ] Las capacidades deben tener **mínimo 3** tecnologías asociadas.
- [ ] Las capacidades no pueden tener tecnologías repetidas.
- [ ] Una capacidad tiene **máximo 20** tecnologías.

---

### HU-3 — Listar capacidades  
**Rol:** admin  
**Descripción:** Yo como admin necesito listar las capacidades para visualizar cuáles ya están creadas.

**Criterios de aceptación:**
- [ ] Permitir parametrizar orden asc/desc por `nombre` o por cantidad de tecnologías asociadas.
- [ ] Servicio paginado.
- [ ] De cada capacidad listada, devolver listado de tecnologías solo con `id` y `nombre`.

---

### HU-4 — Registrar bootcamp  
**Rol:** admin  
**Descripción:** Yo como admin necesito registrar bootcamps para dar inicio a eventos del bootcamp.

**Criterios de aceptación:**
- [ ] Cada bootcamp debe tener `id`, `nombre`, `descripción`, `fecha de lanzamiento`, `duración` y listado de capacidades asociadas.
- [ ] Un bootcamp debe tener como **mínimo 1** capacidad asociada y como **máximo 4**.

---

### HU-5 — Listar bootcamps  
**Rol:** admin  
**Descripción:** Yo como admin necesito listar los bootcamps para visualizar cuáles ya están creados.

**Criterios de aceptación:**
- [ ] Permitir parametrizar orden asc/desc por `nombre` o por cantidad de capacidades asociadas.
- [ ] Servicio paginado.
- [ ] De cada bootcamp listado, devolver listado de capacidades (`id`, `nombre`) y listado de tecnologías (`id`, `nombre`).

---

### HU-6 — Eliminar bootcamp  
**Rol:** admin  
**Descripción:** Yo como admin necesito eliminar los bootcamps para que ya no estén disponibles para las personas.

**Criterios de aceptación:**
- [ ] Eliminar bootcamp y capacidades/tecnologías asociadas cuando estén referenciadas **solo por ese bootcamp**.
- [ ] No eliminar capacidades/tecnologías si están referenciadas por otros bootcamps.
- [ ] Operación transaccional.

---

### HU-7 — Inscribirme en bootcamps  
**Rol:** persona  
**Descripción:** Yo como persona necesito inscribirme en varios bootcamps para poder participar en las actividades.

**Criterios de aceptación:**
- [ ] Una persona puede inscribirse en varios bootcamps siempre que no coincidan en `fecha` y `duración`.
- [ ] Máximo **5** bootcamps al mismo tiempo.

---

### HU-8 — Registrar reporte de bootcamp  
**Rol:** admin  
**Descripción:** Yo como admin necesito registrar los reportes de los bootcamps para sacar métricas sobre el comportamiento de los usuarios.

**Criterios de aceptación:**
- [ ] Guardar en la base de datos de reportes toda la información necesaria al registrar un bootcamp.
- [ ] Guardar: información del bootcamp, cantidad de capacidades, cantidad de tecnologías, cantidad de personas inscritas.
- [ ] Esta acción debe realizarse sin afectar el rendimiento del registro del bootcamp.

---

### HU-9 — Mostrar el bootcamp con mayor cantidad de personas  
**Rol:** admin  
**Descripción:** Yo como admin necesito listar el bootcamp con la mayor cantidad de personas para identificar el más exitoso.

**Criterios de aceptación:**
- [ ] Retornar toda la información del bootcamp.
- [ ] Incluir nombre y correo de cada persona inscrita al bootcamp.
- [ ] Incluir cada una de las capacidades y cada una de las tecnologías asociadas al bootcamp.

---

