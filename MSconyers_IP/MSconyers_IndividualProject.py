# Import libraries
import requests
import urllib.request
import time
from bs4 import BeautifulSoup
import tkinter as tk


class App():  # Class for an instance of the application

    def __init__(self, master):  #main method

        master.title('MetaGrabber')  # sets title of the application
        canvas = tk.Canvas(master, height = 700, width = 1000)  #sets the default canvas size
        canvas.pack()

        frame = tk.Frame(master, bg='#80c1ff', bd = 4)  #creates frame for the entry box and run button
        frame.place(relx = 0.5, rely = 0, relwidth=1, relheight=0.1, anchor='n')

        self.button = tk.Button(frame, text="Run", font='helvetica', bg= 'gray', command=lambda:self.websiteCall(entry.get()))  # calls the websiteCall method that grabs the meta tags
        self.button.place(relx = 0.7, relheight = 1, relwidth = 0.3)

        self.urlLabel = tk.Label(frame, text = "Enter URL here:", font = 'helvetica', bg = "#80c1ff", justify = 'left')  # description box
        self.urlLabel.place( rely = 0, relwidth = 0.2, relheight = .5)

        entry = tk.Entry(frame, font = 40)  # creates entry field for website to be inputed
        entry.place(rely = .5,relwidth = 0.65, relheight = .5)

        lowerFrame = tk.Frame(master, bg='#80c1ff', bd = 5 )  # frame hold the output field
        lowerFrame.place(relx = 0.5, rely = 0.1, relwidth=1, relheight = 0.82, anchor='n')

        scrollbar = tk.Scrollbar(lowerFrame)  # allows for scrolling if list is too long to be viewed in window
        scrollbar.pack(side = 'right', fill = 'y')

        scrollbar2 = tk.Scrollbar(lowerFrame, orient = "horizontal") # allows for scrolling if list is too long to be viewed in window
        scrollbar2.pack(side = 'bottom', fill = 'x')

        self.txtBox =  tk.Text(lowerFrame,width = 500,font='helvetica', height = 400, yscrollcommand = scrollbar.set, xscrollcommand = scrollbar2.set, wrap = "none") # text box to hold outputed meta tags
        self.txtBox.pack(expand = 0, fill = 'both')

        scrollbar.config(command = self.txtBox.yview)
        scrollbar2.config(command = self.txtBox.xview)

        bottomFrame = tk.Frame(master, bg='#80c1ff', bd = 5)  # frame to hold web code and quit button
        bottomFrame.place(relx = 0.5, rely= 0.92, relwidth = 1, relheight = 0.08, anchor = 'n')

        self.quitButton = tk.Button(bottomFrame, text="Quit",font='helvetica', bg= 'gray', command = frame.quit)  # button to quit application
        self.quitButton.place(relx = 0.9,rely = 0.1, relheight = 0.64, relwidth = 0.1)

        self.codeLabel = tk.Label(bottomFrame, text = "Status Code:", width = 10, height = 1,font='helvetica', bg = "#80c1ff")  # description box
        self.codeLabel.place(relx = .001)

        self.codeBox = tk.Text(bottomFrame, width = 5, height = 1, font='helvetica')  # displays the site codde status
        self.codeBox.place(relx = 0.13)

        self.infoButton = tk.Button(bottomFrame, text = "About", font='helvetica', bg = 'gray', command = self.openWin)  # opens a dialog box that gives basic instructions
        self.infoButton.place(relx = .3, rely = 0.1, relheight = 0.64, relwidth = 0.1)


    # def openWin(self): # function to hold dialog window
    #
    #     global top
    #     if top is not None:
    #         top.destroy()
    #
    #     top = tk.Toplevel(root)  # set the window to be dependent on base application
    #
    #     cavas2 = tk.Canvas(top, height = 120, width = 365)  # sets the size of the window
    #     cavas2.pack()
    #     top.title('About') # sets the title for the dialog box
    #
    #     frame2 = tk.Frame(top, bg = '#80c1ff', bd = 5)  # sets frame that holds the dialog
    #     frame2.place(relx = 0.5, relwidth = 1, relheight = .5, anchor = 'n')
    #
    #     self.label = tk.Label(frame2, text = "Welcome to the MetaGrabber!\n This application will grab the meta tags of any website you type in! \n Just type in the site and hit RUN!", justify = 'left', anchor = 'nw')
    #     self.label.place(relheight = 0.99, relwidth = 1)  # dialog of basic instructions
    #
    #     frame2Lower = tk.Frame(top, bg='#80c1ff', bd = 5)  # holds exit button
    #     frame2Lower.place(relx = 0.5, rely= 0.5, relwidth = 1, relheight = 0.5, anchor = 'n')
    #
    #     self.btn2 = tk.Button(frame2Lower, text = "close window", font='helvetica', bg = 'gray', command = top.destroy)  # closes the window and returns to the base application
    #     self.btn2.place(relx = 0.21, rely = 0.1, relheight = 0.9, relwidth = 0.6)



    def websiteCall(self, entry): #function call the website and scan it for meta tags

        self.txtBox.delete('1.0','end') # clears the text box

        try:
            url = entry  # passes the user inout itnto the url variable
            response = requests.get(url)  #passes the url into a request
            soup = BeautifulSoup(response.text,'lxml')  #beautifulsoup sets the url info to text to scan through
            metatags = soup.find_all('meta') # puts all meta tags to a variable

            for x in metatags:  # prints the tags to the screen
                self.txtBox.insert( 'end',str(x) + '\n')

        except:
            self.txtBox.insert('end', "Improper website URL. Please input a correct URL.\nA complete url needs to be inlcuded. \nExample: https://examplesite.com/")  # outputs if an improper url or no url is inputed

        self.codeGrab(url) # grabs the status code of the website


    def codeGrab(self, url):  # function to grab the http status code of the website

        self.codeBox.delete('1.0','end') # clears the textbox
        code = urllib.request.urlopen(url).getcode()  # sets the status code to a variable
        self.codeBox.insert('end', code)  # outputs the status code to the text box



root = tk.Tk() #initializes tkinter
b = App(root)  # creates an object for the application
top = None
root.mainloop()  # runs the application

# test url: https://www.englishforlifeacademy.com/
