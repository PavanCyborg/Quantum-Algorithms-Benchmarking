import matplotlib.pyplot as plt
def loadDatafromJson():
    import json
    
    # Define the file name
    file_name = '__data.json'
    
    # Read the data from the file
    with open(file_name, 'r') as file:
        data = json.load(file)
    
    print("Data has been loaded from", file_name)
    return data

def DataExtraction(data):
    global min_qbits,max_qbits,skp_qubits,Type_of_Simulator,benchmark_name,QV_,Processor,Cores,platform
    global avg_creation_times,std_creation_times,avg_elapsed_times,std_elapsed_times,avg_quantum_times,std_quantum_times,avg_circuit_depths,avg_transpiled_depths
    global avg_1Q_algorithmic_gate_counts,avg_1Q_Transpiled_gate_counts,avg_2Q_algorithmic_gate_counts,avg_2Q_Transpiled_gate_counts,avg_xi,avg_tr_xi
    global max_memory,avg_f,avg_Hf,std_f,std_hf,last_updated,gate_counts_plots,Memory_utilization_plot
    
    # Extract the data 
    configuration= data['configuration']
    min_qbits = configuration['min_qbits']
    max_qbits = configuration['max_qbits']
    skp_qubits = configuration['skp_qubits']
    Type_of_Simulator = configuration['Type_of_Simulator']
    platform = Type_of_Simulator
    benchmark_name = configuration['benchmark_name']
    QV_ = configuration['QV_']
    Processor = configuration['Processor']
    Cores = configuration['cores']
    avg_creation_times = data["avg_creation_times (ms)"]
    std_creation_times =data["std_creation_times (ms)"]
    avg_elapsed_times = data["avg_elapsed_times (ms)"]
    std_elapsed_times = data["std_elapsed_times (ms)"]
    avg_quantum_times = data["avg_quantum_times (ms)"]
    std_quantum_times = data["std_quantum_times (ms)"]
    avg_circuit_depths = data["avg_circuit_depths"]
    avg_transpiled_depths = data["avg_transpiled_depths"]
    avg_1Q_algorithmic_gate_counts = data["avg_1Q_algorithmic_gate_counts"]
    avg_2Q_algorithmic_gate_counts = data["avg_2Q_algorithmic_gate_counts"]
    avg_xi = data["avg_xi (n2q/n1q+n2q)"]
    avg_1Q_Transpiled_gate_counts = data["avg_1Q_Transpiled_gate_counts"]
    avg_2Q_Transpiled_gate_counts = data["avg_2Q_Transpiled_gate_counts"]
    avg_tr_xi = data["avg_tr_xi (tr_n2q/tr_n1q+tr_n2q)"]
    max_memory = data["max_memory (MB)"]
    avg_f=data["Average_Rescaled_fidelity"]
    avg_Hf=data["Average_Hellinger_fidelity"]
    std_f = data["std_Rescaled_Fidelity"]
    std_hf = data["std_hellinger_fidelity"]
    gate_counts_plots = data["gate_counts_plots"] 
    last_updated = data['last_updated']
    
    if len(max_memory)==0:
        Memory_utilization_plot = False
    else:
        Memory_utilization_plot = False
    
    print("Data extraction complete.")
    print("Data Last updated on :", last_updated)


