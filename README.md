# NAP Browser Unlocked - Shep

Adds 'SEB/1.0' to the end of users default user agent.

## Requirements

- Python 3.12.2
- Chrome web browser
- Following Python packages:
  - selenium
  - webdriver-manager
  - keyboard

## Installation

1. Install required Python packages:
```bash
pip install selenium webdriver-manager keyboard
```

2. Chrome browser should be installed on your system

## Usage

Run the script from the command line:
```bash
python seb_browser.py
```

The application will:
1. Detect your system's default user agent
2. Modify it by appending "SEB/1.0"
3. Launch Chrome in fullscreen mode
4. Navigate to the assessment administration page

## How It Works

The script performs these steps:
1. Opens a temporary headless browser to detect your system's default user agent
2. Modifies this user agent by appending "SEB/1.0"
3. Opens a visible Chrome browser with the modified user agent in kiosk mode

## Keybind(s)

- **Ctrl+Shift+S**: Switch to student login page (works only once)

## License

[MIT License](https://opensource.org/licenses/MIT)