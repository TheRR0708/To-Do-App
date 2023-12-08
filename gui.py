import PySimpleGUI as sg
import tkinter as tk

label1 = sg.Text("Select file to compress:")
output_text1 = sg.Input()
add_button1 = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination folder:")
output_text2 = sg.Input()
add_button2 = sg.FolderBrowse("Choose")

compress_button  = sg.Button("Compress")

window = sg.Window("File Zipper", layout= [[label1,output_text1,add_button1]
                                           ,[label2,output_text2, add_button2],[compress_button]])
window.read()
window.close()