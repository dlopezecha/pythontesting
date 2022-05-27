def area_rectangulo(base, altura):
    if not isinstance(base, (int, float)):
        raise ValueError('La base debe ser del tipo real')
    if not isinstance(altura, (int, float)):
        raise ValueError('La altura debe ser del tipo real')
    if base < 0:
        raise ValueError('La base debe ser positiva')
    if altura < 0:
        raise ValueError('La altura debe ser positiva')
    return base * altura
    