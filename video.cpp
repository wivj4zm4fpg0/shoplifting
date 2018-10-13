#include <iostream>
#include <stdio.h>
#include <opencv2/opencv.hpp>
using namespace::std;
using namespace::cv;

Rect box;
bool drawing_box = false;

double delay = 0.0333667;
float scale = 0;
int second = 0;
int minite = 0;
int hour = 0;
int time_ = 0;

int g_slider_position = 0;
int g_run = 1;
int g_dontset = 0;
VideoCapture g_cap;

void draw_box(Mat& img, Rect box)
{
    rectangle(img, box.tl(), box.br(), Scalar(0x00, 0x00, 0xff), 2);
}

void my_mouse_callback(int event, int x, int y, int flags, void* param)
{
    Mat& image = *(Mat*)param;
    switch (event) {
        case EVENT_MOUSEMOVE:
            if (drawing_box) {
                box.width = x - box.x;
                box.height = box.width * 3 / 4;
                if (x > box.x && y < box.y || x < box.x && y > box.y) {
                    box.height *= -1;
                }
            }
            break;
        case EVENT_LBUTTONDOWN:
            drawing_box = true;
            box = Rect(x, y, 0, 0);
            break;
        case EVENT_LBUTTONUP:
            drawing_box = false;
            if (abs(box.width) <= 320) {
                scale = 0;
            }
            else {
                scale = 320 / (float)box.width;
            }
            if (box.width < 0) {
                box.x += box.width;
                box.width *= -1;
            }
            if (box.height < 0) {
                box.y += box.height;
                box.height *= -1;
            }
            cout << "x :" << box.x << ", y :" << box.y << ", width :" << box.width << ", height :" << box.height << ", scale :" << abs(scale) << endl;
            break;
    }
}

void onTrackbarSlide(int pos, void *)
{
    g_cap.set(CAP_PROP_POS_FRAMES, pos);
    if (!g_dontset) {
        g_run = 1;

        time_ = (int)(g_cap.get(CAP_PROP_POS_MSEC) / 1000 - delay);
        second = time_ % 60;
        minite = time_ / 60;
        hour = time_ / 3600;
    }
    g_dontset = 0;
}

int main(int argc, char** argv)
{
    box = Rect(-1, -1, 0, 0);
    namedWindow("video", 0);
    g_cap.open(string(argv[1]));
    int frames = (int)g_cap.get(CAP_PROP_FRAME_COUNT);
    int tmpw = (int)g_cap.get(CAP_PROP_FRAME_WIDTH);
    int tmph = (int)g_cap.get(CAP_PROP_FRAME_HEIGHT);
    float fps = g_cap.get(CAP_PROP_FPS);
    cout << "Video has " << frames << " frames of dimensions(" << tmpw << ", " << tmph << ")." << "fps :" << fps << endl;
    // createTrackbar("Position", "video", &g_slider_position, (int)(frames / fps), onTrackbarSlide);
    createTrackbar("Position", "video", &g_slider_position, frames, onTrackbarSlide);
    Mat frame, boxframe;
    setMouseCallback("video", my_mouse_callback, (void*)&frame);
    while (1) {
        if (g_run != 0) {
            g_cap >> frame;
            if (frame.empty()) {
                break;
            }
            int current_pos = (int)g_cap.get(CAP_PROP_POS_FRAMES);
            g_dontset = 1;
            setTrackbarPos("Position", "video", current_pos);
            frame.copyTo(boxframe);
            draw_box(boxframe, box);
            imshow("video", boxframe);
            delay = 0.0333667 + minite * 60;
            if ((g_cap.get(CAP_PROP_POS_MSEC) / 1000 - delay) >= second) {
                printf("%02d:%02d:%02d\n", hour, minite, second);
                second++;
                if (second == 60) {
                    second = 0;
                    minite++;
                }
                if (minite == 60) {
                    minite = 0;
                    hour++;
                }
            }
            g_run -= 1;
        }
        if (g_run == 0) {
            frame.copyTo(boxframe);
            draw_box(boxframe, box);
            imshow("video", boxframe);
        }
        char c = (char)cv::waitKey(17);
        if (c == 's') {
            g_run = 1;
            cout << "Single step, run = " << g_run << endl;
        }
        if (c == 'r') {
            g_run = -1;
            cout << "Run mode, run = " << g_run << endl;
        }
        if (c == 27 || c == 'q') {
            break;
        }
    }
    return(0);
}
