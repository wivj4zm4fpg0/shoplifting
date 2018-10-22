import pandas as pd

csv = pd.read_csv('under_sampling.csv', sep=' ')


def time_format(string):
    times = string.split(":")
    during_time = int(times[1]) * 60 + int(times[2])
    return during_time


with open('out.csv', 'w') as f:
    f.write('id video_name class start_time end_time x y width height fps\n')
    for i in range(len(csv['id'])):
        time = time_format(csv['end_time'][i]) - time_format(csv['start_time'][i])
        fps = ''
        if time == 10 or time == 9:
            fps = 4
        elif time == 8 or time == 7:
            fps = 5
        elif time == 6:
            fps = 6
        elif time == 5:
            fps = 7
        elif time == 4:
            fps = 9
        elif time == 3:
            fps = 11
        elif 11 <= time <= 16:
            fps = 3
        elif 17 <= time <= 31:
            fps = 2
        elif time >= 32:
            fps = 1
        f.write('{} {} {} {} {} {} {} {} {} {}\n'.format(i, csv['video_name'][i], csv['class'][i], csv['start_time'][i],
                                                         csv['end_time'][i], csv['x'][i], csv['y'][i], csv['width'][i],
                                                         csv['height'][i], fps))