def Plot_General_Benchmarks():
    import numpy as np
    # Plot histograms for average creation time, average elapsed time, average quantum processing time, and average circuit depth versus the number of qubits
    global num_qubits_range
    # Define the range of qubits for the x-axis
    num_qubits_range = range(min_qbits, max_qbits+1,skp_qubits)
    print("num_qubits_range =",num_qubits_range)

    # Plot histograms for average creation time, average elapsed time, average quantum processing time, and average circuit depth versus the number of qubits

    # Add labels to the bars
    def autolabel(rects,ax,str='{:.3f}',text_color="black"):
            max_y_value=ax.get_ylim()[1]  # Get the maximum value on the y-axis
            threshold=0.3*max_y_value   # Define threshold as 30% of max y-axis value
            for rect in rects:
                height = rect.get_height()
                if height < threshold:
                    rotation = 90
                    va = 'bottom'  # Place text above the bar
                    xytext = (0, 3)  # Offset slightly above the bar
                else:
                    rotation = 90
                    va = 'center'  # Place text inside the bar
                    xytext = (0, 0)  # No offset
                ax.annotate(str.format(height),  # Formatting to two decimal places
                            xy=(rect.get_x() + rect.get_width() / 2, height/6),
                            xytext=xytext,
                            textcoords="offset points",
                            ha='center', va=va, color=text_color, rotation=rotation)
    
    bar_width = 0.3
    
    # Determine the number of subplots and their arrangement
    if Memory_utilization_plot and gate_counts_plots:
        fig, (ax1, ax2, ax3, ax4, ax5, ax6, ax7) = plt.subplots(7, 1, figsize=(18, 30))
        # Plotting for both memory utilization and gate counts
        # ax1, ax2, ax3, ax4, ax5, ax6, ax7 are available
    elif Memory_utilization_plot:
        fig, (ax1, ax2, ax3, ax6, ax7) = plt.subplots(5, 1, figsize=(18, 30))
        # Plotting for memory utilization only
        # ax1, ax2, ax3, ax6, ax7 are available
    elif gate_counts_plots:
        fig, (ax1, ax2, ax3, ax4, ax5, ax6) = plt.subplots(6, 1, figsize=(18, 30))
        # Plotting for gate counts only
        # ax1, ax2, ax3, ax4, ax5, ax6 are available
    else:
        fig, (ax1, ax2, ax3, ax6) = plt.subplots(4, 1, figsize=(18, 30))
        # Default plotting
        # ax1, ax2, ax3, ax6 are available
    
    fig.suptitle(f"General Benchmarks : {platform} - {benchmark_name} - {Processor}", fontsize=16)
    
    
    ax1.set_xticks(range(min(num_qubits_range), max(num_qubits_range)+1, skp_qubits))
    x = ax1.bar(num_qubits_range, avg_creation_times, yerr=std_creation_times, capsize=15, color='deepskyblue')
    autolabel(ax1.patches, ax1)
    ax1.set_xlabel('Number of Qubits')
    ax1.set_ylabel('Average Creation Time (ms)')
    ax1.set_title('Average Creation Time vs Number of Qubits',fontsize=14)
    
    
    ax2.set_xticks(range(min(num_qubits_range), max(num_qubits_range)+1, skp_qubits))
    
    
    Elapsed= ax2.bar(np.array(num_qubits_range) - bar_width / 2, avg_elapsed_times,yerr=std_elapsed_times, capsize=15, width=bar_width, color='cyan', label='Elapsed Time')
    Quantum= ax2.bar(np.array(num_qubits_range) + bar_width / 2, avg_quantum_times,yerr=std_quantum_times, capsize=15,width=bar_width, color='deepskyblue',label ='Quantum Time')
    autolabel(Elapsed,ax2,str='{:.1f}')
    autolabel(Quantum,ax2,str='{:.1f}')
    ax2.set_xlabel('Number of Qubits')
    ax2.set_ylabel('Average Time (ms)')
    ax2.set_title('Average Time vs Number of Qubits')
    ax2.legend()
    
    
    ax3.set_xticks(range(min(num_qubits_range), max(num_qubits_range)+1, skp_qubits))
    Normalized = ax3.bar(np.array(num_qubits_range) - bar_width / 2, avg_transpiled_depths, color='cyan', label='Normalized Depth', width=bar_width)  # Adjust width here
    Algorithmic = ax3.bar(np.array(num_qubits_range) + bar_width / 2,avg_circuit_depths, color='deepskyblue', label='Algorithmic Depth', width=bar_width)  # Adjust width here
    autolabel(Normalized,ax3,str='{:.2f}')
    autolabel(Algorithmic,ax3,str='{:.2f}')
    ax3.set_xlabel('Number of Qubits')
    ax3.set_ylabel('Average Circuit Depth')
    ax3.set_title('Average Circuit Depth vs Number of Qubits')
    ax3.legend()
    
    if gate_counts_plots == True:
        ax4.set_xticks(range(min(num_qubits_range), max(num_qubits_range)+1, skp_qubits))
        Normalized_1Q_counts = ax4.bar(np.array(num_qubits_range) - bar_width / 2, avg_1Q_Transpiled_gate_counts, color='cyan', label='Normalized Gate Counts', width=bar_width)  # Adjust width here
        Algorithmic_1Q_counts = ax4.bar(np.array(num_qubits_range) + bar_width / 2, avg_1Q_algorithmic_gate_counts, color='deepskyblue', label='Algorithmic Gate Counts', width=bar_width)  # Adjust width here
        autolabel(Normalized_1Q_counts,ax4,str='{}')
        autolabel(Algorithmic_1Q_counts,ax4,str='{}')
        ax4.set_xlabel('Number of Qubits')
        ax4.set_ylabel('Average 1-Qubit Gate Counts')
        ax4.set_title('Average 1-Qubit Gate Counts vs Number of Qubits')
        ax4.legend()
        
        ax5.set_xticks(range(min(num_qubits_range), max(num_qubits_range)+1, skp_qubits))
        Normalized_2Q_counts = ax5.bar(np.array(num_qubits_range) - bar_width / 2, avg_2Q_Transpiled_gate_counts, color='cyan', label='Normalized Gate Counts', width=bar_width)  # Adjust width here
        Algorithmic_2Q_counts = ax5.bar(np.array(num_qubits_range) + bar_width / 2, avg_2Q_algorithmic_gate_counts, color='deepskyblue', label='Algorithmic Gate Counts', width=bar_width)  # Adjust width here
        autolabel(Normalized_2Q_counts,ax5,str='{}')
        autolabel(Algorithmic_2Q_counts,ax5,str='{}')
        ax5.set_xlabel('Number of Qubits')
        ax5.set_ylabel('Average 2-Qubit Gate Counts')
        ax5.set_title('Average 2-Qubit Gate Counts vs Number of Qubits')
        ax5.legend()
    
    
    ax6.set_xticks(range(min(num_qubits_range), max(num_qubits_range)+1, skp_qubits))
    Hellinger = ax6.bar(np.array(num_qubits_range) - bar_width / 2, avg_Hf,yerr=std_hf, capsize=15, width=bar_width, label='Hellinger Fidelity',color='cyan')  # Adjust width here
    Normalized = ax6.bar(np.array(num_qubits_range) + bar_width / 2, avg_f,yerr=std_f, capsize=15, width=bar_width, label='Normalized Fidelity', color='deepskyblue')  # Adjust width here
    autolabel(Hellinger,ax6,str='{:.2f}')
    autolabel(Normalized,ax6,str='{:.2f}')
    ax6.set_xlabel('Number of Qubits')
    ax6.set_ylabel('Average Value')
    ax6.set_title("Fidelity Comparison")
    ax6.legend()
    
    if Memory_utilization_plot == True:
        ax7.set_xticks(range(min(num_qubits_range), max(num_qubits_range)+1, skp_qubits))
        x = ax7.bar(num_qubits_range, max_memory, color='turquoise', width=bar_width, label="Memory Utilizations")
        autolabel(ax7.patches, ax7)
        ax7.set_xlabel('Number of Qubits')
        ax7.set_ylabel('Maximum Memory Utilized (MB)')
        ax7.set_title('Memory Utilized vs Number of Qubits',fontsize=14)
    
    
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    
    plt.savefig("ParameterPlotsSample.jpg")
    plt.show()
    
