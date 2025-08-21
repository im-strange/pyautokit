# ANSI escape code reset
RESET = "\033[0m"

# Foreground colors
def black(text):   return f"\033[30m{text}{RESET}"
def red(text):     return f"\033[31m{text}{RESET}"
def green(text):   return f"\033[32m{text}{RESET}"
def yellow(text):  return f"\033[33m{text}{RESET}"
def blue(text):    return f"\033[34m{text}{RESET}"
def magenta(text): return f"\033[35m{text}{RESET}"
def cyan(text):    return f"\033[36m{text}{RESET}"
def white(text):   return f"\033[37m{text}{RESET}"

# Bright foreground colors
def bright_black(text):   return f"\033[90m{text}{RESET}"
def bright_red(text):     return f"\033[91m{text}{RESET}"
def bright_green(text):   return f"\033[92m{text}{RESET}"
def bright_yellow(text):  return f"\033[93m{text}{RESET}"
def bright_blue(text):    return f"\033[94m{text}{RESET}"
def bright_magenta(text): return f"\033[95m{text}{RESET}"
def bright_cyan(text):    return f"\033[96m{text}{RESET}"
def bright_white(text):   return f"\033[97m{text}{RESET}"

# Background colors
def bg_black(text):   return f"\033[40m{text}{RESET}"
def bg_red(text):     return f"\033[41m{text}{RESET}"
def bg_green(text):   return f"\033[42m{text}{RESET}"
def bg_yellow(text):  return f"\033[43m{text}{RESET}"
def bg_blue(text):    return f"\033[44m{text}{RESET}"
def bg_magenta(text): return f"\033[45m{text}{RESET}"
def bg_cyan(text):    return f"\033[46m{text}{RESET}"
def bg_white(text):   return f"\033[47m{text}{RESET}"

# Bright background colors
def bg_bright_black(text):   return f"\033[100m{text}{RESET}"
def bg_bright_red(text):     return f"\033[101m{text}{RESET}"
def bg_bright_green(text):   return f"\033[102m{text}{RESET}"
def bg_bright_yellow(text):  return f"\033[103m{text}{RESET}"
def bg_bright_blue(text):    return f"\033[104m{text}{RESET}"
def bg_bright_magenta(text): return f"\033[105m{text}{RESET}"
def bg_bright_cyan(text):    return f"\033[106m{text}{RESET}"
def bg_bright_white(text):   return f"\033[107m{text}{RESET}"

# Text styles
def bold(text):      return f"\033[1m{text}{RESET}"
def dim(text):       return f"\033[2m{text}{RESET}"
def italic(text):    return f"\033[3m{text}{RESET}"
def underline(text): return f"\033[4m{text}{RESET}"
def blink(text):     return f"\033[5m{text}{RESET}"
def reverse(text):   return f"\033[7m{text}{RESET}"
def hidden(text):    return f"\033[8m{text}{RESET}"
def strike(text):    return f"\033[9m{text}{RESET}"
