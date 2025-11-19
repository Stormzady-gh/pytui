"""
System 7 TUI - A faithful recreation of Apple's System 7 in the terminal
"""

import asyncio
from typing import Optional
from datetime import datetime
from textual.app import ComposeResult, on
from textual.containers import Container, Horizontal, Vertical, ScrollableContainer
from textual.widgets import Header, Footer, Static, Button, Label, Input, TextArea
from textual.binding import Binding
from textual.screen import Screen
from rich.text import Text
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

from system7_ui import System7Window, System7App, System7MenuBar, System7Dialog
from apps.finder import FinderApp
from apps.calculator import CalculatorApp
from apps.notepad import NotepadApp


class System7Desktop(System7App):
    """Main System 7 Desktop Environment"""
    
    TITLE = "System 7"
    BINDINGS = [
        Binding("ctrl+q", "quit", "Quit", show=True),
        Binding("ctrl+n", "new_window", "New Window", show=False),
    ]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield MenuBar()
        yield DesktopCanvas()
        yield System7StatusBar()

    def action_new_window(self) -> None:
        """Open a new Finder window."""
        self.query_one(DesktopCanvas).open_finder()


class MenuBar(Static):
    """System 7 Menu Bar"""
    
    DEFAULT_CSS = """
    MenuBar {
        width: 100%;
        height: 1;
        background: $panel;
        color: $text;
        border-bottom: solid $boost;
        padding: 0 1;
        dock: top;
    }
    """

    def render(self) -> Text:
        """Render the menu bar."""
        menu_items = "🍎 File  Edit  View  Special  Window  Help"
        return Text(menu_items, style="bold white on #c0c0c0")


class DesktopCanvas(Container):
    """Main desktop canvas containing windows and icons"""
    
    DEFAULT_CSS = """
    DesktopCanvas {
        width: 1fr;
        height: 1fr;
        background: $primary;
        border: none;
    }
    """

    def compose(self) -> ComposeResult:
        """Create initial desktop elements."""
        yield DesktopGrid()

    def open_finder(self) -> None:
        """Open a new Finder window."""
        grid = self.query_one(DesktopGrid)
        grid.add_window(FinderApp(title="Macintosh HD"))

    def on_mount(self) -> None:
        """Initialize desktop."""
        # Create initial Finder window
        self.open_finder()


class DesktopGrid(Container):
    """Grid container for managing window positions"""
    
    DEFAULT_CSS = """
    DesktopGrid {
        width: 1fr;
        height: 1fr;
        layout: vertical;
        overflow: auto;
    }
    """

    def __init__(self):
        super().__init__()
        self.windows = []
        self.window_offset = 0

    def add_window(self, window: System7Window) -> None:
        """Add a window to the desktop."""
        self.windows.append(window)
        self.mount(window)
        self.window_offset += 2

    def remove_window(self, window: System7Window) -> None:
        """Remove a window from the desktop."""
        if window in self.windows:
            self.windows.remove(window)
            window.remove()


class System7StatusBar(Static):
    """System 7 Status Bar at bottom"""
    
    DEFAULT_CSS = """
    System7StatusBar {
        width: 100%;
        height: 1;
        background: $panel;
        color: $text;
        border-top: solid $boost;
        padding: 0 1;
        dock: bottom;
    }
    """

    def __init__(self):
        super().__init__()
        self.update_time()

    def render(self) -> Text:
        """Render the status bar with time."""
        now = datetime.utcnow().strftime("%H:%M:%S")
        status = f"System 7 TUI  |  {now} UTC"
        return Text(status, style="bold white on #c0c0c0")

    async def update_time(self) -> None:
        """Update time every second."""
        while True:
            self.update(self.render())
            await asyncio.sleep(1)

    def on_mount(self) -> None:
        """Start the time update loop."""
        self.app.set_interval(1, lambda: self.update(self.render()))


if __name__ == "__main__":
    app = System7Desktop()
    app.run()