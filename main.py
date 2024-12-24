import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtMultimediaWidgets import QVideoWidget
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent
from PyQt5.QtCore import QUrl

# 创建主窗口类
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # 设置窗口标题和尺寸
        self.setWindowTitle("动态背景窗口")
        self.setGeometry(100, 100, 800, 600)

        # 添加视频背景
        self.init_video_background()

    def init_video_background(self):
        # 视频显示控件
        video_widget = QVideoWidget(self)
        video_widget.setGeometry(0, 0, self.width(), self.height())  # 视频覆盖整个窗口
        self.setCentralWidget(video_widget)  # 设置为主内容

        # 视频播放器
        self.media_player = QMediaPlayer(None, QMediaPlayer.VideoSurface)
        self.media_player.setVideoOutput(video_widget)

        # 加载视频
        video_path = "video.mp4"  # 替换为你的视频文件路径
        video_url = QUrl.fromLocalFile(video_path)
        self.media_player.setMedia(QMediaContent(video_url))

        # 自动播放视频
        self.media_player.play()

# 主程序入口
if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
