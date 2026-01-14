from gui.controller import App

from gui.pages.main_menu import MainMenu
from gui.pages.program import Program
from gui.pages.select_msg import SelectMsg
from gui.pages.view_recordings import ViewRecordings
from gui.pages.status_report import StatusReport
from gui.pages.system_reboot import SystemReboot
from gui.pages.control import Control

def main():
    
    app = App()

    app.register(MainMenu)
    app.register(Program)
    app.register(SelectMsg)
    app.register(ViewRecordings)
    app.register(StatusReport)
    app.register(SystemReboot)
    app.register(Control)

    app.show_frame("MainMenu")
    app.mainloop()

if __name__ == "__main__":
   main()