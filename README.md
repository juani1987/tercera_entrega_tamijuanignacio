# tercera_entrega_tamijuanignacio
# Proyecto Django MVT

Este es un proyecto de ejemplo usando Django con el patrón MVT.

## Funcionalidades

1. **Herencia de HTML**: Los templates están organizados siguiendo un layout base en `base.html` y extendidos en otras plantillas.
   
   - `index.html` - Template base que define la estructura común del sitio.
   - `index.html` - Página de inicio que muestra categorías.
   - `productos.html` - Página que muestra todos los productos.
   - `clientes.html` - Página que muestra todos los clientes.

2. **Modelos**: Definidos en `models.py`.
   
   - `Categoria`: Modela las categorías de productos.
   - `Producto`: Modela los productos vinculados a categorías.
   - `Cliente`: Modela los clientes con nombre, dirección y teléfono.

3. **Formulario de Búsqueda**: Implementado para buscar productos por nombre en `buscar_producto.html`.
   
   - `forms.py` - Define `ProductoSearchForm` para la búsqueda.
   - `views.py` - `buscar_producto` maneja la lógica de búsqueda y renderiza resultados.

## Orden de Prueba

1. Asegúrate de tener Python y Django instalados.
2. Configura el entorno virtual y activa el entorno.
3. Instala los requerimientos (`pip install -r requirements.txt` si tienes un archivo).
4. Crea las migraciones y aplica (`python manage.py makemigrations` y `python manage.py migrate`).
5. Carga datos de prueba si es necesario (`python manage.py loaddata datos.json`).
6. Ejecuta el servidor de desarrollo (`python manage.py runserver`) y prueba las URLs:

   - Inicio: `http://127.0.0.1:8000/`
   - Productos: `http://127.0.0.1:8000/productos/`
   - Clientes: `http://127.0.0.1:8000/clientes/`
   - Búsqueda de Productos: `http://127.0.0.1:8000/buscar/`

7. Ajusta y desarrolla según sea necesario.

## Notas Adicionales

- Asegúrate de que los archivos estáticos (CSS, JS, imágenes) estén correctamente configurados.
- Revisa los logs de Django (`python manage.py runserver`) para cualquier error o advertencia.
