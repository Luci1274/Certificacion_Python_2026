class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []
    
    def deposit(self, amount, description=""):
        self.ledger.append({"amount": amount, "description": description})

    def withdraw(self, amount, description=""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -abs(amount), "description": description})
            return True
        return False        
        
    def get_balance(self):
        balance = 0
        for movimiento in self.ledger:
            balance += movimiento["amount"]    
        return balance
    
    def transfer(self, amount, destination):
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination.name}")
            destination.deposit(amount, f"Transfer from {self.name}")
            return True
        return False
    
    def check_funds(self, cantidad):
        return cantidad <= self.get_balance()
        
    def __str__(self):
        resultado = self.name.center(30, "*") + "\n"
        for movimiento in self.ledger:  
            descripcion_formateada = f"{movimiento['description'][:23]:<23}"
            monto_formateado = f"{movimiento['amount']:>7.2f}"
            resultado += descripcion_formateada + monto_formateado + "\n"
        resultado += f"Total: {self.get_balance():.2f}"
        return resultado
        

def create_spend_chart(categories):
    # Paso 1: Calcular los retiros totales de cada categoría y el total global
    total_spent = 0
    category_spent = []
    
    for category in categories:
        spent = 0
        for item in category.ledger:
            if item["amount"] < 0:
                spent += abs(item["amount"])
        category_spent.append(spent)
        total_spent += spent

    # Paso 2: Calcular porcentajes redondeados hacia abajo al múltiplo de 10 más cercano
    porcentajes = []
    for spent in category_spent:
        if total_spent > 0:
            # Multiplicamos por 100, dividimos por el total, y usamos // 10 * 10 para truncar al revés de redondear
            porcentajes.append((spent / total_spent * 100) // 10 * 10)
        else:
            porcentajes.append(0)

    # Paso 3 y 4: Construir el gráfico vertical (eje Y de 100 a 0)
    resultado = "Percentage spent by category\n"
    for valor in range(100, -1, -10):
        resultado += f"{valor:>3}| "
        for p in porcentajes:
            if p >= valor:
                resultado += "o  "
            else:
                resultado += "   "
        resultado += "\n"
        
    # Paso 5: Línea horizontal de guiones
    resultado += "    " + "-" * (3 * len(categories) + 1) + "\n"

    # Paso 6: Nombres de las categorías de forma vertical
    max_largo = max(len(c.name) for c in categories)
    for i in range(max_largo):
        resultado += "     "
        for category in categories:
            if i < len(category.name):
                resultado += category.name[i] + "  "
            else:
                resultado += "   "
        if i < max_largo - 1:
            resultado += "\n"

    return resultado