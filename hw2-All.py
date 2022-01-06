from os import close
import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt


from numpy.core.fromnumeric import shape
from tkinter import Tk
from PIL import Image
from PIL import ImageTk
from tkinter import filedialog
from tkinter import Menu
from tkinter import Label

# tkinter


def openMenuItemClicked():
    global path, label
    path = filedialog.askopenfilename(
        filetypes=[('jpeg', '*.jpg'), ('png', '*.png'), ('all files', '*.*')])  # เรียกไฟล์

    if len(path) > 0:  # อ่านภาพได้ไหม?

        imag = cv.imread(path, cv.IMREAD_COLOR)  # อ่านภาพมาแล้ว
        # Resize
        scale_percent = 15
        width = int(imag.shape[1] * scale_percent / 100)
        height = int(imag.shape[0] * scale_percent / 100)
        imag = (width, height)

        imag = cv.resize(img, imag)
        imag = cv.cvtColor(imag, cv.COLOR_BGR2RGB)  # ปรับภาพเป็น RGB
        # ปรับให้เป็น fromarray image เพราะภาพต้นฉบับเป็นตัวเลข(math)
        imag = Image.fromarray(imag)
        imag = ImageTk.PhotoImage(imag)  # ปรับเป็น PhotoImageimage
        if label is None:
            label = Label(image=imag)
            label.image = imag
            label.pack()  # ทำการ pack

        else:
            label.configure(image=imag)
            label.image = imag
    pass


def exitMenuItemClicked():
    pass


def invertMenuItemClicked():
    global pathA, label
    pathA = cv.imread(path, cv.IMREAD_COLOR)  # อ่านภาพมาแล้ว

    pathA = Image_Inversion(pathA)

    

    if label is True:
        label = Label(image=pathA)
        label.image = pathA
        label.pack()  # ทำการ pack

    else:
        label.configure(image=pathA)
        label.image = pathA
    pass


def Image_Inversion(pathA):
    global img5, width, height, type

    img5 = pathA
    width, height, type = img5.shape
    for y in range(0, height):
        for x in range(0, width):

            img5[x, y][0] = (255-img5[x, y][0])
            img5[x, y][1] = (255-img5[x, y][1])
            img5[x, y][2] = (255-img5[x, y][2])

    img5 = cv.cvtColor(img5, cv.COLOR_BGR2RGB)  # ปรับภาพเป็น RGB
    # ปรับให้เป็น fromarray image เพราะภาพต้นฉบับเป็นตัวเลข(math)
    img5 = Image.fromarray(img5)
    img5 = ImageTk.PhotoImage(img5)  # ปรับเป็น PhotoImage
    return img5


def SepiaMenuItemClicked():
    global pathA, label
    pathA = cv.imread(path, cv.IMREAD_COLOR)  # อ่านภาพมาแล้ว
    pathA = Image_Sepia(pathA) # ส่ง

    

    if label is True:
        label = Label(image=pathA)
        label.image = pathA
        label.pack()  # ทำการ pack

    else:
        label.configure(image=pathA)
        label.image = pathA
    pass


def Image_Sepia(pathA):
    global img5, width, height, type

    img5 = pathA
    width, height, type = img5.shape
    for y in range(0, height):
        for x in range(0, width):
            R = (0.393 * img5[x, y][0] + 0.769 *img5[x, y][1] + 0.189*img5[x, y][2])
            G = (0.349*img5[x, y][0] + 0.686 *img5[x, y][1] + 0.168 * img5[x, y][2])
            B = (0.272  * img5[x, y][0] + 0.534 *img5[x, y][1] + 0.131*img5[x, y][2])

            if R > 255:
             img5[x, y][2] = 255
            else:
                img5[x, y][2] = R
            if G > 255:
             img5[x, y][1] = 255
            else:
                img5[x, y][1] = G

            if B > 255:
             img5[x, y][0] = 255
            else:
                img5[x, y][0] = B

            

    img5 = cv.cvtColor(img5, cv.COLOR_BGR2RGB)  # ปรับภาพเป็น RGB
    # ปรับให้เป็น fromarray image เพราะภาพต้นฉบับเป็นตัวเลข(math)
    img5 = Image.fromarray(img5)
    img5 = ImageTk.PhotoImage(img5)  # ปรับเป็น PhotoImage
    return img5


# สร้างหน้าต่าง tkinter
window = Tk()
window.title('Tkinter window')  # Title
window.geometry('480x320')
window.resizable(True, True)

