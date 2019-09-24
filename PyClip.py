from os import system, name
from time import sleep

def autoModuleInstall(modName):
    input("Going to install the missing packages. Please make sure that you are connected to the internet before pressing any other key")
    modQuery = "pip3 install "+str(modName)
    system(modQuery)
    input("Press any key to continue...")

try:
    import pyperclip as cb
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
        self.clrscr()
        self.clipContent = []
        self.refTimer = 1

    def clipMain(self):
        self.clrscr()
        x,rec = input("""PyClip Settings
1.Change refresh timer
2.View caught data
3.Select caught data
4.Delete caught data
0.Exit
00.Go back
"""),0
        if x == "1": self.pyClipTimer()
        elif x == "2": self.clipView()
        elif x == "3": self.clipSelect()
        elif x == "4": self.clipDelete()
        elif x == "0": self.pyClipExit()
        elif x == "00": rec = 1
        else:
            print("Invalid Input!")
            self.pause()
        self.clipMain() if rec == 0 else 0

    def pyClipTimer(self):
        self.clrscr()
        try: self.refTimer = int(input("Enter the refresh timer in integer "))
        except ValueError:
            print("Please enter an integer!")
            self.pause()
            self.pyClipTimer()

    def pyClipExit(self):
        self.clrscr()
        print("Thank you for using PyClip!")
        sleep(2)
        self.clrscr()
        exit()

    def clipView(self):
        self.clrscr()
        if self.clipContent: print("The data caught are as follows\n","\n".join([i for i in self.clipContent]))
        else: print("There is no data caught from your clipboard.")
        self.pause()

    def clipSelect(self):
        self.clrscr()
        rec = 0
        if self.clipContent is not []:
            for i,j in enumerate(self.clipContent):
                print(str(i)+"."+str(j))
            print(str(len(self.clipContent))+".Go back")
            try:
                x = int(input("Please select a value "))
                if x is len(self.clipContent): return
                cb.copy(self.clipContent[x])
            except ValueError:
                print("Please enter an integer")
                rec = 1
            except IndexError:
                print("The entered value does not exist!")
                rec = 1
        else: print("There is no data to select")
        self.pause()
        if rec == 1: self.clipSelect()

    def clipDelete(self):
        None

    def clip(self):
        try:
            if cb.paste() not in self.clipContent and cb.paste() is not "":
                self.clipContent.append(cb.paste())
                print(cb.paste(),"data caught")
            sleep(1)
        except KeyboardInterrupt:
            self.clipMain()
            self.clip()
        self.clip()

startClip = pyclip()
startClip.clip()