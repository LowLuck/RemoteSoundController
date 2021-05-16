from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from audiocontrollerclass import AudioController


def starter():
    sessions = AudioUtilities.GetAllSessions()
    s = []
    s2 = []
    for session in sessions:
        s.append(session)
        s2.append(str(session))
    return s, s2


def sys_clear(lis):
    s = []
    for j in lis:
        if j[:12] != 'DisplayName:':
            s.append(j)
    return s


def refresh(start=True):
    global q, p
    q = starter()
    p = sys_clear(q[1])
    if start:
        print(p)
    return [j.Process.name() for j in q[0] if j.Process]


def main(w):
    audio_controller = AudioController(w)
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
    while True:
        w = input().split()
        if w == 'stop':
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
            print('Command not found')
    print('Exit')
    return


if __name__ == "__main__":
    q = None
    p = None
    namelist = refresh(False)
    print('Processes in work (type refresh to refresh)')
    print(p)
    print('Choose a process to work')

    while True:
        w = input()
        if w in namelist:
            main(w)
            break
        else:
            print('Process not found')
            namelist = refresh()