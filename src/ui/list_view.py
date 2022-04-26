from email import message
from tkinter import *
from tkinter import messagebox
from entities.voucher import Voucher
from services.ht_service import HtService

class ListView:
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
        
        lbox = Listbox(frame1)
        lbox_scrollbar = Scrollbar(frame1, orient=VERTICAL)
        lbox_scrollbar.config(command=lbox.yview)
        lbox_scrollbar.pack(side=RIGHT, fill=Y)
        lbox.pack()

        vouchers = self._service.get_vouchers()
        for voucher in vouchers:
            line_elements = [str(voucher.number), voucher.message]
            if voucher.debit_credit == 0:
                ammount = str(voucher.ammount / 100)
                line_elements.append(ammount)
            elif voucher.debit_credit == 1:
                ammount = '-' + str(voucher.ammount / 100)
                line_elements.append(ammount)
            line = ' '.join(line_elements)
            lbox.insert(END, line)

        def delete_item():
            line = lbox.get(ANCHOR)
            number = line.split(' ')
            number = int(number[0])
            warning_message = f'Do you want to delete voucher nr {number}?'
            proceed = messagebox.askyesno(title='Delete voucher', message=warning_message)
            if proceed == True:
                self._service.delete_voucher(number)
                lbox.delete(ANCHOR)
            return

        delete_button = Button(frame1, text='Delete', command=delete_item)
        delete_button.pack()
        back_button = Button(frame1, text="Back", command=self._back_to_program_view)
        back_button.pack(pady=20)