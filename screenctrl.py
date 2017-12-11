from subprocess import call

def screen_off():
    call("sudo sh -c 'echo \"0\" > /sys/class/backlight/soc\:backlight/brightness'", shell=True)

def screen_on():
    call("sudo sh -c 'echo \"1\" > /sys/class/backlight/soc\:backlight/brightness'", shell=True)
