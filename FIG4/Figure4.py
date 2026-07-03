# import matplotlib.cm as cm
import matplotlib.pyplot as plt
# plt.style.use('seaborn-v0_8-deep')
# from matplotlib.backends.backend_pdf import PdfPages
# import matplotlib.colors as mcolors
# from matplotlib.colors import LinearSegmentedColormap
import numpy as np
from scipy.io import loadmat

def main():

    # data
    Res_a = loadmat('Response_b.mat',mat_dtype=True)
    temp = Res_a['temp_vector'].T*10
    SNT_a = Res_a['SNT'].T
    TET_a = Res_a['TET'].T

    Res_b = loadmat('Response_c.mat',mat_dtype=True)
    SNT_b = Res_b['SNT'].T
    TET_b = Res_b['TET'].T

    Res_c = loadmat('Response_g.mat',mat_dtype=True)
    SNT_c = Res_c['SNT'].T
    TET_c = Res_c['TET'].T

    Res_d = loadmat('Response_e.mat',mat_dtype=True)
    SNT_d = Res_d['SNT'].T
    TET_d = Res_d['TET'].T

    Res_e = loadmat('Response_f.mat',mat_dtype=True)
    SNT_e = Res_e['SNT'].T
    TET_e = Res_e['TET'].T
    

    ftsz = 14
    axftsz = 11
    legftsz = 13
    noteftsz = 11
    linewidth = 2.2



    x_labeltext = - 0.22
    y_labeltext = 1.0
          


    # figure creat

    #plt.tight_layout()
    plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
    plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内
    fig, axes = plt.subplots(1, 2, figsize=(7, 3.3))
    plt.subplots_adjust(top=0.98,bottom=0.1,left=0.1,right=0.98,hspace=0.1,wspace=0.3)
    #plt.subplots_adjust(wspace=0.4)
    #fig.tight_layout()

    # subfig (a)： phase diagram



    axa = axes[0]
    axa.plot(temp,TET_a*1000,linewidth=linewidth)
    axa.plot(temp,TET_b*1000,linewidth=linewidth)
    axa.plot(temp,TET_c*1000,linewidth=linewidth)
    axa.plot(temp,TET_d*1000,linewidth=linewidth)
    # axa.plot(temp,TET_e*100,linewidth=linewidth,linestyle='-',label='C#=1')
    # axa.plot(temp,np.zeros(len(temp)),linewidth=linewidth,linestyle='--',color='k')
    axa.set_box_aspect(1)
    axa.set_ylabel(r'$\chi_{xx} /\chi_{0}\times10^{-3}$',fontsize = legftsz,labelpad=6)
    # axa.ticklabel_format(style='plain', scilimits=(-0,1), axis='y',useMathText=True)
    axa.tick_params(axis='both',labelsize=axftsz)
    axa.set_xlabel(r'$T / \Delta$',fontsize = legftsz)
    axa.set_xlim([0,0.2])
    axa.set_ylim([-6,4])
    axa.set_xticks([0,0.1,0.2])
    axa.set_yticks([-4,-2,0,2])
    axa.legend(['C#=0,trival','C#=-1','C#=0,geometric','C#=2'],fontsize=9)
    axa.text(x_labeltext, y_labeltext, '(a)', transform=axa.transAxes, fontsize=ftsz, va='top') # subfig label

    # expand
    expand =1000

    axb = axes[1]
    axb.plot(temp,SNT_a*expand,linewidth=linewidth)
    axb.plot(temp,SNT_b*expand,linewidth=linewidth)
    axb.plot(temp,SNT_c*expand,linewidth=linewidth)
    axb.plot(temp,SNT_d*expand,linewidth=linewidth)
    # axb.plot(temp,SNT_e*expand,linewidth=linewidth,linestyle='-')
    axb.set_box_aspect(1)
    axb.set_ylabel(r'$\alpha_{H}^{z}/\alpha_{0} \times 10^{-3}$',fontsize = legftsz)
    axb.set_xlabel(r'$T / \Delta$',fontsize = legftsz)
    axb.set_xlim([0,0.2])
    axb.set_ylim([-6,2])
    axb.set_xticks([0,0.1,0.2])
    axb.set_yticks([-4,-2,0])
    # axb.ticklabel_format(style='plain', scilimits=(-0,1), axis='y',useMathText=True)
    axb.text(x_labeltext, y_labeltext, '(b)', transform=axb.transAxes, fontsize=ftsz, va='top') # subfig label



    # plt.savefig('Figure4.pdf')
    plt.savefig('Figure4.png', dpi=600)
    plt.show()

if __name__=='__main__':
    main()