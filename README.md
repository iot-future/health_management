树莓派

```bash


ffmpeg -re -i /dev/video0 -vcodec libx264 -preset:v ultrafast -tune:v zerolatency  -rtsp_transport tcp -f rtsp rtsp://192.168.137.1:8554/live/STREAMNAME
```

pc机

```bash
sudo coffee server.coffee
```

```bash
python deploy/pipeline/pipeline.py --config deploy/pipeline/config/examples/infer_cfg_fall_down.yml --video_file=demo/fall_video.mp4 --device=gpu --pushurl rtsp://172.0.0.1:8554

python deploy/pipeline/pipeline.py --config deploy/pipeline/config/infer_cfg_pphuman.yml -o visual=False --rtsp 

python deploy/pipeline/pipeline.py --config deploy/pipeline/config/examples/infer_cfg_fall_down.yml --rtsp rtsp://192.168.137.1:8554/live/STREAMNAME --device=gpu --pushurl rtsp://172.0.0.1:8554

```

web端rtsp拉流

```bash
npm install ws

cd jsmpeg 

node websocket-relay.js supersecret 8081 8082

ffmpeg -i rtsp://192.168.137.1:8554/live/STREAMNAME  -q 0 -f mpegts -codec:v mpeg1video -s 800x600 http://127.0.0.1:8081/supersecret

ffmpeg -i rtsp://192.168.137.1:8554/aaaa  -q 0 -f mpegts -codec:v mpeg1video -s 800x600 http://127.0.0.1:8081/supersecret

rtsp://192.168.137.1:8554/aaaa
ffmpeg -i rtsp://192.168.137.1:8554/aaaa  -q 0 -f mpegts -codec:v mpeg1video -s 800x600 http://127.0.0.1:8081/supersecret
```

