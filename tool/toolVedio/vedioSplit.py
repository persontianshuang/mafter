from pydub import AudioSegment
import os, re

# mp3 = AudioSegment.from_mp3('./29593856.mp3') # 打开mp3文件
# mp3[14*1000-500:24*1000+500].export('./2.mp3', format="mp3") # 切割前17.5秒并覆盖保存


mp4_version = AudioSegment.from_file("/Users/user/language/sp/lr/2-01.mp4", "mp4")
mp4_version[:10000].export('/Users/user/language/sp/lr/2.mp4')
