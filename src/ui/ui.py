from ui.program_view import ProgramView
from ui.voucher_view import VoucherView
from ui.list_view import ListView
from ui.income_statement_view import IncomeStatementView
from ui.accountscheme_view import AccountSchemeView

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
        
        self._current_view = ProgramView(self._root, self._show_voucher_view, self._show_list_view, self._show_income_statement_view, self._show_accountscheme_view)

        self._current_view.pack()
    
    def _show_voucher_view(self):
        self._hide_current_view()
        
        self._current_view = VoucherView(self._root, self._show_program_view)

        self._current_view.pack()
    
    def _show_list_view(self):
        self._hide_current_view()
        
        self._current_view = ListView(self._root, self._show_program_view)

        self._current_view.pack()

    def _show_income_statement_view(self):
        self._hide_current_view()
        
        self._current_view = IncomeStatementView(self._root, self._show_program_view)

        self._current_view.pack()

    def _show_accountscheme_view(self):
        self._hide_current_view()
        
        self._current_view = AccountSchemeView(self._root, self._show_program_view)

        self._current_view.pack()