ffmpeg -i $1 -c copy -map 0 -segment_time 3600 -segment_list kct_segments_$(date +%H_%M).csv -f segment $1%03d.asf
