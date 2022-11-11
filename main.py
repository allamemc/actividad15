import pandas as pd
import matplotlib.pyplot as plt

vdm = ['Valdemoro',25000]
pi = ['Pinto',40000]
geta = ['Getafe',20000]
arj = ['Aranjuez',70000]
ses = ['Seseña',68900]
sol = ['Sol',10000]

lista_ciu=[vdm,pi,geta,arj,ses,sol]
ciudades=pd.DataFrame(lista_ciu,columns=['Nombre','Habitantes'])
print(ciudades)

plt.plot(ciudades['Nombre'],ciudades['Habitantes'])
plt.show()

plt.scatter(ciudades['Nombre'],ciudades['Habitantes'])
plt.show()

plt.bar(ciudades['Nombre'],ciudades['Habitantes'])
plt.show()

ciudades_sort=ciudades.sort_values('Habitantes', ascending=False)
plt.bar(ciudades_sort['Nombre'],ciudades_sort['Habitantes'])
plt.show()

ciudades_sort=ciudades.sort_values('Habitantes', ascending=False)
plt.bar(ciudades_sort['Nombre'],ciudades_sort['Habitantes'],color=['b','r','g','m','k','c'])
plt.show()

plt.pie(ciudades['Habitantes'],labels=ciudades['Nombre'])
plt.show()