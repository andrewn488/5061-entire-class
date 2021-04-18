"""FQ20 - OMSBA 5061 - Week 10
​
TW15: Plotting
​
Maroon Team: Andrew Nalundasan, Tamlyn Tamura, and Chequala Fuller
​
Description: Write the read_data and plot_data functions to get the
desired plot. This lab requires you to read in data from a file, massage
it slightly, and plot it using pyplot (see Chap. 11 in the textbook).
"""
​
import pylab
​
fh = 'tw15_plotting.csv'
def read_data(filename):
    """
    >>> data = [(3, 4, 9), (1, 99, 100), (-3, 44, 1000)]
    >>> print("unsorted:", data)
    unsorted: [(3, 4, 9), (1, 99, 100), (-3, 44, 1000)]
    >>> data.sort()  # sort by first tuple value
    >>> print("sorted:", data)
    sorted: [(-3, 44, 1000), (1, 99, 100), (3, 4, 9)]
    """
    
    plotting = open(fh, 'r')
    line = plotting.readline()
    
    my_list = []
    for values in plotting:
        contents = values.split(',')
        x = float(contents[0])
        y1 = float(contents[1])
        y2 = float(contents[2])
        my_list.append((x, y1, y2))

    my_list.sort()
    plotting.close()
    return my_list
    
def plot_data(data):
    x_list = []
    for elem in data:
        x = elem[0]
        x_list.append(x)
​
    y1_list = []
    for elem in data:
        y1 = elem[1]
        y1_list.append(y1)
​
    y2_list = []
    for elem in data:
        y2 = elem[2]
        y2_list.append(y2)
        
    pylab.plot(x_list, y1_list)
    pylab.plot(x_list, y2_list)
    pylab.title('tw15_plotting - CPSC 5061 - Seattle University')
    pylab.xlabel('x')
    pylab.ylabel('y1, y2')
    pylab.show()
​
if __name__ == '__main__':
    plot_data(read_data('tw15_plotting.csv'))
