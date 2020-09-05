from exemplo_principal import vParalelepipedo, atParalelepipedo

l = int(input('Digite a largura do paralelepípedo: '))
a = int(input('Digite a altura do paralelepípedo: '))
p = int(input('Digite a pofundidade do paralelepípedo: '))
v = vParalelepipedo(l,a,p)
areat = atParalelepipedo(l,a,p)
print(f'O volume do paralelepípedo é igual a {v} e a área total é igual a {areat}')


