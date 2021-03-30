
import PySimpleGUI as sg
import selenium as sel
import parse_file as pf

sg.theme('Light Blue 2')

layout = [
          [sg.Text('Select File')],
          [sg.Input(key='-IN-'), sg.FileBrowse(target = ('-IN-'))],
          [sg.Text('Select Starting Date')],
          [sg.CalendarButton('Date',format='%m-%d-%y', key = '-DATE-', target = '-DATESELECTED-', enable_events=True), sg.In(enable_events = True, key = '-DATESELECTED-', size = (10, 1))],
          [sg.Text('Enter AZBOA Site credentials')],
          [sg.Text('ID:'),sg.InputText(key = '-ID-')],
          [sg.Text('Pasword'),sg.InputText(key = '-PASSWORD-')],
          [sg.Text('Choose Browser')],
          [sg.InputCombo(('Chrome','Mozilla'),size=(20,20), key = '-BROWSER-')],
          [sg.Submit(), sg.Cancel(), sg.Exit() ] 
          ]

window = sg.Window('CPE Logger', layout)


while True: #Event loop
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'Exit':
           break
    if event == 'Submit':
        #Get the pertinent data from the UI form
        file = values['Browse']
        date = values['-DATE-']
        date_selected = values['-DATESELECTED-']
        id = values['-ID-']
        password = values['-PASSWORD-']
        browser = values['-BROWSER-']
        print(file, date, id,password,browser)
        if (not browser or not file or not date_selected or not id or not password or not browser):
            sg.Popup('Yo, something missing',title = 'ERROR!!')
        else:
            login_dict = {}
            login_dict['file'] = file
            login_dict['date_selected'] = date_selected
            login_dict['id'] = id
            login_dict['password'] = password
            login_dict['browser'] = browser
            #print(login_dict)
            pf.run(login_dict)
            #pf.launch_browser()
            #pf.parse_file(file)




window.close()
