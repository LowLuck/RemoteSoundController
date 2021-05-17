from pycaw.pycaw import AudioUtilities
from audiocontrollerclass import AudioController


class AudiocontrollerCode:
    def __init__(self):
        self.q = None
        self.p = None
        self.processname = ''

    def process_get(self):
        sessions = AudioUtilities.GetAllSessions()
        s = []
        s2 = []
        for session in sessions:
            s.append(session)
            s2.append(str(session))
        return s, s2

    def sys_clear(self, lis):
        s = []
        for j in lis:
            if j[:12] != 'DisplayName:':
                s.append(j)
        return s

    def refresh(self, first=True):
        self.q = self.process_get()
        self.p = self.sys_clear(self.q[1])
        if first:
            print(self.p)
        return [j.Process.name() for j in self.q[0] if j.Process]

    def work_start(self):
        print(f'\n'
              f'WARNING! Values are percentages of master volume! \n'
              f'1 -- sound equals to master, 0.5 half of main etc. \n'
              f'up <number> -- increase <percent> \n'
              f'down <number> --  decrease <percent> \n'
              f'half -- half of volume \n'
              f'full -- max volume \n'
              f'mute -- mute \n'
              f'unmute -- unmute \n'
              f'stop -- stop the program')

    # not in use
    #     audio_controller = AudioController(self.processname)
    #     while True: # DO NOT FORGET TO ADD NEW FUNCTIONS TO CLIENT!
    #         # w = input().split()
    #         if w[0] == 'stop':
    #             break
    #         elif w[0] == 'up':
    #             num = w[1]
    #             audio_controller.increase_volume(float(num))
    #         elif w[0] == 'down':
    #             num = w[1]
    #             audio_controller.decrease_volume(float(num))
    #         elif w[0] == 'half':
    #             audio_controller.set_volume(0.5)
    #         elif w[0] == 'full':
    #             audio_controller.set_volume(1)
    #         elif w[0] == 'mute':
    #             audio_controller.mute()
    #         elif w[0] == 'unmute':
    #             audio_controller.unmute()
    #         else:
    #             print('Command not found')
    #     print('Exit')
    #     return

    def serverwork(self, into):
        w = into.split()
        audio_controller = AudioController(self.processname)
        while True:  # DO NOT FORGET TO ADD NEW FUNCTIONS TO CLIENT!
            if w[0] == 'stop':
                break
            elif w[0] == 'up':
                num = w[1]
                audio_controller.increase_volume(float(num))
            elif w[0] == 'down':
                num = w[1]
                audio_controller.decrease_volume(float(num))
            elif w[0] == 'half':
                audio_controller.set_volume(0.5)
            elif w[0] == 'full':
                audio_controller.set_volume(1)
            elif w[0] == 'mute':
                audio_controller.mute()
            elif w[0] == 'unmute':
                audio_controller.unmute()
            else:
                print(w)
                # print('Command not found')

    def main_start(self):
        namelist = self.refresh(False)
        print('Processes in work (type refresh to refresh)')
        print(self.p)
        print('Choose a process to work')

        while True:
            w = input()
            if w in namelist:
                self.processname = w
                self.work_start()
                break
            else:
                print('Process not found')
                namelist = self.refresh()

    def get_process(self):
        if self.processname:
            return self.processname
        else:
            return False

    def set_process(self, processname):
        self.processname = processname


if __name__ == '__main__':
    Class = AudiocontrollerCode()
    Class.main_start()
