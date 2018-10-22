import pandas as pd
import random
import operator

csv = pd.read_csv('out.csv', sep=' ')
action_index = 0
no_action_index = 0
subset = {}

random_csv = list(range(len(csv)))
random.shuffle(random_csv)
with open('label.csv', 'w') as f:
    f.write('id video_name class subset\n')
    for i in random_csv:
        if csv['class'][i] == 0:
            if no_action_index <= 98:
                subset[i] = 'train'
            else:
                subset[i] = 'val'
            no_action_index += 1
        else:
            if action_index <= 98:
                subset[i] = 'train'
            else:
                subset[i] = 'val'
            action_index += 1

    sorted_subset = sorted(subset.items(), key=operator.itemgetter(0))
    for i in range(len(csv)):
        f.write('{} {} {} {}\n'.format(csv['id'][i], csv['video_name'][i], csv['class'][i], sorted_subset[i][1]))
