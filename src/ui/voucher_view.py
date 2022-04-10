from tkinter import *
from services.ht_service import HtService

class VoucherView:
    def __init__(self, root):
        self._root = root
        self._frame = None

        self._initialize()


    def pack(self):
        self._frame.pack()

    def destroy(self):
        self._frame.destroy()
    
    def _initialize(self):
        pass