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
    print('Рабочие процессы')
    print(p)
    print('Напишите название процесса, звук которого нужно именить')
    w = input()
    audio_controller = AudioController(w)
    print(f'\n'
          f'ВНИМАНИЕ! Звук в процентах от основного звука компьютера! \n'
          f'1 -- равен основному звуку, 0.5 половина от основного и т.д \n'
          f'up <number> -- увеличить громкость на <процент> \n'
          f'down <number> -- понизить громкость на <процент> \n'
          f'mute -- заглушить \n'
          f'unmute -- разглушить \n'
          f'stop -- выход')
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
