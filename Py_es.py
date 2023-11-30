import tkinter as tk
import customtkinter
import sqlite3


root = customtkinter.CTk()  # Объект класса
root.title("Заметки")   # Заголовок
root.geometry("400x700") # Размер окна блакнота
root.resizable(0, 0)     # запрет редоктирования размера окна

note_label = customtkinter.CTkLabel(root, text= "Заметки", fg_color="green50")  # поле с заметками
note_label.pack(pady = 4)

