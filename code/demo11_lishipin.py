# 1. 找到链接里的 contId
# 2. 拿到 videoStatus 返回的 json -> 获取 surUrl
# 3. srcURL修整，替换成 contId
# 4. 下载视频

import requests

url = "https://www.pearvideo.com/video_1032352"
contId = url.split("_")[1]  # 1032352

videoStatusUrl = f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.1645753204645688"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36 Edg/104.0.1293.54",
    # Referer 是防盗链, 上一级请求来源, 即 videoStatusUrl 的请求来源
    "Referer": url  # "https://www.pearvideo.com/video_1032352"
}

resp = requests.get(videoStatusUrl, headers=header)
dic = resp.json()
srcUrl = dic["videoInfo"]["videos"]["srcUrl"]  # https://video.pearvideo.com/mp4/short/20170210/1660393303179-10189305-hd.mp4
systemTime = dic["systemTime"]  # 1660393303179

srcUrl = srcUrl.replace(systemTime, f"cont-{contId}")
# 真实视频地址: https://video.pearvideo.com/mp4/short/20170210/cont-1032352-10189305-hd.mp4


videoName = "200秒看懂中国各省界限怎么划分.mp4"

with open(videoName, mode="wb") as v:
    v.write(requests.get(srcUrl).content)
