from tkinter import Canvas
from ui.program_view import ProgramView
from ui.voucher_view import VoucherView
from ui.list_view import ListView

class UI():
    def __init__(self, root):
        self._root = root
        self._current_view = None

    def start(self):
        self._show_program_view()

    def _hide_current_view(self):
        if self._current_view:
            self._current_view.destroy()

        self._current_view = None


    def _show_program_view(self):
        self._hide_current_view()
        
        self._current_view = ProgramView(self._root)

        self._current_view.pack()