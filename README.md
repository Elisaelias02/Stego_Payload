# Stego Tool - LSB (Least Significant Bit)

Herramienta de **esteganografía** en Python que permite ocultar y extraer datos (texto o archivos binarios) dentro de imágenes PNG utilizando la técnica del Bit Menos Significativo (Least Significant Bit, **LSB**).

Este *script* es una creación de **Elisa Elias**
---

## Requisitos

Necesitarás tener **Python 3** instalado, junto con la librería `Pillow` (fork de PIL) para el procesamiento de imágenes.

```bash
pip install Pillow
```

---

## Uso

El script utiliza la librería `argparse`, por lo que su ejecución se realiza a través de comandos claros en la terminal.

### Ocultar Datos (`hide`)

Permite ocultar un payload (texto o archivo) dentro de una imagen.

| Argumento        |                                                          Descripción |                Obligatorio               |
| ---------------- | -------------------------------------------------------------------: | :--------------------------------------: |
| `-i`, `--image`  |                              Ruta de la imagen original (portadora). |                    Sí                    |
| `-o`, `--output` | Ruta donde se guardará la imagen esteganografiada (debe ser `.png`). |                    Sí                    |
| `-t`, `--text`   |                                                  El texto a ocultar. | No (usar `-f` en su lugar para archivos) |
| `-f`, `--file`   |                    La ruta del archivo binario o de texto a ocultar. |   No (usar `-t` en su lugar para texto)  |

**Ejemplos**:

```bash
# Ocultar texto
python stego.py hide -i cover.png -t "La clave es 12345" -o stego_out.png

# Ocultar un archivo zip completo
python stego.py hide -i cover.png -f payload.zip -o stego_payload.png
```

---

### Extraer Datos (`extract`)

Permite recuperar el payload (texto o archivo) de la imagen que lo contiene.

| Argumento        |                                                                                                  Descripción | Obligatorio |
| ---------------- | -----------------------------------------------------------------------------------------------------------: | :---------: |
| `-i`, `--image`  |                                                                          Ruta de la imagen esteganografiada. |      Sí     |
| `-o`, `--output` | Ruta para guardar el archivo extraído. Si no se especifica, el script intentará mostrar el texto en consola. |      No     |

**Ejemplos**:

```bash
# Extraer y mostrar texto en consola
python stego.py extract -i stego_out.png

# Extraer y guardar un archivo binario
python stego.py extract -i stego_payload.png -o recovered_file.zip
```

---

## Advertencia (Esteganálisis)

La técnica LSB modifica los bits menos perceptibles de los píxeles de la imagen. Aunque la imagen resultante es visualmente idéntica a la original, su tamaño de archivo puede cambiar (incluso aumentar) y la presencia de datos ocultos puede ser detectada por herramientas avanzadas de esteganálisis. Utiliza esta herramienta únicamente para fines legítimos, educativos o de análisis forense.

---

## Licencia y atribución

Creado por **Elisa Elias** **H4ck The World**. Usa, estudia y mejora bajo responsabilidad propia.
