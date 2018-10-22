import pandas as pd

csv = pd.read_csv('out.csv', sep=' ')

width_count = 0
height_count = 0
aspect_ratio_sum = 0
aspect_ratio_avg = 0
width_sum = 0
height_sum = 0

for i in range(len(csv)):
    if csv['width'][i] > csv['height'][i]:
        width_count += 1
    else:
        height_count += 1
    aspect_ratio_sum += csv['width'][i] / csv['height'][i]
    width_sum += csv['width'][i]
    height_sum += csv['height'][i]

aspect_ratio_avg = aspect_ratio_sum / len(csv)

print('width = {}'.format(width_count))
print('height = {}'.format(height_count))
print('aspect ratio average = {}'.format(aspect_ratio_avg))
print('width average = {}'.format(width_sum / len(csv)))
print('height average = {}'.format(height_sum / len(csv)))

