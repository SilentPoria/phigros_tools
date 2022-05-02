import tkinter as tk
from tkinter import  messagebox
from tkinter import filedialog
import csv,threading,time
import sys,zipfile,os,shutil
import tkinter.filedialog,tkinter.messagebox
import zipfile
def main():
    global e0, e1, e2, e3, e4, e5, e6, e7, e8, e9, e10
    #主体
    app = tk.Tk()
    app.title("autoCsv 2.0")
    app.resizable(width=False, height=False)
    app.geometry('800x750')
    app.attributes('-alpha', 1)
    background_label = tk.Label(app,)
    background_label.place(x=0, y=0, relwidth=1, relheight=1)
    #进度文本框
    txt = tk.Text(app, relief="ridge", bd=8, fg="Black", font=("黑体", 12), bg="#FFE4E1")
    txt.place(x=380, y=10, relwidth=0.50, relheight=0.9)
    #标签
    l0 = tk.Label(app, text="保存路径：", )
    l0.place(x=50, y=80, relwidth=0.17, relheight=0.06)
    l1 = tk.Label(app,text="Chart谱面文件(含后缀)：",)
    l1.place(x=50,y=80,relwidth=0.17,relheight=0.06)
    l2 = tk.Label(app, text="Music音乐文件(含后缀)：",)
    l2.place(x=50, y=140, relwidth=0.17, relheight=0.06)
    l3 = tk.Label(app, text="Image图片文件(含后缀)：",)
    l3.place(x=50, y=200, relwidth=0.17, relheight=0.06)
    l4 = tk.Label(app, text="AspectRatio宽高比：",)
    l4.place(x=50, y=260, relwidth=0.17, relheight=0.06)
    l5 = tk.Label(app, text="ScaleRatio按键大小：",)
    l5.place(x=50, y=320, relwidth=0.17, relheight=0.06)
    l6 = tk.Label(app, text="GlobalAlpha背景透明度：", )
    l6.place(x=50, y=380, relwidth=0.17, relheight=0.06)
    l7 = tk.Label(app, text="Name名字：", )
    l7.place(x=50, y=440, relwidth=0.17, relheight=0.06)
    l8 = tk.Label(app, text="Level等级：", )
    l8.place(x=50, y=500, relwidth=0.17, relheight=0.06)
    l9 = tk.Label(app, text="Illustrator曲绘作者：", )
    l9.place(x=50, y=560, relwidth=0.17, relheight=0.06)
    l10 = tk.Label(app, text="Designer谱师：", )
    l10.place(x=50, y=620, relwidth=0.17, relheight=0.06)
    #输入框
    e0 = tk.Entry(app, bg="white", font=("黑体", 12), fg="Black", relief="flat")
    e0.place(x=200, y=20, relwidth=0.20, relheight=0.06)
    e1 = tk.Entry(app, bg="white", font=("黑体", 12), fg="Black", relief="flat")
    e1.place(x=200, y=80, relwidth=0.20, relheight=0.06)
    e2 = tk.Entry(app, bg="white", font=("黑体", 12), fg="Black", relief="flat")
    e2.place(x=200, y=140, relwidth=0.20, relheight=0.06)
    e3 = tk.Entry(app, bg="white", font=("黑体", 12), fg="Black", relief="flat")
    e3.place(x=200, y=200, relwidth=0.20, relheight=0.05)
    e4 = tk.Entry(app, bg="white", font=("黑体", 12), fg="Black", relief="flat")
    e4.place(x=200, y=260, relwidth=0.20, relheight=0.05)
    e5 = tk.Entry(app, bg="white", font=("黑体", 12), fg="Black", relief="flat")
    e5.place(x=200, y=320, relwidth=0.20, relheight=0.05)
    e6 = tk.Entry(app, bg="white", font=("黑体", 12), fg="Black", relief="flat")
    e6.place(x=200, y=380, relwidth=0.20, relheight=0.05)
    e7 = tk.Entry(app, bg="white", font=("黑体", 12), fg="Black", relief="flat")
    e7.place(x=200, y=440, relwidth=0.20, relheight=0.05)
    e8 = tk.Entry(app, bg="white", font=("黑体", 12), fg="Black", relief="flat")
    e8.place(x=200, y=500, relwidth=0.20, relheight=0.05)
    e9 = tk.Entry(app, bg="white", font=("黑体", 12), fg="Black", relief="flat")
    e9.place(x=200, y=560, relwidth=0.20, relheight=0.05)
    e10 = tk.Entry(app, bg="white", font=("黑体", 12), fg="Black", relief="flat")
    e10.place(x=200, y=620, relwidth=0.20, relheight=0.05)
    def unzip_file(zip_src):
        # 解压后存储到temp
        dst_dir = './temp'
        r = zipfile.is_zipfile(zip_src)
        if r:
            fz = zipfile.ZipFile(zip_src, 'r')
            for file in fz.namelist():
                fz.extract(file, dst_dir)
            return True
        else:
            return False
    def open_zip():
        global file
        # 删除残留temp
        try:
            shutil.rmtree('./temp')
        except:
            pass
        # 选择zip
        file = tkinter.filedialog.askopenfilename()
        # 创建temp文件夹
        os.mkdir('./temp')
        # 解压zip
        if unzip_file(file):
            return True
        else:
            return False
    # 文件名识别
    def class_file(filenames):
        state = False
        for filename in filenames:
            print(filenames)
            cF = filename.split('.')[-1]
            print(cF)
            if cF == 'txt':
                print(filenames[-1])
                state = True
        if state:
            read_txt(filenames[-1])
            return state
        else:
            messagebox.showwarning('warning','zip没有txt')
            return state
    def zip(file):
        zipfile_name = os.path.basename(file) + '.zip'
        with zipfile.ZipFile(zipfile_name, 'w') as zfile:
            for foldername, subfolders, files in os.walk(file):
                fpath = foldername.replace(file, '')
                if file == foldername:
                    for i in files:
                        zfile.write(os.path.join(foldername, i), os.path.join(fpath, i))
                        continue
                        zfile.write(foldername, fpath)
                        for i in files:
                            zfile.write(os.path.join(foldername, i), os.path.join(fpath, i))
            zfile.close()
    def read_temp():
        if open_zip():
            filenames = os.listdir('./temp')
            if class_file(filenames):
                e0.delete(0, len(e0.get()))
                e0.insert('insert', './temp/')
                thread_it(edit_name)

    def read_txt(txt=None):
        if txt == None:
            txtr = filedialog.askopenfilename(filetypes =[('txt', '.txt')])
        else:
            txtr = './temp/'+str(txt)
        f = open(txtr,mode='r',encoding='utf-8')
        read_contect = f.readlines()
        for i in read_contect:
            a = i.split('\n')[0].split(':')
            print(a)
            if a[0] == 'Name':
                e7.select_clear
                e7.insert(0, a[1])
            elif a[0] == 'Song':
                e2.select_clear
                e2.insert(0, a[1])
            elif a[0] == 'Picture':
                e3.select_clear
                e3.insert(0, a[1])
            elif a[0] == 'Chart':
                e1.select_clear
                e1.insert(0, a[1])
            elif a[0] == 'Level':
                e8.select_clear
                e8.insert(0, a[1])
            elif a[0] == 'Composer':
                e9.select_clear
                e9.insert(0, a[1])
            elif a[0] == 'Charter':
                e10.select_clear
                e10.insert(0, a[1])
        f.close()
    def info_csv():
        filepath = filedialog.askdirectory()
        e0.insert('insert',filepath)
    def get_result():
        result_list=['None','None','None','1.777778','8e3','0.6','Untitled','SP Lv.?','nameless','namless']
        list = []
        for i in range(0, 11):
            temp = 'e%s' % str(i) + '.get()'
            get_e = eval(temp)
            if len(get_e) == 0:
                if i == 0:
                    messagebox.showerror("警告", """出错啦，请检查路径是否正确！""")
                    break
                else:
                    get_e = result_list[i-1]
                list.append(get_e)
            else:
                list.append(get_e)
        return list
    def edit_name(event=None):
        list = []
        try:
            e_ct = get_result()
            path = e_ct[0]
            # 给文本框写入内容，第一个参数是位置参数，1代表第一行，0代表第几个字符，第二个参数是内容
            txt.insert('1.0',"\t\t=====执行进度区=====\n\n")
            txt.insert('2.0', "*" * 42)
            # 提示框
            txt.insert('3.0', "Chart谱面文件：%s \n" % e_ct[1])
            txt.insert('4.0', "Music音乐:%s \n" % e_ct[2])
            txt.insert('5.0', "Image图片:%s \n" % e_ct[3])
            txt.insert('6.0', "AspectRatio宽高比:%s \n" % e_ct[4])
            txt.insert('7.0', "ScaleRatio按键大小:%s\n" % e_ct[5])
            txt.insert('8.0', "GlobalAlpha背景透明度:%s\n" % e_ct[6])
            txt.insert('9.0', "Name名字:%s \n" % e_ct[7])
            txt.insert('10.0', "Level等级:%s \n" % e_ct[8])
            txt.insert('11.0', "Illustrator曲绘:%s \n" % e_ct[9])
            txt.insert('12.0', "Designer谱师:%s \n" % e_ct[10])
            txt.insert('13.0', '-' * 48)
            txt.insert('14.0', "开始处理数据：-- %s\n" % time.ctime())
            txt.insert('15.0', '-' * 48)
            time.sleep(1)
            write_csv(e_ct)
            txt.insert('16.0', "info.csv文件已经输出到%s\n" % path)
            txt.insert('17.0', '-' * 48)
            txt.insert('18.0', "处理数据完成：-- %s\n" % time.ctime())
            txt.insert('19.0', '-' * 48)
            txt.insert('20.0', "打包数据ing：-- %s\n" % time.ctime())
            txt.insert('21.0', '-' * 48)
            zip('temp')
            txt.insert('22.0', "打包数据完成：-- %s\n" % time.ctime())
            txt.insert('23.0', '-' * 48)
            try:
                shutil.rmtree('./temp')
            except:
                pass
        except NameError:
            messagebox.showerror("警告", """出错啦，请检查日志文件！""")
    def write_csv(list):
        basic = ['Chart','Music','Image','AspectRatio','ScaleRatio','GlobalAlpha','Name','Level','Illustrator','Designer']
        path = str(list[0]+'/info.csv')
        list.pop(0)
        f = open(path,'w',encoding='utf-8')
        csv_writer = csv.writer(f)
        csv_writer.writerow(basic)
        csv_writer.writerow(list)
        f.close()
    def thread_it(func, *args):
        txt.delete("1.0", "20.0")
        t = threading.Thread(target=func,args=args)
        t.setDaemon(True)
        t.start()
    def thread_zip(func, *args):

        t = threading.Thread(target=func, args=args)
        t.setDaemon(True)
        t.start()

    def about_version():
        messagebox.showwarning('about','1.本软件仅供学习，技术交流。请勿用于非法用途，否则后果自负！\n 2.作者：UnicornTrue b站 UID 498761895 \n 3.本程序基于python编写')
    # 运行按钮
    b1 = tk.Button(app, text="点击执行", bg="#B2DFEE", fg="red", command=lambda :thread_it(edit_name))
    b1.place(x=50, y=680, relwidth=0.20, relheight=0.05)
    # 文件选择
    b0 = tk.Button(app, text="选择保存路径", command=info_csv)
    b0.place(x=50, y=20, relwidth=0.16, relheight=0.05)
    # 增加菜单栏
    menu_bar = tk.Menu(app)
    # 绑定主菜单栏
    menu_bar.add_cascade(label='About', command=about_version)
    menu_bar.add_cascade(label='read_txt', command=read_txt)
    menu_bar.add_cascade(label='read_zip', command=read_temp)
    app['menu'] = menu_bar
    #提示
    txt.insert('1.0', "\t\t=====使用指南=====\n\n")
    txt.insert('2.0', "*" * 42)
    txt.insert('3.0',' |属性|\t\t|说明|\n')
    txt.insert('4.0', '|Chart      ||谱面(zip文件内完整路径)|\n')
    txt.insert('5.0', '|Music      ||音乐(zip文件内完整路径)|\n')
    txt.insert('6.0', '|Image      ||图片(zip文件内完整路径)|\n')
    txt.insert('7.0', '|AspectRatio||宽高比|\n')
    txt.insert('8.0', '|ScaleRatio ||按键缩放(默认8e3)|\n')
    txt.insert('9.0', '|GlobalAlpha||背景变暗(背景不透明度，默认0.6)|\n')
    txt.insert('10.0', '|Name       ||名称|\n')
    txt.insert('11.0', '|Level      ||等级|\n')
    txt.insert('12.0', '|Illustrator||曲绘|\n')
    txt.insert('13.0', '|Designer   ||谱师|\n')
    txt.insert('14.0', '|菜单栏read_txt读取rpe生成的txt自动填写csv|\n')
    txt.insert('15.0', '|菜单栏read_zip读取txt填写csv并打包|\n')
    txt.insert('16.0', "*" * 42)
    # 保持窗口刷新
    app.mainloop()
main()