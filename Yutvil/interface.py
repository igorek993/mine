# -*- coding: utf-8 -*-

import tkinter as tk

FONT = "Courier", 20

root = tk.Tk()
root.iconbitmap("C:\\Users\igorek\PycharmProjects\mine\Yutvil\logo.ico")
root.geometry("1200x768")
root.title("ДОГОВОР ОКАЗАНИЯ УСЛУГ")
root.resizable(height=False, width=False)

contract_number_label = tk.Label(root, text="Номер договора:")
contract_number_label.config(font=FONT, width=15)
contract_number_label.place(relx=0.0, rely=0.01, anchor='nw')

contract_number_entry = tk.Entry(root, width=20, font=FONT)
contract_number_entry.place(relx=0.25, rely=0.01, anchor='nw')

date_label = tk.Label(root, text="Дата договора: День")
date_label.config(font=FONT)
date_label.place(relx=0.0, rely=0.10, anchor='nw')

day = tk.StringVar()
day.set("01")
todays_day_drop = tk.OptionMenu(root, day, "01", "02", "03", "04", "05", "06", "07",
                                "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"
                                , "23", "24", "25", "26", "27", "28", "29", "30", "31")
todays_day_drop.config(font=FONT)
todays_day_drop.place(relx=0.26, rely=0.09, anchor='nw')

month_label = tk.Label(root, text="Месяц")
month_label.config(font=FONT)
month_label.place(relx=0.34, rely=0.10, anchor='nw')

month = tk.StringVar()
month.set("января")
month_drop = tk.OptionMenu(root, month, "января", "февраля", "марта", "апреля", "мая", "июня", "июля",
                           "августа", "сентября", "октября", "ноября", "декабря")
month_drop.config(font=FONT)
month_drop.place(relx=0.42, rely=0.09, anchor='nw')

year_label = tk.Label(root, text="Год")
year_label.config(font=FONT)
year_label.place(relx=0.55, rely=0.10, anchor='nw')

year = tk.StringVar()
year.set("2020")
year_drop = tk.OptionMenu(root, year, "2020", "2021", "2022", "2023", "2024", "2025", "2026",
                          "2027", "2028", "2029", "2030")
year_drop.config(font=FONT)
year_drop.place(relx=0.61, rely=0.09, anchor='nw')

passport_details_label = tk.Label(root, text="Паспортные данные:")
passport_details_label.config(font=FONT)
passport_details_label.place(relx=0.0, rely=0.20, anchor='nw')

sex = tk.StringVar()
sex.set("М")
sex_drop = tk.OptionMenu(root, sex, "М", "Ж")
sex_drop.config(font=FONT)
sex_drop.place(relx=0.25, rely=0.19, anchor='nw')

full_name_label = tk.Label(root, text="ФИО:")
full_name_label.config(font=FONT)
full_name_label.place(relx=0.32, rely=0.20, anchor='nw')

full_name_entry = tk.Entry(root, width=40, font=FONT)
full_name_entry.place(relx=0.40, rely=0.20, anchor='nw')

date_of_birth_label = tk.Label(root, text="Дата рождения:")
date_of_birth_label.config(font=FONT)
date_of_birth_label.place(relx=0.14, rely=0.30, anchor='nw')

date_of_birth_text = tk.StringVar()
date_of_birth_text.set("ДД.ММ.ГГГГ")
date_of_birth_entry = tk.Entry(root, textvariable=date_of_birth_text, width=10, font=FONT)
date_of_birth_entry.place(relx=0.37, rely=0.30, anchor='nw')

locality_label = tk.Label(root, text="Место рождения:")
locality_label.config(font=FONT)
locality_label.place(relx=0.54, rely=0.30, anchor='nw')

locality_text = tk.StringVar()
locality_text.set("Гор. Название")
locality_entry = tk.Entry(root, textvariable=locality_text, width=15, font=FONT)
locality_entry.place(relx=0.75, rely=0.30, anchor='nw')

passport_series_label = tk.Label(root, text="Серия паспорта:")
passport_series_label.config(font=FONT)
passport_series_label.place(relx=0.14, rely=0.40, anchor='nw')

passport_series_entry = tk.Entry(root, width=10, font=FONT)
passport_series_entry.place(relx=0.37, rely=0.40, anchor='nw')

passport_number_label = tk.Label(root, text="Номер паспорта:")
passport_number_label.config(font=FONT)
passport_number_label.place(relx=0.54, rely=0.40, anchor='nw')

passport_number_entry = tk.Entry(root, width=15, font=FONT)
passport_number_entry.place(relx=0.75, rely=0.40, anchor='nw')

passport_issue_date_label = tk.Label(root, text="Дата выдачи:")
passport_issue_date_label.config(font=FONT)
passport_issue_date_label.place(relx=0.14, rely=0.50, anchor='nw')

passport_issue_date_text = tk.StringVar()
passport_issue_date_text.set("ДД.ММ.ГГГГ")
passport_issue_date_entry = tk.Entry(root, textvariable=passport_issue_date_text, width=10, font=FONT)
passport_issue_date_entry.place(relx=0.37, rely=0.50, anchor='nw')

kod_podrazdelenia_label = tk.Label(root, text="Код подразделения:")
kod_podrazdelenia_label.config(font=FONT)
kod_podrazdelenia_label.place(relx=0.54, rely=0.50, anchor='nw')

kod_podrazdelenia_entry = tk.Entry(root, width=15, font=FONT)
kod_podrazdelenia_entry.place(relx=0.79, rely=0.50, anchor='nw')

who_issued_passport_label = tk.Label(root, text="Где выдан:")
who_issued_passport_label.config(font=FONT)
who_issued_passport_label.place(relx=0.14, rely=0.60, anchor='nw')

who_issued_passport_entry = tk.Entry(root, width=44, font=FONT)
who_issued_passport_entry.place(relx=0.37, rely=0.60, anchor='nw')

residential_address_label = tk.Label(root, text="Адрес регистр:")
residential_address_label.config(font=FONT)
residential_address_label.place(relx=0.14, rely=0.70, anchor='nw')

residential_address_entry = tk.Entry(root, width=44, font=FONT)
residential_address_entry.place(relx=0.37, rely=0.70, anchor='nw')


root.mainloop()
