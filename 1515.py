# ______ función leer ______
def leer():
    n = int(input("Un valor="))
    return n

# ______ función para encontrar el primer dígito y contar ocurrencias ______
def sumaDig():
    contarIgual = 0

    # Leer el primer número para obtener el primer dígito
    n = leer()
    nOriginal = n

    # Encontrar el primer dígito del número original
    while nOriginal >= 10:
        nOriginal = nOriginal // 10
    primer_digito = nOriginal
    print(f"El primer dígito es: {primer_digito}")

    # Leer otro número y contar cuántas veces aparece el primer dígito en él
    digito = leer()
    nAux = digito  # Guardar el valor original para usarlo en la impresión final

    while digito > 0:
        nn = digito % 10
        if nn == primer_digito:
            contarIgual = contarIgual + 1
        digito = digito // 10

    print(f"El dígito {primer_digito} se encuentra {contarIgual} veces en {nAux}")

# ______ función main _____
sumaDig()
