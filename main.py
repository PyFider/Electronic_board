# Import Modules
from tkinter import *
from tkinter import messagebox

font_size = 7 # Size background and pen
font_size_choose_mel = 7 # choose size pen
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
w.iconbitmap(r"icon.ico")

# Func colors
def white_mel():
	global font_size, color, menu, font_size_choose_mel, font_size_choose_mel, color_figure
	color = "white"
	color_figure = "white"
	font_size = font_size_choose_mel

def grey_mel():
	global font_size, color, menu, font_size_choose_mel, font_size_choose_mel, color_figure
	color = "grey"
	color_figure = "grey"
	font_size = font_size_choose_mel

def black_mel():
	global font_size, color, menu, font_size_choose_mel, font_size_choose_mel, color_figure
	color = "black"
	color_figure = "black"
	font_size = font_size_choose_mel

def purple_mel():
	global font_size, color, menu, font_size_choose_mel, font_size_choose_mel, color_figure
	color = "purple"
	color_figure = "purple"
	font_size = font_size_choose_mel

def blue_mel():
	global font_size, color, menu, font_size_choose_mel, font_size_choose_mel, color_figure
	color = "blue"
	color_figure = "blue"
	font_size = font_size_choose_mel

def magenta_mel():
	global font_size, color, menu, font_size_choose_mel, font_size_choose_mel, color_figure
	color = "magenta"
	color_figure = "magenta"
	font_size = font_size_choose_mel

def rose_mel():
	global font_size, color, menu, font_size_choose_mel, font_size_choose_mel, color_figure
	color = "#F66CB7"
	color_figure = "#F66CB7"
	font_size = font_size_choose_mel

def red_mel():
	global font_size, color, menu, font_size_choose_mel, font_size_choose_mel, color_figure
	color = "red"
	color_figure = "red"
	font_size = font_size_choose_mel

def cyan_mel():
	global font_size, color, menu, font_size_choose_mel, font_size_choose_mel, color_figure
	color = "#23FFF2"
	color_figure = "#23FFF2"
	font_size = font_size_choose_mel

def orange_mel():
	global font_size, color, menu, font_size_choose_mel, font_size_choose_mel, color_figure
	color = "orange"
	color_figure = "orange"
	font_size = font_size_choose_mel

def dark_green_mel():
	global font_size, color, menu, font_size_choose_mel, font_size_choose_mel, color_figure
	color = "#0A5432"
	color_figure = "#0A5432"
	font_size = font_size_choose_mel

def green_mel():
	global font_size, color, menu, font_size_choose_mel, font_size_choose_mel, color_figure
	color = "#00FF00"
	color_figure = "#00FF00"
	font_size = font_size_choose_mel

def yellow_mel():
	global font_size, color, menu, font_size_choose_mel, font_size_choose_mel, color_figure
	color = "yellow"
	color_figure = "yellow"
	font_size = font_size_choose_mel

# All in mel color func
def standart_mel_all():
	global color, font_size, eraser_color
	color = "#0A5432"
	eraser_color = "#0A5432"
	font_size = 2000	

def white_mel_all():
	global color, font_size, eraser_color
	color = "white"
	eraser_color = "white"
	font_size = 2000

def grey_mel_all():
	global color, font_size, eraser_color
	color = "grey"
	eraser_color = "grey"
	font_size = 2000

def black_mel_all():
	global color, font_size, eraser_color
	color = "black"
	eraser_color = "black"
	font_size = 2000

def purple_mel_all():
	global color, font_size, eraser_color
	color = "purple"
	eraser_color = "purple"
	font_size = 2000

def blue_mel_all():
	global color, font_size, eraser_color
	color = "blue"
	eraser_color = "blue"
	font_size = 2000

def magenta_mel_all():
	global color, font_size, eraser_color
	color = "magenta"
	eraser_color = "magenta"
	font_size = 2000

def rose_mel_all():
	global color, font_size, eraser_color
	color = "#F66CB7"
	eraser_color = "#F66CB7"
	font_size = 2000

