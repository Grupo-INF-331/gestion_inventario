# Gestión de Inventario para Bodega

**Integrantes del equipo:** Joaquin Aguilera, Marcelo Fernandez

**Fecha:** 26/03/2025

**Enlace al repositorio GitHub (público):**

---

## ✅ 1. Especificación del Requerimiento
### 1.1 Validación (¿Estamos construyendo lo que el usuario necesita?)

- Definir de manera más clara el control de inventario dentro de la aplicación

- Se delimitó el alcance: no es un sistema POS completo, sino un programa sencillo de inventario. Las funcionalidades necesarias para el usuario existen y funcionan, por lo que satisface las necesidades del cliente.

#### Supuestos:

- La autenticación puede ser básica (login por username y password, sin roles).

- No se requiere despliegue en la nube

- El sistema será de escritorio (sin visual y por medio de una línea de comandos)

- No se requiere integración con hardware (ej. lector de códigos).

- La categoría es seleccionable desde un set predefinido (el usuario debe elegir indicando el número de la opción).

### 1.2 Verificación (¿Estamos construyéndolo correctamente?)
- Plan de pruebas dividido en ciclos (como se detalla más abajo).

- Cada funcionalidad del CRUD será testeada con entradas válidas e inválidas.

- Se probará autenticación con credenciales correctas e incorrectas.

- Se validarán los log generados con datos de prueba que se almacenarán en un archivo llamado app.log.

---

## 🧠 2. Organización del Proyecto
### Estructura del Proyecto
Mediante el uso de Python + Flask:

```arduino

gestion_inventario/
│
├── main.py                     # Punto de entrada de la aplicación
├── login.py                   # Funciones de login y autenticación
├── inventario.py              # Funciones CRUD para inventario
├── utils.py                   # Funciones auxiliares como logging
├── logs/                      # Carpeta para guardar los archivos de log
│   └── app.log
└── data/                      # Carpeta para los .txt (almacenamiento local)
    ├── usuarios.txt
    └── inventario.txt

```
### Flujo de Trabajo

- **Ramas Git**:
  - `main`: protegida, estable
  - `dev`: integración
  - `feature/*`: nuevas funcionalidades
- **Slack**: Integrado con GitHub para visualizar commits, PRs, merges.
- **Paradigma Git Flow**: Separación clara de desarrollo y producción.

---

## 🖥️ 3. Codificación

### Lenguaje: Python

### Funcionalidades:

- **CRUD de productos**
- **Autenticación simple**
- **Gestión de stock** (incrementar/disminuir cantidad)
- **Búsqueda y filtrado** por nombre y categoría
- **Reportes**:
  - Total de productos
  - Valor total del inventario (`precio_unitario * cantidad`)
  - Productos agotados (`cantidad == 0`)

Extras Técnicos:
Manejo de excepciones (ej. productos sin nombre, duplicados, etc.)

Logging con logging de Python

- Archivo `README.md` incluye:
- Nombre
- Descripción
- Instalación
- Cómo usar
- Cómo contribuir
- Licencia

---

## 🧪 4. Pruebas

### Estrategia

- Pruebas individuales (Ciclo 1)
- Pruebas cruzadas en equipo (Ciclo 2)
- Pruebas adicionales si es necesario (Ciclo 3)
- Herramienta: `pytest` o pruebas manuales
- Registro: Excel o app.greentest.ai

### Formato sugerido de pruebas:

| Id_Test | Entrada                         | Resultado Esperado               | Resultado Obtenido         | Éxito/Fallo | Comentario              |
|---------|----------------------------------|----------------------------------|-----------------------------|--------------|--------------------------|
| T001    | Crear producto sin nombre        | Rechaza producto                 | Rechaza producto            | ✅            | Validación funciona       |
| T002    | Login con credenciales válidas   | Acceso permitido                 | Acceso permitido            | ✅            |                          |
| T003    | Reporte con inventario vacío     | Total = 0, Productos agotados = 0| Total = 0, Productos agotados = 0 | ✅      |                          |

---

## ⚠️ 5. Problemas Encontrados y Soluciones

- ❌ Error en validación de cantidades negativas → ✅ Se agregó validación extra.
- ❌ Conflictos al hacer merge de ramas → ✅ Uso de `git rebase` para resolver.
- ❌ Slack no notificaba correctamente → ✅ Se reconfiguró integración desde GitHub Apps.

---

## 📎 Extras

- [ ] Pruebas documentadas en [app.greentest.ai](https://app.greentest.ai) (recomendado para puntos extra)
- [ ] Capturas de:
- Pull requests
- Slack mostrando commits
- Aplicación funcionando
- Logs
- [ ] Video corto mostrando el uso (opcional pero recomendable)

---

## 📌 Licencia

Este proyecto está licenciado bajo la licencia MIT. Ver archivo [LICENSE](LICENSE) para más detalles.
