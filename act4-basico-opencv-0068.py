
# ==============================================================================
# 0. IMPORTACIÓN DE LIBRERÍAS
# ==============================================================================
import cv2       # OpenCV para procesamiento de imágenes.
import numpy as np  # NumPy para trabajar con matrices.
import sys       # Permite detener el programa si ocurre un error.

# ==============================================================================
# DATOS PERSONALES
# ==============================================================================
nombre = "Christian Garcia Jimenez"
nc = "0068"
fecha = "19/11/2026"

print(f" ------ {nombre} Nc = {nc} ------ ")
print(f" ------ Fecha = {fecha} ------- ")

# ==============================================================================
# FUNCIÓN PARA CREAR VENTANAS CON NOMBRE Y TAMAÑO PERSONALIZADO
# ==============================================================================
def mostrar_ventana(titulo, imagen):

    # Construimos el nombre personalizado de la ventana
    titulo_ventana = f"VISION ARTIFICIAL - {titulo} - NC: {nc}"

    # Creamos una ventana que permita cambiar su tamaño
    cv2.namedWindow(titulo_ventana, cv2.WINDOW_NORMAL)

    # Establecemos el tamaño de la ventana
    cv2.resizeWindow(titulo_ventana, 1000, 700)

    # Mostramos la imagen
    cv2.imshow(titulo_ventana, imagen)

    # Esperamos a que se presione una tecla
    cv2.waitKey(0)


# ==============================================================================
# 1. LECTURA DE LA IMAGEN DESDE LA CARPETA
# ==============================================================================
print("\n1. LECTURA DE IMÁGENES")

img = cv2.imread('image.png')

if img is None:
    print("Error: No se pudo leer 'image.png'. Revisa el nombre y ubicación.")
    sys.exit()
else:
    print("Imagen cargada exitosamente.")

# ==============================================================================
# 2. PROPIEDADES DE LA IMAGEN
# ==============================================================================
print("\n2. PROPIEDADES DE LA IMAGEN")

height, width, channels = img.shape

print(f"Dimensiones de la imagen: {width}x{height} píxeles")
print(f"Número de canales de color: {channels}")
print(f"Tipo de dato de la imagen: {img.dtype}")
print(f"Total de datos/píxeles: {img.size}")

# ==============================================================================
# 3. VISUALIZACIÓN DE LA IMAGEN ORIGINAL
# ==============================================================================
print("\n3. MOSTRANDO IMAGEN ORIGINAL")
print("Presiona cualquier tecla sobre la ventana para continuar...")

mostrar_ventana("IMAGEN ORIGINAL", img)

# ==============================================================================
# 4. ACCESO Y MODIFICACIÓN DE PÍXELES INDIVIDUALES
# ==============================================================================
print("\n4. ACCEDIENDO Y MODIFICANDO PÍXELES")

pixel_img = img.copy()

y, x = 100, 150

# Verificamos que las coordenadas existan en la imagen
if y >= height or x >= width:
    print("Error: La imagen es demasiado pequeña para analizar ese píxel.")
    cv2.destroyAllWindows()
    sys.exit()

pixel = pixel_img[y, x]

print(f"Valor del píxel en ({x}, {y}): {pixel} (Formato BGR)")

# Cambiamos el píxel a color rojo
pixel_img[y, x] = [0, 0, 255]

# Dibujamos un círculo amarillo alrededor del píxel
cv2.circle(pixel_img, (x, y), 15, (0, 255, 255), 2)

mostrar_ventana("PIXEL MODIFICADO Christian Garcia 0068", pixel_img)

# ==============================================================================
# 5. REGIÓN DE INTERÉS (ROI - REGION OF INTEREST)
# ==============================================================================
print("\n5. REGIÓN DE INTERÉS (ROI)")

roi_img = img.copy()

# Recortamos una región de la imagen
roi = roi_img[50:200, 100:300]

