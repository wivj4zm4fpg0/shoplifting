import argparse
import os
import re
import time

from joblib import Parallel, delayed


def parser():
    arg_parse = argparse.ArgumentParser()
    arg_parse.add_argument(
        'input_path', default=None, type=str,
        help='input path'
    )
    arg_parse.add_argument(
        'output_path', default=None, type=str,
        help='output path'
    )
    arg_parse.add_argument(
        '-ft', '--flow_type', default=0, type=int, choices=[0, 1, 2],
        help='flow type id. 0: farnback, 1: tvl1, 2: brox'
    )
    arg_parse.add_argument(
        '-pn', '--parallel_number', default=-1, type=int,
        help='parallel process number'
    )
    return arg_parse.parse_args()


class ExtractVideos:
    def __init__(self, args):
        self.args = args
        self.flow = {0: 'farn', 1: 'tvl1', 2: 'brox'}
        self.input_video_paths = []
        self.flow_x_paths = []
        self.flow_y_paths = []
        self.n_frames_paths = []

    def make_directory(self):
        input_path = self.args.input_path
        output_path = self.args.output_path
        for class_dir in os.listdir(input_path):
            self.n_frames_paths.append(os.path.join(
                output_path,
                'flow',
                self.flow[self.args.flow_type],
                'flow_x',
                class_dir
            ))
            self.n_frames_paths.append(os.path.join(
                output_path,
                'flow',
                self.flow[self.args.flow_type],
                'flow_y',
                class_dir
            ))
            for video in os.listdir(os.path.join(input_path, class_dir)):
                video_path = os.path.join(input_path, class_dir, video)
                flow_x_path = os.path.join(
                    output_path,
                    'flow',
                    self.flow[self.args.flow_type],
                    'flow_x',
                    class_dir,
                    video
                )
                flow_y_path = os.path.join(
                    output_path,
                    'flow',
                    self.flow[self.args.flow_type],
                    'flow_y',
                    class_dir,
                    video
                )
                if not os.path.isfile(os.path.join(flow_x_path, 'image_00001.jpg')):
                    os.makedirs(flow_x_path, exist_ok=True)
                    os.makedirs(flow_y_path, exist_ok=True)
                    self.input_video_paths.append(video_path)
                    self.flow_x_paths.append(flow_x_path)
                    self.flow_y_paths.append(flow_y_path)
                    print('create {}'.format(flow_x_path))
                    print('create {}'.format(flow_y_path))

    def process(self, input_video_path, flow_x_path, flow_y_path):
        file_name = '/image'
        regex = r'([()&;])'
        regex_later = r'\\\1'
        input_video_path = re.sub(regex, regex_later, input_video_path)
        flow_x_path = re.sub(regex, regex_later, flow_x_path)
        flow_y_path = re.sub(regex, regex_later, flow_y_path)

        print('processing {}'.format(''.join(input_video_path.split('/')[-1:])))
        os.system(
            'extract_cpu -f={} -i=temp/image -x={} -y={} -t={} -o=dir -s=1'.format(
                input_video_path,
                flow_x_path + file_name,
                flow_y_path + file_name,
                self.args.flow_type
            )
        )

    def large_data_processing(self):
        Parallel(
            n_jobs=self.args.parallel_number,
        )([delayed(self.process)(
            self.input_video_paths[i],
            self.flow_x_paths[i],
            self.flow_y_paths[i]
        ) for i in range(len(self.input_video_paths))])

    def create_frame_number(self):
        for path in self.n_frames_paths:
            os.system('scripts/n_frames.sh {}'.format(path))


if __name__ == '__main__':
    extract_videos = ExtractVideos(parser())
    start_time = time.time()
    extract_videos.make_directory()
    extract_videos.large_data_processing()
    extract_videos.create_frame_number()
    end_time = time.time() - start_time
    print('Time :{}[sec]'.format(end_time))
