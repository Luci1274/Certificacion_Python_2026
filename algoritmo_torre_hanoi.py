def hanoi_solver(n):

    source = list(range(n, 0, -1))
    target = []
    auxiliary = []
    
    movimientos = []
    
    movimientos.append(f"{source} {auxiliary} {target}")
    
    def move(n, source_rod, target_rod, auxiliary_rod):
        if n > 0:
            move(n - 1, source_rod, auxiliary_rod, target_rod)
            
            target_rod.append(source_rod.pop())
            
            movimientos.append(f"{source} {auxiliary} {target}")
            
            move(n - 1, auxiliary_rod, target_rod, source_rod)

    move(n, source, target, auxiliary)

    return "\n".join(movimientos)