# Menubar
menubar = Menu(window)  # สร้างMenubar tkinter
# menubar คือ parent, tearoff คือ เส้นปะ เลยตั้งเป็น 0
filemenu = Menu(menubar, tearoff=0)
# menubar คือ parent, tearoff คือ เส้นปะ เลยตั้งเป็น 0
editmenu = Menu(menubar, tearoff=0)
# menubar คือ parent, tearoff คือ เส้นปะ เลยตั้งเป็น 0
toolmenu = Menu(menubar, tearoff=0)

# ใส่เมนู File ลงไปใน  menubar
menubar.add_cascade(label='File', menu=filemenu)
# ใส่เมนูย่อย ของ File ลงไปใน File
filemenu.add_command(label='Open', command=openMenuItemClicked)
# ใส่เมนูย่อย ของ File ลงไปใน File
filemenu.add_command(label='Exit', command=exitMenuItemClicked)

# ใส่เมนู Edit ลงไปใน  menubar
menubar.add_cascade(label='Edit', menu=editmenu)
editmenu.add_command(label='Undo')
window.config(menu=menubar)  # โชว์ menubar

# ใส่เมนู Tools ลงไปใน  menubar
menubar.add_cascade(label='Tools', menu=toolmenu)
toolmenu.add_command(label='Sepia', command=SepiaMenuItemClicked)
toolmenu.add_command(label='Invert', command=invertMenuItemClicked)
window.config(menu=menubar)  # โชว์ menubar


# Resize
img = cv.imread('./toomtam1.png', cv.IMREAD_COLOR)  # ใช้อ่านภาพจากไฟล์เข้ามา

scale_percent = 15
width = int(img.shape[1] * scale_percent / 100)
height = int(img.shape[0] * scale_percent / 100)
dsize = (width, height)

output = cv.resize(img, dsize)


# CV
#cv.imshow('toomtam1', output)
#cv.imwrite('toomtam new.png', output)
# cv.waitKey(0)
# cv.destroyAllWindows()

# plt
#plt.imshow(output, cmap='gray', interpolation='bicubic')

#plt.xticks([]), plt.yticks([])
# plt.show();


#print('img[0,3]=', output[0,3])
# cv.waitKey(0)
# cv.destroyAllWindows()

# image Blue
img1 = output.copy()
img2 = output.copy()
img3 = output.copy()
img4 = output.copy()

width, height, type = output.shape
for y in range(0, height):
    for x in range(0, width):
        img2[x, y][0] = output[x, y][0]
        img2[x, y][1] = 0
        img2[x, y][2] = 0

        img3[x, y][0] = 0
        img3[x, y][1] = output[x, y][1]
        img3[x, y][2] = 0

        img4[x, y][0] = 0
        img4[x, y][1] = 0
        img4[x, y][2] = output[x, y][2]


img1 = cv.cvtColor(img1, cv.COLOR_BGR2RGB)  # ปรับภาพเป็น RGB
# ปรับให้เป็น fromarray image เพราะภาพต้นฉบับเป็นตัวเลข(math)
img1 = Image.fromarray(img1)
img1 = ImageTk.PhotoImage(img1)  # ปรับเป็น PhotoImage

cv.imshow('output image blue channel', img2)  # import ภาพเข้ามา
img2 = cv.cvtColor(img2, cv.COLOR_BGR2RGB)  # ปรับภาพเป็น RGB
# ปรับให้เป็น fromarray image เพราะภาพต้นฉบับเป็นตัวเลข(math)
img2 = Image.fromarray(img2)
img2 = ImageTk.PhotoImage(img2)  # ปรับเป็น PhotoImage

cv.imshow('output image green channel', img3)  # import ภาพเข้ามา
img3 = cv.cvtColor(img3, cv.COLOR_BGR2RGB)  # ปรับภาพเป็น RGB
# ปรับให้เป็น fromarray image เพราะภาพต้นฉบับเป็นตัวเลข(math)
img3 = Image.fromarray(img3)
img3 = ImageTk.PhotoImage(img3)  # ปรับเป็น PhotoImage

cv.imshow('output image red channel', img4)  # import ภาพเข้ามา
img4 = cv.cvtColor(img4, cv.COLOR_BGR2RGB)  # ปรับภาพเป็น RGB
# ปรับให้เป็น fromarray image เพราะภาพต้นฉบับเป็นตัวเลข(math)
img4 = Image.fromarray(img4)
img8 = ImageTk.PhotoImage(img4)  # ปรับเป็น PhotoImage


# ใส่อุปกรณ์เพิ่มเติมเข้าไป label
label = None
# cv.waitKey(0)
# cv.destroyAllWindows()


window.mainloop()  # เพื่อให้การวนรอบ ถ้าไม่มีมันจะไม่โชว์
