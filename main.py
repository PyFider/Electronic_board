# Import Modules
from tkinter import *
from tkinter import messagebox
from tkinter import colorchooser

font_size = 7 # Size background and pen
color = "white" # Color pen
color_figure = "white" # Color figures
eraser_color = "#0A5432" # Eraser color

# Main window character
w = Tk()
w.title("Электронная доска")
w["bg"] = "#0A5432"
w.eval('tk::PlaceWindow . center') # Window in center
w.geometry("1000x700")
w.attributes('-fullscreen', True)
w.iconbitmap(r"C:\Users\user\Desktop\все файлы\Python\Python projects\Электронная доска\icon.ico")

# Func colors
def white_mel():
	global font_size, color, color_figure
	color = "white"
	color_figure = "white"

def grey_mel():
	global font_size, color, color_figure
	color = "grey"
	color_figure = "grey"

def black_mel():
	global font_size, color, color_figure
	color = "black"
	color_figure = "black"

def purple_mel():
	global font_size, color, color_figure
	color = "purple"
	color_figure = "purple"

def blue_mel():
	global font_size, color, color_figure
	color = "blue"
	color_figure = "blue"

def magenta_mel():
	global font_size, color, color_figure
	color = "magenta"
	color_figure = "magenta"

def rose_mel():
	global font_size, color, color_figure
	color = "#F66CB7"
	color_figure = "#F66CB7"

def red_mel():
	global font_size, color, menu, color_figure
	color = "red"
	color_figure = "red"

def cyan_mel():
	global font_size, color, color_figure
	color = "#23FFF2"
	color_figure = "#23FFF2"

def orange_mel():
	global font_size, color, color_figure
	color = "orange"
	color_figure = "orange"

def dark_green_mel():
	global font_size, color, color_figure
	color = "#0A5432"
	color_figure = "#0A5432"

def green_mel():
	global font_size, color, color_figure
	color = "#00FF00"
	color_figure = "#00FF00"

def yellow_mel():
	global font_size, color, color_figure
	color = "yellow"
	color_figure = "yellow"

def palitra():
	global color, color_figure
	color_palitra = colorchooser.askcolor() # Переменная нужна для последующего указания индекса указа текста
	color = color_palitra[1]
	color_figure = color_palitra[1]

# All in mel color func
def standart_mel_all():
	global eraser_color
	c.create_oval(0, 0, 50, 50, outline = "#0A5432", fill = "#0A5432", width = 10000)
	eraser_color = "#0A5432"

def white_mel_all():
	global eraser_color
	c.create_oval(0, 0, 50, 50, outline = "white", fill = "white", width = 10000)
	eraser_color = "white"

def grey_mel_all():
	global eraser_color
	c.create_oval(0, 0, 50, 50, outline = "grey", fill = "grey", width = 10000)
	eraser_color = "grey"

def black_mel_all():
	global eraser_color
	c.create_oval(0, 0, 50, 50, outline = "black", fill = "black", width = 10000)
	eraser_color = "black"

def purple_mel_all():
	global eraser_color
	c.create_oval(0, 0, 50, 50, outline = "purple", fill = "purple", width = 10000)
	eraser_color = "purple"

def blue_mel_all():
	global eraser_color
	c.create_oval(0, 0, 50, 50, outline = "blue", fill = "blue", width = 10000)
	eraser_color = "blue"

def magenta_mel_all():
	global eraser_color
	c.create_oval(0, 0, 50, 50, outline = "magenta", fill = "magenta", width = 10000)
	eraser_color = "magenta"

def rose_mel_all():
	global eraser_color
	c.create_oval(0, 0, 50, 50, outline = "#F66CB7", fill = "#F66CB7", width = 10000)
	eraser_color = "#F66CB7"

def red_mel_all():
	global eraser_color
	c.create_oval(0, 0, 50, 50, outline = "red", fill = "red", width = 10000)
	eraser_color = "red"

def cyan_mel_all():
	global eraser_color
	c.create_oval(0, 0, 50, 50, outline = "#23FFF2", fill = "#23FFF2", width = 10000)
	eraser_color = "#23FFF2"

def orange_mel_all():
	global eraser_color
	c.create_oval(0, 0, 50, 50, outline = "orange", fill = "orange", width = 10000)
	eraser_color = "orange"

def green_mel_all():
	global eraser_color
	c.create_oval(0, 0, 50, 50, outline = "green", fill = "green", width = 10000)
	eraser_color = "green"

def yellow_mel_all():
	global eraser_color
	c.create_oval(0, 0, 50, 50, outline = "yellow", fill = "yellow", width = 10000)
	eraser_color = "yellow"

def palitra_all():
	global color, color_figure
	color_palitra_all = colorchooser.askcolor() # Переменная нужна для последующего указания индекса указа текста
	c.create_oval(0, 0, 50, 50, outline = color_palitra_all[1], fill = color_palitra_all[1], width = 10000)

