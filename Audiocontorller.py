from pycaw.pycaw import AudioUtilities
from audiocontrollerclass import AudioController


class AudiocontrollerCode:
    def __init__(self):
        self.q = None
        self.p = None
        self.processname = ''

    def process_get(self):
        sessions = AudioUtilities.GetAllSessions()
        objects = []
        strs = []
        for session in sessions:
            objects.append(session)
            strs.append(str(session))
        return objects, strs

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

    def serverwork(self, into):
        w = into.split()
        audio_controller = AudioController(self.processname)
        if w[0] == 'up':
            num = w[1]
            return audio_controller.increase_volume(float(num))
        elif w[0] == 'down':
            num = w[1]
            return audio_controller.decrease_volume(float(num))
        elif w[0] == 'half':
            return audio_controller.set_volume(0.5)
        elif w[0] == 'full':
            return audio_controller.set_volume(1)
        elif w[0] == 'mute':
            return audio_controller.mute()
        elif w[0] == 'unmute':
            return audio_controller.unmute()
        else:
            print('Command not found')
            print(w)

    def get_process(self):
        if self.processname:
            return self.processname
        else:
            return False

    def set_process(self, processname):
        self.processname = processname

