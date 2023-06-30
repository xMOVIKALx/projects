import matplotlib.pyplot as plt
items = input("Enter your items with space like(tea water juice) : ")
items = items.split()
colorsin = input("Enter colors respectively items : ")
colorsin = colorsin.split()
sizesin = input("Enter values respectively (without %) : ")
sizesin = sizesin.split()
labels = [i for i in items]
sizes = [int(l) for l in sizesin]
colors = [j for j in colorsin]
plt.pie(sizes, labels=labels, colors=colors, autopct="%1.1f%%")
plt.show()