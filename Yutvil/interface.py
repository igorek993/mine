# -*- coding: utf-8 -*-

import tkinter as tk
from tkinter.filedialog import asksaveasfile
from Yutvil.sale_agreement_mailmerge import SaleAgreement

FONT = "Courier", 18

root = tk.Tk()
root.iconbitmap("C:\\Users\igorek\PycharmProjects\mine\Yutvil\logo.ico")
root.geometry("1200x768")
root.title("ДОГОВОР ОКАЗАНИЯ УСЛУГ")
root.resizable(height=False, width=False)

contract_number_label = tk.Label(root, text="Номер договора:")
contract_number_label.config(font=FONT, width=15)
contract_number_label.place(relx=0.0, rely=0.01, anchor='nw')

contract_number_entry = tk.Entry(root, width=10, font=FONT)
contract_number_entry.place(relx=0.22, rely=0.01, anchor='nw')

date_label = tk.Label(root, text="Дата: День")
date_label.config(font=FONT)
date_label.place(relx=0.36, rely=0.01, anchor='nw')

today_day = tk.StringVar()
today_day.set("01")
todays_day_drop = tk.OptionMenu(root, today_day, "01", "02", "03", "04", "05", "06", "07",
                                "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"
                                , "23", "24", "25", "26", "27", "28", "29", "30", "31")
todays_day_drop.config(font=FONT)
todays_day_drop.place(relx=0.51, rely=0.0, anchor='nw')

month_label = tk.Label(root, text="Месяц")
month_label.config(font=FONT)
month_label.place(relx=0.59, rely=0.01, anchor='nw')

month_text = tk.StringVar()
month_text.set("января")
month_drop = tk.OptionMenu(root, month_text, "января", "февраля", "марта", "апреля", "мая", "июня", "июля",
                           "августа", "сентября", "октября", "ноября", "декабря")
month_drop.config(font=FONT)
month_drop.place(relx=0.67, rely=0.0, anchor='nw')

year_label = tk.Label(root, text="Год")
year_label.config(font=FONT)
year_label.place(relx=0.80, rely=0.01, anchor='nw')

year_text = tk.StringVar()
year_text.set("2020")
year_drop = tk.OptionMenu(root, year_text, "2020", "2021", "2022", "2023", "2024", "2025", "2026",
                          "2027", "2028", "2029", "2030")
year_drop.config(font=FONT)
year_drop.place(relx=0.85, rely=0.0, anchor='nw')

passport_details_label = tk.Label(root, text="Паспортные данные:")
passport_details_label.config(font=FONT)
passport_details_label.place(relx=0.0, rely=0.07, anchor='nw')

sex = tk.StringVar()
sex.set("М")
sex_drop = tk.OptionMenu(root, sex, "М", "Ж")
sex_drop.config(font=FONT)
sex_drop.place(relx=0.25, rely=0.06, anchor='nw')

full_name_label = tk.Label(root, text="ФИО:")
full_name_label.config(font=FONT)
full_name_label.place(relx=0.32, rely=0.07, anchor='nw')

full_name_entry = tk.Entry(root, width=40, font=FONT)
full_name_entry.place(relx=0.40, rely=0.07, anchor='nw')

date_of_birth_label = tk.Label(root, text="Дата рождения:")
date_of_birth_label.config(font=FONT)
date_of_birth_label.place(relx=0.14, rely=0.14, anchor='nw')

date_of_birth_text = tk.StringVar()
date_of_birth_text.set("ДД.ММ.ГГГГ")
date_of_birth_entry = tk.Entry(root, textvariable=date_of_birth_text, width=10, font=FONT)
date_of_birth_entry.place(relx=0.37, rely=0.14, anchor='nw')

locality_label = tk.Label(root, text="Место рождения:")
locality_label.config(font=FONT)
locality_label.place(relx=0.54, rely=0.14, anchor='nw')

locality_text = tk.StringVar()
locality_text.set("Гор. Название")
locality_entry = tk.Entry(root, textvariable=locality_text, width=15, font=FONT)
locality_entry.place(relx=0.75, rely=0.14, anchor='nw')

passport_series_label = tk.Label(root, text="Серия паспорта:")
passport_series_label.config(font=FONT)
passport_series_label.place(relx=0.14, rely=0.21, anchor='nw')

passport_series_entry = tk.Entry(root, width=10, font=FONT)
passport_series_entry.place(relx=0.37, rely=0.21, anchor='nw')

passport_number_label = tk.Label(root, text="Номер паспорта:")
passport_number_label.config(font=FONT)
passport_number_label.place(relx=0.54, rely=0.21, anchor='nw')

