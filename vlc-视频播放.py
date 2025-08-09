import tkinter as tk
import vlc

class VLCPlayer:
  def __init__(self, window, video_path):
      self.window = window
      window.title("VLC播放器")

      # 创建VLC实例
      self.instance = vlc.Instance()
      self.player = self.instance.media_player_new()

      # 创建视频帧容器
      self.frame = tk.Frame(window, width=800, height=600)
      self.frame.pack()

      # 获取窗口ID
      self.win_id = self.frame.winfo_id()
      self.player.set_hwnd(self.win_id)

      # 加载视频
      media = self.instance.media_new(video_path)
      self.player.set_media(media)
      self.player.play()

      # 添加控制按钮
      self.btn_stop = tk.Button(window, text="重置", command=self.stop)
      self.btn_stop1 = tk.Button(window, text="开始", command=self.start)
      self.btn_stop.pack(side=tk.LEFT)
      self.btn_stop1.pack(side=tk.RIGHT)

  def stop(self):
      self.player.stop()
  def start(self):
        if not self.player.is_playing():
            self.player.play()

# 使用示例
if __name__ == "__main__":#区分代码是被直接运行还是被导入到其他模块中  
#在这个条件块内的代码，只有当模块被直接运行时才会执行；如果模块被导入（__name__ ！= "__main__"），这部分代码不会执行
#当模块被导入时：__name__ == "模块文件名"
  root = tk.Tk()
  player = VLCPlayer(root,r"C:\Users\Administrator\Desktop\进阶\最后成品.mp4")
  root.mainloop()