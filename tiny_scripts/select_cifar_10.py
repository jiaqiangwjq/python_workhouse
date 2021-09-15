'''
Selected cifar-10. The .csv file format:

class_index,data_index
3,0
8,1
8,2
...

'''

import pickle
import pandas as pd

file = 'E:\pycharm\LEARN\data\cifar-10\cifar-10-batches-py\\test_batch'

with open(file, 'rb') as f:
    dict = pickle.load(f, encoding='bytes')

dict.keys()

batch_label = dict[b'batch_label']
labels = dict[b'labels']
data = dict[b'data']
filenames = dict[b'filenames']

length = len(labels)
data_index = [i for i in range(length)]
class_index = labels
csv_dict = {'class_index': class_index, 'data_index': data_index}

df = pd.DataFrame(csv_dict)
df.to_csv('selected_cifar10.csv', index=False)