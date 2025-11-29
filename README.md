# 2fAuth - TOTP Generator

A simple Python script to generate Time-based One-Time Passwords (TOTP) for Two-Factor Authentication (2FA).

## Description

This script generates 6-digit TOTP codes that change every 30 seconds, commonly used for two-factor authentication with services like Google Authenticator, Authy, or other 2FA applications.

## Features

- Generates time-based one-time passwords (TOTP)
- Compatible with standard 2FA authenticator apps
- Simple command-line interface
- Secure secret key management via environment variables

## Requirements

- Python 3.6 or higher
- pip (Python package manager)

## Dependencies

The following Python packages are required:

- `pyotp` - For generating TOTP codes
- `python-dotenv` - For loading environment variables from .env file
- `requests` - HTTP library (if needed for future features)

## Installation

1. Clone or download this repository:
   ```bash
   cd /Users/ebarto/PythonProjects/2fAuth
   ```

2. Create and activate a virtual environment (recommended):
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate  # On macOS/Linux
   # or
   .venv\Scripts\activate  # On Windows
   ```

3. Install the required dependencies:
   ```bash
   pip install pyotp python-dotenv requests
   ```

   Alternatively, you can create a `requirements.txt` file with the following content:
   ```
   pyotp
   python-dotenv
   requests
   ```

   And install using:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Create a `.env` file in the project root directory:
   ```bash
   touch .env
   ```

2. Add your TOTP secret key to the `.env` file:
   ```
   SECRET=YOUR_SECRET_KEY_HERE
   ```

   **Important:** Replace `YOUR_SECRET_KEY_HERE` with your actual TOTP secret key. This is typically provided when you set up 2FA on a service (the string you would normally enter into Google Authenticator or similar apps).

## Usage

Run the script to generate the current TOTP code:

```bash
python main.py
```

The output will display the current 6-digit OTP:
```
current otp: 123456
```

The code changes every 30 seconds based on the current time.

## Security Considerations

**IMPORTANT SECURITY NOTES:**

- **Never commit your `.env` file to version control.** The `.env` file is already included in `.gitignore` to prevent accidental commits.
- **Keep your SECRET key private.** Anyone with access to your secret key can generate valid OTP codes for your accounts.
- **Use strong secret keys.** The secret should be a random base32-encoded string (typically provided by the service you're securing).
- **Secure your environment.** Ensure your development machine and the `.env` file have appropriate file permissions.

## How TOTP Works

TOTP (Time-based One-Time Password) is an algorithm that generates a one-time password using:
1. A shared secret key (stored in your `.env` file)
2. The current time (synchronized between client and server)

The generated code is valid for approximately 30 seconds and provides an additional security layer beyond just a password.

## Troubleshooting

### "Module not found" errors
Make sure you've installed all dependencies:
```bash
pip install pyotp python-dotenv requests
```

### Codes don't match
- Ensure your system clock is accurate (TOTP is time-based)
- Verify you're using the correct secret key in your `.env` file
- The secret should be in base32 format (uppercase letters A-Z and numbers 2-7)

### Virtual environment issues
Make sure your virtual environment is activated:
```bash
source .venv/bin/activate  # macOS/Linux
```

## License

This project is provided as-is for personal use.

## Contributing

Feel free to submit issues or pull requests for improvements.
