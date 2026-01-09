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
                config.debug_success('The service is stopped')
            
            elif(result.returncode == 1062):
                config.debug_warning('The service is\'t stopped. The service may have been stopped earlier')

            else:
                config.debug_error(f'Error with the service stop, code: {result.returncode}')
                print(result.stderr.strip())
        else:
            config.debug_warning('Run the application as an administrator!')

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
                config.debug_success(f'The service start type changed on: {start_type}')
            
            else:
                config.debug_error(f'Error with the service stop, code: {result.returncode}')
                print(result.stderr.strip())
        else:
            config.debug_warning('Run the application as an administrator!')

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
        
        config.debug_success('Registry was changed')

    except Exception as e:
        config.debug_error(e)
