import matplotlib.pyplot as plt
from textwrap import wrap

x = [9,10,23,7]
y = ["Human resource formation","Social appropriation of knowledge","Technological development and innovation","Generation of new knowledge"]
y = [ '\n'.join(wrap(l, 20)) for l in y ]

print(y)

plt.figure(dpi=300)
plt.barh(width=x,y=y,align='center')

plt.title("Contribution of the work for graduates")
plt.tight_layout()

plt.savefig("fig9topology.tiff",format="tiff")
