import matplotlib.pyplot as plt

x = [x for x in range(2012,2019)]
y = [14,21,21,21,14,23,27]

plt.figure(dpi=300)
plt.grid(axis='y')
plt.bar(x=x,height=y,color="blue")

plt.xlabel("Year")
plt.ylabel("Number of finished works")
plt.title("Final works by year")
plt.savefig("fig5worksbyyear.png",format="png")