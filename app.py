from tkinter import Tk
from tkinter.messagebox import showinfo
from tkinter.ttk import Treeview
import windnd
import readAllFile as raf
import util


window = Tk()
window.iconbitmap('./bitbug_favicon.ico')

def dragged_files(files):
    msg = '\n'.join((item.decode('gbk') for item in files))

    dirs = raf.readDir(msg)
    for path in dirs:
        util.deal_and_save(path)

    showinfo('您拖放文件是', msg)


# 设置标题

window.title('ExcelToCvs')
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
# 设置大小 widthxheightt+x+y

width = 650
height = 500
window_size = f'{width}x{height}+{round((screen_width - width) / 2)}+{round((screen_height - height) / 2)}'
window.geometry(window_size)

# 编写控件Treeview

table = Treeview(columns=('id', 'name', 'money', 'type'), show='headings')

table.column('id', width=100)

table.column('name', width=100)

table.column('money', width=100)

table.column('type', width=100)

table.heading('id', text='记录编号')

table.heading('name', text='缴费者')

table.heading('money', text='缴费金额')

table.heading('type', text='缴费类型')

# 让控件显示
table.pack()

# 让窗口运行
windnd.hook_dropfiles(window, func=dragged_files)
window.mainloop()
