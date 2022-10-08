
# For downloading python we use a library named pytube 
# Why we use this ?

'''
1. It supports both Progressive (it can be stracted and squashed into different screen sizes) and Dash Streams (high quality streaming of media content over the internet)
2. Command-line interface included 
3. Outputs caption tracks to .srt format
4. Ability to capture thumbnail URL
5. Extensively Documented Source Code
6. No third-party dependencies
'''
from tkinter import *

from pytube import YouTube

def on_progress (stream, chunk, bytes_remaining):
    print('progress:', bytes_remaining, "      ", end ='\r', flush=True)

def on_complete(stream, filename):
    print()
    print('-----Completed-----')
    print('stream:', stream)
    print('filename:', filename)

def rgb_hack(rgb):
     return "#%02x%02x%02x" % rgb  

''' ----------------------------------------------------------------------- '''

''' We have to create an API Window '''
# to create display window Tk() is used to initialize tkinter
root = Tk()
# geometry() used to set the window’s width and height
root.geometry('500x300') 
# resizable(0,0) is used to set the fix size of window adjustable with its features
root.resizable(0, 0) 
# title() is used to give the title of window


root.title('youtube downloader')
root.config(bg=rgb_hack((118,238,198)))
SAVE_PATH = "E:\Python programming" #to_do
#output path
# OUTPUT_PATH = "E:\Python programming"

''' ----------------------------------------------------------------------- '''
# We have to create a Link Entry where we have to paste the link
'''
1. Label() widget is used to display text that users can’t be able to modify.
2. root is the name of the window
3. text which we display the title of the label
4. font in which our text is written
5. pack organized widget in block
'''
Label(root, text="Download Youtube videos for free", font='san-serif 14 bold').pack()
link = StringVar() # Specifying the variable type
Label(root, text="Paste your link here", font='san-serif 15 bold').place(x=150, y=55)
link_enter = Entry(root, width=70, textvariable=link).place(x=30, y=90)


def download(): 

    url =YouTube(str(link.get()))
    
    url.download()
    Label(root, text = 'DOWNLOADED', font = 'arial 15').place(x= 180 , y = 210)  
    url.register_on_progress_callback(on_progress)
    url.register_on_complete_callback(on_complete)
    res = input('resolution(720p/360p):')
    

Button(root,text = 'DOWNLOAD', font = 'arial 15 bold' ,bg = 'pale violet red', padx = 2, command = "download").place(x=180 ,y = 150)

root.mainloop()

