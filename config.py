from colorama import init, Fore, Back, Style

def printLogo() -> None:
    print(
        """
         ,─.─.   ,───.                   
,─..─.─.╱  ╲==╲.──.'  ╲     .──.─. .─.─. 
│, ╲=╱╲=│─ │==│╲==╲─╱╲ ╲   ╱==╱ ─│╱=╱  │ 
│─ │╱ │╱ , ╱==╱╱==╱─│_╲ │  │==│ ,││=│ ─│ 
 ╲, ,     _│==│╲==╲,   ─ ╲ │==│─ │ =╱  │ 
 │ ─  ─  , │==│╱==╱ ─   ,│ │==│,  ╲╱ ─ │ 
  ╲  ,  ─ ╱==╱╱==╱─  ╱╲ ─ ╲│==│─   ,   ╱ 
  │─  ╱╲ ╱==╱ ╲==╲ _.╲=╲.─'╱==╱ , _  .'  
  `──`  `──`   `──`        `──`..───'    
"""
    )

def debug_warning(text: str) -> None:
    """
    Add colors and styles for warning log
    
    :param text: Text for print with style
    :type text: str
    """

    print(f'\n{Fore.YELLOW}{Style.BRIGHT}!# {text}{Style.RESET_ALL}\n')

def debug_error(text: str) -> None:
    """
    Add colors and styles for error log
    
    :param text: Text for print with style
    :type text: str
    """

    print(f'\n{Fore.RED}{Style.BRIGHT}!!! {text}{Style.RESET_ALL}\n')

def debug_success(text: str) -> None:
    """
    Add colors and styles for error log
    
    :param text: Text for print with style
    :type text: str
    """

    print(f'\n{Fore.GREEN}{Style.BRIGHT}# {text}{Style.RESET_ALL}\n')