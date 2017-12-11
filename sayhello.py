from subprocess import call


def hello():
    cmd_beg = 'espeak -ven-us+f1 -s200 -a200 -p80 '
    cmd_end = ' 2>/dev/null'
    
    
    message = '"Hello world"'
    
    
    call([cmd_beg+message+cmd_end], shell=True)