passport_number_entry = tk.Entry(root, width=15, font=FONT)
passport_number_entry.place(relx=0.75, rely=0.21, anchor='nw')

passport_issue_date_label = tk.Label(root, text="Дата выдачи:")
passport_issue_date_label.config(font=FONT)
passport_issue_date_label.place(relx=0.14, rely=0.28, anchor='nw')

passport_issue_date_text = tk.StringVar()
passport_issue_date_text.set("ДД.ММ.ГГГГ")
passport_issue_date_entry = tk.Entry(root, textvariable=passport_issue_date_text, width=10, font=FONT)
passport_issue_date_entry.place(relx=0.37, rely=0.28, anchor='nw')

kod_podrazdelenia_label = tk.Label(root, text="Код подразделения:")
kod_podrazdelenia_label.config(font=FONT)
kod_podrazdelenia_label.place(relx=0.54, rely=0.28, anchor='nw')

kod_podrazdelenia_entry = tk.Entry(root, width=15, font=FONT)
kod_podrazdelenia_entry.place(relx=0.79, rely=0.28, anchor='nw')

who_issued_passport_label = tk.Label(root, text="Где выдан:")
who_issued_passport_label.config(font=FONT)
who_issued_passport_label.place(relx=0.14, rely=0.35, anchor='nw')

who_issued_passport_entry = tk.Entry(root, width=44, font=FONT)
who_issued_passport_entry.place(relx=0.37, rely=0.35, anchor='nw')

residential_address_label = tk.Label(root, text="Адрес регистр:")
residential_address_label.config(font=FONT)
residential_address_label.place(relx=0.14, rely=0.42, anchor='nw')

residential_address_entry = tk.Entry(root, width=44, font=FONT)
residential_address_entry.place(relx=0.37, rely=0.42, anchor='nw')

property_type_label = tk.Label(root, text="Тип имущества:")
property_type_label.config(font=FONT)
property_type_label.place(relx=0.55, rely=0.48, anchor='nw')

property_type_text = tk.StringVar()
property_type_text.set("квартира")
property_type_drop = tk.OptionMenu(root, property_type_text, "квартира", "комната", "нежилое помещение", "жилой дом",
                                   "земельный участок")
property_type_drop.config(font=FONT)
property_type_drop.place(relx=0.75, rely=0.47, anchor='nw')

property_address_label = tk.Label(root, text="Адресс имущества:")
property_address_label.config(font=FONT)
property_address_label.place(relx=0.0, rely=0.48, anchor='nw')

property_address_entry = tk.Entry(root, width=23, font=FONT)
property_address_entry.place(relx=0.23, rely=0.48, anchor='nw')

deposit_sum_label = tk.Label(root, text="Сумма задатка «Потенциальному продавцу»:")
deposit_sum_label.config(font=FONT)
deposit_sum_label.place(relx=0.0, rely=0.55, anchor='nw')

deposit_sum_entry = tk.Entry(root, width=20, font=FONT)
deposit_sum_entry.place(relx=0.50, rely=0.55, anchor='nw')

rubley_label = tk.Label(root, text="руб;")
rubley_label.config(font=FONT)
rubley_label.place(relx=0.75, rely=0.55, anchor='nw')

agent_name_label = tk.Label(root, text="ФИО агента:")
agent_name_label.config(font=FONT)
agent_name_label.place(relx=0.0, rely=0.62, anchor='nw')

agent_name_entry = tk.Entry(root, width=15, font=FONT)
agent_name_entry.place(relx=0.15, rely=0.62, anchor='nw')

fees_label = tk.Label(root, text="Вознаграждение Риэлтора:")
fees_label.config(font=FONT)
fees_label.place(relx=0.39, rely=0.62, anchor='nw')

fees_entry = tk.Entry(root, width=20, font=FONT)
fees_entry.place(relx=0.68, rely=0.62, anchor='nw')

rubley_label = tk.Label(root, text="руб;")
rubley_label.config(font=FONT)
rubley_label.place(relx=0.93, rely=0.62, anchor='nw')

pre_fees_label = tk.Label(root, text="Вознагр. при подп:")
pre_fees_label.config(font=FONT)
pre_fees_label.place(relx=0.0, rely=0.69, anchor='nw')

pre_fees_entry = tk.Entry(root, width=15, font=FONT)
pre_fees_entry.place(relx=0.22, rely=0.69, anchor='nw')

rubley_label = tk.Label(root, text="руб;")
rubley_label.config(font=FONT)
rubley_label.place(relx=0.41, rely=0.69, anchor='nw')

