# Gestión de Inventario para Bodega

**Integrantes del equipo:** Joaquin Aguilera, Marcelo Fernandez

**Fecha:** 26/03/2025

**Enlace al repositorio GitHub (público):**

---

## ✅ 1. Especificación del Requerimiento
### 1.1 Validación (¿Estamos construyendo lo que el usuario necesita?)
Antes de iniciar la programación, se buscará especificar lo que desea el cliente mediante preguntas y supuestos, buscando minimizar el errror entre lo que espera el cliente y el producto que finalmente se le entregará, para ello, se realizan las siguientes aclaraciones y supuestos:
- Se realizaron preguntas en Foro con el usuario (profesor).
- 
- Se definieron claramente los campos de cada producto: "nombre, descripción, cantidad disponible, precio unitario y categoría"

- Se delimitó el alcance: se requiere una App sencilla que invluya el crud visible y operable solo mediante Linea de comandos.

- El reporte debe ofrecer Información de Storks y productos disponibles solo bajo demanda.

#### Supuestos:

- La autenticación puede ser básica (login por username y password), existiendo solo un rol general.

- El sistema debe ser .

- No se requiere integración con hardware (ej. lector de códigos).

- El usuario puede agregar productos con categorias nuevas y éstas serán agregadas de manera automática.

- El filtro debe funcionar con el nombre del producto, su categoría, o su SKU.

- No es necesario una base de datos en la nube con datos clasificados, basta con archivos locales.

- El reporte debe mostrar la cantidad de productos disponibles,nombre de agotados, y el  valor total.

- Se debe poder actualizar cualquier variable de cada producto, preguntando cual desea configurarse especificamente.

### 1.2 Verificación (¿Estamos construyéndolo correctamente?)
Para asegurar que se cumpla lo solicitado por el cliente, se realizará las siguientes verificaciones:
- Plan de pruebas dividido en 2 ciclos (se describirán abajo).

- Cada funcionalidad del CRUD será testeada con entradas válidas e inválidas.

- Se probará autenticación con credenciales correctas e incorrectas.

- Se validarán los reportes generados con datos de prueba.

- Se probará el funcionamiento con usuario de prueba externo al desarrollo del programa.

---
## 🧠 2. Organización del Proyecto
### Estructura del Proyecto
El proyecto fué programado en diferentes archivos modularizando cada área del programa, esto fué trabajado con el paradigma de flujo Git Flow, siendo utilizadas las siguientes ramas:
- main: rama principal donde se envia el código estable listo para producción.
  
- develop: rama base para integrar las funcionalidades nuevas que se programen.

- feature/*: ramas de cada funcionalidad.
### Flujo de Trabajo
- **Ramas Git**:
/gestion_inventario/
├── data/
│   ├── inventario.txt
│   └── usuarios.txt
├── logs/
│   └── app.log
├── eliminar.md
├── Entregable.md
├── inventario.py
├── login.py
├── main.py
├── Readme.md
├── utils.py

## 🖥️ 3. Codificación

### Lenguaje: Python (recomendado)

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
