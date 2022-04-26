from tkinter import *
from services.ht_service import HtService

class IncomeStatementView:
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

        lbox = Listbox(frame1, width=50)
        lbox_scrollbar = Scrollbar(frame1, orient=VERTICAL)
        lbox_scrollbar.config(command=lbox.yview)
        lbox_scrollbar.pack(side=RIGHT, fill=Y)
        lbox.pack()

        lines = self._service.get_income_statement_lines()
        for line in lines:
            lbox.insert(END, line)

        back_button = Button(frame1, text="Back", command=self._back_to_program_view)
        back_button.pack(pady=20)