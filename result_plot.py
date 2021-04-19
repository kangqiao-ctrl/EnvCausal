import matplotlib.pyplot as plt
import seaborn as sns

def imp_normalize_sorted(dict):
    return {k: (dict.get(k,0))/(sum(dict.values())*2) for k in plot_order}
    
def set_axes(dict_1,dict_2,axes,bars=[]):
    tg_value=[imp_normalize_sorted(dict_1).get(i,0) for i in plot_order]
    pd_value=[imp_normalize_sorted(dict_2).get(i,0) for i in plot_order]
    tg_bar = axes.bar(plot_order,tg_value)
    pd_bar = axes.bar(plot_order,pd_value,bottom=tg_value,color='#45b2d1')
    bars.append([tg_bar,pd_bar])
    
def add_subplot_axes(ax,rect,facecolor='w'):
    fig = plt.gcf()
    box = ax.get_position()
    width = box.width
    height = box.height
    inax_position  = ax.transAxes.transform(rect[0:2])
    transFigure = fig.transFigure.inverted()
    infig_position = transFigure.transform(inax_position)
    x = infig_position[0]
    y = infig_position[1]
    width *= rect[2]
    height *= rect[3]  # <= Typo was here
    subax = fig.add_axes([x,y,width,height],facecolor=facecolor)
    x_labelsize = subax.get_xticklabels()[0].get_size()
    y_labelsize = subax.get_yticklabels()[0].get_size()
    x_labelsize *= rect[2]**0.5
    y_labelsize *= rect[3]**0.5
    subax.xaxis.set_tick_params(labelsize=x_labelsize)
    subax.yaxis.set_tick_params(labelsize=y_labelsize)
    return subax
    
def shap_clean_plot(value,data,ax):
    add_subplot_axes(ax,[0.55,0.45,0.42,0.5])
    shap.summary_plot(shap_reorder(value), df_reorder(data),feature_names=['' for i in range(12)],plot_type='violin',sort=False, show=False,color_bar=False)
    axtemp = plt.gca()
    axtemp.set_xlabel('')
    axtemp.set_xticks([])
    axtemp.set_yticklabels(order_rev,{'fontsize':13})
    axtemp.spines['right'].set_visible(True)
    axtemp.spines['top'].set_visible(True)
    axtemp.spines['left'].set_visible(True)
    axtemp.tick_params(axis='y',length=0,width=0,which='major')