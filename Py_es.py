import tkinter as tk
import customtkinter
import sqlite3


root = customtkinter.CTk()  # Объект класса
root.title("Заметки")   # Заголовок
root.geometry("400x700") # Размер окна блакнота
root.resizable(0, 0)     # запрет редоктирования размера окна

note_label = customtkinter.CTkLabel(root, text= "Заметки", fg_color="green50")  # поле с заметками
note_label.pack(pady = 4)

note_entry = customtkinter.CTkEntry(root) # окно для ввода заметок
note_entry.pack(pady=3)

save_button = customtkinter.CTkButton(root, text="Добавить", fg_color="blue30", command=save_button) # кнопка сохранения
save_button.pack(pady=7)

delete_button = customtkinter.CTkButton(root, text="Удалить", fg_color="red80", command=delete_button) # кнопка удаления
delete_button.pack(pady=7)