def red_mel_all():
	global color, font_size, eraser_color
	color = "red"
	eraser_color = "red"
	font_size = 2000

def cyan_mel_all():
	global color, font_size, eraser_color
	color = "#23FFF2"
	font_size = 2000

def orange_mel_all():
	global color, font_size, eraser_color
	color = "orange"
	eraser_color = "orange"
	font_size = 2000

def green_mel_all():
	global color, font_size, eraser_color
	color = "green"
	eraser_color = "green"
	font_size = 2000

def yellow_mel_all():
	global color, font_size, eraser_color
	color = "yellow"
	eraser_color = "yellow"
	font_size = 2000

# Func size
def mel_size_1():
	global font_size_choose_mel
	font_size_choose_mel = 1

def mel_size_5():
	global font_size_choose_mel
	font_size_choose_mel = 5

def mel_size_7():
	global font_size_choose_mel
	font_size_choose_mel = 7

def mel_size_10():
	global font_size_choose_mel
	font_size_choose_mel = 10

def mel_size_15():
	global font_size_choose_mel
	font_size_choose_mel = 15

def mel_size_20():
	global font_size_choose_mel
	font_size_choose_mel = 20

def mel_size_25():
	global font_size_choose_mel
	font_size_choose_mel = 25

def mel_size_30():
	global font_size_choose_mel
	font_size_choose_mel = 30

def mel_size_35():
	global font_size_choose_mel
	font_size_choose_mel = 35

def mel_size_40():
	global font_size_choose_mel
	font_size = 40

def mel_size_45():
	global font_size_choose_mel
	font_size_choose_mel = 45

def mel_size_50():
	global font_size_choose_mel
	font_size_choose_mel = 50

def mel_size_55():
	global font_size_choose_mel
	font_size_choose_mel = 55

def mel_size_60():
	global font_size_choose_mel
	font_size_choose_mel = 60

def mel_size_65():
	global font_size_choose_mel
	font_size_choose_mel = 65

def mel_size_70():
	global font_size_choose_mel
	font_size_choose_mel = 70

def mel_size_75():
	global font_size_choose_mel
	font_size_choose_mel = 75

def mel_size_80():
	global font_size_choose_mel
	font_size_choose_mel = 80

def mel_size_85():
	global font_size_choose_mel
	font_size_choose_mel = 85

def mel_size_90():
	global font_size_choose_mel
	font_size_choose_mel = 90

def mel_size_95():
	global font_size_choose_mel
	font_size_choose_mel = 95

def mel_size_100():
	global font_size_choose_mel
	font_size_choose_mel = 100


# Figures
# triangles
def equilateral_triangle():
	c.create_line(50, 220, 130, 50, width = font_size_choose_mel, fill = color_figure)
	c.create_line(130, 50, 210, 220, width = font_size_choose_mel, fill = color_figure)
	c.create_line(50, 220, 210, 220, width = font_size_choose_mel, fill = color_figure)

def right_triangle():
	c.create_line(50, 200, 50, 50, width = font_size_choose_mel, fill = color_figure)
	c.create_line(50, 200, 500, 200, width = font_size_choose_mel, fill = color_figure)
	c.create_line(500, 200, 50, 50, width = font_size_choose_mel, fill = color_figure)

def random_triangle():
	c.create_line(50, 200, 140, 50, width = font_size_choose_mel, fill = color_figure)
	c.create_line(140, 50, 300, 200, width = font_size_choose_mel, fill = color_figure)
	c.create_line(50, 200, 300, 200, width = font_size_choose_mel, fill = color_figure)

# Quadrilateral
def parallelogram():
	c.create_line(50, 200, 140, 50, width = font_size_choose_mel, fill = color_figure)
	c.create_line(50, 200, 350, 200, width = font_size_choose_mel, fill = color_figure)
	c.create_line(350, 200, 440, 50, width = font_size_choose_mel, fill = color_figure)
	c.create_line(140, 50, 440, 50, width = font_size_choose_mel, fill = color_figure)