from matplotlib.patches import Rectangle
import matplotlib.cm as cm
from matplotlib.colors import ListedColormap, LinearSegmentedColormap, Normalize
from matplotlib.patches import Circle
import math
############### Color Map functions
 
# Create a selection of colormaps from which to choose; default to custom_spectral
cmap_spectral = plt.get_cmap('Spectral')
cmap_greys = plt.get_cmap('Greys')
cmap_blues = plt.get_cmap('Blues')
cmap_custom_spectral = None

# the default colormap is the spectral map
cmap = cmap_spectral
cmap_orig = cmap_spectral

# current cmap normalization function (default None)
cmap_norm = None

default_fade_low_fidelity_level = 0.16
default_fade_rate = 0.7


# Specify a normalization function here (default None)
def set_custom_cmap_norm(vmin, vmax):

    global cmap_norm
    
    if vmin == vmax or (vmin == 0.0 and vmax == 1.0):
        print("... setting cmap norm to None")
        cmap_norm = None
    else:
        print(f"... setting cmap norm to [{vmin}, {vmax}]")
        cmap_norm = Normalize(vmin=vmin, vmax=vmax)
    
# Remake the custom spectral colormap with user settings
def set_custom_cmap_style(
            fade_low_fidelity_level=default_fade_low_fidelity_level,
            fade_rate=default_fade_rate):
            
    #print("... set custom map style")
    global cmap, cmap_custom_spectral, cmap_orig
    cmap_custom_spectral = create_custom_spectral_cmap(
                fade_low_fidelity_level=fade_low_fidelity_level, fade_rate=fade_rate)
    cmap = cmap_custom_spectral
    cmap_orig = cmap_custom_spectral


