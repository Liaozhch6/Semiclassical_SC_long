import matplotlib.cm as cm
import matplotlib.pyplot as plt
# plt.style.use('seaborn-v0_8-deep')
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.colors as mcolors
import numpy as np
from scipy.io import loadmat
from matplotlib.colors import LinearSegmentedColormap

import warnings

import matplotlib.pyplot as plt
import numpy as np

from matplotlib.collections import LineCollection


def colored_line_between_pts(x, y, c, ax, **lc_kwargs):
 
 

    if "array" in lc_kwargs:
        warnings.warn('The provided "array" keyword argument will be overridden')

    # Check color array size (LineCollection still works, but values are unused)
    if len(c) != len(x) - 1:
        warnings.warn(
            "The c argument should have a length one less than the length of x and y. "
            "If it has the same length, use the colored_line function instead."
        )

    # Create a set of line segments so that we can color them individually
    # This creates the points as an N x 1 x 2 array so that we can stack points
    # together easily to get the segments. The segments array for line collection
    # needs to be (numlines) x (points per line) x 2 (for x and y)
    points = np.array([x, y]).T.reshape(-1, 1, 2)
    segments = np.concatenate([points[:-1], points[1:]], axis=1)
    lc = LineCollection(segments, **lc_kwargs)

    # Set the values used for colormapping
    lc.set_array(c)

    return ax.add_collection(lc)



