from matplotlib import pyplot as plt

nodes = [20,40,60,80,100]
areas = [250, 500, 750, 1000, 1250]
flows = [10, 20, 30, 40, 50]

throughput = []
avg_delay = []
delivery_ratio = []
drop_ratio = []

with open('result.txt') as f:
    
    lines = f.readlines()
    
    for line in lines:
        if line.startswith('Throughput'):
            throughput.append(line.split()[1])
        elif line.startswith('Average Delay'):
            avg_delay.append(line.split()[2])
        elif line.startswith('Delivery ratio'):
            delivery_ratio.append(line.split()[2])
        elif line.startswith('Drop ratio'):
            drop_ratio.append(line.split()[2])
            

def plot_graph(y_values, x_values, x_label, y_label, fig_name) -> None:
    plt.plot(x_values, y_values, '-o')
    plt.xlabel(x_label)
    plt.ylabel(y_label)
    plt.savefig(f'./figures/{x_label}_variation/'+fig_name)    
    plt.close()


def main(x_axis, x_label) -> None:
    plot_graph([float(thr) for thr in throughput], x_axis, x_label, 'throughput', 'throughput.jpg')
    plot_graph([float(delay) for delay in avg_delay], x_axis, x_label, 'average delay', 'average_delay.jpg')
    plot_graph([float(delv_rat) for delv_rat in delivery_ratio], x_axis, x_label, 'delivery ratio', 'delivery_ratio.jpg')
    plot_graph([float(drop_rat) for drop_rat in drop_ratio], x_axis, x_label, 'drop ratio', 'drop_ratio.jpg')

if __name__ == '__main__':
    
    type = input('Enter the type: ')
    x_axis , x_labels = '',''
    
    if type == 'nodes':
        x_axis, x_labels = nodes, 'nodes'
    elif type == 'areas':
        x_axis, x_labels = areas, 'area'
    elif type == 'flows':
        x_axis, x_labels = flows, 'flows'
    
    main(x_axis, x_labels)    
    