# Figures
# triangles
def equilateral_triangle():
	c.create_line(50, 220, 130, 50, width = 7, fill = color_figure)
	c.create_line(130, 50, 210, 220, width = 7, fill = color_figure)
	c.create_line(50, 220, 210, 220, width = 7, fill = color_figure)

def right_triangle():
	c.create_line(50, 200, 50, 50, width = 7, fill = color_figure)
	c.create_line(50, 200, 500, 200, width = 7, fill = color_figure)
	c.create_line(500, 200, 50, 50, width = 7, fill = color_figure)

def random_triangle():
	c.create_line(50, 200, 140, 50, width = 7, fill = color_figure)
	c.create_line(140, 50, 300, 200, width = 7, fill = color_figure)
	c.create_line(50, 200, 300, 200, width = 7, fill = color_figure)

# Quadrilateral
def parallelogram():
	c.create_line(50, 200, 140, 50, width = 7, fill = color_figure)
	c.create_line(50, 200, 350, 200, width = 7, fill = color_figure)
	c.create_line(350, 200, 440, 50, width = 7, fill = color_figure)
	c.create_line(140, 50, 440, 50, width = 7, fill = color_figure)

def isosceles_trapezoid():
	c.create_line(50, 200, 140, 50, width = 7, fill = color_figure)
	c.create_line(50, 200, 440, 200, width = 7, fill = color_figure)
	c.create_line(440, 200, 350, 50, width = 7, fill = color_figure)
	c.create_line(140, 50, 350, 50, width = 7, fill = color_figure)

def arbitrary_trapezoid():
	c.create_line(50, 200, 200, 50, width = 7, fill = color_figure)
	c.create_line(50, 200, 440, 200, width = 7, fill = color_figure)
	c.create_line(440, 200, 390, 50, width = 7, fill = color_figure)
	c.create_line(200, 50, 390, 50, width = 7, fill = color_figure)

def rectangular_trapezoid():
	c.create_line(50, 200, 50, 50, width = 7, fill = color_figure)
	c.create_line(50, 200, 440, 200, width = 7, fill = color_figure)
	c.create_line(440, 200, 300, 50, width = 7, fill = color_figure)
	c.create_line(50, 50, 300, 50, width = 7, fill = color_figure)

def arbitrary_quadrilateral():
	c.create_line(50, 200, 20, 30, width = 7, fill = color_figure)
	c.create_line(50, 200, 500, 177, width = 7, fill = color_figure)
	c.create_line(500, 177, 535, 40, width = 7, fill = color_figure)
	c.create_line(25, 30, 535, 40, width = 7, fill = color_figure)

# Other Func
current_x, current_y = 0,0
def locate_xy(event):
    global current_x, current_y
    current_x, current_y = event.x, event.y

def addLine(event):
    global current_x, current_y
    c.create_line((current_x,current_y,event.x,event.y),fill = color, width = 7)
    current_x, current_y = event.x, event.y

def clear():
	global eraser_color
	c.create_oval(0, 0, 50, 50, outline = eraser_color, fill = eraser_color, width = 10000)

def eraser():
	global color, menu
	color = eraser_color

def mel_use():
	global color, menu
	color = "white"

def full_screen_true():
	w.attributes('-fullscreen', True)

def full_screen_false():
	w.attributes('-fullscreen', False)

def info():
	messagebox.showinfo("Info", "Электронная доска v Alpha 1.5.5")

def sponsor():
	messagebox.showinfo("Info about Kostya and Roma", "Sponsors Kostya and Roma :)")

def exit():
    answer = messagebox.askyesno( # Question quit's
        title="Выйти", # Title Message box
        message="Вы уверены?") # Text Message box
    if answer: # If yes
        w.destroy() # Destroy window

# Widgets
c = Canvas(w, bg = "#0A5432", cursor = "circle")
c.place(relx = 0, rely = 0, relwidth = 1, relheight = 1)

c.bind('<Button-1>', locate_xy) # Mouse control(B1 - lkm, B3 - rkm, B2 - centralkm)
c.bind('<B1-Motion>',addLine)

# Menu widget
menu = Menu(w, tearoff = False) # Tearoff - ------ is false
tools = Menu(menu, tearoff = False) # Tools menu options
figures = Menu(menu, tearoff = False) # Figures menu options
quadrilateral = Menu(menu, tearoff = False) # Quadrilateral menu options
trapezoid = Menu(menu, tearoff = False) # Trapezoid menu options
triangles = Menu(menu, tearoff = False) # Triangles menu options
mel = Menu(menu, tearoff = False) # Mel menu options
board_all_in_color = Menu(menu, tearoff = False) # Board all in color menu options
settings = Menu(menu, tearoff = False) # Main settings menu
settings_fullscreen = Menu(menu, tearoff = False) # Settings fullscreen's menu
settings_view = Menu(menu, tearoff = False) # Settings view's menu
settings_grid = Menu(menu, tearoff = False) # Settings grid's menu
configurate = Menu(menu, tearoff = False) # Config menu

