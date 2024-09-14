# This Python file uses the following encoding: utf-8
import sys
import numpy as np
import cv2
from ultralytics import YOLO
import torch
import time
import pyautogui
import requests
import multiprocessing
from PySide6.QtCore import QTimer
from PySide6.QtGui import QImage, QPixmap
from PySide6.QtWidgets import QApplication, QMainWindow
# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow


# 流媒体服务器的地址

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()  # 实例化Ui_MainWindow类
        self.ui.setupUi(self)  # 设置UI界面
        self.device = torch.device('cuda:0' if torch.cuda.is_available() else 'cpu')  # 根据是否有CUDA设备选择运行设备
        print('device:',self.device)  # 打印当前使用的设备

        self.yolo = YOLO("./best.pt",task="detect")

        self.isopencam = False  # 初始化相机未打开的状态
        self.isstartcheck = False  # 初始化检测未开始的状态

        self.ui.connectcam.clicked.connect(self.Connectcam)
        self.ui.startcheck.clicked.connect(self.Starcheck)
        self.ui.confslider.valueChanged.connect(self.Confchange)
        self.ui.urlon.clicked.connect(self.Urlon)
        self.idfconf = 20
        self.urlkey = False
        self.server_url = '127.0.0.1:5050/receive'

    def Connectcam(self):
        if self.isopencam ==  False:
            cam_address_text = self.ui.cam_address.text()
            if cam_address_text.isdigit():
                self.camaddress = int(cam_address_text)
            else:
                # 如果输入的不是纯数字，则保持为字符串类型
                self.camaddress = str(cam_address_text)

            self.ui.camlabel.setText('链接中......')
            
            QApplication.processEvents()
            if(self.camaddress == 'screen'):
                self.screen_width, self.screen_height = pyautogui.size()
            else:
                self.cap = cv2.VideoCapture(self.camaddress)
            # 创建一个 QTimer 定时器用于更新图像
            self.timer = QTimer(self)
            self.timer.setInterval(30)  # 每 100 毫秒更新一次图像
            self.timer.timeout.connect(self.Updataframe)
            self.ui.warningtext.append("相机已连接")

            self.ui.cam_address.setEnabled(False)
            # 启动定时器
            self.timer.start()

    def Urlon(self):
        if self.urlkey == False:
            self.server_url = self.ui.url_address.text()
            self.urlkey = True
            self.ui.urlon.setText('关闭url')
        else:
            self.server_url = self.ui.url_address.text()
            self.urlkey = False            
            self.ui.urlon.setText('上传url')

    
    def Updataframe(self):
        # 读取图像
        if(self.camaddress == 'screen'):
            x1, y1, width, height = 200, 200, 600, 400
            x2, y2 = x1 + width, y1 + height
            screenshot = pyautogui.screenshot(region=(x1, y1, x2, y2))
            # 将截取的图像转换为OpenCV格式
            screenshot_np = np.array(screenshot)
            image = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2BGR)
        else:
            ret,image = self.cap.read()
            if not ret:
                self.timer.stop()
        #处理
        if self.isstartcheck == True:
            result_pic = self.Idfbottle(image)
            result = cv2.cvtColor(result_pic, cv2.COLOR_BGR2RGB)
        else:
            result = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        if self.urlkey ==True:
            # 将图像编码为JPEG格式
            _, img_encoded = cv2.imencode('.jpg', result)
            
            # 将图像发送到流媒体服务器
            try:
                response = requests.post(self.server_url, files={'file': img_encoded.tostring()})
                if response.status_code != 200:
                    print(f"Error: Failed to send frame. Status code: {response.status_code}")
            except requests.exceptions.RequestException as e:
                print(f"Error: {e}")


        # 将图像转换为 QImage 格式
        result = cv2.resize(result,(800,600))
        qimage = QImage(result.data, result.shape[1], result.shape[0], QImage.Format_RGB888).scaled(self.ui.camlabel.size())
        # 将 QImage 显示在 QLabel 上
        self.ui.camlabel.setPixmap(QPixmap.fromImage(qimage))


    def Starcheck(self):
        if self.isstartcheck == False:
            self.isstartcheck = True
            self.ui.startcheck.setText('停止检测')
        else:
            self.isstartcheck = False
            self.ui.startcheck.setText('开始检测')

    def Confchange(self,value):
        self.idfconf = value
        self.ui.conflabel.setText(f'置信度：{value}%')

    def Idfbottle(self,image):
        # 预测目标
        prev_time = time.time()
        result = self.yolo(image,conf=(self.idfconf*0.01))
        
        bottle_results = []
        
        for detection in result[0].boxes.data:
            # print(detection[5])
            if detection[5] == 0:  # 瓶子
                bottle_results.append(detection)
            

        for detection in bottle_results:
            # print(detection[0])
            cv2.rectangle(image, (int(detection[0]), int(detection[1])), (int(detection[2]), int(detection[3])), (255, 0, 0), 2)
            cv2.putText(image, f"bottle:{np.around(float(detection[4]),3)}", (int(detection[0]), int(detection[1]) - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 0, 0), 2)


        bottlenum = len(bottle_results)
        self.ui.statistc.setText(f'水瓶数:{bottlenum}')

        if self.ui.whichcheck.currentIndex() > 0:
            self.Warning(image,bottlenum)

        current_time = time.time()
        fps = 1 / (current_time - prev_time)
        self.prev_time = current_time
        cv2.putText(image, f"FPS: {np.around(fps, 1)}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        return image

    def Warning(self, image, bottlenum):
        """
        根据预警设置进行预警，并保存预警图像

        Args:
            image: 当前图像帧
            peoplenum: 检测到的人数
            bussnum: 检测到的大巴车数
        """

        # 获取预警阈值
        waringnum = int(self.ui.warningnum.text())  # 从UI界面获取预警值

        # 如果预警阈值为0，则不进行预警
        if waringnum == 0:
            return

        # 判断预警类型
        if self.ui.whichcheck.currentIndex() == 1:  # 人数预警
            if bottlenum > waringnum:
                self.ui.warningtext.append(f'人数预警：当前数量{bottlenum}')  # 在UI界面上显示预警信息

                # 保存预警图像
                localtime = time.localtime()  # 获取本地时间
                formatted_time = time.strftime("%Y_%m_%d_%H%M%S", localtime)  # 格式化时间为文件名
                cv2.imwrite(f'./image/image{formatted_time}.png', image)  # 保存图像

                self.iswarninged = True  # 设置预警标志
        else:
            return  # 其他情况不进行预警



if __name__ == "__main__":
    multiprocessing.freeze_support()
    app = QApplication(sys.argv)
    widget = MainWindow()
    widget.show()
    sys.exit(app.exec())
