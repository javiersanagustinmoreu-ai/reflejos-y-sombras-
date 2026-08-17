#!/usr/bin/env python3
"""
scripts/validate_images.py

Busca en index.html la constante ORDEN y comprueba que para cada id
exista al menos un archivo en la carpeta img/ con cualquiera de las
extensiones aceptadas por la web (jpg, JPG, jpeg, JPEG, png, PNG).

Salida:
 - imprime una línea por obra indicando si encontró un fichero y cuál
 - código de salida 0 si todo está presente, 1 si faltan imágenes

Uso:
  python3 scripts/validate_images.py

El script asume que se ejecuta desde la raíz del repositorio.
"""

from __future__ import annotations
import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]
INDEX_PATH = REPO_ROOT / 'index.html'
IMG_DIR = REPO_ROOT / 'img'

# Copia orden y extensiones coherentes con index.html
IMG_EXTS = ['jpg', 'JPG', 'jpeg', 'JPEG', 'png', 'PNG']

def extract_orden(index_text: str) -> list[str]:
    """Extrae la lista ORDEN declarada como: const ORDEN = [ "id1","id2", ... ];"""
    # Primer intento estricto
    m = re.search(r"const\s+ORDEN\s*=\s*\[([^\]]*)\]", index_text, re.S)
    if not m:
        # Intento más permisivo (por si hay ; al final o saltos variados)
        m = re.search(r"const\s+ORDEN\s*=\s*\[((?:.|\n)*?)\]\s*;", index_text, re.S)
        if not m:
            return []
    inner = m.group(1)
    # Captura cadenas entre comillas simples o dobles
    items = re.findall(r"['\"]([^'\"]+)['\"]", inner)
    return [it.strip() for it in items if it.strip()]


def main() -> int:
    if not INDEX_PATH.exists():
        print(f"ERROR: no se encontró {INDEX_PATH}. Ejecuta el script desde la raíz del repo.")
        return 2

    text = INDEX_PATH.read_text(encoding='utf-8')
    orden = extract_orden(text)

    # Añadir imágenes extra que la web usa (portada, biografia)
    extras = ['portada', 'biografia']
    expected = extras + orden

    if not IMG_DIR.exists():
        print(f"Aviso: no existe la carpeta {IMG_DIR}. Ninguna imagen podrá validarse.")
    else:
        print(f"Comprobando imágenes en: {IMG_DIR.resolve()}\n")

    missing = []

    for id_ in expected:
        found_file = None
        for ext in IMG_EXTS:
            candidate = IMG_DIR / f"{id_}.{ext}"
            if candidate.exists():
                found_file = candidate.name
                break
        if found_file:
            print(f"✓ {id_:20} → {found_file}")
        else:
            print(f"✗ {id_:20} → MISSING (esperado: img/{id_}.[{', '.join(IMG_EXTS)}])")
            missing.append(id_)

    print('\nResumen:')
    if missing:
        print(f"Faltan {len(missing)} imagen(es): {', '.join(missing)}")
        return 1
    else:
        print('Todas las imágenes esperadas están presentes.')
        return 0

if __name__ == '__main__':
    raise SystemExit(main())
