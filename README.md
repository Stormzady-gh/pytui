# System 7 TUI - Terminal User Interface

A faithful recreation of Apple's classic System 7 operating system as a Python Terminal User Interface (TUI).

## Features

✨ **Authentic System 7 Aesthetic**
- Classic beige color scheme (#c0c0c0)
- Iconic window chrome and borders
- System 7 menu bar
- Status bar with clock

🪟 **Window Management**
- Draggable windows (coming soon)
- Multiple window support
- Window minimize/maximize
- Focus management

📁 **Applications Included**
- **Finder** - File browser
- **Calculator** - Basic calculator
- **Notepad** - Simple text editor

⌨️ **Keyboard Shortcuts**
- `Ctrl+Q` - Quit
- `Ctrl+N` - New Finder window
- `Ctrl+S` - Save (in Notepad)
- `Ctrl+W` - Close window

## Installation

```bash
# Clone and setup
git clone https://github.com/Stormzady-gh/system7-tui.git
cd system7-tui

# Install dependencies
pip install -r requirements.txt
```

## Running

```bash
python main.py
```

Or with the console script:
```bash
system7
```

## Project Structure

```
system7-tui/
├── main.py              # Main application and desktop
├── system7_ui.py        # Core UI components
├── apps/
│   ├── __init__.py
│   ├── finder.py        # File browser
│   ├── calculator.py    # Calculator app
│   └── notepad.py       # Text editor
├── requirements.txt     # Python dependencies
├── setup.py            # Setup configuration
└── README.md           # This file
```

## Architecture

### Core Components

- **System7App** - Base class for all applications
- **System7Window** - Styled window container
- **System7Button** - System 7 styled button
- **System7Dialog** - Dialog boxes
- **System7MenuBar** - Menu bar component

### Applications

Each application is a standalone module that extends `System7Window` with specific functionality.

## Customization

### Colors

Modify the color scheme in `system7_ui.py`:
```python
# Current System 7 colors:
# Panel background: #c0c0c0 (light gray)
# Title bar: #000080 (dark blue)
# Text: black
```

### Adding New Applications

1. Create a new file in `apps/`
2. Extend `System7Window`
3. Implement `compose()` method
4. Add to desktop in `main.py`

Example:
```python
class MyApp(System7Window):
    def __init__(self, *args, **kwargs):
        super().__init__(title="My App", *args, **kwargs)
    
    def compose(self) -> ComposeResult:
        yield Label("My App Title", classes="window-title")
        yield Static("App content goes here")
```

## Planned Features

- [ ] Draggable windows
- [ ] Dockable application bar
- [ ] File picker dialogs
- [ ] Color picker
- [ ] Sound/beep functionality
- [ ] Desk accessories
- [ ] System 7 sounds
- [ ] Network browser
- [ ] Hierarchical menus
- [ ] Full System 7 color palette

## Technical Details

### Built With
- **Textual** - Modern Python TUI framework
- **Rich** - Rich text and beautiful formatting
- **Python 3.8+**

### Why Textual?
Textual provides:
- Event-driven architecture
- CSS-like styling system
- Modern terminal capabilities
- Responsive layouts
- Clean widget API

## Compatibility

- macOS, Linux, Windows
- Requires a terminal that supports 256 colors or True Color
- Works best on terminals with at least 100x30 character dimensions

## License

MIT License - Feel free to use and modify!

## Contributing

Contributions welcome! Feel free to:
- Report bugs
- Suggest features
- Submit pull requests
- Improve documentation

## Author

Created by **Stormzady** as a nostalgic tribute to System 7.

---

*"It just works!"* - Steve Jobs, probably