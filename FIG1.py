import matplotlib.cm as cm
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-deep')
from matplotlib.backends.backend_pdf import PdfPages
import matplotlib.colors as mcolors
from mpl_toolkits.axes_grid1.inset_locator import inset_axes
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

    elecbandFile_mu0 = 'elecband_mu0.mat'
    elecBand_mu0 = loadmat(elecbandFile_mu0,mat_dtype=True)
    elec_Ek = elecBand_mu0["Ek"]
    elec_kx  = elecBand_mu0["kx"].T
    mu1 = len(elec_kx)*[0];
    mu2 = len(elec_kx)*[1];

 

    BdGFile_mu05 = 'BdG_mu1a.mat'
    BdGBand_mu05 = loadmat(BdGFile_mu05,mat_dtype=True)
    Ek_mu05 = BdGBand_mu05['Ek']
    Ch_mu05 = BdGBand_mu05['Ch']
    Sx_mu05 = BdGBand_mu05['Sx']
    Sy_mu05 = BdGBand_mu05['Sy']
    Sz_mu05 = BdGBand_mu05['Sz']
    k_mu05 = BdGBand_mu05['kx'].T

    Rho_mu05 = Ch_mu05

        # Fermi surface
    FR_mu0 = 1.0
    FR1_mu035 = 0.26
    FR2_mu035 = 1.4
    FR1_mu05 = 1
    FR2_mu05 = 1.9

    theta = np.linspace(0,2*np.pi,50)
    kfx_mu0 = -FR_mu0*np.cos(theta)
    kfy_mu0 = -FR_mu0*np.sin(theta)

    kf1x_mu035 = FR1_mu035*np.cos(theta)
    kf1y_mu035 = FR1_mu035*np.sin(theta)
    kf2x_mu035 = FR2_mu035*np.cos(theta)
    kf2y_mu035 = FR2_mu035*np.sin(theta)
    kf1x_mu05 = FR1_mu05*np.cos(theta)
    kf1y_mu05 = FR1_mu05*np.sin(theta)
    kf2x_mu05 = FR2_mu05*np.cos(theta)
    kf2y_mu05 = FR2_mu05*np.sin(theta)
   
    

    # Define the colors
    # colors1 = ["#3264A0", "white", "#9B3737"]
    colors1 = ["#008fd5","white","#fc4f30"]
    # colors1 = ["#1f77b4","white","#ff7f0e"]

    # Create a custom colormap
    custom_cmap = LinearSegmentedColormap.from_list("CustomMap1", colors1, N=255,gamma=1)
    # custom_cmap = "PuOr"

    # colors2 = ["#3264A0", "tan", "#9B3737"]
    # colors2 = ["#ff7f0e","#888888","#1f77b4"]
    colors2 = ["#fc4f30","#D7C8DE","#008fd5"]
    custom_cmap2 = LinearSegmentedColormap.from_list("CustomMap2", colors2, N=255)
    
    c_map = custom_cmap

    cmapline= plt.get_cmap(custom_cmap2)
    norm = plt.Normalize(-1, 1)
    line_colors1_mu05 = cmapline(norm(Rho_mu05[:,0]))
    line_colors2_mu05 = cmapline(norm(Rho_mu05[:,1]))
    line_colors3_mu05 = cmapline(norm(Rho_mu05[:,2]))
    line_colors4_mu05 = cmapline(norm(Rho_mu05[:,3]))

    ftsz = 14
    axftsz = 11
    legftsz = 13
    linewidth1 = 1
    linewidth_elecband = 2.2
    lwidthKF = 1
    pointscale = 0.75
    transparancy = 1
    line_c = "#008fd5"
    arrow_c = "#008fd5"

    line_c1 = "#1f77b4"
    line_c2 = "#ff7f0e"

    x_labeltext = - 0.15
    y_labeltext = 1.00

    # figure creat

    #plt.tight_layout()
    plt.rcParams['xtick.direction'] = 'in'  # 将x周的刻度线方向设置向内
    plt.rcParams['ytick.direction'] = 'in'  # 将y轴的刻度方向设置向内
    fig, axes = plt.subplots(1, 2, figsize=(7, 3.2))
    plt.subplots_adjust(top=0.98,bottom=0.12,left=0.06,right=0.98,hspace=0.0,wspace=0.24)
    plt.rcParams['xtick.direction']='in'
    plt.rcParams['ytick.direction']='in'
    #plt.subplots_adjust(wspace=0.4)
    #fig.tight_layout()


    axa = axes[0]
    axa.plot(elec_kx,elec_Ek[:,0]-1,linewidth=linewidth_elecband,color=line_c)
    axa.plot(elec_kx,elec_Ek[:,1]-1,linewidth=linewidth_elecband,color=line_c)
    axa.plot(elec_kx,mu1,linewidth=linewidth1,linestyle='--',color='k')
    axa.set_box_aspect(1)
    axa.set_ylim([-2,2])
    axa.set_yticks([0])
    axa.set_xticks([0])
    axa.set_ylabel(r'$\xi_k$',fontsize = legftsz,labelpad=6)
    axa.set_xlabel(r'$k$',fontsize = legftsz)
    # axa.text(-0.07, 0.53, r'$\mu$', transform=axa.transAxes, fontsize=11, va='top')
    axa.text(x_labeltext, y_labeltext, '(a)', transform=axa.transAxes, fontsize=ftsz, va='top')
    # inst figure
    axins = inset_axes(axa, width="35%", height="35%", loc="upper right", borderpad=0.4)
    axins.plot(kf1x_mu05,kf1y_mu05,linewidth = lwidthKF,linestyle='-',alpha=transparancy,c='k')
    axins.plot(kf2x_mu05,kf2y_mu05,linewidth = lwidthKF,linestyle='-',alpha=transparancy,c='k')
    axins.set_xlabel(r'$k_x$',fontsize = 8,labelpad =-2)
    axins.set_ylabel(r'$k_y$',fontsize = 8,labelpad =-2)
    axins.set_xticks([0])
    axins.set_yticks([0])
    axins.set_xticklabels('')
    axins.set_yticklabels('')
    axins.set_xlim([-2.75, 2.75,])
    axins.set_ylim([-2.75, 2.75,])
    axins.set_box_aspect(1)
    axins.tick_params(axis='both', labelsize=8) 


    axb = axes[1]
    for i in range(len(k_mu05)-1):
        axb.plot(k_mu05[i:i+2],Ek_mu05[i:i+2,0],color=line_colors1_mu05[i,:],lw=linewidth_elecband)
        axb.plot(k_mu05[i:i+2],Ek_mu05[i:i+2,1],color=line_colors2_mu05[i,:],lw=linewidth_elecband)
        axb.plot(k_mu05[i:i+2],Ek_mu05[i:i+2,2],color=line_colors3_mu05[i,:],lw=linewidth_elecband)
        axb.plot(k_mu05[i:i+2],Ek_mu05[i:i+2,3],color=line_colors4_mu05[i,:],lw=linewidth_elecband)
    axb.plot(k_mu05,len(k_mu05)*[0],linewidth=1,linestyle='--',color='k')
    axb.scatter(-1.43,0.67,s=300, facecolor='none',edgecolor='grey',marker='o')
    axb.set_box_aspect(1)
    axb.set_ylabel(r'$E_k$',fontsize = legftsz,labelpad=6)
    axb.set_yticks([0])
    axb.set_xticks([0])
    axb.set_xlim([-2.75, 2.75,])
    # axb.set_ylim([-2.75, 2.75,])
    axb.set_xlabel(r'$k$',fontsize = legftsz)
    axb.text(x_labeltext, y_labeltext, '(b)', transform=axb.transAxes, fontsize=ftsz, va='top') # subfig label
    # inset axes....
    axins = axb.inset_axes([0.63, 0.63, 0.35, 0.35])
    for i in range(len(k_mu05)-1):
        axins.plot(k_mu05[i:i+2],Ek_mu05[i:i+2,1],color=line_colors2_mu05[i,:],lw=linewidth_elecband)
        axins.plot(k_mu05[i:i+2],Ek_mu05[i:i+2,2],color=line_colors3_mu05[i,:],lw=linewidth_elecband)
    axins.plot(k_mu05,len(k_mu05)*[0],linewidth=1,linestyle='--',color='k')
    # sub region of the original image
    x1, x2, y1, y2 = -1.25, -0.75, -0.35, 0.35
    axins.set_xlim(x1, x2)
    axins.set_ylim(y1, y2)
    axins.set_xticks([-1.01])
    axins.set_yticks([0])
    axins.set_xticklabels('')
    axins.set_yticklabels('')
    axins.set_xlabel(r'$k_{F1}$',fontsize = 8,labelpad =-2)
    axins.tick_params(axis='both', labelsize=8) 


    axb.indicate_inset_zoom(axins)


    # plt.savefig('Figure1.pdf')
    plt.savefig('Figure1.png', dpi=600)
    plt.show()

if __name__=='__main__':
    main()