# Create the custom spectral colormap from the base spectral
def create_custom_spectral_cmap(
            fade_low_fidelity_level=default_fade_low_fidelity_level,
            fade_rate=default_fade_rate):

    # determine the breakpoint from the fade level
    num_colors = 100
    breakpoint = round(fade_low_fidelity_level * num_colors)
    
    # get color list for spectral map
    spectral_colors = [cmap_spectral(v/num_colors) for v in range(num_colors)]

    #print(fade_rate)
    
    # create a list of colors to replace those below the breakpoint
    # and fill with "faded" color entries (in reverse)
    low_colors = [0] * breakpoint
    #for i in reversed(range(breakpoint)):
    for i in range(breakpoint):
    
        # x is index of low colors, normalized 0 -> 1
        x = i / breakpoint
    
        # get color at this index
        bc = spectral_colors[i]
        r0 = bc[0]
        g0 = bc[1]
        b0 = bc[2]
        z0 = bc[3]
        
        r_delta = 0.92 - r0
        
        #print(f"{x} {bc} {r_delta}")
         
        # compute saturation and greyness ratio
        sat_ratio = 1 - x
        
        #grey_ratio = 1 - x
        '''  attempt at a reflective gradient   
        if i >= breakpoint/2:
            xf = 2*(x - 0.5)
            yf = pow(xf, 1/fade_rate)/2
            grey_ratio = 1 - (yf + 0.5)
        else:
            xf = 2*(0.5 - x)
            yf = pow(xf, 1/fade_rate)/2
            grey_ratio = 1 - (0.5 - yf)
        '''   
        grey_ratio = 1 - math.pow(x, 1/fade_rate)
        
        #print(f"  {xf} {yf} ")
        #print(f"  {sat_ratio} {grey_ratio}")

        r = r0 + r_delta * sat_ratio
        
        g_delta = r - g0
        b_delta = r - b0
        g = g0 + g_delta * grey_ratio
        b = b0 + b_delta * grey_ratio 
            
        #print(f"{r} {g} {b}\n")    
        low_colors[i] = (r,g,b,z0)
        
    #print(low_colors)

    # combine the faded low colors with the regular spectral cmap to make a custom version
    cmap_custom_spectral = ListedColormap(low_colors + spectral_colors[breakpoint:])

    #spectral_colors = [cmap_custom_spectral(v/10) for v in range(10)]
    #for i in range(10): print(spectral_colors[i])
    #print("")
    
    return cmap_custom_spectral

# Make the custom spectral color map the default on module init
set_custom_cmap_style()

# Arrange the stored annotations optimally and add to plot 
def anno_volumetric_data(ax, depth_base=2, label='Depth',
        labelpos=(0.2, 0.7), labelrot=0, type=1, fill=True):
    
    # sort all arrays by the x point of the text (anno_offs)
    global x_anno_offs, y_anno_offs, anno_labels, x_annos, y_annos
    all_annos = sorted(zip(x_anno_offs, y_anno_offs, anno_labels, x_annos, y_annos))
    x_anno_offs = [a for a,b,c,d,e in all_annos]
    y_anno_offs = [b for a,b,c,d,e in all_annos]
    anno_labels = [c for a,b,c,d,e in all_annos]
    x_annos = [d for a,b,c,d,e in all_annos]
    y_annos = [e for a,b,c,d,e in all_annos]
    
    #print(f"{x_anno_offs}")
    #print(f"{y_anno_offs}")
    #print(f"{anno_labels}")
    
    for i in range(len(anno_labels)):
        x_anno = x_annos[i]
        y_anno = y_annos[i]
        x_anno_off = x_anno_offs[i]
        y_anno_off = y_anno_offs[i]
        label = anno_labels[i]
        
        if i > 0:
            x_delta = abs(x_anno_off - x_anno_offs[i - 1])
            y_delta = abs(y_anno_off - y_anno_offs[i - 1])
            
            if y_delta < 0.7 and x_delta < 2:
                y_anno_off = y_anno_offs[i] = y_anno_offs[i - 1] - 0.6
                #x_anno_off = x_anno_offs[i] = x_anno_offs[i - 1] + 0.1
                    
        ax.annotate(label,
            xy=(x_anno+0.0, y_anno+0.1),
            arrowprops=dict(facecolor='black', shrink=0.0,
                width=0.5, headwidth=4, headlength=5, edgecolor=(0.8,0.8,0.8)),
            xytext=(x_anno_off + labelpos[0], y_anno_off + labelpos[1]),
            rotation=labelrot,
            horizontalalignment='left', verticalalignment='baseline',
            color=(0.2,0.2,0.2),
            clip_on=True)
    # if saveplots == True:
    plt.savefig("VolumetricPlotSample.jpg")
    plt.show()

