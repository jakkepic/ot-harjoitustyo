from tkinter import *
from services.ht_service import HtService


class ProgramView:
    def __init__(self, root):
        self._root = root
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

        button1 = Button(frame1, text="Add Voucher", padx=30)
        button1.pack(pady=20)

        button2 = Button(frame1, text="View Vouchers", padx=25)
        button2.pack(pady=20)

        button3 = Button(frame1, text="Income Statement")
        button3.pack(pady=20)

        button1 = Button(frame1, text="Account Scheme", padx=20)
        button1.pack(pady=20)
