"""
System 7 UI Components - Core widgets styled as System 7
"""

from typing import Optional
from textual.app import ComposeResult, on
from textual.containers import Container, Horizontal, Vertical
from textual.widgets import Static, Button, Label, Input
from textual.binding import Binding
from rich.text import Text
from rich.panel import Panel
from rich.style import Style


class System7App:
    """Base class for System 7 applications"""
    pass


class System7Window(Container):
    """A window styled like System 7"""
    
    DEFAULT_CSS = """
    System7Window {
        width: 60;
        height: 20;
        border: solid $accent;
        background: $panel;
        margin: 1 2;
        layout: vertical;
    }
    
    System7Window > .window-title {
        width: 1fr;
        height: 1;
        background: #000080;
        color: white;
        padding: 0 1;
        dock: top;
    }
    
    System7Window > .window-content {
        width: 1fr;
        height: 1fr;
        background: $panel;
        border: none;
    }
    """

    def __init__(self, title: str = "Untitled", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = title
        self.is_focused = False

    def compose(self) -> ComposeResult:
        """Create window components."""
        with Vertical(classes="window-title"):
            yield Label(self.title, id="window-title")
        with Container(classes="window-content"):
            yield Static("", id="window-body")

    def set_content(self, content: str) -> None:
        """Set the window content."""
        self.query_one("#window-body", Static).update(content)


class System7Button(Button):
    """A button styled like System 7"""
    
    DEFAULT_CSS = """
    System7Button {
        width: auto;
        height: 1;
        margin: 1 1;
        border: solid #c0c0c0;
        background: $panel;
        color: $text;
        padding: 0 2;
        text-align: center;
    }
    
    System7Button:hover {
        background: $boost;
    }
    
    System7Button:focus {
        background: $accent;
        color: white;
    }
    """


class System7Dialog(Container):
    """A dialog box styled like System 7"""
    
    DEFAULT_CSS = """
    System7Dialog {
        width: 50;
        height: auto;
        border: solid $accent;
        background: $panel;
        padding: 1 2;
    }
    """

    def __init__(self, title: str = "Dialog", *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.title = title

    def compose(self) -> ComposeResult:
        """Create dialog components."""
        yield Label(self.title, classes="dialog-title")


class System7MenuBar(Static):
    """Menu bar component"""
    
    DEFAULT_CSS = """
    System7MenuBar {
        width: 100%;
        height: 1;
        background: $panel;
        border-bottom: solid $boost;
    }
    """

    def render(self) -> Text:
        """Render the menu bar."""
        return Text("File  Edit  View  Window  Help", style="bold")