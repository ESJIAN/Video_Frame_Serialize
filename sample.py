import cv2 as cv

# 打开视频文件
cap = cv.VideoCapture("C:\\Users\\鑫宇韩\\Downloads\\output.mp4")

frame_count = 0  # 初始化帧计数器,方便后续命名

while cap.isOpened():
    # 一帧一帧捕捉
    ret, frame = cap.read()
    if ret:
        # 将帧转换为灰度图像（如果需要彩色图像，这一步可以省略）
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # 构建保存的图片文件名，例如 output_0001.jpg, output_0002.jpg 等
        img_name = f'E:\\output\\outimage{frame_count:04d}.jpeg'
        # 路径中最好不要存在中文名
        # 保存当前帧为图片
        try:
            # 能识别img_name字符串中的路径，并且按相应文件名字创建文件
            cv.imwrite(img_name, gray)
        except Exception as e:
            print(f"保存图片时出错: {e}")
            break

        # 显示灰度图像（可选，为了查看过程）
        cv.imshow('frame', gray)

        # 按q键退出循环，仅仅在创建窗口时候才成立
        if cv.waitKey(5) & 0xFF == ord('q'):
            break
        # 如果你此时仅仅是关闭任务窗口，仅仅是关闭一次循环同时创建的窗口任务
        frame_count += 1  # 帧计数器加1
    else:
        break  # 如果读取帧失败，也跳出循环

# 释放资源
cap.release()
cv.destroyAllWindows()