def isosceles_trapezoid():
	c.create_line(50, 200, 140, 50, width = font_size_choose_mel, fill = color_figure)
	c.create_line(50, 200, 440, 200, width = font_size_choose_mel, fill = color_figure)
	c.create_line(440, 200, 350, 50, width = font_size_choose_mel, fill = color_figure)
	c.create_line(140, 50, 350, 50, width = font_size_choose_mel, fill = color_figure)

def arbitrary_trapezoid():
	c.create_line(50, 200, 200, 50, width = font_size_choose_mel, fill = color_figure)
	c.create_line(50, 200, 440, 200, width = font_size_choose_mel, fill = color_figure)
	c.create_line(440, 200, 390, 50, width = font_size_choose_mel, fill = color_figure)
	c.create_line(200, 50, 390, 50, width = font_size_choose_mel, fill = color_figure)

def rectangular_trapezoid():
	c.create_line(50, 200, 50, 50, width = font_size_choose_mel, fill = color_figure)
	c.create_line(50, 200, 440, 200, width = font_size_choose_mel, fill = color_figure)
	c.create_line(440, 200, 300, 50, width = font_size_choose_mel, fill = color_figure)
	c.create_line(50, 50, 300, 50, width = font_size_choose_mel, fill = color_figure)

def arbitrary_quadrilateral():
	c.create_line(50, 200, 20, 30, width = font_size_choose_mel, fill = color_figure)
	c.create_line(50, 200, 500, 177, width = font_size_choose_mel, fill = color_figure)
	c.create_line(500, 177, 535, 40, width = font_size_choose_mel, fill = color_figure)
	c.create_line(25, 30, 535, 40, width = font_size_choose_mel, fill = color_figure)

# Other Func
def text_user(event):
	global font_size, color

	x1 = event.x - font_size
	x2 = event.x + font_size
	
	y1 = event.y - font_size
	y2 = event.y + font_size

	oval = c.create_oval(x1,
	y1,
	x2,
	y2,
	fill = color,
	outline = color)

def clear():
	c.delete("all")

def eraser():
	global font_size, color, menu
	color = eraser_color
	font_size = 30

def mel_use():
	global font_size, color, menu, font_size_choose_mel
	color = "white"
	font_size = font_size_choose_mel

def full_screen_true():
	w.attributes('-fullscreen', True)

def full_screen_false():
	w.attributes('-fullscreen', False)

def info():
	messagebox.showinfo("Info", "Электронная доска v 1.3.0")

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

c.bind("<B1-Motion>", text_user) # Mouse control(B1 - lkm, B3 - rkm, B2 - centralkm)

# Menu widget
menu = Menu(w, tearoff = False) # Tearoff - ------ is false
tools = Menu(menu, tearoff = False) # Tools menu options
figures = Menu(menu, tearoff = False) # Figures menu options
quadrilateral = Menu(menu, tearoff = False) # Quadrilateral menu options
trapezoid = Menu(menu, tearoff = False) # Trapezoid menu options
triangles = Menu(menu, tearoff = False) # Triangles menu options
mel = Menu(menu, tearoff = False) # Mel menu options
mel_color = Menu(menu, tearoff = False) # Color mel's menu options
board_all_in_color = Menu(menu, tearoff = False) # Board all in color menu options
mel_size = Menu(menu, tearoff = False) # Size mel
settings = Menu(menu, tearoff = False) # Main settings menu
settings_fullscreen = Menu(menu, tearoff = False) # Settings fullscreen's menu
settings_view = Menu(menu, tearoff = False) # Settings view's menu
settings_grid = Menu(menu, tearoff = False) # Settings grid's menu
configurate = Menu(menu, tearoff = False) # Config menu

