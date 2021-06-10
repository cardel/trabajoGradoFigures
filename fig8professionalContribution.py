import matplotlib.pyplot as plt

data= ["Muy significativo","Muy significativo",
"Significativo","Significativo","Significativo",
"Algo significativo","Muy significativo","Significativo",
"Muy significativo","Muy significativo","Muy significativo",
"Muy significativo","Muy significativo","Significativo",
"Muy significativo","Significativo","Muy significativo",
"Algo significativo","Algo significativo","Muy significativo",
"Significativo","Muy significativo","Significativo",
"Muy significativo","Significativo","Algo significativo",
"Muy significativo","Significativo","Muy significativo",
"Muy significativo","Muy significativo","Significativo",
"Muy significativo","Muy significativo","Significativo",
"Muy significativo","Muy significativo","Significativo",
"Muy significativo","Muy significativo","Significativo",
"Significativo","Algo significativo","Algo significativo",
"Muy significativo","Muy significativo","Poco significativo"
"Muy significativo","Significativo","Algo significativo","Significativo",
"Significativo","Significativo","Algo significativo","Poco significativo",
"Significativo","Muy significativo","Muy significativo",
"Poco significativo","Muy significativo","Muy significativo",
"Significativo","Muy significativo","Algo significativo",
"Algo significativo","Significativo","Algo significativo",
"Significativo","Algo significativo","Poco significativo"
"Significativo","Significativo","Significativo",
"Muy significativo","Significativo","Muy significativo",
"Significativo","Muy significativo","Muy significativo",
]

x = ["Very significant","Significant","Something significant","Little significant"]
y = [data.count("Muy significativo"),
    data.count("Significativo"),
    data.count("Algo significativo"),
    data.count("Poco significativo")]

print(y)

plt.figure(dpi=300)
plt.pie(x=y,labels=x,autopct='%1.0f%%',
        shadow=False)

plt.title("Contribution of the work for graduates")
plt.savefig("fig8contribution.png",format="png")
