from rich.console import Console
from rich.table import Table

class OptionsTable:
    def __init__(self, title, column_names):
        self.console = Console()
        self.table = Table(title=title)
        for name in column_names:
            self.table.add_column(name, style="cyan", no_wrap=True)
    
    def add_row(self, option, current_setting="", required="", description=""):
        """Add a row to the table."""
        self.table.add_row(option, current_setting, required, description)
    
    def modify_row(self, row_index, option=None, current_setting=None):
        """Modify an existing row. 'row_index' is 0-based."""
        if 0 <= row_index < len(self.table.rows):
            row = self.table.rows[row_index]
            if option is not None:
                row.cells[0].text = option
            if current_setting is not None:
                row.cells[1].text = current_setting
            
    
    def set_current_setting(self, row_index, current_setting):
        """Set the current setting for a row."""
        if 0 <= row_index < len(self.table.rows):
            self.table.rows[row_index].cells[1].text = current_setting
    
    def display(self):
        """Display the table."""
        self.console.print(self.table)
