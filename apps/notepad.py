"""
Notepad Application - System 7 Style Text Editor
"""

from textual.app import ComposeResult, on
from textual.containers import Vertical
from textual.widgets import TextArea, Static
from textual.binding import Binding
from system7_ui import System7Window


class NotepadApp(System7Window):
    """System 7 Notepad - Simple Text Editor"""
    
    BINDINGS = [
        Binding("ctrl+s", "save", "Save"),
        Binding("ctrl+w", "close_window", "Close"),
    ]
    
    DEFAULT_CSS = """
    NotepadApp {
        width: 80;
        height: 24;
    }
    """

    def __init__(self, *args, **kwargs):
        super().__init__(title="Untitled - Notepad", *args, **kwargs)
        self.is_modified = False

    def compose(self) -> ComposeResult:
        """Create notepad components."""
        yield Static(self.title, classes="window-title")
        with Vertical():
            yield TextArea(language="text", id="notepad-text")

    def on_text_area_changed(self) -> None:
        """Mark document as modified."""
        if not self.is_modified:
            self.is_modified = True
            self.title = f"* {self.title}"

    def action_save(self) -> None:
        """Save the document."""
        self.is_modified = False
        # In a real app, this would save to a file

    def action_close_window(self) -> None:
        """Close the window."""
        self.remove()