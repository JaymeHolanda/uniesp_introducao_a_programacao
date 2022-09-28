#[FORBELLONE, 2022] Construa um algoritmo que, tendo como dados de entrada dois pontos quaisquer do plano, P(x1, y1) e Q(x2, y2), imprima a distância entre eles.
#A formulá que efetua tal cálculo é: d = (x2 - x1)2 + (y2 - y1)2

x1 = float(input(" Digite o valor de X1 "))
x2 = float(input(" Digite o valor de X2 "))
y1 = float(input(" Digite o valor de Y1 "))
y2 = float(input(" Digite o valor de Y2 "))

d1 =  (x2 - x1)**2
d2 = (y2 - y1)**2 
d3 = (d1 + d2)**0.5  

print(f'Sua resposta é {d3:.3f}')
