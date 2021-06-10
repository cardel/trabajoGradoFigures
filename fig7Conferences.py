import matplotlib.pyplot as plt

x = ["CCC","CLEI","RREDSI","REDIS"]
y = [6,2,19,1]

print(sum(y))

plt.figure(dpi=300)
plt.pie(x=y,labels=x,autopct='%1.0f%%',
        shadow=False)

plt.title("Participation in academic events")
plt.savefig("fig7congress.png",format="png")
