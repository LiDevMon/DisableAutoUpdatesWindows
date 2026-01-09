import checkSystem
from config import debug_error, debug_warning, debug_success, init, printLogo
from winreg import REG_DWORD

if __name__ == '__main__':
    init()
    
    printLogo()

    windowsVersion :int = checkSystem.checkWindowsVersion()
    print(f'\n\t\tWindows {windowsVersion}')

    if(windowsVersion == 10 or windowsVersion == 11):
        checkSystem.stopUpdateService('wuauserv')
        checkSystem.changeServiceStartType('wuauserv', 'disabled')
        checkSystem.regeditDisableUpdate('NoAutoUpdate', 1, REG_DWORD, r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate\AU')

    if(windowsVersion == 7):
        checkSystem.stopUpdateService('wuauserv')
        checkSystem.changeServiceStartType('wuauserv', 'disabled')
        checkSystem.regeditDisableUpdate('DisableOSUpgrade', 1, REG_DWORD, r'SOFTWARE\Policies\Microsoft\Windows\WindowsUpdate')

    print('Programm is complete!\n')
    print('Author:\n')
    print('https://github.com/LiDevMon', '\n')
    input('Press ENTER to extit')