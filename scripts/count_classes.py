import argparse
import pandas as pd

parser = argparse.ArgumentParser()
parser.add_argument(
    '-i', '--input_file', default=None, type=str
)
args = parser.parse_args()

csv = pd.read_csv(args.input_file, sep=' ')

action = 0
no_action = 0

train_action = 0
val_action = 0

train_no_action = 0
val_no_action = 0

for i in range(len(csv)):
    if csv['class'][i] == 0:
        no_action += 1
        if csv['subset'][i] == 'training':
            train_no_action += 1
        elif csv['subset'][i] == 'validation':
            val_no_action += 1
    else:
        action += 1
        if csv['subset'][i] == 'training':
            train_action += 1
        elif csv['subset'][i] == 'validation':
            val_action += 1

print('action = {}'.format(action))
print('no_action = {}'.format(no_action))
print('train action = {}'.format(train_action))
print('train no_action = {}'.format(train_no_action))
print('validation action = {}'.format(val_action))
print('validation no_action = {}'.format(val_no_action))
