class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def set_width(self, value):
        self.width = value

    def set_height(self, value):
        self.height = value
        
    def get_area(self):
        return self.width * self.height
    
    def get_perimeter(self):
        return 2 * (self.width + self.height)
    
    def get_diagonal(self):
        return (self.width**2 + self.height**2) ** 0.5
    
    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."
        fila = ("*" * self.width) + "\n"
        return fila * self.height
    
    def get_amount_inside(self, figura):
        # Se calcula cuántas veces cabe horizontal y verticalmente sin rotar
        cabes_ancho = self.width // figura.width
        cabes_alto = self.height // figura.height
        return cabes_ancho * cabes_alto

    def __str__(self):
        return f"Rectangle(width={self.width}, height={self.height})"
    
    
class Square(Rectangle):
    def __init__(self, side):
        # Almacena el lado tanto en el ancho como en el alto del Rectangle
        super().__init__(side, side)
        
    def set_side(self, value):
        self.width = value
        self.height = value

    def set_width(self, value):
        self.set_side(value)
        
    def set_height(self, value):
        self.set_side(value)

    def __str__(self):
        return f"Square(side={self.width})"
    
