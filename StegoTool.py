#!/usr/bin/env python3
"""
Stego Tool - Cinn4mor0ll
"""

import sys
from PIL import Image
import argparse

ASCII_ART = """
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣄⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣿⠟⠉⠉⠉⠻⣮⡄
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡏⠀⠀⠀⠀⠀⢻⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⠁⠀⠀⠀⠀⠀⢸⣿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡟⠀⠀⠀⠀⠀⠀⣾⡿
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⡀⣀⡀⠀⠀⣠⣿⠟⠀⠀⠀⠀⠀⠀⣸⣿⠁
⠀⠀⠀⠀⠀⠀⣀⣤⣶⠿⠟⠛⠛⠙⠛⠛⠛⠳⢷⣾⡟⠉⠀⠀⠀⠀⠀⢀⣴⣿⠃⠀
⠀⠀⠀⠀⣀⣀⣴⡾⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠀⠀⠀⠀⢀⣤⣾⠟⠁⠀⠀
⠀⠀⠀⠀⣤⡿⠟⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣦⣶⡿⠟⠁⠀⠀⠀⠀
⠀⠀⠀⣼⡟⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠘⢿⣆⠀⠀⠀⠀⠀⠀
⠀⠀⢰⣿⠃⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡾⠁⠹⠆⠀⠀⠈⣿⡆⠀⠀⠀⠀⠀
⠀⠀⣾⡏⠀⣿⠀⠀⠀⣴⠛⢳⡄⠀⠀⠀⠀⠀⠀⢀⣀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡇⠀⠀⠀⠀⠀
⠀⣸⡿⠁⠀⣟⠀⠀⠀⠃⠀⠀⠀⠀⢰⣇⣤⠖⠲⠶⠛⠀⠀⠀⠀⠀⠀⣠⣾⠟⠀⠀⠀⠀⠀⠀
⣰⣿⠃⠀⠀⢻⣄⠀⠀⠀⠀⠀⠀⠀⠀⠈⠀⠀⠀⠀⠀⠀⢀⣀⣤⣴⡾⠟⠉⠀⠀⠀⠀⠀⠀⠀
⣿⡇⠀⠀⠀⠀⠛⢶⣤⣀⣀⣀⣀⣀⣀⣠⣤⣤⣴⣶⡶⠿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⢿⣧⠀⠀⠀⠀⠀⠀⠀⣽⡿⠛⠛⠛⠋⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠈⢿⣧⣀⣀⣀⣀⣤⣾⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠉⠛⠛⠛⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
"""

class StegoTool:
    def __init__(self):
        self.delimiter = "<<<END_OF_PAYLOAD>>>"  # Marcador de fin de datos
    
    def text_to_binary(self, text):
        """Convierte texto a representación binaria"""
        binary = ''.join(format(ord(char), '08b') for char in text)
        return binary
    
    def binary_to_text(self, binary):
        """Convierte binario de vuelta a texto"""
        text = ''
        for i in range(0, len(binary), 8):
            byte = binary[i:i+8]
            if len(byte) == 8:
                text += chr(int(byte, 2))
        return text
    
    def hide_data(self, image_path, data, output_path):
        """
        Oculta datos en una imagen usando LSB
        """
        try:
            # Cargar imagen
            img = Image.open(image_path)
            
            # Convertir a RGB si es necesario
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            # Convertir datos a string si son bytes
            if isinstance(data, bytes):
                data = data.decode('utf-8', errors='ignore')
            
            # Agregar delimitador para saber dónde termina el payload
            data_with_delimiter = data + self.delimiter
            
            # Convertir datos a binario
            binary_data = self.text_to_binary(data_with_delimiter)
            data_length = len(binary_data)
            
            print(f"[*] Imagen original: {image_path}")
            print(f"[*] Tamaño de la imagen: {img.size}")
            print(f"[*] Datos a ocultar: {len(data)} bytes")
            print(f"[*] Datos en binario: {data_length} bits")
            
            # Verificar que la imagen es suficientemente grande
            max_bytes = img.size[0] * img.size[1] * 3  # 3 canales RGB
            if data_length > max_bytes:
                print(f"[-] Error: La imagen es muy pequeña para ocultar estos datos")
                print(f"    Necesitas al menos {data_length} bits, pero solo hay {max_bytes} bits disponibles")
                return False
            
            # Convertir imagen a lista de píxeles
            pixels = list(img.getdata())
            new_pixels = []
            
            data_index = 0
            
            # Modificar los píxeles
            for pixel in pixels:
                if data_index < data_length:
                    # Modificar cada canal RGB
                    r, g, b = pixel
                    
                    # Modificar canal R
                    if data_index < data_length:
                        r = (r & 0xFE) | int(binary_data[data_index])
                        data_index += 1
                    
                    # Modificar canal G
                    if data_index < data_length:
                        g = (g & 0xFE) | int(binary_data[data_index])
                        data_index += 1
                    
                    # Modificar canal B
                    if data_index < data_length:
                        b = (b & 0xFE) | int(binary_data[data_index])
                        data_index += 1
                    
                    new_pixels.append((r, g, b))
                else:
                    # Resto de píxeles sin modificar
                    new_pixels.append(pixel)
            
            # Crear nueva imagen
            stego_img = Image.new(img.mode, img.size)
            stego_img.putdata(new_pixels)
            
            # Guardar imagen
            stego_img.save(output_path, 'PNG')
            
            print(f"[+] Datos ocultados exitosamente en: {output_path}")
            print(f"[+] Bits modificados: {data_index}/{max_bytes}")
            
            return True
            
        except Exception as e:
            print(f"[-] Error ocultando datos: {str(e)}")
            return False
    
    def extract_data(self, image_path):
        """
        Extrae datos ocultos de una imagen
        """
        try:
            # Cargar imagen
            img = Image.open(image_path)
            
            if img.mode != 'RGB':
                img = img.convert('RGB')
            
            print(f"[*] Extrayendo datos de: {image_path}")
            
            # Convertir imagen a lista de píxeles
            pixels = list(img.getdata())
            
            # Extraer bits
            binary_data = ''
            
            for pixel in pixels:
                r, g, b = pixel
                
                # Extraer LSB de cada canal
                binary_data += str(r & 1)
                binary_data += str(g & 1)
                binary_data += str(b & 1)
            
            # Convertir binario a texto
            extracted_text = self.binary_to_text(binary_data)
            
            # Buscar delimitador
            if self.delimiter in extracted_text:
                # Extraer solo hasta el delimitador
                data = extracted_text.split(self.delimiter)[0]
                print(f"[+] Datos extraídos: {len(data)} bytes")
                return data
            else:
                print("[-] No se encontró delimitador. La imagen podría no contener datos ocultos.")
                return None
            
        except Exception as e:
            print(f"[-] Error extrayendo datos: {str(e)}")
            return None
    
    def hide_file(self, image_path, file_path, output_path):
        """
        Oculta un archivo completo en una imagen
        """
        try:
            # Leer archivo
            with open(file_path, 'rb') as f:
                file_data = f.read()
            
            print(f"[*] Archivo a ocultar: {file_path}")
            print(f"[*] Tamaño del archivo: {len(file_data)} bytes")
            
            # Convertir bytes a string hexadecimal para preservar datos binarios
            hex_data = file_data.hex()
            
            # Ocultar en imagen
            return self.hide_data(image_path, hex_data, output_path)
            
        except Exception as e:
            print(f"[-] Error ocultando archivo: {str(e)}")
            return False
    
    def extract_file(self, image_path, output_path):
        """
        Extrae un archivo oculto de una imagen
        """
        try:
            # Extraer datos
            hex_data = self.extract_data(image_path)
            
            if hex_data is None:
                return False
            
            # Convertir hex de vuelta a bytes
            file_data = bytes.fromhex(hex_data)
            
            # Guardar archivo
            with open(output_path, 'wb') as f:
                f.write(file_data)
            
            print(f"[+] Archivo extraído: {output_path}")
            print(f"[+] Tamaño: {len(file_data)} bytes")
            
            return True
            
        except Exception as e:
            print(f"[-] Error extrayendo archivo: {str(e)}")
            return False

