"""
Finder Application - System 7 File Browser
"""

from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical, Container
from textual.widgets import Static, Button, Label
from textual.binding import Binding
from rich.text import Text
from rich.table import Table
from system7_ui import System7Window, System7Button


class FinderApp(System7Window):
    """System 7 Finder - File Browser"""
    
    BINDINGS = [
        Binding("ctrl+w", "close_window", "Close"),
    ]
    
    DEFAULT_CSS = """
    FinderApp {
        width: 70;
        height: 24;
    }
    
    FinderApp .finder-toolbar {
        height: 3;
        background: $panel;
        border-bottom: solid $boost;
    }
    
    FinderApp .finder-content {
        height: 1fr;
        border-top: solid $boost;
    }
    
    FinderApp .folder-icon {
        width: 1fr;
        height: auto;
        margin: 1 1;
    }
    """

    def __init__(self, title: str = "Finder", *args, **kwargs):
        super().__init__(title=title, *args, **kwargs)
        self.current_path = "Macintosh HD"

    def compose(self) -> ComposeResult:
        """Create Finder window components."""
        yield Label(self.title, classes="window-title")
        yield FinderToolbar()
        yield FinderContent()

    def action_close_window(self) -> None:
        """Close this window."""
        self.remove()


class FinderToolbar(Static):
    """Finder toolbar with navigation buttons"""
    
    DEFAULT_CSS = """
    FinderToolbar {
        height: 3;
        background: $panel;
        border-bottom: solid $boost;
        padding: 1 1;
    }
    """

    def compose(self) -> ComposeResult:
        """Create toolbar components."""
        with Horizontal():
            yield System7Button("[◀]", id="back-btn")
            yield System7Button("[▶]", id="forward-btn")
            yield System7Button("[⬆]", id="up-btn")
            yield System7Button("[🔍]", id="search-btn")

    def render(self) -> Text:
        """Render toolbar."""
        return Text("")


class FinderContent(Container):
    """Main content area showing files and folders"""
    
    DEFAULT_CSS = """
    FinderContent {
        height: 1fr;
        width: 1fr;
        background: $panel;
        border: none;
    }
    """

    def compose(self) -> ComposeResult:
        """Create content area with sample folders."""
        yield Label("📁 Applications", classes="folder-icon")
        yield Label("📁 Documents", classes="folder-icon")
        yield Label("📁 Downloads", classes="folder-icon")
        yield Label("📁 System Folder", classes="folder-icon")
        yield Label("💾 Hard Drive (2 GB)", classes="folder-icon")