# Dibujamos un rectángulo verde en la región seleccionada
cv2.rectangle(roi_img, (100, 50), (300, 200), (0, 255, 0), 2)

mostrar_ventana("IMAGEN CON ROI MARCADA", roi_img)

mostrar_ventana("ROI EXTRAIDA - RECORTE", roi)

# ==============================================================================
# 6. SEPARACIÓN Y FUSIÓN DE CANALES DE COLOR (BGR)
# ==============================================================================
print("\n6. SEPARANDO Y FUSIONANDO CANALES")

# Separamos los canales azul, verde y rojo
b, g, r = cv2.split(img)

mostrar_ventana("CANAL AZUL - ESCALA DE GRISES", b)
mostrar_ventana("CANAL VERDE - ESCALA DE GRISES", g)
mostrar_ventana("CANAL ROJO - ESCALA DE GRISES", r)

# Creamos matrices de ceros
zeros = np.zeros_like(b)

# Fusionamos los canales para mostrar cada color por separado
blue_img = cv2.merge([b, zeros, zeros])
green_img = cv2.merge([zeros, g, zeros])
red_img = cv2.merge([zeros, zeros, r])

mostrar_ventana("CANAL AZUL - COLOREADO", blue_img)
mostrar_ventana("CANAL VERDE - COLOREADO", green_img)
mostrar_ventana("CANAL ROJO - COLOREADO", red_img)

# ==============================================================================
# 7. REDIMENSIONAMIENTO DE IMÁGENES (RESIZING)
# ==============================================================================
print("\n7. REDIMENSIONANDO IMÁGENES")

# Cambiamos el tamaño a 400 x 300 píxeles
resized_img = cv2.resize(img, (400, 300))

mostrar_ventana("REDIMENSIONADA A 400x300", resized_img)

# Reducimos la imagen a la mitad
half_size = cv2.resize(img, None, fx=0.5, fy=0.5)

# Ampliamos la imagen 1.5 veces
double_size = cv2.resize(img, None, fx=1.5, fy=1.5)

mostrar_ventana("MITAD DE TAMANO - 0.5x", half_size)
mostrar_ventana("AMPLIADA - 1.5x", double_size)

# ==============================================================================
# 8. ROTACIÓN DE IMÁGENES
# ==============================================================================
print("\n8. ROTANDO IMÁGENES")

height, width = img.shape[:2]

# Creamos la matriz de rotación de 45 grados
rotation_matrix = cv2.getRotationMatrix2D(
    (width / 2, height / 2), 45, 1
)

# Aplicamos la rotación
rotated_img = cv2.warpAffine(
    img, rotation_matrix, (width, height)
)

mostrar_ventana("IMAGEN ROTADA - 45 GRADOS", rotated_img)

# ==============================================================================
# 9. VOLTEO / ESPEJO DE IMÁGENES (FLIPPING)
# ==============================================================================
print("\n9. VOLTEANDO IMÁGENES")

# Volteo horizontal
horizontal_flip = cv2.flip(img, 1)

mostrar_ventana("VOLTEO HORIZONTAL - ESPEJO", horizontal_flip)

# Volteo vertical
vertical_flip = cv2.flip(img, 0)

mostrar_ventana("VOLTEO VERTICAL - DE CABEZA", vertical_flip)

# Volteo en ambos ejes
both_flip = cv2.flip(img, -1)

mostrar_ventana("VOLTEO EN AMBOS EJES", both_flip)

# ==============================================================================
# 10. GUARDADO DE RESULTADOS Y LIMPIEZA
# ==============================================================================
print("\n10. GUARDANDO IMAGEN RESULTANTE")

# Guardamos la imagen rotada
result = cv2.imwrite('image.png', rotated_img)

if result:
    print("Imagen rotada guardada exitosamente como 'image.png'")
else:
    print("Error: No se pudo guardar la imagen rotada.")

# Cerramos todas las ventanas
cv2.destroyAllWindows()

print("\n¡Todas las operaciones se completaron con éxito!")





