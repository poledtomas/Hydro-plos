import matplotlib.pyplot as plt
import pandas as pd

cen=str(input("Select centrality? For exampale: 1020 \n"))
data_dir="C:\\Users\\tposo\\OneDrive - České vysoké učení technické v Praze\\Plocha\\diplomka\\LHC276\\dndeta\\data"

dndeta=pd.read_csv(data_dir+"\\dndeta_%s.dat"%cen, sep="\t", header=None, names=["rap","dndeta"])
dndeta_exp=pd.read_csv(data_dir+"\\exp_dndeta_%s.dat"%cen, sep="\t", header=None, names=["rap", "rap_max", "rap_min","dndeta","chyba","chybaminus","neco","neco1"])

fig, axes = plt.subplots(sharex=True, figsize=(9,8))
axes.errorbar(dndeta_exp["rap"],dndeta_exp["dndeta"], yerr =(dndeta_exp["chyba"]), fmt='o',ecolor='black',color='red',elinewidth=2,capsize=4, label="ALICE data")
axes.plot(dndeta["rap"],dndeta["dndeta"], color='darkcyan', linewidth=2.5, label="Trento3d IS + vHLLE + SMASH")
axes.grid(True)
axes.set_ylim([0, 1000])
axes.set_xlabel('$\eta$',fontsize=18)
axes.set_ylabel('$dN_{ch}/d\eta$',fontsize=18)
axes.legend(loc=2,fontsize=15)
axes.annotate('$\mathrm{Pb+Pb\ \sqrt{s_{NN}}=2.76\ TeV}$ '+ '%s'%int(cen[:2])+' - '+'%s'%int(cen[2:4])+"%",(-5, 100),fontsize=15)

plt.show()
fig.savefig('dndeta_276_%s.png'%cen)
