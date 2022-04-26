from tkinter import *
from tkinter import messagebox
from services.ht_service import HtService

class VoucherView:
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
        
        e1_label = Label(frame1, text='Voucher number:')
        e1_label.pack()
        entry1 = Entry(frame1)
        entry1.pack()
        
        e2_label = Label(frame1, text='Account:')
        e2_label.pack()
        entry2 = Entry(frame1)
        entry2.pack()

        e3_label = Label(frame1, text="Debit('d')/Credit('c')")
        e3_label.pack()
        entry3 = Entry(frame1)
        entry3.pack()

        e4_label = Label(frame1, text='Ammount (cents):')
        e4_label.pack()
        entry4 = Entry(frame1)
        entry4.pack()

        e5_label = Label(frame1, text='Message:')
        e5_label.pack()
        entry5 = Entry(frame1)
        entry5.pack()
        
        def save_new_voucher():
            voucher_number = int(entry1.get())
            account = str(entry2.get())
            if self._service.find_account(account) == False:
                messagebox.showerror(title='Invalid input', message="Account not found")
                return
            debitcredit = entry3.get()
            if debitcredit == 'd':
                debitcredit = int(0)
            elif debitcredit == 'c':
                debitcredit = int(1)
            else:
                messagebox.showerror(title='Invalid input', message="Input 'd' for debit and 'c' for credit")
                return
            ammount1 = int(entry4.get())
            description = str(entry5.get())

            success = self._service.save_voucher(number=voucher_number, cost_centre=account, debit_credit=debitcredit, ammount=ammount1, message=description)
            if success == True:
                messagebox.showinfo(title='Success!', message='Saved voucher')
            else:
                messagebox.showerror(title='Task failed', message='Failed to save voucher, please check input')

        save_button = Button(frame1, text='Save', command=save_new_voucher)
        save_button.pack(pady=20)
        back_button = Button(frame1, text="Back", command=self._back_to_program_view)
        back_button.pack()