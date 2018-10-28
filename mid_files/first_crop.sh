#!/bin/bash -eu

cd $1

ffmpeg -y -i video--U5SQGQl7ew.mp4 -ss 00:00:07 -to 00:00:50 video--U5SQGQl7ew_crop.mp4
rm video--U5SQGQl7ew.mp4

rm video-2OM3oqQ2RbE.mp4

ffmpeg -y -i video-4WZo39BbE3o_resize.mp4 -ss 00:07:44 -to 00:09:30 video-4WZo39BbE3o_1.mp4
ffmpeg -y -i video-4WZo39BbE3o_resize.mp4 -ss 00:09:32 -to 00:10:37 video-4WZo39BbE3o_2.mp4
ffmpeg -y -i video-4WZo39BbE3o_resize.mp4 -ss 00:11:12 -to 00:12:56 video-4WZo39BbE3o_3.mp4
ffmpeg -y -i video-4WZo39BbE3o_resize.mp4 -ss 00:12:58 -to 00:13:30 video-4WZo39BbE3o_4.mp4
rm video-4WZo39BbE3o_resize.mp4

ffmpeg -y -i video-64zoxiMu0p8_resize.mp4 -ss 00:00:16 -to 00:10:30 video-64zoxiMu0p8_1.mp4
rm video-64zoxiMu0p8_resize.mp4

ffmpeg -y -i video-F-zT2pI-lnQ_resize.mp4 -ss 00:01:35 -to 00:02:24 video-F-zT2pI-lnQ_1.mp4
ffmpeg -y -i video-F-zT2pI-lnQ_resize.mp4 -ss 00:02:25 -to 00:03:08 video-F-zT2pI-lnQ_2.mp4
rm video-F-zT2pI-lnQ_resize.mp4

ffmpeg -y -i video-FPa3kNwnNRk_resize.mp4 -ss 00:00:06 -to 00:00:54 video-FPa3kNwnNRk_1.mp4
ffmpeg -y -i video-FPa3kNwnNRk_resize.mp4 -ss 00:00:58 -to 00:01:54 video-FPa3kNwnNRk_2.mp4
ffmpeg -y -i video-FPa3kNwnNRk_resize.mp4 -ss 00:01:58 -to 00:02:14 video-FPa3kNwnNRk_3.mp4
rm video-FPa3kNwnNRk_resize.mp4

ffmpeg -y -i video-US59wO9bAv4_resize.mp4 -ss 00:00:06 -to 00:00:49 video-US59wO9bAv4_1.mp4
rm video-US59wO9bAv4_resize.mp4

ffmpeg -y -i video-Z65lGGMaSFE_resize.mp4 -ss 00:04:05 -to 00:05:08 video-Z65lGGMaSFE_1.mp4
ffmpeg -y -i video-Z65lGGMaSFE_resize.mp4 -ss 00:05:52 -to 00:06:44 video-Z65lGGMaSFE_2.mp4
rm video-Z65lGGMaSFE_resize.mp4

rm video-auHHRoN7xg4_resize.mp4
rm video-b_WbXpc8ASI_resize.mp4
rm video-sf3WSCoqdo8_resize.mp4
rm video-txjZXdu5Xiw_resize.mp4

ffmpeg -y -i video-u6dGiANdDNQ.mp4 -ss 00:00:05 -to 00:01:02 video-u6dGiANdDNQ_1.mp4
rm video-u6dGiANdDNQ.mp4

ffmpeg -y -i video-uGpFQT3Uiig_resize.mp4 -ss 00:00:06 -to 00:01:36 video-uGpFQT3Uiig_1.mp4
ffmpeg -y -i video-uGpFQT3Uiig_resize.mp4 -ss 00:01:39 -to 00:02:34 video-uGpFQT3Uiig_2.mp4
ffmpeg -y -i video-uGpFQT3Uiig_resize.mp4 -ss 00:02:37 -to 00:03:15 video-uGpFQT3Uiig_3.mp4
ffmpeg -y -i video-uGpFQT3Uiig_resize.mp4 -ss 00:03:18 -to 00:03:35 video-uGpFQT3Uiig_4.mp4
ffmpeg -y -i video-uGpFQT3Uiig_resize.mp4 -ss 00:03:39 -to 00:05:01 video-uGpFQT3Uiig_5.mp4
ffmpeg -y -i video-uGpFQT3Uiig_resize.mp4 -ss 00:05:04 -to 00:05:50 video-uGpFQT3Uiig_6.mp4
rm video-uGpFQT3Uiig_resize.mp4

ffmpeg -y -i video-yDPZ5Yrn2OI.mp4 -ss 00:00:12 -to 00:07:50 video-yDPZ5Yrn2OI_1.mp4
rm video-yDPZ5Yrn2OI.mp4

rm video-zICx1okhU0Y_resize.mp4
rm video-zj8wFJxaxVM.mp4

rm *.webm *.mkv
