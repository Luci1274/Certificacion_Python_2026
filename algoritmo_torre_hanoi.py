def hanoi_solver(n):
    # Listas que representan las tres varillas (A, B y C)
    # La varilla A arranca con los discos de mayor a menor [n, n-1, ..., 1]
    source = list(range(n, 0, -1))
    target = []
    auxiliary = []
    
    # Lista donde vamos a ir guardando el estado de las varillas en cada paso
    movimientos = []
    
    # Guardamos el estado inicial tal como lo pide la consigna
    movimientos.append(f"{source} {auxiliary} {target}")
    
    # Esta es nuestra función recursiva interna que hace la magia
    def move(n, source_rod, target_rod, auxiliary_rod):
        if n > 0:
            # Paso 1: Mover n-1 discos de la varilla origen a la auxiliar usando la destino
            move(n - 1, source_rod, auxiliary_rod, target_rod)
            
            # Paso 2: Mover el disco que quedó en el origen a la varilla destino
            target_rod.append(source_rod.pop())
            
            # Guardamos cómo quedaron las varillas originales (source, auxiliary, target)
            # después de este movimiento exacto.
            movimientos.append(f"{source} {auxiliary} {target}")
            
            # Paso 3: Mover los n-1 discos que dejamos en la auxiliar hacia la destino
            move(n - 1, auxiliary_rod, target_rod, source_rod)

    # Ejecutamos la función recursiva pasando el total de discos
    move(n, source, target, auxiliary)
    
    # Unimos todos los estados guardados con un salto de línea
    return "\n".join(movimientos)