def main():
    # Mostrar el ASCII Art al inicio
    print(ASCII_ART)
    
    parser = argparse.ArgumentParser(
        description='Stego Tool - Oculta/Extrae datos en imágenes usando LSB',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Ejemplos de uso:

  Ocultar texto:
    python stego.py hide -i imagen.png -t "Texto secreto" -o output.png
  
  Ocultar archivo:
    python stego.py hide -i imagen.png -f agent.py -o output.png
  
  Extraer datos:
    python stego.py extract -i output.png
  
  Extraer archivo:
    python stego.py extract -i output.png -o agent_extracted.py
        """
    )
    
    subparsers = parser.add_subparsers(dest='command', help='Comando a ejecutar')
    
    # Comando: hide
    hide_parser = subparsers.add_parser('hide', help='Ocultar datos en imagen')
    hide_parser.add_argument('-i', '--image', required=True, help='Imagen original')
    hide_parser.add_argument('-t', '--text', help='Texto a ocultar')
    hide_parser.add_argument('-f', '--file', help='Archivo a ocultar')
    hide_parser.add_argument('-o', '--output', required=True, help='Imagen de salida')
    
    # Comando: extract
    extract_parser = subparsers.add_parser('extract', help='Extraer datos de imagen')
    extract_parser.add_argument('-i', '--image', required=True, help='Imagen con datos ocultos')
    extract_parser.add_argument('-o', '--output', help='Archivo de salida (para archivos ocultos)')
    
    args = parser.parse_args()
    
    if args.command is None:
        # Si no se da ningún comando, ya se mostró el ASCII Art
        parser.print_help()
        sys.exit(1)
    
    stego = StegoTool()
    
    if args.command == 'hide':
        if args.text:
            # Ocultar texto
            success = stego.hide_data(args.image, args.text, args.output)
        elif args.file:
            # Ocultar archivo
            success = stego.hide_file(args.image, args.file, args.output)
        else:
            print("[-] Debes especificar -t (texto) o -f (archivo)")
            sys.exit(1)
        
        sys.exit(0 if success else 1)
    
    elif args.command == 'extract':
        if args.output:
            # Extraer archivo
            success = stego.extract_file(args.image, args.output)
        else:
            # Extraer y mostrar datos
            data = stego.extract_data(args.image)
            if data:
                print("\n" + "="*50)
                print("DATOS EXTRAÍDOS:")
                print("="*50)
                print(data)
                print("="*50)
                success = True
            else:
                success = False
        
        sys.exit(0 if success else 1)

if __name__ == "__main__":
    main()
