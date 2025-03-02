def binario_a_decimal(binario):
    """
    Convierte un número binario de 8 dígitos a decimal
    """
    # Verificar que sea un string de 8 caracteres
    if len(binario) != 8:
        return "Error: El número binario debe tener exactamente 8 dígitos"
    
    # Verificar que solo contenga 0 y 1
    if not all(bit in '01' for bit in binario):
        return "Error: El número binario solo puede contener 0's y 1's"
    
    # Convertir a decimal
    decimal = 0
    for i in range(8):
        decimal += int(binario[i]) * (2 ** (7 - i))
    
    return decimal

def decimal_a_binario(decimal):
    """
    Convierte un número decimal a binario de 8 dígitos
    """
    # Verificar que sea un número entero
    try:
        decimal = int(decimal)
    except ValueError:
        return "Error: Debe ingresar un número entero"
    
    # Verificar que pueda representarse con 8 bits (0-255)
    if decimal < 0 or decimal > 255:
        return "Error: El número debe estar entre 0 y 255 para representarse con 8 bits"
    
    # Convertir a binario
    binario = ""
    for i in range(7, -1, -1):
        bit = "1" if decimal >= 2**i else "0"
        if bit == "1":
            decimal -= 2**i
        binario += bit
    
    return binario

def main():
    while True:
        print("\n=== CONVERSOR BINARIO-DECIMAL ===")
        print("1. Convertir de binario a decimal")
        print("2. Convertir de decimal a binario")
        print("3. Salir")
        
        opcion = input("\nSeleccione una opción (1/2/3): ")
        
        if opcion == "1":
            binario = input("Ingrese un número binario de 8 dígitos: ")
            resultado = binario_a_decimal(binario)
            if isinstance(resultado, int):
                print(f"El número decimal equivalente es: {resultado}")
            else:
                print(resultado)
        
        elif opcion == "2":
            decimal = input("Ingrese un número decimal (0-255): ")
            resultado = decimal_a_binario(decimal)
            if resultado.startswith("Error"):
                print(resultado)
            else:
                print(f"El número binario equivalente es: {resultado}")
        
        elif opcion == "3":
            print("Gracias por usar el conversor. ¡Hasta luego!")
            break
        
        else:
            print("Opción no válida. Por favor, intente nuevamente.")

if __name__ == "__main__":
    main()