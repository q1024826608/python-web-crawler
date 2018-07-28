# -*- coding=utf-8 -*-
# author__ = 'nuagevoler'

import tkinter as tk
from tkinter import ttk
from tkinter import scrolledtext
from tkinter import Spinbox
from tkinter import messagebox as mBox
import tkinter.filedialog
import bs4tool
import savefile
import urllib.request

keyword = "某科学的超电磁炮"
baseurl = 'http://tieba.baidu.com/f?kw=KEYWORD&ie=utf-8&pn='
childbaseurl = 'http://tieba.baidu.com'
count = 0
endnum = 500
text = ''
# 选择文件


def select_file():
    filename = tkinter.filedialog.askopenfilename()
    if filename != '':
        print("您选择的文件是："+filename)
    else:
        print("您选择的文件为空")
# 选择路径


def select_path():
    filename = tkinter.filedialog.askdirectory()
    if filename != '':
        print("您选择的路径是："+filename)
        return filename
    else:
        print("您选择的路径为空")
        return ".."

# 添加菜单


def addmenu(root):
    menuBar = tk.Menu(root)  # 1
    root.config(menu=menuBar)
    fileMenu = tk.Menu(menuBar, tearoff=0)  # 2
    fileMenu.add_command(label="新建")
    fileMenu.add_separator()  # 4
    fileMenu.add_command(label="退出", command=_quit)
    # Add menu items
    menuBar.add_cascade(label="文件", menu=fileMenu)
    helpMenu = tk.Menu(menuBar, tearoff=0)  # 6
    helpMenu.add_command(label="关于", command=_msgBox)
    menuBar.add_cascade(label="帮助", menu=helpMenu)

# Display a Message Box
# Callback function


def _msgBox():
    mBox.showinfo("提示", "吧名不可为空!")
    # mBox.showwarning('Python Message Warning Box',
    # 'A Python GUIcreated using tkinter:\nWarning: There might be a bug in this code.')
    # mBox.showerror('Python Message Error Box',
    # 'A Python GUI created using tkinter:\nError: Houston ~ we DO have a serious PROBLEM!')

# Display a Message Box with Yes and no


def _msgBoxYN():
    answer = mBox.askyesno("Python Message Dual Choice Box",
                           "Are you sure you really wish to do this?")
    print(answer)


def _quit():  # 7
    root.quit()
    root.destroy()
    exit()


class Application(ttk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.baseurl = tk.StringVar()
        self.baseurl.set(keyword)
        self.endnum = tk.StringVar()
        self.endnum.set(endnum)
        self.pack()
        self.create_widgets()

    def create_widgets(self):               # 创建窗体
        # topfream
        self.topfream = ttk.Frame(self)
        self.label_title = ttk.Label(self.topfream, text="python百度贴吧爬虫工具")
        self.label_title.pack(side="top")
        self.topfream.pack(side="top")

        # centerframe
        self.centerframe = ttk.Frame(self)
        self.label_baseurl = ttk.Label(self.centerframe, text="贴吧名:")
        self.label_baseurl.grid(row=0, column=0, padx=3)
        self.label_num = ttk.Label(self.centerframe, text="帖子数:")
        self.label_num.grid(row=1, column=0, padx=3)
        self.entry_baseurl = ttk.Entry(
            self.centerframe, textvariable=self.baseurl)
        # self.entry_baseurl.pack(side="left",expand="yes",fill="x",padx=5)
        self.entry_baseurl.grid(row=0, column=1, padx=3)
        self.entry_num = tk.Scale(self.centerframe, orient="horizontal",
                                  resolution=50, length=150, from_=50, to=1000, variable=self.endnum)
        # self.entry_num = tk.Spinbox(self.centerframe,from_ = 50,to = 1000,increment = 50)
        # self.entry_baseurl.pack(side="left",expand="yes",fill="x",padx=5)
        self.entry_num.grid(row=1, column=1, padx=3)
        self.centerframe.pack(side="top", expand="yes", fill="both")
        # centerframe end

        # footerfram
        self.footerfram = ttk.Frame(self)
        self.footerfram.pack(side="bottom", expand="yes", fill="both")

        self.showtext = ttk.Label(self.footerfram, width=30)
        self.showtext.pack_forget()

        self.progresbarfram = ttk.Frame(self.footerfram)
        self.progresbarfram.pack(side="top")
        self.progresbar = ttk.Progressbar(
            self.progresbarfram, length=200, maximum=50)
        self.progresbar.pack_forget()

        self.btn_submit = ttk.Button(self.footerfram, text="开始")
        self.btn_submit["command"] = self.start_spider
        self.btn_submit.pack(side="top", expand="yes",
                             fill="both", padx=5, pady=5)

        # self.btn_selfile = tk.Button(self.footerfram,text="test")
        # self.btn_selfile["command"] = self.selectpath
        # self.btn_selfile.pack(side="top",expand="yes",fill="both",padx=5,pady=5)
        # footerfram end
    def selectpath(self):
        # select_path()
        print(self.entry_num.get())

    def start_spider(self):
        # print("开始爬取内容!")
        savepath = select_path()
        entytext = self.entry_baseurl.get()
        if entytext == "":
            _msgBox()
        # print(" 输入内容为： " + entytext)
        self.progresbar.config(maximum=int(self.entry_num.get()))
        self.progresbar.pack()
        urlbase = baseurl.replace("KEYWORD", urllib.request.quote(entytext))
        count = 0
        barvalue = 0
        endnum = int(self.entry_num.get())
        while count < endnum:
            # 获取链接
            text = bs4tool.geturls(urlbase, count)
            count = count + 50
            urls = text.split('\n')
            self.progresbar.config(value=barvalue)
            self.progresbar.update()
            for url in urls:
                # 链接为空
                if url == '':
                    continue
                filename = url.split("\t")[0].replace(
                    '/', '')+'_'+url.split('\t')[1]
                # 设置存储文件名,去掉非法字符
                filename = filename.replace('?', '').replace(
                    '=', '')
                # 帖子链接地址
                url = childbaseurl + url.split("\t")[0]
                print(url+' -> start download ')
                # res = bs4tool.gettext(url)    # 格式化内容
                # 获取内容
                res = bs4tool.gethtml(url)
                # 保存内容
                savefile.SaveFile(res, savepath+"/"+filename+'.html').save()
                # 更新进度条
                barvalue = barvalue + 1
                self.progresbar.config(value=barvalue)
                self.progresbar.update()
        self.progresbar.config(value=endnum)
        self.progresbar.update()


root = tk.Tk()
# 修改窗体图标
# root.iconbitmap(r'C:\Python27\DLLs\pyc.ico')
# 添加菜单栏
addmenu(root)
# 初始化窗体
app = Application(master=root)
# 设值标题
app.master.title("python spider tool")
# 设值窗体大小
# app.master.minsize(400, 400)
app.mainloop()
