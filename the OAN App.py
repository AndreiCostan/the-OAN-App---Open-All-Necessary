import os, time, locale, getpass
import pyperclip as pc
from datetime import date

def open_targeted_folder(folders):
    for folder in folders:
        try:
            os.startfile(folder)
            time.sleep(0.5)
        except:
            print(f'Error!  {folder}  not found!')

def open_targeted_apps(apps):
    for app in apps:
        try:
            os.startfile(app)
            time.sleep(1)
        except:
            print(f'Error!  {app}  not found!')

def open_targeted_excels(excels):
    for excel in excels:
        try:
            os.startfile(excel)
            time.sleep(5)
        except:
            print(f'Error!  {excel}  not found!')

locale.setlocale(locale.LC_TIME, 'ro_RO')
year = date.today().year
month = date.today().strftime('%m.%B').capitalize()
today = date.today().strftime('%d.%m')
pc.copy('Password_Example_forApp1')

folders_tuple = (
    f'D:\\{year}\\{month}\\{today}',
    f'D:\\{year}\\{month}\\{today}\\folder 2',
    f'C:\\Users\\{getpass.getuser()}\\Desktop\\Folder Example 1',
    f'C:\\Users\\{getpass.getuser()}\\Desktop\\Folder Example 2',
    f'D:\\Work',
    f'D:\\Tools',
    f'D:\\_Employee One Devs\\_temp'
)

apps_tuple = (
    f'outlook',
    f'C:\\Program Files (x86)\\WinSCP\\WinSCP.exe',
    f'C:\\Program Files\\Mozilla Firefox\\firefox.exe',
    f'C:\\Program Files\\Notepad++\\notepad++.exe',
    f'C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\App Example 1\\App1.exe',
    f'C:\\Users\\{getpass.getuser()}\\AppData\\Roaming\\App Example 2\\App2.exe'
)

excels_tuple = (
    f'D:\\Tools\\Excel 1.xlsx',
    f'D:\\Tools\\Excel 2.xlsx',
    f'D:\\Tools\\Excel 3.xlsx',
    f'D:\\Tools\\Excel 4.xlsx',
    f'D:\\Employees\\Employee One\\Misc\\Excel 5.xlsx',
    f'D:\\Employees\\Employee One\\Misc\\Excel 6.xlsx',
    f'D:\\Employees\\Employee One\\Misc\\Excel 7.xlsx',
    f'D:\\Tools\\Excel 8.xlsx'
)

if __name__ == "__main__":
    open_targeted_folder(folders_tuple)
    open_targeted_apps(apps_tuple)
    open_targeted_excels(excels_tuple)

locale.setlocale(locale.LC_TIME, 'en_EN')