end_fees_label = tk.Label(root, text="Вознагр. остаток:")
end_fees_label.config(font=FONT)
end_fees_label.place(relx=0.49, rely=0.69, anchor='nw')

end_fees_entry = tk.Entry(root, width=15, font=FONT)
end_fees_entry.place(relx=0.70, rely=0.69, anchor='nw')

rubley_label = tk.Label(root, text="руб;")
rubley_label.config(font=FONT)
rubley_label.place(relx=0.89, rely=0.69, anchor='nw')

contract_end_day_label = tk.Label(root, text="Договор действителен до:")
contract_end_day_label.config(font=FONT)
contract_end_day_label.place(relx=0.0, rely=0.76, anchor='nw')

end_day = tk.StringVar()
end_day.set("01")
end_day_drop = tk.OptionMenu(root, end_day, "01", "02", "03", "04", "05", "06", "07",
                             "08", "09", "10", "11", "12", "13", "14", "15", "16", "17", "18", "19", "20", "21", "22"
                             , "23", "24", "25", "26", "27", "28", "29", "30", "31")
end_day_drop.config(font=FONT)
end_day_drop.place(relx=0.29, rely=0.75, anchor='nw')

end_month_label = tk.Label(root, text="Месяц")
end_month_label.config(font=FONT)
end_month_label.place(relx=0.36, rely=0.76, anchor='nw')

end_month = tk.StringVar()
end_month.set("января")
end_month_drop = tk.OptionMenu(root, end_month, "января", "февраля", "марта", "апреля", "мая", "июня", "июля",
                               "августа", "сентября", "октября", "ноября", "декабря")
end_month_drop.config(font=FONT)
end_month_drop.place(relx=0.44, rely=0.75, anchor='nw')

end_year_label = tk.Label(root, text="Год")
end_year_label.config(font=FONT)
end_year_label.place(relx=0.56, rely=0.76, anchor='nw')

end_year_text = tk.StringVar()
end_year_text.set("2020")
end_year_drop = tk.OptionMenu(root, end_year_text, "2020", "2021", "2022", "2023", "2024", "2025", "2026",
                              "2027", "2028", "2029", "2030")
end_year_drop.config(font=FONT)
end_year_drop.place(relx=0.62, rely=0.75, anchor='nw')

phone_label = tk.Label(root, text="Телефон:")
phone_label.config(font=FONT)
phone_label.place(relx=0.0, rely=0.82, anchor='nw')

phone_entry = tk.Entry(root, width=15, font=FONT)
phone_entry.place(relx=0.1, rely=0.82, anchor='nw')

email_label = tk.Label(root, text="Email:")
email_label.config(font=FONT)
email_label.place(relx=0.0, rely=0.89, anchor='nw')

email_entry = tk.Entry(root, width=15, font=FONT)
email_entry.place(relx=0.10, rely=0.89, anchor='nw')


def get_property_gender(property_type):
    if property_type == ("квартира" or "комната"):
        return "расположенная"
    elif property_type == "нежилое помещение":
        return "расположенное"
    elif property_type == ("жилой дом" or "земельный участок"):
        return "расположенный"


def get_sex_gender(sex):
    if sex == "М":
        return "именуемый"
    elif sex == "Ж":
        return "именуемая"


doc = SaleAgreement()

save_doc = tk.Button(root, padx=50, fg="red", pady=20, text="Сохранить договор", command=lambda: doc.save_doc(
    full_name_entry.get(),
    agent_name=agent_name_entry.get(), property_address=property_address_entry.get(),
    contract_number=contract_number_entry.get(), who_issued_passport=who_issued_passport_entry.get(),
    deposit_sum=deposit_sum_entry.get(), locality=locality_entry.get(), passport_release_date=
    passport_issue_date_entry.get(), kod_podrazdelenia=kod_podrazdelenia_entry.get(), contract_end_month=
    end_month.get(), residential_address=residential_address_entry.get(), passport_series=passport_series_entry.get(),
    email=email_entry.get(), raspoloshenii_aya=get_property_gender(property_type_text.get()),
    contract_end_day=end_day.get(),
    month=month_text.get(), end_fees=end_fees_entry.get(), passport_number=passport_number_entry.get(),
    todays_year=year_text.get(), fees=fees_entry.get(), property_type=property_type_text.get(),
    birth_date=date_of_birth_entry.get(), todays_day=today_day.get(), full_name=full_name_entry.get(),
    pre_fees=pre_fees_entry.get(), phone=phone_entry.get(), contract_end_year=end_year_text.get(),
    imenuyemi_aya=get_sex_gender(sex.get())))
save_doc.place(relx=0.30, rely=0.85, anchor='nw')

root.mainloop()
