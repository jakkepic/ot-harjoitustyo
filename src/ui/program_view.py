from tkinter import *
from services.ht_service import HtService


class ProgramView:
    def __init__(self, root, handle_add_voucher, handle_list_view, handle_income_statement, handle_account_scheme):
        self._root = root
        self._handle_add_voucher = handle_add_voucher
        self._handle_list_view = handle_list_view
        self._handle_income_statement = handle_income_statement
        self._handle_account_scheme = handle_account_scheme
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

        button1 = Button(frame1, text="Add Voucher", padx=30, command=self._handle_add_voucher)
        button1.pack(pady=20)

        button2 = Button(frame1, text="View Vouchers", padx=25, command=self._handle_list_view)
        button2.pack(pady=20)

        button3 = Button(frame1, text="Income Statement", command=self._handle_income_statement)
        button3.pack(pady=20)

        button4 = Button(frame1, text="Account Scheme", padx=20, command=self._handle_account_scheme)
        button4.pack(pady=20)

        exit_button = Button(frame1, text="Exit", command=self._root.destroy)
        exit_button.pack()
