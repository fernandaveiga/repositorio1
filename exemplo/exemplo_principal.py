def vParalelepipedo(l, a, p):
    '''
    calculo do volume de um paralelepipedo
    l=largura
    a=altura
    p=profundidade
    '''

    volume = l*a*p
    return volume

def atParalelepipedo(l,a,p):
    '''
    Calculo da área d superfície total do paralelpipedo
    l=largurs
    a=altura
    p=profundidade
    '''
    at = (2*(l*a))+(2*(a*p))+(2*(p*l))
    return at
