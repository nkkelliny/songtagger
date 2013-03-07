import numpy as np
data = np.loadtxt('_csv file location_', 'r')
ave_columns = data.sum(axis=0)/(float(data.shape[0]))
#data.sum()

reader = int_wrapper(reader)
with open('_csv file locatione_', 'rb') as f:

    for row in reader (f):
        sum += int_wrapper(reader)
        row_count += 1
        
avg = sum/row_count
print str(avg)
def int_wrapper(reader):
    for v in reader:
        yield map(int, v)
