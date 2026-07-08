import os,numpy as np,matplotlib;matplotlib.use("Agg")
import matplotlib.pyplot as plt
os.makedirs("figures",exist_ok=True);os.makedirs("results",exist_ok=True)
rng=np.random.default_rng(7);g=50
xx,yy=np.meshgrid(np.arange(g),np.arange(g))
# a gene high in a curved tissue region
expr=np.exp(-((xx-30)**2+(yy-20)**2)/120)+0.6*np.exp(-((xx-15)**2+(yy-38)**2)/90)
expr+=rng.normal(0,0.05,(g,g))
plt.figure(figsize=(6,5));plt.imshow(expr,cmap="magma",origin="lower")
plt.colorbar(label="expression");plt.xlabel("x (spots)");plt.ylabel("y (spots)")
plt.title("Spatial expression of a marker gene (demo data)")
plt.tight_layout();plt.savefig("figures/demo.png",dpi=150)
open("results/summary.txt","w").write("2 spatial expression domains\n");print("ok")