# Plot one group of data for volumetric presentation    
def plot_volumetric_data(ax, w_data, d_data, f_data, depth_base=2, label='Depth',
        labelpos=(0.2, 0.7), labelrot=0, type=1, fill=True, w_max=18, do_label=False, do_border=True,
        x_size=1.0, y_size=1.0, zorder=1, offset_flag=False,
        max_depth=0, suppress_low_fidelity=False):

    # since data may come back out of order, save point at max y for annotation
    i_anno = 0
    x_anno = 0 
    y_anno = 0
    
    # plot data rectangles
    low_fidelity_count = True
    
    last_y = -1
    k = 0

    # determine y-axis dimension for one pixel to use for offset of bars that start at 0
    (_, dy) = get_pixel_dims(ax)
    
    # do this loop in reverse to handle the case where earlier cells are overlapped by later cells
    for i in reversed(range(len(d_data))):
        x = depth_index(d_data[i], depth_base)
        y = float(w_data[i])
        f = f_data[i]
        
        # each time we star a new row, reset the offset counter
        # DEVNOTE: this is highly specialized for the QA area plots, where there are 8 bars
        # that represent time starting from 0 secs.  We offset by one pixel each and center the group
        if y != last_y:
            last_y = y;
            k = 3              # hardcoded for 8 cells, offset by 3
        
        #print(f"{i = } {x = } {y = }")
        
        if max_depth > 0 and d_data[i] > max_depth:
            #print(f"... excessive depth (2), skipped; w={y} d={d_data[i]}")
            break;
            
        # reject cells with low fidelity
        if suppress_low_fidelity and f < suppress_low_fidelity_level:
            if low_fidelity_count: break
            else: low_fidelity_count = True
        
        # the only time this is False is when doing merged gradation plots
        if do_border == True:
        
            # this case is for an array of x_sizes, i.e. each box has different width
            if isinstance(x_size, list):
                
                # draw each of the cells, with no offset
                if not offset_flag:
                    ax.add_patch(box_at(x, y, f, type=type, fill=fill, x_size=x_size[i], y_size=y_size, zorder=zorder))
                    
                # use an offset for y value, AND account for x and width to draw starting at 0
                else:
                    ax.add_patch(box_at((x/2 + x_size[i]/4), y + k*dy, f, type=type, fill=fill, x_size=x+ x_size[i]/2, y_size=y_size, zorder=zorder))
                
            # this case is for only a single cell
            else:
                ax.add_patch(box_at(x, y, f, type=type, fill=fill, x_size=x_size, y_size=y_size))

        # save the annotation point with the largest y value
        if y >= y_anno:
            x_anno = x
            y_anno = y
            i_anno = i
        
        # move the next bar down (if using offset)
        k -= 1
    
    # if no data rectangles plotted, no need for a label
    if x_anno == 0 or y_anno == 0:
        return
        
    x_annos.append(x_anno)
    y_annos.append(y_anno)
    
    anno_dist = math.sqrt( (y_anno - 1)**2 + (x_anno - 1)**2 )
    
    # adjust radius of annotation circle based on maximum width of apps
    anno_max = 10
    if w_max > 10:
        anno_max = 14
    if w_max > 14:
        anno_max = 18
        
    scale = anno_max / anno_dist

    # offset of text from end of arrow
    if scale > 1:
        x_anno_off = scale * x_anno - x_anno - 0.5
        y_anno_off = scale * y_anno - y_anno
    else:
        x_anno_off = 0.7
        y_anno_off = 0.5
        
    x_anno_off += x_anno
    y_anno_off += y_anno
    
    # print(f"... {xx} {yy} {anno_dist}")
    x_anno_offs.append(x_anno_off)
    y_anno_offs.append(y_anno_off)
    
    anno_labels.append(label)
    
    if do_label:
        ax.annotate(label, xy=(x_anno+labelpos[0], y_anno+labelpos[1]), rotation=labelrot,
            horizontalalignment='left', verticalalignment='bottom', color=(0.2,0.2,0.2))

