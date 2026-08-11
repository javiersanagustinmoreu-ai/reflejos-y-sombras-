# Reflejos y sombras — Sitio estático

Pequeña página estática que muestra la exposición "Reflejos y sombras" (index.html).

## Cómo ejecutar
Desde un clone local basta con servir el directorio o abrir index.html en el navegador.

Opción recomendada (para evitar problemas de CORS y cabeceras):

```bash
python -m http.server 8000
# luego abrir http://localhost:8000
```

## Nombres de imagen esperados
El código (index.html) busca imágenes en la carpeta `img/` usando el `id` de cada obra y probando extensiones en este orden: `jpg, JPG, jpeg, JPEG, png, PNG`.

Base names esperados (sin extensión):

- portada
- antes-de-encontrar
- luz-retenida
- hacia-arriba
- cerro-encendido
- entre-fragmentos
- llanura-interior
- antes-de-ver
- en-el-umbral
- mirada-encarnada
- ardiente-calma
- sin-distancia
- pupila-azul
- no-caigas
- antes-de-reconocer

Cualquier una de las extensiones listadas funcionará mientras el nombre base coincida exactamente (guiones, minúsculas, sin espacios ni caracteres extra).

## Discrepancias actuales
Actualmente el repositorio contiene tanto los nombres originales con espacios como las versiones normalizadas que añadí. Mantengo las originales intactas hasta que me indiques borrarlas.

## Validación rápida
He añadido un script para comprobar que para cada id exista al menos un archivo de imagen con las extensiones aceptadas. Ejecuta:

```bash
python3 scripts/validate_images.py
```

## Siguientes pasos sugeridos
- Cuando subas las tres imágenes que faltan (`hacia-arriba`, `cerro-encendido`, `entre-fragmentos`), vuelve a ejecutar el script de validación.
- Si quieres que elimine los nombres antiguos (con espacios) puedo hacerlo en un commit separado.

© Javier Sanagustín Moreu — Todos los derechos reservados.
