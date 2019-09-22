from os import system, name
from time import sleep

def autoModuleInstall(modName):
    input("Going to install the missing packages. Please make sure that you are connected to the internet before pressing any other key")
    modQuery = "pip3 install "+str(modName)
    system(modQuery)
    input("Press any key to continue...")

try:
    import pyperclip
except (ImportError, ModuleNotFoundError) as moduleName:
    print("The following packages are not available")
    print(moduleName.name)
    x = input("1.Auto install\nAny other key to exit\n")
    if x == "1": autoModuleInstall(moduleName.name)
    else: exit()

class pyclip:
    def clrscr(self): system("clear") if name is not "nt" else system("cls")
    def pause(self, mes="Please press any key to continue"): input(mes)
    
    def __init__(self):
        self.clipContent = []
        self.refTimer = 1

    def clipMain(self):
        self.clrscr()
        x,rec = input("""PyClip Settings
1.Change refresh timer
0.Exit
00.Go back
"""),0
        if x == "1": self.pyClipTimer()
        elif x == "0": self.pyClipExit()
        elif x == "00": rec = 1
        else:
            print("Invalid Input!")
            self.pause()
        self.clipMain() if rec == 0 else 0

    def pyClipTimer(self):
        self.clrscr()
        self.refTimer = int(input("Enter the refresh timer in integer "))

    def pyClipExit(self):
        self.clrscr()
        print("Thank you for using PyClip!")
        sleep(2)
        self.clrscr()
        exit()

    def clip(self):
        self.clrscr()
        try:
            print("Catching clipboard data")
            sleep(1)
        except KeyboardInterrupt:
            self.clipMain()
            self.clip()
        self.clip()

startClip = pyclip()
startClip.clip()