x_annos = []
y_annos = []
x_anno_offs = []
y_anno_offs = []
anno_labels = []

# init arrays to hold annotation points for label spreading
def vplot_anno_init ():

    global x_annos, y_annos, x_anno_offs, y_anno_offs, anno_labels
    
    x_annos = []
    y_annos = []
    x_anno_offs = []
    y_anno_offs = []
    anno_labels = []

# Number of ticks on volumetric depth axis
max_depth_log = 22

# average transpile factor between base QV depth and our depth based on results from QV notebook
QV_transpile_factor = 12.7 

# format a number using K,M,B,T for large numbers, optionally rounding to 'digits' decimal places if num > 1
# (sign handling may be incorrect)
def format_number(num, digits=0):
    if isinstance(num, str): num = float(num)
    num = float('{:.3g}'.format(abs(num)))
    sign = ''
    metric = {'T': 1000000000000, 'B': 1000000000, 'M': 1000000, 'K': 1000, '': 1}
    for index in metric:
        num_check = num / metric[index]
        if num_check >= 1:
            num = round(num_check, digits)
            sign = index
            break
    numstr = f"{str(num)}"
    if '.' in numstr:
        numstr = numstr.rstrip('0').rstrip('.')
    return f"{numstr}{sign}"

# Return the color associated with the spcific value, using color map norm
def get_color(value):
    
    # if there is a normalize function installed, scale the data
    if cmap_norm:
        value = float(cmap_norm(value))
        
    if cmap == cmap_spectral:
        value = 0.05 + value*0.9
    elif cmap == cmap_blues:
        value = 0.00 + value*1.0
    else:
        value = 0.0 + value*0.95
        
    return cmap(value)

# Return the x and y equivalent to a single pixel for the given plot axis
def get_pixel_dims(ax):

    # transform 0 -> 1 to pixel dimensions
    pixdims = ax.transData.transform([(0,1),(1,0)])-ax.transData.transform((0,0))
    xpix = pixdims[1][0]
    ypix = pixdims[0][1]
    
    #determine x- and y-axis dimension for one pixel 
    dx = (1 / xpix)
    dy = (1 / ypix)
    
    return (dx, dy)

############### Helper functions
 
# return the base index for a circuit depth value
# take the log in the depth base, and add 1
def depth_index(d, depth_base):
    if depth_base <= 1:
        return d
    if d == 0:
        return 0
    return math.log(d, depth_base) + 1

# draw a box at x,y with various attributes   
def box_at(x, y, value, type=1, fill=True, x_size=1.0, y_size=1.0, alpha=1.0, zorder=1):
    
    value = min(value, 1.0)
    value = max(value, 0.0)

    fc = get_color(value)
    ec = (0.5,0.5,0.5)
    
    return Rectangle((x - (x_size/2), y - (y_size/2)), x_size, y_size,
             alpha=alpha,
             edgecolor = ec,
             facecolor = fc,
             fill=fill,
             lw=0.5*y_size,
             zorder=zorder)

# draw a circle at x,y with various attributes 
def circle_at(x, y, value, type=1, fill=True):
    size = 1.0
    
    value = min(value, 1.0)
    value = max(value, 0.0)

    fc = get_color(value)
    ec = (0.5,0.5,0.5)
    
    return Circle((x, y), size/2,
             alpha = 0.7,                       # DEVNOTE: changed to 0.7 from 0.5, to handle only one cell
             edgecolor = ec,
             facecolor = fc,
             fill=fill,
             lw=0.5)
             
