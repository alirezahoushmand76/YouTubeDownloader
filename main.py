import tkinter
import customtkinter
from pytube import YouTube

def startDownload():
    try:
        ytlink = link.get()
        ytObject = YouTube(ytlink,on_progress_callback=on_progress)
        video = ytObject.streams.get_highest_resolution()

        title.configure(text=ytObject.title, text_color="white")
        finishLabel.configure(text="")
        video.download()
        finishLabel.configure(text="Downloaded!")
    except:
        print("Youtube link is invalid!")
        finishLabel.configure(text="Download Error!", text_color="red")


def on_progress(stream, chunk, bytes_remaining):
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    percentage_of_completion = bytes_downloaded / total_size * 100
    print(percentage_of_completion)


#System Settings
customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

# Our app frame
app = customtkinter.CTK()
app.geometry("720x480")
app.title("Youtube Downloader")

#Adding UI Elements
title = customtkinter.CTKLabel(app, text="Insert a youtube link")
title.pack(padx=10, pady=10)

# Finish Downloading
finishLabel = customtkinter.CTkLabel(app,text="")
finishLabel.pack()

# Progress percentage
pPercentage = customtkinter.CTkLabel(app,text="0%")
pPercentage.pack()

progressBar = customtkinter.CTkProgressBar(app, width=400)
progressBar.set(0)
progressBar.pack(padx=10, pady=10)

#Link input
url_var = tkinter.StringVar()
link = customtkinter.CTkEntry(app, width=350, height=40, textvariable=url_var)
link.pack()

# Download Button
download = customtkinter.CTkButton(app, text="Download", command=startDownload)

#Run app
app.mainloop()

