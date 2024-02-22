# -*- coding UTF-8 -*-
# КОММАНДА: SHOW-META
# АВТОР: Rohit Alderson
# DATE: Thursday, 21 February 2024 г. 03:39:15 (+03)

from src.config import COLOR_CODE, GLOBAL_SOFT_INFO, print_banner, print_welcome_text
from src.httpweb_number import HttpWebNumber
from src.blocked_countries import BlockedCountries
from src.update.update import Update
from src.noblack_auto import print_noblack_auto_text
from time import sleep
import requests
import bs4

if name == "main":
    # Показ текст соглашении
    print_welcome_text()

    while True:
        # Показ баннера
        print_banner()

        # Меню управления
        print(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[1] {COLOR_CODE["GREEN"]}'
            f'Поиск {COLOR_CODE["PINK"]}по номеру{COLOR_CODE["GREEN"]} телефона{COLOR_CODE["RESET"]}\n'
            
            f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[2] {COLOR_CODE["GREEN"]}'
            f'Провести техническую проверку {COLOR_CODE["PINK"]}на работоспосбность сервиса{COLOR_CODE["GREEN"]}{COLOR_CODE["RESET"]}\n')

        try:
        
            # Выбор варианта поиска
            user_chooice = input(f'{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[–] {COLOR_CODE["LI_G"]}'
                f'Выберите вариант поиска: {COLOR_CODE["RESET"]}').strip()
            
            # Поиск по номеру телефона
            if not user_chooice or user_chooice == "1":
                httpweb_number = HttpWebNumber()
                httpweb_number.print_number_results
                sleep(3)

            # Проверка тех. части
            elif user_chooice == "2":
                # Проверка на блокировку
                BlockedCountries().print_ip_result()
                
                # Проверка обновлении
                Update().get()
                
                input(f'\n{COLOR_CODE["CYAN"]}{COLOR_CODE["BOLD"]}[{COLOR_CODE["RED"]}!{COLOR_CODE["CYAN"]}] {COLOR_CODE["LI_G"]}' + 
                  f'Чтобы вернуться назад, нажмите{COLOR_CODE["DARK"]} {COLOR_CODE["RESET"]}ENTER ')

            # Повторный опрос
            else: continue

        except KeyboardInterrupt:
            print(f'\n{COLOR_CODE["RED"]}[!] {COLOR_CODE["YELLOW"]}Вынужденная остановка работы! {COLOR_CODE["RESET"]}\n')
            break