def box4_at(x, y, value, type=1, fill=True, alpha=1.0):
    size = 1.0
    
    value = min(value, 1.0)
    value = max(value, 0.0)

    fc = get_color(value)
    ec = (0.3,0.3,0.3)
    ec = fc
    
    return Rectangle((x - size/8, y - size/2), size/4, size,
             alpha=alpha,
             edgecolor = ec,
             facecolor = fc,
             fill=fill,
             lw=0.1)

# Draw a Quantum Volume rectangle with specified width and depth, and grey-scale value 
def qv_box_at(x, y, qv_width, qv_depth, value, depth_base):
    #print(f"{qv_width} {qv_depth} {depth_index(qv_depth, depth_base)}")
    return Rectangle((x - 0.5, y - 0.5), depth_index(qv_depth, depth_base), qv_width,
             edgecolor = (value,value,value),
             facecolor = (value,value,value),
             fill=True,
             lw=1)

def bkg_box_at(x, y, value=0.9):
    size = 0.6
    return Rectangle((x - size/2, y - size/2), size, size,
             edgecolor = (.75,.75,.75),
             facecolor = (value,value,value),
             fill=True,
             lw=0.5)
             
def bkg_empty_box_at(x, y):
    size = 0.6
    return Rectangle((x - size/2, y - size/2), size, size,
             edgecolor = (.75,.75,.75),
             facecolor = (1.0,1.0,1.0),
             fill=True,
             lw=0.5)

