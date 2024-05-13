import cv2 as cv

# 打开视频文件
video_path = "C:\\Users\\ESJIA\\Downloads\\bad.m4s"
cap = cv.VideoCapture(video_path)


def save_progress(frame_count):
    """保存处理进度到文件"""
    with open(r'E:\output\progres.txt', "w") as f:
        f.write(str(frame_count))


def load_progress():
    """加载之前的处理进度"""
    try:
        with open(r'E:\output\progres.txt', "r") as f:
            return int(f.read()) #由于仅仅存放数字字符所以可以直接使用int()函数转换字符类型为数值类型
    except FileNotFoundError:
        return 0  # 如果文件不存在，返回0开始处理


def get_total_frames(video_path):  #获取视频总帧数
    # 创建一个VideoCapture对象
    cap2 = cv.VideoCapture(video_path)
    # 检查是否成功打开视频文件
    if not cap2.isOpened():
        print("Error opening video file")
        exit()
    # 获取视频的总帧数
    total_frames = int(cap2.get(cv.CAP_PROP_FRAME_COUNT))
    # 释放VideoCapture对象
    cap2.release()
    return total_frames


total_frames = get_total_frames(video_path)  # 获取视频总帧数
frame_count = load_progress()  # 初始化帧计数器，读取进度文件progress.txt中的数字判断是否延续上次结束的任务
cap.set(cv.CAP_PROP_POS_FRAMES, frame_count)  # 新增: 直接跳转到指定帧

while cap.isOpened():
    # 一帧一帧捕捉
    ret, frame = cap.read()
    if ret:
        # 将帧转换为灰度图像（如果需要彩色图像，这一步可以省略）
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # 构建保存的图片文件名，例如 output_0001.jpg, output_0002.jpg 等
        img_name = r'E:\output\outimage{frame_count:04d}.jpeg'
        # 此字符串若不包括绝对路径名则在项目下的相对路径创建文件
        # 路径中最好不要存在中文名
        # 保存当前帧为图片
        try:
            # 能识别img_name字符串中的路径，并且按相应文件名字创建文件
            cv.imwrite(img_name, gray)
            #若存在对应文件则覆盖对应文件
        except Exception as e:
            print(f"保存图片时出错: {e}")
            break

        # 显示灰度图像（可选，为了查看过程）
        cv.imshow('bacut', gray)
        save_progress(frame_count)
        print(f'图片处理进度:{frame_count / total_frames * 100:.2f}%')

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

#继续实现断点继且切割的功能

