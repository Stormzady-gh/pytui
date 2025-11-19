"""
Calculator Application - System 7 Style
"""

from textual.app import ComposeResult, on
from textual.containers import Horizontal, Vertical, Container
from textual.widgets import Button, Static, Label
from textual.binding import Binding
from system7_ui import System7Window, System7Button


class CalculatorApp(System7Window):
    """System 7 Calculator"""
    
    DEFAULT_CSS = """
    CalculatorApp {
        width: 30;
        height: 18;
    }
    
    CalculatorApp .calc-display {
        width: 1fr;
        height: 2;
        background: #c0c0c0;
        border: inset $text;
        padding: 1 1;
        margin: 1 1;
    }
    
    CalculatorApp .calc-buttons {
        width: 1fr;
        height: 1fr;
        layout: vertical;
    }
    """

    def __init__(self, *args, **kwargs):
        super().__init__(title="Calculator", *args, **kwargs)
        self.current_value = "0"
        self.operation = None
        self.previous_value = None

    def compose(self) -> ComposeResult:
        """Create calculator components."""
        yield Label(self.title, classes="window-title")
        yield CalculatorDisplay(value="0")
        yield CalculatorKeypad()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        """Handle button presses."""
        button_id = event.button.id
        
        if button_id and button_id.startswith("calc-"):
            char = button_id.replace("calc-", "")
            display = self.query_one(CalculatorDisplay)
            
            if char in "0123456789":
                if display.value == "0":
                    display.update_value(char)
                else:
                    display.update_value(display.value + char)
            elif char == "C":
                display.update_value("0")
                self.current_value = "0"
                self.operation = None
                self.previous_value = None


class CalculatorDisplay(Static):
    """Calculator display screen"""
    
    def __init__(self, value: str = "0"):
        super().__init__(value)
        self.value = value

    def render(self) -> str:
        """Render the display."""
        return f"  {self.value:>16}"

    def update_value(self, new_value: str) -> None:
        """Update the displayed value."""
        self.value = new_value
        self.update(self.render())


class CalculatorKeypad(Container):
    """Calculator buttons keypad"""
    
    DEFAULT_CSS = """
    CalculatorKeypad {
        width: 1fr;
        height: 1fr;
        layout: vertical;
        padding: 1 1;
    }
    """

    def compose(self) -> ComposeResult:
        """Create button grid."""
        buttons = [
            ["7", "8", "9", "/"],
            ["4", "5", "6", "*"],
            ["1", "2", "3", "-"],
            ["0", ".", "=", "+"],
            ["C", "←", "", ""],
        ]

        for row in buttons:
            with Horizontal():
                for btn in row:
                    if btn:
                        yield System7Button(btn, id=f"calc-{btn}")