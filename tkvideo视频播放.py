import tkinter as tk
from tkvideo import tkvideo

# 创建窗口
window = tk.Tk()
window.title("视频播放器")

# 创建视频标签
video_label = tk.Label(window)
video_label.pack()

# 加载并播放视频
player = tkvideo(r"C:\Users\Administrator\Desktop\进阶\最后成品.mp4", video_label, 
               loop=1,      # 循环播放
               size=(640, 480))  # 显示尺寸
#视频播放倍数在0.5倍，播放慢，可以播放简短视频以至于看清细节
#结构简单，视频播放没有声音
player.play()

window.mainloop()