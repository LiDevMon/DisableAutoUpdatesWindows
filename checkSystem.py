import platform
import subprocess
import config
import winreg

import os
import ctypes

def checkWindowsVersion() -> int:
    """
    Check windows version and return number

    :rtype: int
    """

    if(platform.system().lower() == "windows"):
        return int(platform.release())

def is_admin() -> bool:
    try:
        return os.getuid() == 0
    except AttributeError:
        return ctypes.windll.shell32.IsUserAnAdmin() != 0

def stopUpdateService(service_name:str) -> None:
    try:
        if is_admin():
            result = subprocess.run(['sc', 'stop', service_name], capture_output=True, text=True, check=False)

            if(result.returncode == 0):
                config.debug_success('Служба успешно остановлена')
            
            elif(result.returncode == 1062):
                config.debug_warning('Служба не запущена. Скорее всего она была остановлена ранее.')

            else:
                config.debug_error(f'Ошибка при остановке службы код: {result.returncode}')
                print(result.stderr.strip())
        else:
            config.debug_warning('Запустите программу от имени администратора!')

    except Exception as e:
        config.debug_error(e)

def changeServiceStartType(service_name:str, start_type:str) -> None:
    """
    Docstring for changeServiceStartType
    
    :param service_name: Service name for change start type
    :type service_name: str
    :param start_type: auto, disabled, demand
    :type start_type: str
    """

    try:
        if is_admin():
            result = subprocess.run(['sc', 'config', service_name, 'start=', start_type], capture_output=True, text=True, check=False)

            if(result.returncode == 0):
                config.debug_success(f'Тип запуска службы изменён на {start_type}')
            
            else:
                config.debug_error(f'Ошибка при остановке службы код: {result.returncode}')
                print(result.stderr.strip())
        else:
            config.debug_warning('Запустите программу от имени администратора!')

    except Exception as e:
        config.debug_error(e)

def regeditDisableUpdate(key_name:str, value:str, key_type:winreg.HKEYType, path:str) -> None:
    """
    Docstring for regeditDisableUpdate
    
    :param key_name: Name for key
    :type key_name: str
    :param value: Key value
    :type value: str
    :param key_type: Key type (winreg.REG_SZ for example)
    :type key_type: winreg.HKEYType
    :param path: Path to put key
    :type path: str
    """
    try:
        with winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, path, 0, access=winreg.KEY_ALL_ACCESS) as key:
            winreg.SetValueEx(key, key_name, 0, key_type, value)
        
        config.debug_success('Реестр изменён')

    except Exception as e:
        config.debug_error(e)