def main():

    # data

    # elecBand = loadmat('elecband.mat',mat_dtype=True)
    # ek = elecBand["ek"]
    # # labelpointx = elecBand["dotsx"]
    # # labelpointy = elecBand["dotsy"]

    # elec_Ek1 = ek[:,0]
    # elec_Ek2 = ek[:,1]

    # tick_label = [0,141,241,341]
    # name_label = [r'$(0,0)$',r'$(\pi,\pi)$',r'$(\pi,0)$',r'$(0,0)$']


    k = np.arange(1,342,1)

    BC_b = loadmat('BC_b.mat',mat_dtype=True)
    bc_b = BC_b['bc']

    BC_c = loadmat('BC_c.mat',mat_dtype=True)
    bc_c = BC_c['bc']

    BC_d = loadmat('BC_g.mat',mat_dtype=True)
    bc_d = BC_d['bc']

    BC_e = loadmat('BC_e.mat',mat_dtype=True)
    bc_e = BC_e['bc']

    BC_f = loadmat('BC_f.mat',mat_dtype=True)
    bc_f = BC_f['bc']
 

    Max=8
    # Max_BCkk_mu05 = np.abs(BCkk_mu05).max()
    # Max_BCxx_mu05 = np.abs(BCxx_mu05).max()


    # line of chemical potential

    # point = len(elec_Ek1)
    # mu_v = [-2.5,-2,-1,0]
    # muline_b = mu_v[0]*np.ones([point,1])
    # muline_c = mu_v[1]*np.ones([point,1])
    # muline_d = mu_v[2]*np.ones([point,1])
    # muline_e = mu_v[3]*np.ones([point,1])

    # print(np.size(elec_Ek1))

    # Define the colors
    # colors1 = ["#3264A0", "white", "#9B3737"]
    colors1 = ["#008fd5","white","#fc4f30"]
    # colors1 = ["#1f77b4","white","#ff7f0e"]

    # Create a custom colormap
    custom_cmap = LinearSegmentedColormap.from_list("CustomMap1", colors1, N=255,gamma=1)
    # custom_cmap = "PuOr"

    colors2 = ["#c44e52","#D7C8DE","#4c72b0"]
    custom_cmap2 = LinearSegmentedColormap.from_list("CustomMap2", colors2, N=255)
    

    ftsz = 14
    axftsz = 11
    legftsz = 13
    lw_band = 2.2;
    lw_mu = 1;

    x_labeltext = - 0.23
    y_labeltext = 1.00

    k_bc_label = [-1,0,1]
    k_bc_expand = [-1.05,1.05]

    # figure creat

    #plt.tight_layout()
    plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
    plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内
    fig, axes = plt.subplots(2, 2, figsize=(7, 6))
    plt.subplots_adjust(top=0.96,bottom=0.08,left=0.08,right=0.92,hspace=0.2,wspace=0.2)
    plt.rcParams['xtick.direction']='in'
    plt.rcParams['ytick.direction']='in'
    #plt.subplots_adjust(wspace=0.4)
    #fig.tight_layout()


    # axa = axes[0,0]
    # # band spectrum
    # axa.plot(k,elec_Ek1,linewidth=lw_band)
    # axa.plot(k,elec_Ek2,linewidth=lw_band)
    # # chemcal potential
    # axa.plot(muline_b,linewidth=lw_mu,linestyle='--',color='k')
    # axa.plot(muline_c,linewidth=lw_mu,linestyle='--',color='k')
    # axa.plot(muline_d,linewidth=lw_mu,linestyle='--',color='k')
    # axa.plot(muline_e,linewidth=lw_mu,linestyle='--',color='k')
    # axa.set_box_aspect(1)
    # # axa.set_ylim([-1,5]
    # axa.set_yticks([-2,-1,0,1,2])
    # axa.set_ylabel(r'$E/(2t)$',fontsize = legftsz)
    # axa.set_xticks(tick_label)
    # axa.set_xticklabels(name_label,fontsize = legftsz)
    # axa.set_xlabel('high symmetry points')
    # axa.text(1.02, 0.08, r'b', transform=axa.transAxes, fontsize=ftsz, va='top')
    # axa.text(1.02, 0.18, r'c', transform=axa.transAxes, fontsize=ftsz, va='top')
    # axa.text(1.02, 0.36, r'd', transform=axa.transAxes, fontsize=ftsz, va='top')
    # axa.text(1.02, 0.55, r'e', transform=axa.transAxes, fontsize=ftsz, va='top')
    # axa.text(x_labeltext, y_labeltext, '(a)', transform=axa.transAxes, fontsize=ftsz, va='top')

    axb = axes[0,0]
    im=axb.imshow(bc_b,interpolation='none',cmap=custom_cmap,origin='lower', extent=[-1, 1, -1, 1],aspect='auto',vmax=Max, vmin=-Max)
    axb.set_box_aspect(1)
    axb.set_xlabel(r'$k_x/\pi$',fontsize = legftsz)
    axb.set_ylabel(r'$k_y/\pi$',fontsize = legftsz)
    axb.set_xticks(k_bc_label)
    axb.set_yticks(k_bc_label)
    axb.set_xlim(k_bc_expand)
    axb.set_ylim(k_bc_expand)
    axb.text(0.05, 0.95, r'C#=0,trivial', transform=axb.transAxes, fontsize=ftsz, va='top')
    axb.text(x_labeltext, y_labeltext, '(a)', transform=axb.transAxes, fontsize=ftsz, va='top') # subfig label

    axc = axes[0,1]
    im=axc.imshow(bc_c,interpolation='none',cmap=custom_cmap,origin='lower', extent=[-1, 1, -1, 1],aspect='auto',vmax=Max, vmin=-Max)
    axc.set_box_aspect(1)
    axc.set_xlabel(r'$k_x/\pi$',fontsize = legftsz)
    axc.set_ylabel(r'$k_y/\pi$',fontsize = legftsz)
    axc.set_xticks(k_bc_label)
    axc.set_yticks(k_bc_label)
    axc.set_xlim(k_bc_expand)
    axc.set_ylim(k_bc_expand)
    axc.text(0.05, 0.95, r'C#=-1', transform=axc.transAxes, fontsize=ftsz, va='top')
    axc.text(x_labeltext, y_labeltext, '(b)', transform=axc.transAxes, fontsize=ftsz, va='top') # subfig label


    axd = axes[1,0]
    im=axd.imshow(bc_d,interpolation='none',cmap=custom_cmap,origin='lower', extent=[-1, 1, -1, 1],aspect='auto',vmax=Max, vmin=-Max)
    axd.set_box_aspect(1)
    axd.set_xlabel(r'$k_x/\pi$',fontsize = legftsz)
    axd.set_ylabel(r'$k_y/\pi$',fontsize = legftsz)
    axd.set_xticks(k_bc_label)
    axd.set_yticks(k_bc_label)
    axd.set_xlim(k_bc_expand)
    axd.set_ylim(k_bc_expand)
    axd.text(0.05, 0.95, r'C#=0,geometric', transform=axd.transAxes, fontsize=ftsz, va='top')
    axd.text(x_labeltext, y_labeltext, '(c)', transform=axd.transAxes, fontsize=ftsz, va='top') # subfig label

    axe = axes[1,1]
    im=axe.imshow(bc_e,interpolation='none',cmap=custom_cmap,origin='lower', extent=[-1, 1, -1, 1],aspect='auto',vmax=Max, vmin=-Max)
    axe.set_box_aspect(1)
    axe.set_xlabel(r'$k_x/\pi$',fontsize = legftsz)
    axe.set_ylabel(r'$k_y/\pi$',fontsize = legftsz)
    axe.set_xticks(k_bc_label)
    axe.set_yticks(k_bc_label)
    axe.set_xlim(k_bc_expand)
    axe.set_ylim(k_bc_expand)
    axe.text(0.05, 0.95, r'C#=2', transform=axe.transAxes, fontsize=ftsz, va='top')
    axe.text(x_labeltext, y_labeltext, '(d)', transform=axe.transAxes, fontsize=ftsz, va='top') # subfig label

    # axf = axes[2,1]
    # im=axf.imshow(bc_f,interpolation='none',cmap=custom_cmap,origin='lower', extent=[-1, 1, -1, 1],aspect='auto',vmax=Max, vmin=-Max)
    # axf.set_box_aspect(1)
    # axf.set_xlabel(r'$k_x/\pi$',fontsize = legftsz)
    # axf.set_ylabel(r'$k_y/\pi$',fontsize = legftsz)
    # axf.set_xticks(k_bc_label)
    # axf.set_yticks(k_bc_label)
    # axf.set_xlim(k_bc_expand)
    # axf.set_ylim(k_bc_expand)
    # axf.text(0.05, 0.95, r'C#=1', transform=axf.transAxes, fontsize=ftsz, va='top')
    # axf.text(x_labeltext, y_labeltext, '(f)', transform=axf.transAxes, fontsize=ftsz, va='top') # subfig label


    xshift = 0.01
    yshift = 0.02
    l = 0.935
    b = 0.42 + yshift
    w = 0.025
    h = 0.16

    #对应 l,b,w,h；设置colorbar位置；
    rect = [l,b,w,h] 
    cbar_ax = fig.add_axes(rect) 
    cb = plt.colorbar(im, cax=cbar_ax, ticks=[-8,0,8],drawedges=False)
    # cbar_ax.axis["left"].major_ticklabels.set_ha("center")

    # plt.figtext(0.946,0.585+ yshift,r'$+$',fontsize=legftsz)
    # plt.figtext(0.946,0.405+ yshift,r'$-$',fontsize=legftsz)

    # plt.savefig('Figure3.pdf')
    plt.savefig('Figure3.png', dpi=600)
    plt.show()

if __name__=='__main__':
    main()

