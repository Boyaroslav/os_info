import os, random

os_names = {
    'alpine': 'ascii/alpine',
    'ansroid': 'ascii/android',
    'arch': 'ascii/arch',
    'debian': 'ascii/debian',
    'fedora': 'ascii/fedora',
    'kali': 'ascii/kali',
    'manjaro': 'ascii/manjaro',
    'parrot': 'ascii/parrot',
    'slackware': 'ascii/slackware',
    'xubuntu': 'ascii/xubuntu',
    'ubuntu': 'ascii/ubuntu'}



class os_info():
    def __init__(self):
        self.distro_name = os.popen('cat /etc/*-release | grep "PRETTY_NAME"', 'r').read()


    def distro(self):
        return self.distro_name[self.distro_name.index('=') + 1::][1:-2]


    def architecture(self):
        return os.popen('uname -m', 'r').read().rstrip('\n')  #rstrip removes stupid \n at the end

    
    def sys_time(self, date_or_time=0, beauty=0):
        #  beauty argument allows to return time in beautiful way
        #  date_or_time allows to return "year month day" or "hours minutes seconds"
        if not date_or_time:
            ans = os.popen('date +"%H %M %S"').read()
        else:
            ans = os.popen('date +"%Y %m %d"').read()
        if beauty:
            ans = ans.split()
            ans = f"{ans[0]}:{ans[1]}:{ans[2]}" 
        
        return ans


    def ascii_logo(self, name=None):
        #  if you want custom ascii, include it in argument
        if not name:
            name = self.distro()
        key = 0
        if random.randint(0, 1):
            path = 'ascii/other'
        else:
            path = 'ascii/coca-cola'
        for i in os_names:
            if i in name.lower() and not key:
                path = os_names[i]
                key = 1

        #  reading askii logo
        ascii = open(path, 'r').readlines()
        for i in range(0, len(ascii)):
            ascii[i] = ascii[i].rsplit('\n')

        return ascii
        