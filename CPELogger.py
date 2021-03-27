
import PySimpleGUI as sg
import csv as csv
import os as os

sg.theme('Light Blue 2')

layout = [
          [sg.Text('Select File')],
          [ sg.Input(), sg.FileBrowse()],
          [sg.Text('Select Starting Date')],
          [sg.CalendarButton('Date',format='%m-%d-%y')],
          [sg.Text('Enter AZBOA Site credentials')],
          [sg.Text('Email:'),sg.InputText()],
          [sg.Text('Pasword'),sg.InputText()],
          [sg.Text('Choose Browser')],
          [sg.InputCombo(('Chrome'),size=(20,20))],
          [sg.Submit(), sg.Cancel(), sg.Exit() ] 
          ]

window = sg.Window('CPE Logger', layout)

event, values = window.read()
window.close()
print(f'You clicked {event}')
print(f'You chose filenames {values[0]}')