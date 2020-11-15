import traceback
import threading
from tkinter import *
from tkinter.ttk import *
from tkinter import messagebox
from settings import PITCHES
import tuner


class Program():
    '''TkInter GUI for the String Tuner'''
    
    def __init__(self):
        '''Sets up the root window and starts the mainloop'''
        #Create root window
        self.root = Tk()
        self.root.title("String Tuner")
        self.root.minsize(600, 250)
        self.root.resizable(False, False)
        
        #Define callback for error messages
        self.root.report_callback_exception = self.display_error
        
        #Create variables to track current instrument and string
        self.instrument = StringVar()
        self.string = StringVar()
        
        #Create the instrument picker section
        self.picker_cont = Frame(self.root)
        self.picker_cont.pack()

        self.picker_lbl = Label(
            self.picker_cont,
            text='Instrument',
            justify=RIGHT,
        )
        self.picker_lbl.pack(side=LEFT)
        
        self.picker_cbox = Combobox(
            self.picker_cont,
            textvariable = self.instrument,
            state="readonly",
        )
        self.picker_cbox['values'] = list(PITCHES.keys())
        self.picker_cbox.bind(
            '<<ComboboxSelected>>',
            self.draw_radios
        )
        self.picker_cbox.set(self.picker_cbox['values'][0])
        self.picker_cbox.pack()

        #Create radio buttons
        self.radio_cont = Frame(self.root)
        self.radio_cont.pack()
        self.draw_radios()

        #Create display
        self.display_cont = Frame(self.root)
        self.display_cont.pack()

        self.display_text = StringVar(self.display_cont)
        self.display_offset = StringVar(self.display_cont)

        self.display_text_lbl = Label(
            self.display_cont,
            textvariable=self.display_text,
        )
        self.display_text_lbl.pack()
        
        self.display_offset_lbl = Label(
            self.display_cont,
            textvariable=self.display_offset,
        )
        self.display_offset_lbl.pack()
        
        #Start updating display
        self.display_thread = threading.Thread(
            target = self.display_update,
            daemon = True
        )
        self.display_thread.start()

        #Start the main loop
        mainloop()
        
    def draw_radios(self, event=None):
        '''Redraws the radio buttons for strings.'''
        #Clear current radio buttons
        for widget in self.radio_cont.winfo_children():
            widget.destroy()

        #Reset current string
        self.string.set('') 
            
        #Get string names for the current instrument
        strings = PITCHES[self.instrument.get()].keys()
        
        #Create radio buttons
        for string in strings:
            Radiobutton(
                self.radio_cont,
                text=string,
                variable=self.string,
                value=string,
            ).pack(side=LEFT)
