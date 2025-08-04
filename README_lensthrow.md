README:

# LensThrow — Local HTTP Server with Tkinter GUI

## Overview

**LensThrow** is a Python application featuring a modern dark-themed Tkinter GUI that enables you to create and publish local HTTP websites instantly on your network. It allows you to write and edit HTML, CSS, JavaScript (saved as `.java`), and Python scripts which can be served via a simple embedded HTTP server.

This project was created by **CDIMDET** to provide a lightweight, easy-to-use local web server interface with embedded code editing and quick deployment features.

---

## Features

- Detects your local IP address automatically.
- Lets you write and edit HTML, CSS, JavaScript, and Python code within the GUI.
- Generates and serves files through a simple HTTP server accessible on your local network.
- Includes a mandatory acceptance of Terms of Use before allowing public publishing.
- Provides buttons to start the server ("Make Public") or instantly delete all generated files ("Scram").
- Modern dark mode theme for better visual comfort.

---

## Requirements

- Python 3.x (tested with Python 3.8+)
- Standard Python libraries: `tkinter`, `socket`, `threading`, `http.server`, `os`

No external dependencies needed.

---

## Usage

1. Run the `lens_throw.py` script using Python 3.
2. The app will automatically detect your local IP.
3. Edit your HTML, CSS, JavaScript, and Python code in their respective text areas.
4. Click **"📜 Read Terms"** and carefully read the Terms of Use.
5. Accept the terms to enable the **"Accept CDIMDET Terms"** checkbox.
6. Check the box and click **"🟢 Make Public"** to start the local HTTP server.
7. Access the site on any device in your network via `http://<Your_IP>:<Port>`.
8. Use **"🔴 Scram (Delete All)"** to instantly delete all generated files.

---

## Important Security Warning

- The application executes the Python code you write using `exec()`. This means any Python code typed in can affect your computer directly, including modifying files, accessing the network, or other system operations.
- **Use extreme caution when running or sharing code via this tool.**
- This software is provided **"as is"** without any warranties. CDIMDET is **not responsible** for any damage or loss caused by usage.
- Only run code you trust or understand fully.
- The public server runs on your local network only, but be mindful of your network security.

---

## License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

## Contact

For questions or support, contact CDIMDET at **CDIMDET@gmail.com**.

---

## Acknowledgments

Created by CDIMDET - Free Ray Technology.
