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
        self._frame = Frame(self._root, width=400, height=500, bg="white")
        self._frame.pack()

        e1_label = Label(self._frame, text='Account number:')
        e1_label.pack()
        entry1 = Entry(self._frame)
        entry1.pack()

        e2_label = Label(self._frame, text='Account name:')
        e2_label.pack()
        entry2 = Entry(self._frame)
        entry2.pack()

        def save_new_account():
            number = entry1.get()
            name = entry2.get()
            if self._service.find_account(number) == True:
                messagebox.showerror(title='Invalid input', message="Number already in use")
                return
            self._service.save_new_account(number, name)
            messagebox.showinfo(title='SUCCESS!', message='Account saved')
            line = ' '.join([number, name])
            lbox.insert(END, line)

        save_button = Button(self._frame, text='Save', command=save_new_account)
        save_button.pack()

        back_button = Button(self._frame, text="Back", command=self._back_to_program_view)
        back_button.pack(pady=20)

        lbox = Listbox(self._frame)
        lbox_scrollbar = Scrollbar(self._frame, orient=VERTICAL)
        lbox_scrollbar.config(command=lbox.yview)
        lbox_scrollbar.pack(side=RIGHT, fill=Y)
        lbox.pack()

        accounts = self._service.get_accounts()
        for account in accounts:
            elements = [account[0], account[1]]
            line = ' '.join(elements)
            lbox.insert(END, line)

        