import matplotlib.pyplot as plt
import numpy as np

#dane do wykresu
labels = 'Warszawa','Kraków','Lublin','Katowice','Zakopane'
print(type(labels))

sizes = [56,34,27,28,39]
explode = (0,0.1,0,0,0.2)

fig,ax = plt.subplots()
fig.patch.set_facecolor('#D3D3D3')
ax.set_facecolor('beige')
ax.pie(sizes,explode=explode,labels=labels,autopct='%1.1f%%',shadow=True,startangle=90)
ax.axis("equal")
plt.show()


#drugi wykres
#wykres typu bar - słupkowy z definicją własnych kolorów

#dane do wykresu
categories = ["A","B","C","D","E","K"]
values = [23,45,67,12,41,78]

colors = ["red","blue","orange","green","#45AA23","#783BCC"]

fig,ax = plt.subplots(figsize=(8,6))

#ustawienia
fig.patch.set_facecolor('#D3D3D3')
ax.set_facecolor('orange')

bars = plt.bar(categories,values,color=colors,edgecolor="black")

#dodanie etykiet
for bar, value in zip(bars,values):
    plt.text(bar.get_x() + bar.get_width()/2,bar.get_height()-1,str(value),ha="center",
             color="white",fontsize=16)

plt.title("Przykład wykresu słupkowego",fontsize=20)
plt.xlabel("Kategorie",fontsize=14)
plt.ylabel("Wartości",fontsize=14)
plt.grid(axis="y",linestyle="--",alpha=0.6)

plt.show()
