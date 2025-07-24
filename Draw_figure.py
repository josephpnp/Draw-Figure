import cv2 as cv
img_1 = cv.imread("imagen.jpg")
img =cv.resize(img_1, (1920, 800))
print("Que quieres dibujar:")
respuesta_1 = input("Retangulo(1)\n" \
"Circulo(2)\n" \
"Linea(3)\n" \
"Ingrese su respuesta: ")

class figure:
    def __init__(self, **args):
        if "coordenadas1x" in args and "coordenadas1y" in args:
            self.punto1 = args["coordenadas1x"]
            self.punto1_2 = args["coordenadas1y"]

        if "coordenadas2x" in args and "coordenadas2y" in args:
            self.punto2 = args["coordenadas2x"]
            self.punto2_2 = args["coordenadas2y"]

        if "radius" in args:
            self.radius = args["radius"]
            
        if "color_r" in args:
            self.color_r = args["color_r"]

        if "color_g" in args:
            self.color_g = args["color_g"]

        if "color_b" in args:
            self.color_b = args["color_b"]

        if "thickness" in args:
            self.thickness = args["thickness"]

    def draw_rectangle(self):
        print("Dibujando...")
        cv.rectangle(img, (self.punto1, self.punto1_2), (self.punto2, self.punto2_2), (self.color_b, self.color_g, self.color_r), self.thickness)
        cv.imshow('Rectangle', img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def draw_circle(self):
        print("Dibujando...")
        cv.circle(img, (self.punto1, self.punto1_2), self.radius, (self.color_b, self.color_g, self.color_r), self.thickness)
        cv.imshow('Circle', img)
        cv.waitKey(0)
        cv.destroyAllWindows()

    def draw_line(self):
        print("Dibujando...")
        cv.line(img, (self.punto1, self.punto1_2), (self.punto2, self.punto2_2), (self.color_b, self.color_g, self.color_r), self.thickness)
        cv.imshow('Line', img)
        cv.waitKey(0)
        cv.destroyAllWindows()

while True:
    if respuesta_1 == "1":
        punto1 = int(input("ingrese la coordenada x del primer punto (0-800): "))
        punto1_2 = int(input("ingrese la coordenada y del primer punto (0-1920): "))
        punto2 = int(input("ingrese la coordenada x del segundo punto (0-800): "))
        punto2_2 = int(input("ingrese la coordenada y del segundo punto (0-1920): "))
        color_b = int(input("ingrese la cantidad de color azul (0-255): "))
        color_g = int(input("ingrese la cantidad de color verde (0-255): "))
        color_r = int(input("ingrese la cantidad de color rojo (0-255): "))
        thickness = int(input("ingrese la cantidad de grosor: "))
        rectangulo = figure(coordenadas1x = punto1, coordenadas1y = punto1_2, coordenadas2x = punto2, coordenadas2y = punto2_2,  color_b = int(color_b), color_g = int(color_g), color_r = int(color_r), thickness = int(thickness))
        rectangulo.draw_rectangle()
        break

    if respuesta_1 == "2":
        punto1 = int(input("ingrese la coordenada x del primer punto (0-800): "))
        punto1_2 = int(input("ingrese la coordenada y del primer punto (0-1920): "))
        radius = int(input("ingrese el radio: "))
        color_b = int(input("ingrese la cantidad de color azul (0-255): "))
        color_g = int(input("ingrese la cantidad de color verde (0-255): "))
        color_r = int(input("ingrese la cantidad de color rojo (0-255): "))
        thickness = int(input("ingrese la cantidad de grosor: "))
        circulo = figure(coordenadas1x = punto1, coordenadas1y = punto1_2, radius = radius, color_b = int(color_b), color_g = int(color_g), color_r = int(color_r), thickness = int(thickness))
        circulo.draw_circle()
        break
    if respuesta_1 == "3":
        punto1 = int(input("ingrese la coordenada x del primer punto (0-800): "))
        punto1_2 = int(input("ingrese la coordenada y del primer punto (0-1920): "))
        punto2 = int(input("ingrese la coordenada x del segundo punto (0-800): "))
        punto2_2 = int(input("ingrese la coordenada y del segundo punto (0-1920): "))
        color_b = int(input("ingrese la cantidad de color azul (0-255): "))
        color_g = int(input("ingrese la cantidad de color verde (0-255): "))
        color_r = int(input("ingrese la cantidad de color rojo (0-255): "))
        thickness = int(input("ingrese la cantidad de grosor: "))
        linea = figure(coordenadas1x = punto1, coordenadas1y = punto1_2, coordenadas2x = punto2, coordenadas2y = punto2_2,  color_b = int(color_b), color_g = int(color_g), color_r = int(color_r), thickness = int(thickness))
        linea.draw_line()
        break