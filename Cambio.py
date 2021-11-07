# -*- coding: utf-8 -*-
"""
¿Tienes cambio?
"""
h='\u2500'
v='\u2502'
c='\u253C'
ct='\u252C'
ci='\u2534'

cambio=float(input("¿Cuánto dinero tienes?: "))

euros=int(cambio)
b50=euros//50
euros-=b50*50
b20=euros//20
euros-=b20*20
b10=euros//10
euros-=b10*10
b5=euros//5
euros-=b5*5
b2=euros//2
euros-=b2*2
b1=euros//1
euros-=b1*1

centimos=round(cambio*100)%100
m50=centimos//50
centimos-=m50*50
m20=centimos//20
centimos-=m20*20
m10=centimos//10
centimos-=m10*10
m5=centimos//5
centimos-=m5*5
m2=centimos//2
centimos-=m2*2
m1=centimos//1

print("\nAquí tienes tu cambio:")

print(h*30 + ct + h*10)
texto="Billetes de 50 Euros"
print(f'{texto:30}{v}{b50:^10}')
print(h*30 + c + h*10)
texto="Billetes de 20 Euros"
print(f'{texto:30}{v}{b20:^10}')
print(h*30 + c + h*10)
texto="Billetes de 10 Euros"
print(f'{texto:30}{v}{b10:^10}')
print(h*30 + c + h*10)
texto="Billetes de 5 Euros"
print(f'{texto:30}{v}{b5:^10}')
print(h*30 + c + h*10)
print(h*30 + c + h*10)
texto="Monedas de 2 Euros"
print(f'{texto:30}{v}{b2:^10}')
print(h*30 + c + h*10)
texto="Monedas de 1 Euro"
print(f'{texto:30}{v}{b1:^10}')
print(h*30 + c + h*10)
texto="Monedas de 50 céntimos"
print(f'{texto:30}{v}{m50:^10}')
print(h*30 + c + h*10)
texto="Monedas de 20 céntimos"
print(f'{texto:30}{v}{m20:^10}')
print(h*30 + c + h*10)
texto="Monedas de 10 céntimos"
print(f'{texto:30}{v}{m10:^10}')
print(h*30 + c + h*10)
texto="Monedas de 5 céntimos"
print(f'{texto:30}{v}{m5:^10}')
print(h*30 + c + h*10)
texto="Monedas de 2 céntimos"
print(f'{texto:30}{v}{m2:^10}')
print(h*30 + c + h*10)
texto="Monedas de 1 céntimo"
print(f'{texto:30}{v}{m1:^10}')
print(h*30 + ci + h*10)