# Tools menu
menu.add_cascade(label = '🖊️Инструменты🖊️', menu = tools)
tools.add_separator()
tools.add_command(label='🐁Мышь🐁', command = mouse)
tools.add_cascade(label='🏏Мел🏏', menu = mel)
mel.add_separator()
mel.add_cascade(label = '📒Цвета📒', menu = mel_color)
mel_color.add_separator()
mel_color.add_cascade(label='Белый', command = white_mel)
mel_color.add_cascade(label='Серый', command = grey_mel)
mel_color.add_cascade(label='Чёрный', command = black_mel)
mel_color.add_cascade(label='Фиолетовый', command = purple_mel)
mel_color.add_cascade(label='Синий', command = blue_mel)
mel_color.add_cascade(label='Мажента', command = magenta_mel)
mel_color.add_cascade(label='Розовый', command = rose_mel)
mel_color.add_cascade(label='Красный', command = red_mel)
mel_color.add_cascade(label='Циановый', command = cyan_mel)
mel_color.add_cascade(label='Оранжевый', command = orange_mel)
mel_color.add_cascade(label='Тёмно-зелёный', command = dark_green_mel)
mel_color.add_cascade(label='Зелённый', command = green_mel)
mel_color.add_cascade(label='Жёлтый', command = yellow_mel)
mel_color.add_separator()

mel.add_cascade(label = '📐Размер📐', menu = mel_size)
mel_size.add_separator()
mel_size.add_command(label = "1", command = mel_size_1)
mel_size.add_command(label = "5", command = mel_size_5)
mel_size.add_command(label = "7", command = mel_size_7)
mel_size.add_command(label = "10", command = mel_size_10)
mel_size.add_command(label = "15", command = mel_size_15)
mel_size.add_command(label = "20", command = mel_size_20)
mel_size.add_command(label = "25", command = mel_size_25)
mel_size.add_command(label = "30", command = mel_size_30)
mel_size.add_command(label = "35", command = mel_size_35)
mel_size.add_command(label = "40", command = mel_size_40)
mel_size.add_command(label = "45", command = mel_size_45)
mel_size.add_command(label = "50", command = mel_size_50)
mel_size.add_command(label = "55", command = mel_size_55)
mel_size.add_command(label = "60", command = mel_size_60)
mel_size.add_command(label = "65", command = mel_size_65)
mel_size.add_command(label = "70", command = mel_size_70)
mel_size.add_command(label = "75", command = mel_size_75)
mel_size.add_command(label = "80", command = mel_size_80)
mel_size.add_command(label = "85", command = mel_size_85)
mel_size.add_command(label = "90", command = mel_size_90)
mel_size.add_command(label = "95", command = mel_size_95)
mel_size.add_command(label = "100", command = mel_size_100)
mel.add_separator()
mel_size.add_separator()

tools.add_cascade(label='Создание фигур', menu = figures)
figures.add_cascade(label = "Треугольники", menu = triangles)
triangles.add_command(label = "Равнобедренный треугольник", command = equilateral_triangle)
triangles.add_command(label = "Произвольный треугольник", command = random_triangle)
triangles.add_command(label = "Прямоугольный треугольник", command = right_triangle)

figures.add_cascade(label = "Четырёхугольники", menu = quadrilateral)
quadrilateral.add_command(label = "Параллелограмм", command = parallelogram)
quadrilateral.add_cascade(label = "Трапеция", menu = trapezoid)
trapezoid.add_command(label = "Равнобедренная трапеция", command = isosceles_trapezoid)
trapezoid.add_command(label = "Произвольная трапеция", command = arbitrary_trapezoid)
trapezoid.add_command(label = "Прямоугольная трапеция", command = rectangular_trapezoid)
quadrilateral.add_command(label = "Произвольный четырёхугольник", command = arbitrary_quadrilateral)
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
settings_view.add_separator()
board_all_in_color.add_separator()

# Configure
menu.add_cascade(label = "📄Конфигурация📄", menu = configurate)
configurate.add_separator()
configurate.add_cascade(label='❕Информация❕', command = info)
configurate.add_cascade(label='❔Спонсор❔', command = sponsor)
configurate.add_separator()
configurate.add_cascade(label='🚪Закрыть доску🚪', command = exit)
configurate.add_separator()

w.config(menu=menu)

# Start programm
w.mainloop()