# Plot the background for the volumetric analysis    
def plot_volumetric_background(max_qubits=11, QV=32, depth_base=2, suptitle=None, avail_qubits=0, colorbar_label="Avg Result Fidelity"):

    if suptitle == None:
        suptitle = f"Volumetric Positioning\nCircuit Dimensions and Fidelity Overlaid on Quantum Volume = {QV}"

    QV0 = QV
    qv_estimate = False
    est_str = ""
    if QV == 0:                 # QV = 0 indicates "do not draw QV background or label"
        QV = 2048
        
    elif QV < 0:                # QV < 0 indicates "add est. to label"
        QV = -QV
        qv_estimate = True
        est_str = " (est.)"
        
    if avail_qubits > 0 and max_qubits > avail_qubits:
        max_qubits = avail_qubits
        
    max_width = 13
    if max_qubits > 11: max_width = 18
    if max_qubits > 14: max_width = 20
    if max_qubits > 16: max_width = 24
    if max_qubits > 24: max_width = 33
    #print(f"... {avail_qubits} {max_qubits} {max_width}")
    
    plot_width = 6.8
    plot_height = 0.5 + plot_width * (max_width / max_depth_log)
    #print(f"... {plot_width} {plot_height}")
    
    # define matplotlib figure and axis; use constrained layout to fit colorbar to right
    fig, ax = plt.subplots(figsize=(plot_width, plot_height), constrained_layout=True)

    plt.suptitle(suptitle)

    plt.xlim(0, max_depth_log)
    plt.ylim(0, max_width)

    # circuit depth axis (x axis)
    xbasis = [x for x in range(1,max_depth_log)]
    xround = [depth_base**(x-1) for x in xbasis]
    xlabels = [format_number(x) for x in xround]
    ax.set_xlabel('Circuit Depth')
    ax.set_xticks(xbasis)  
    plt.xticks(xbasis, xlabels, color='black', rotation=45, ha='right', va='top', rotation_mode="anchor")
    
    # other label options
    #plt.xticks(xbasis, xlabels, color='black', rotation=-60, ha='left')
    #plt.xticks(xbasis, xlabels, color='black', rotation=-45, ha='left', va='center', rotation_mode="anchor")

    # circuit width axis (y axis)
    ybasis = [y for y in range(1,max_width)]
    yround = [1,2,3,4,5,6,7,8,10,12,15]     # not used now
    ylabels = [str(y) for y in yround]      # not used now 
    #ax.set_ylabel('Circuit Width (Number of Qubits)')
    ax.set_ylabel('Circuit Width')
    ax.set_yticks(ybasis)

    #create simple line plot (not used right now)
    #ax.plot([0, 10],[0, 10])
    
    log2QV = math.log2(QV)
    QV_width = log2QV
    QV_depth = log2QV * QV_transpile_factor
    
    # show a quantum volume rectangle of QV = 64 e.g. (6 x 6)
    if QV0 != 0:
        ax.add_patch(qv_box_at(1, 1, QV_width, QV_depth, 0.87, depth_base))
    else:
        ax.add_patch(qv_box_at(1, 1, QV_width, QV_depth, 0.91, depth_base))
    
    # the untranspiled version is commented out - we do not show this by default
    # also show a quantum volume rectangle un-transpiled
    # ax.add_patch(qv_box_at(1, 1, QV_width, QV_width, 0.80, depth_base))

    # show 2D array of volumetric cells based on this QV_transpiled
    # DEVNOTE: we use +1 only to make the visuals work; s/b without
    # Also, the second arg of the min( below seems incorrect, needs correction
    maxprod = (QV_width + 1) * (QV_depth + 1)
    for w in range(1, min(max_width, round(QV) + 1)):
        
        # don't show VB squares if width greater than known available qubits
        if avail_qubits != 0 and w > avail_qubits:
            continue
        
        i_success = 0
        for d in xround:
        
            # polarization factor for low circuit widths
            maxtest = maxprod / ( 1 - 1 / (2**w) )
            
            # if circuit would fail here, don't draw box
            if d > maxtest: continue
            if w * d > maxtest: continue
            
            # guess for how to capture how hardware decays with width, not entirely correct

            # # reduce maxtext by a factor of number of qubits > QV_width
            # # just an approximation to account for qubit distances
            # if w > QV_width:
            #     over = w - QV_width 
            #     maxtest = maxtest / (1 + (over/QV_width))

            # draw a box at this width and depth
            id = depth_index(d, depth_base) 
            
            # show vb rectangles; if not showing QV, make all hollow (or less dark)
            if QV0 == 0:
                #ax.add_patch(bkg_empty_box_at(id, w))
                ax.add_patch(bkg_box_at(id, w, 0.95))
            
            else:
                ax.add_patch(bkg_box_at(id, w, 0.9))
            
            # save index of last successful depth
            i_success += 1
        
        # plot empty rectangle after others       
        d = xround[i_success]
        id = depth_index(d, depth_base) 
        ax.add_patch(bkg_empty_box_at(id, w))
        
    
    # Add annotation showing quantum volume
    if QV0 != 0:
        t = ax.text(max_depth_log - 2.0, 1.5, f"QV{est_str}={QV}", size=12,
                horizontalalignment='right', verticalalignment='center', color=(0.2,0.2,0.2),
                bbox=dict(boxstyle="square,pad=0.3", fc=(.9,.9,.9), ec="grey", lw=1))
                
    # add colorbar to right of plot
    plt.colorbar(cm.ScalarMappable(cmap=cmap), cax=None, ax=ax,
            shrink=0.6, label=colorbar_label, panchor=(0.0, 0.7))
            
    return ax

def Volumetric_Positioning_Plot():
    # Quantum Volume Plot
    Suptitle = f"Volumetric Positioning - {Type_of_Simulator}"
    appname=benchmark_name
    if QV_ == None:
        QV=2048
    else:
        QV=QV_
    depth_base =2
    
    ax = plot_volumetric_background(max_qubits=max_qbits, QV=QV,depth_base=depth_base, suptitle=Suptitle, colorbar_label="Avg Result Fidelity")
    
    w_data = num_qubits_range
    # determine width for circuit
    w_max = 0
    for i in range(len(w_data)):
        y = float(w_data[i])
        w_max = max(w_max, y)
    
    if len(avg_transpiled_depths)==0:
        d_tr_data = avg_circuit_depths #if there are not transpiled depths use circuit Depths
    else:
        d_tr_data = avg_transpiled_depths
        
    f_data = avg_f
    
    plot_volumetric_data(ax, w_data, d_tr_data, f_data, depth_base, fill=True,label=appname, labelpos=(0.4, 0.6), labelrot=15, type=1, w_max=w_max)
    anno_volumetric_data(ax, depth_base,label=appname, labelpos=(0.4, 0.6), labelrot=15, type=1, fill=False)

if __name__=="__main__":
    data=loadDatafromJson()
    DataExtraction(data)
    Plot_General_Benchmarks()
    Volumetric_Positioning_Plot()
