import pandas as pd

n_frames = 64

csv = pd.read_csv('under_sampling.csv', sep=' ')


def time_format(string):
    times = string.split(":")
    during_time = int(times[1]) * 60 + int(times[2])
    return during_time


def get_fps(time, n_frames):
    fps = 1
    while fps * time < n_frames:
        fps += 1
    return fps


with open('out.csv', 'w') as f:
    f.write('id video_name class start_time end_time x y width height fps\n')
    for i in range(len(csv['id'])):
        time = time_format(csv['end_time'][i]) - time_format(csv['start_time'][i])
        f.write('{} {} {} {} {} {} {} {} {} {}\n'.format(i, csv['video_name'][i], csv['class'][i], csv['start_time'][i],
                                                         csv['end_time'][i], csv['x'][i], csv['y'][i], csv['width'][i],
                                                         csv['height'][i], get_fps(time, n_frames)))
