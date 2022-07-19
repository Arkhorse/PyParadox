import PySimpleGUI as pysg

PROGRAMNAME = "Test"
buffoutversion = "1.24.0"
fallout4version = "222"
F4SEmods = [
    "Buffout 4",
    "Active Effects",
    "No Activate Lockpicking"
]

# Test version
def buffout4VersionHandle():
    expectedVersion = "1.24.0"
    actualVersion = "1.24.0"
    if expectedVersion == actualVersion:
        buffout4Color = "Green"
    elif expectedVersion != actualVersion:
        buffout4Color = "Red"
    else:
        buffout4Color = "Yellow"

    return buffout4Color

buffout4Color = buffout4VersionHandle()

def MainWindow():

    pysg.theme('DarkAmber')

    layout = [
        [pysg.Push(), pysg.Text(f'Wecome to {PROGRAMNAME}'), pysg.Push()],
        [pysg.Push(), pysg.Text(f'Current Fallout 4 Version:'), pysg.Text(f'{fallout4version}'), pysg.Text(f'Current Buffout 4 Version:'), pysg.Text(f'{buffoutversion}', text_color=buffout4Color), pysg.Push()],
        [pysg.Push(), pysg.Text('Loaded F4SE mods:'), pysg.Push()],
        [pysg.Push(), pysg.Listbox(values=F4SEmods, size=(25, 5) ), pysg.Push()],
        [pysg.Push(), pysg.Button('Ok'), pysg.Button('Close')]
    ]

    window = pysg.Window('Test', layout)

    return window

window = MainWindow()
while True:
    event, values = window.read()
    if event == pysg.WIN_CLOSED or event == 'Close':
        break

window.close()
