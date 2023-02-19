import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import math as mt

cen=str(input("Select centrality? For exampale: 1020 \n"))
number=int(input('\n (1) antispec \n (2) spec \n'))
data_dir="C:\\Users\\tposo\\OneDrive - České vysoké učení technické v Praze\\Plocha\\diplomka\\LHC276\\spectrum\\data"

spec_pion_exp=pd.read_csv(data_dir+"\\exp_spec_pi_%s.dat"%cen, sep="\t", header=None, names=["pt", "pt_max", "pt_min","spec","chyba","chybaminus","sys","sysminus","neco1","neco"])
spec_proton_exp=pd.read_csv(data_dir+"\\exp_spec_p_%s.dat"%cen, sep="\t", header=None, names=["pt", "pt_max", "pt_min","spec","chyba","chybaminus","sys","sysminus","neco1","neco"])
spec_kaon_exp=pd.read_csv(data_dir+"\\exp_spec_k_%s.dat"%cen, sep="\t", header=None, names=["pt", "pt_max", "pt_min","spec","chyba","chybaminus","sys","sysminus","neco1","neco"])

spec_pionminus_exp=pd.read_csv(data_dir+"\\exp_spec_pi-_%s.dat"%cen, sep="\t", header=None, names=["pt", "pt_max", "pt_min","spec","chyba","chybaminus","sys","sysminus","neco1","neco"])
spec_protonbar_exp=pd.read_csv(data_dir+"\\exp_spec_pbar_%s.dat"%cen, sep="\t", header=None, names=["pt", "pt_max", "pt_min","spec","chyba","chybaminus","sys","sysminus","neco1","neco"])
spec_kaonminus_exp=pd.read_csv(data_dir+"\\exp_spec_k-_%s.dat"%cen, sep="\t", header=None, names=["pt", "pt_max", "pt_min","spec","chyba","chybaminus","sys","sysminus","neco1","neco"])

if number==2:
    spec_hadrons=pd.read_csv(data_dir+"\\spec_%s.dat"%cen, sep="\t", header=None, names=["pt", "pion","errorpi","kaon","errorkaon","proton","errorp"])
if number==1:
    antispec_hadrons=pd.read_csv(data_dir+"\\antispec%s.dat"%cen, sep="\t", header=None, names=["pt", "pion","errorpi","kaon","errorkaon","proton","errorp"])

fig, axes = plt.subplots(sharex=True, figsize=(12,8))
axes.autoscale(tight=True)
axes.set_yscale("log")

if number==1:
    axes.errorbar(spec_pionminus_exp["pt"],spec_pionminus_exp["spec"], yerr =(spec_pionminus_exp["chyba"]), fmt='o',ecolor='black',color='blue',elinewidth=2,capsize=4, label="ALICE data")
    axes.errorbar(spec_protonbar_exp["pt"],spec_protonbar_exp["spec"]/50, yerr =(spec_protonbar_exp["chyba"])/50, fmt='o',color='blue',ecolor='black',elinewidth=2,capsize=4)
    axes.errorbar(spec_kaonminus_exp["pt"],spec_kaonminus_exp["spec"]/10, yerr =(spec_kaonminus_exp["chyba"])/10, fmt='o',color='blue',ecolor='black',elinewidth=2,capsize=4)


    axes.plot(antispec_hadrons["pt"],antispec_hadrons["kaon"]/10, color='darkcyan',linewidth=2)
    axes.plot(antispec_hadrons["pt"],antispec_hadrons["pion"], color='darkcyan',linewidth=2, label="Trento3d IS + vHLLE + SMASH")
    axes.plot(antispec_hadrons["pt"],antispec_hadrons["proton"]/50,color='darkcyan',linewidth=2)
    axes.annotate('$\pi^-$', (0.6, 100),fontsize=17)
    axes.annotate('$K^-/10$', (0.1, 5),fontsize=17)
    axes.annotate(''r'$\bar{p}/50$', (0.25, 0.1),fontsize=17)

if number ==2:
    axes.errorbar(spec_pion_exp["pt"],spec_pion_exp["spec"], yerr =(spec_pion_exp["chyba"]), fmt='o',ecolor='black',color='red',elinewidth=2,capsize=4, label="ALICE data")
    axes.errorbar(spec_proton_exp["pt"],spec_proton_exp["spec"]/50, yerr =(spec_proton_exp["chyba"])/50, fmt='o',color='red',ecolor='black',elinewidth=2,capsize=4)
    axes.errorbar(spec_kaon_exp["pt"],spec_kaon_exp["spec"]/10, yerr =(spec_kaon_exp["chyba"])/10, fmt='o',color='red',ecolor='black',elinewidth=2,capsize=4)

    axes.plot(spec_hadrons["pt"],spec_hadrons["kaon"]/10, color='darkcyan',linewidth=2)
    axes.plot(spec_hadrons["pt"],spec_hadrons["pion"], color='darkcyan',linewidth=2, label="Trento3d IS + vHLLE + SMASH")
    axes.plot(spec_hadrons["pt"],spec_hadrons["proton"]/50,color='darkcyan',linewidth=2)
    axes.annotate('$\pi^+$', (0.6, 100),fontsize=17)
    axes.annotate('$K^+/10$', (0.1, 5),fontsize=17)
    axes.annotate('$p/50$', (0.25, 0.1),fontsize=17)

axes.autoscale(tight=True)
axes.grid(True)
axes.annotate('$\mathrm{Pb+Pb\ \sqrt{s_{NN}}=2.76\ TeV}$ '+ '%s'%int(cen[:2])+' - '+'%s'%int(cen[2:4])+"%", (0.5,2e-3),fontsize=22)
axes.set_xlabel('$p_t$[GeV]',fontsize=18)
axes.set_ylabel('$d^2N/(2 \pi ptdp_tdy)$[$GeV^{-2}$]',fontsize=18)
axes.legend(loc=0,fontsize=15)
axes.tick_params(axis='x', labelsize=15)
axes.tick_params(axis='y', labelsize=15)
axes.set_xlim([0, 2.5])
axes.set_ylim([10e-4, 2000])
if number ==2:
    fig.savefig('atnispec276_%s.png'%cen)
if number ==1:
    fig.savefig('spec276_%s.png'%cen)

plt.show()
