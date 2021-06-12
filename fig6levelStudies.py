import matplotlib.pyplot as plt

data= ["Pregrado","Pregrado","Maestría",
"Pregrado","Pregrado","Pregrado",
"Pregrado","Especialización","Pregrado",
"Pregrado","Pregrado","Pregrado","Pregrado",
"Pregrado","Pregrado","Pregrado","Pregrado",
"Pregrado","Pregrado","Pregrado","Pregrado",
"Pregrado","Pregrado","Pregrado","Pregrado",
"Pregrado","Pregrado","Pregrado","Pregrado",
"Pregrado","Pregrado","Pregrado","Pregrado",
"Pregrado","Pregrado","Pregrado","Pregrado",
"Maestría","Pregrado","Pregrado","Pregrado",
"Pregrado","Pregrado","Pregrado","Pregrado",
"Maestría","Especialización","Pregrado",
"Pregrado","Pregrado","Maestría","Pregrado",
"Especialización","Maestría","Pregrado","Especialización",
"Especialización","Pregrado","Especialización",
"Pregrado","Pregrado","Pregrado",
"Pregrado","Pregrado","Pregrado",
"Maestría","Pregrado","Pregrado",
"Pregrado","Pregrado","Pregrado",
"Pregrado","Maestría","Pregrado","Maestría",
"Pregrado","Pregrado","Pregrado","Pregrado",]

x = ["Specialization","Master","Bachelor"]
y = [data.count("Especialización"),
    data.count("Maestría"),
    data.count("Pregrado")]

print(y)

plt.figure(dpi=300)
plt.pie(x=y,labels=x,autopct='%1.0f%%',
        shadow=False)

plt.title("Graduate's studies level")
plt.savefig("fig6graduatelevel.tiff",format="tiff")
