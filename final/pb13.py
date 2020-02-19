import sys

T = [
'.-',
'-...',
'-.-.',
'-..',
'.',
'..-.',
'--.',
'....',
'..',
'.---',
'-.-',
'.-..',
'--',
'-.',
'---',
'.--.',
'--.-',
'.-.',
'...',
'-',
'..-',
'...-',
'.--',
'-..-',
'-.--',
'--..'
]


def palin(s):
    n = len(s)
    m = n//2
    for i in range(m):
        if s[i] != s[n-i-1]:
            return False
    return True


def morse(s):
    n = len(s)
    t = ''
    for i in range(n):
        t += T[ord(s[i]) - ord('A')]
    return t


for s in sys.stdin:
    s = s[:-1]
    pal1 = palin(s)
    m = morse(s)
    pal2 = palin(m)
    if pal1:
        if pal2:
            print('SUPERPALINDROM')
        else:
            print('PALINDROM')
    else:
        if pal2:
            print('PALINDROM DE MORSE')
        else:
            print('RES')