# Tools menu
menu.add_cascade(label = '🖊️Инструменты🖊️', menu = tools)
tools.add_separator()
tools.add_cascade(label='🏏Мел🏏', menu = mel)
mel.add_separator()
mel.add_cascade(label='Белый цвет', command = white_mel)
mel.add_cascade(label='Серый цвет', command = grey_mel)
mel.add_cascade(label='Чёрный цвет', command = black_mel)
mel.add_cascade(label='Фиолетовый цвет', command = purple_mel)
mel.add_cascade(label='Синий цвет', command = blue_mel)
mel.add_cascade(label='Мажента цвет', command = magenta_mel)
mel.add_cascade(label='Розовый цвет', command = rose_mel)
mel.add_cascade(label='Красный цвет', command = red_mel)
mel.add_cascade(label='Циановый цвет', command = cyan_mel)
mel.add_cascade(label='Оранжевый цвет', command = orange_mel)
mel.add_cascade(label='Тёмно-зелёный цвет', command = dark_green_mel)
mel.add_cascade(label='Зелённый цвет', command = green_mel)
mel.add_cascade(label='Жёлтый цвет', command = yellow_mel)
mel.add_separator()
mel.add_cascade(label='Палитра', command = palitra)
mel.add_separator()

tools.add_cascade(label='Создание фигур', menu = figures)
figures.add_separator()
figures.add_cascade(label = "Треугольники", menu = triangles)
triangles.add_separator()
triangles.add_command(label = "Равнобедренный треугольник", command = equilateral_triangle)
triangles.add_command(label = "Произвольный треугольник", command = random_triangle)
triangles.add_command(label = "Прямоугольный треугольник", command = right_triangle)
triangles.add_separator()

figures.add_cascade(label = "Четырёхугольники", menu = quadrilateral)
quadrilateral.add_separator()
quadrilateral.add_command(label = "Параллелограмм", command = parallelogram)
quadrilateral.add_cascade(label = "Трапеция", menu = trapezoid)
trapezoid.add_separator()
trapezoid.add_command(label = "Равнобедренная трапеция", command = isosceles_trapezoid)
trapezoid.add_command(label = "Произвольная трапеция", command = arbitrary_trapezoid)
trapezoid.add_command(label = "Прямоугольная трапеция", command = rectangular_trapezoid)
trapezoid.add_separator()
quadrilateral.add_command(label = "Произвольный четырёхугольник", command = arbitrary_quadrilateral)
quadrilateral.add_separator()
figures.add_separator()
tools.add_separator()

tools.add_command(label='🥻Тряпка🥻',  command = eraser)
tools.add_separator()

# Other menu
menu.add_cascade(label='🧹Очистить доску🧹', command = clear)

menu.add_cascade(label = '⚙️Настройки⚙️', menu = settings)
settings.add_separator()
settings.add_cascade(label = '♐Вид♐', menu = settings_view)
settings_view.add_separator()
settings_view.add_cascade(label = '♐Полный экран♐', menu = settings_fullscreen)
settings_fullscreen.add_separator()
settings_fullscreen.add_command(label = '♐Полный экран - Вкл♐', command = full_screen_true)
settings_fullscreen.add_command(label = '♐Полный экран - Выкл♐', command = full_screen_false)
settings_fullscreen.add_separator()

settings_grid.add_separator()
settings_grid.add_separator()
settings_view.add_separator()
settings.add_separator()

settings_view.add_cascade(label='⬜Изменить цвет доски⬜',  menu = board_all_in_color)
board_all_in_color.add_separator()
board_all_in_color.add_cascade(label='Стандартный', command = standart_mel_all)
board_all_in_color.add_cascade(label='Белый', command = white_mel_all)
board_all_in_color.add_cascade(label='Серый', command = grey_mel_all)
board_all_in_color.add_cascade(label='Чёрный', command = black_mel_all)
board_all_in_color.add_cascade(label='Фиолетовый', command = purple_mel_all)
board_all_in_color.add_cascade(label='Синий', command = blue_mel_all)
board_all_in_color.add_cascade(label='Мажента', command = magenta_mel_all)
board_all_in_color.add_cascade(label='Розовый', command = rose_mel_all)
board_all_in_color.add_cascade(label='Красный', command = red_mel_all)
board_all_in_color.add_cascade(label='Циановый', command = cyan_mel_all)
board_all_in_color.add_cascade(label='Оранжевый', command = orange_mel_all)
board_all_in_color.add_cascade(label='Зелённый', command = green_mel_all)
board_all_in_color.add_cascade(label='Жёлтый', command = yellow_mel_all)
board_all_in_color.add_separator()
board_all_in_color.add_cascade(label='Палитра', command = palitra_all)
settings_view.add_separator()
board_all_in_color.add_separator()

# Configure
menu.add_cascade(label = "📄Конфигурация📄", menu = configurate)
configurate.add_separator()
configurate.add_cascade(label='❕Справка❕', command = info)
configurate.add_cascade(label='❔Спонсор❔', command = sponsor)
configurate.add_separator()
configurate.add_cascade(label='🚪Закрыть доску🚪', command = exit)
configurate.add_separator()

w.config(menu=menu)

# Start programm
w.mainloop()
