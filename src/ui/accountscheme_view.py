from tkinter import *
from tkinter import messagebox
from services.ht_service import HtService

class AccountSchemeView:
    def __init__(self, root, back_to_program_view):
        self._root = root
        self._service = HtService()
        self._back_to_program_view = back_to_program_view
        self._frame = None

        self._initialize()


    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        self._frame = Frame(self._root, bg="red", width=400, height=400)
        self._frame.pack()
        frame1 = Frame(self._frame, bg="white")
        frame1.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

        e1_label = Label(frame1, text='Account number:')
        e1_label.pack()
        entry1 = Entry(frame1)
        entry1.pack()

        e2_label = Label(frame1, text='Account name:')
        e2_label.pack()
        entry2 = Entry(frame1)
        entry2.pack()

        def save_new_account():
            number = entry1.get()
            name = entry2.get()
            if self._service.find_account(number) == True:
                messagebox.showerror(title='Invalid input', message="Number already in use")
                return
            self._service.save_new_account(number, name)
            messagebox.showinfo(title='SUCCESS!', message='Account saved')

        save_button = Button(frame1, text='Save', command=save_new_account)
        save_button.pack()

        back_button = Button(frame1, text="Back", command=self._back_to_program_view)
        back_button.pack(pady=20)