class HashTable:
    def __init__(self):
        # Inicializa collection como un diccionario vacío
        self.collection = {}
        
    def hash(self, cadena):
        # Suma los valores Unicode de cada carácter
        valor = 0
        for c in cadena:
            valor += ord(c)
        return valor
    
    def add(self, clave, valor):
        # USAMOS self.hash para llamar a nuestro método
        hash_calculado = self.hash(clave)
        
        # Si el valor hash no existe, creamos el sub-diccionario para las colisiones
        if hash_calculado not in self.collection:
            self.collection[hash_calculado] = {}
            
        # Guardamos el par clave-valor real dentro de ese hash
        self.collection[hash_calculado][clave] = valor
    
    def remove(self, clave):
        hash_calculado = self.hash(clave)
        
        # Verificamos si el hash existe y si la clave real está dentro de él
        if hash_calculado in self.collection and clave in self.collection[hash_calculado]:
            self.collection[hash_calculado].pop(clave)
                
    def lookup(self, clave):
        hash_calculado = self.hash(clave)
        
        # Verificamos si el hash y la clave existen
        if hash_calculado in self.collection and clave in self.collection[hash_calculado]:
            # Devolvemos el valor específico asociado a esa clave
            return self.collection[hash_calculado][clave]
            
        # Si no existe, devolvemos None
        return None