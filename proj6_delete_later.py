import matplotlib.pyplot as plt

def plot_walk(animal):
    xs, ys = zip(*animal['positions'])
    #xs, ys = k

    plt.figure(figsize=(10,10))
    plt.scatter(xs, ys, color=animal['color'], edgecolor='k', alpha=0.7, s=100, marker=animal['marker'])
    plt.plot(xs, ys, lw=1.5, ls='--', color=animal['color'])
    plt.grid(True)
    plt.title(f'Path of Random Walk for {animal["name"]}')
    plt.xlabel('East-West')
    plt.ylabel('North-South')
    
    # Save the plot to a file
    #plt.savefig(f'{animal["name"]}_rw.png', dpi=300)
    #plt.close() 
    plt.show()

