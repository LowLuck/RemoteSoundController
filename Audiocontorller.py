from pycaw.pycaw import AudioUtilities, ISimpleAudioVolume
from audiocontrollerclass import AudioController


def main():
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


if __name__ == "__main__":
    q = main()
    p = sys_clear(q[1])
    print('Processes in work')
    print(p)
    print('Choose a process to work')
    w = input()
    audio_controller = AudioController(w)
    print(f'\n'
          f'WARNING! Values are percentages of master volume! \n'
          f'1 -- sound equals to master, 0.5 half of main etc. \n'
          f'up <number> -- increase <percent> \n'
          f'down <number> --  decrease <percent> \n'
          f'mute -- mute \n'
          f'unmute -- unmute \n'
          f'stop -- stop the program')
    while True:
        w = input()
        if w == 'stop':
            break
        elif w[:2] == 'up':
            num = w[3:]
            audio_controller.increase_volume(float(num))
        elif w[:4] == 'down':
            num = w[5:]
            audio_controller.decrease_volume(float(num))
        elif w[:4] == 'mute':
            audio_controller.mute()
        elif w[:6] == 'unmute':
            audio_controller.unmute()
        else:
            print('Command not found')
    print('Exit')
