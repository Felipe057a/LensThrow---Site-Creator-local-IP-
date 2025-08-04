import tkinter as tk
from tkinter import ttk, messagebox
import socket
import threading
import http.server
import socketserver
import os

# Detect default local IP
def get_local_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip = s.getsockname()[0]
        s.close()
    except:
        ip = "127.0.0.1"
    return ip

# Start HTTP server
def start_http_server(ip, port):
    os.makedirs("public", exist_ok=True)

    with open("public/index.html", "w", encoding="utf-8") as f:
        f.write(text_html.get("1.0", tk.END))

    with open("public/style.css", "w", encoding="utf-8") as f:
        f.write(text_css.get("1.0", tk.END))

    with open("public/script.java", "w", encoding="utf-8") as f:
        f.write(text_java.get("1.0", tk.END))

    with open("public/logic.py", "w", encoding="utf-8") as f:
        f.write(text_python.get("1.0", tk.END))

    try:
        with open("public/index.html", "r+", encoding="utf-8") as f:
            html = f.read()
            if "<head>" in html:
                html = html.replace("<head>", f"<head>\n<style>\n{text_css.get('1.0', tk.END)}</style>\n")
            if "</body>" in html:
                html = html.replace("</body>", f"<script>\n{text_java.get('1.0', tk.END)}</script>\n</body>")
            f.seek(0)
            f.write(html)
            f.truncate()
    except:
        pass

    handler = http.server.SimpleHTTPRequestHandler
    os.chdir("public")
    with socketserver.TCPServer((ip, port), handler) as httpd:
        print(f"Public server at http://{ip}:{port}")
        try:
            httpd.serve_forever()
        except:
            pass

# Execute Python code
def run_python():
    code = text_python.get("1.0", tk.END)
    try:
        exec(code, {})
    except Exception as e:
        messagebox.showerror("Execution Error", str(e))

# Make Public button
def tornar_publico():
    if not tornar_publico_var.get():
        messagebox.showwarning("Attention", "You must accept CDIMDET's terms to publish.")
        return

    ip = label_ip["text"]
    try:
        port = int(entry_porta.get())
    except:
        messagebox.showwarning("Error", "Invalid port")
        return

    threading.Thread(target=start_http_server, args=(ip, port), daemon=True).start()
    messagebox.showinfo("Public Site", f"Access it at: http://{ip}:{port}")

# Scram button
def scram():
    try:
        for filename in ["index.html", "style.css", "script.java", "logic.py"]:
            path = os.path.join("public", filename)
            if os.path.exists(path):
                os.remove(path)
        messagebox.showinfo("Scram", "Files deleted instantly!")
    except Exception as e:
        messagebox.showerror("Deletion Error", str(e))

# Modern dark style
def aplicar_estilo():
    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TFrame", background="#1f1f1f")
    style.configure("TLabel", background="#1f1f1f", foreground="white", font=("Segoe UI", 10))
    style.configure("TEntry", font=("Segoe UI", 10))
    style.configure("TButton", font=("Segoe UI", 10, "bold"), padding=6)
    style.configure("TCheckbutton", background="#1f1f1f", foreground="white", font=("Segoe UI", 10))

# Show Terms
def mostrar_termos():
    termos = tk.Toplevel(root)
    termos.title("Terms of Use - CDIMDET")
    termos.geometry("700x500")
    termos.configure(bg="#101010")

    texto = tk.Text(termos, wrap=tk.WORD, bg="#202020", fg="white", font=("Segoe UI", 10))
    texto.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

    texto.insert(tk.END, """
🔒 TERMS OF USE AND LIABILITY
This system was created by the company CDIMDET.

By using this application, you acknowledge and agree to the following terms:

1. CDIMDET is NOT responsible for any direct or indirect damage caused by the publication, execution, or use of this code.
2. All content published by you in this system is your full responsibility.
3. You must ensure that the content published DOES NOT violate any local, national, or international law.
4. The public server that will be started is local and can be accessed by any device on your local network.
5. The Python code runs locally and can affect files, memory, or devices — use with caution.
6. CDIMDET provides this tool "as is", without warranties, support, or legal commitments.
7. The public email of this company is CDIMDET@gmail.com

⚠️ BY CLICKING “I ACCEPT THE TERMS”, YOU CONFIRM THAT YOU HAVE READ, UNDERSTOOD, AND AGREED TO ALL THE ABOVE TERMS.

🔧 Created by CDIMDET - Free Ray Technology.
""")

    texto.config(state=tk.DISABLED)

    def aceitar_termos():
        tornar_publico_var.set(True)
        chk_publicar.configure(state=tk.NORMAL)
        termos.destroy()

    btn = ttk.Button(termos, text="✔ I Accept the Terms", command=aceitar_termos)
    btn.pack(pady=10)

# Interface
root = tk.Tk()
root.title("LensThrow, Last Version (Able to updates on GitHub repos")
root.geometry("1000x700")
root.configure(bg="#1f1f1f")

aplicar_estilo()

frame = ttk.Frame(root, padding=20)
frame.pack(fill=tk.BOTH, expand=True)

# Detected IP
ttk.Label(frame, text="Local IP:").grid(row=0, column=0, sticky="w")
label_ip = ttk.Label(frame, text=get_local_ip())
label_ip.grid(row=0, column=1, sticky="w")

# Port
ttk.Label(frame, text="Port:").grid(row=1, column=0, sticky="w")
entry_porta = ttk.Entry(frame, width=10)
entry_porta.insert(0, "8080")
entry_porta.grid(row=1, column=1, sticky="w")

# Checkbutton (disabled until accepted)
tornar_publico_var = tk.BooleanVar(value=False)
chk_publicar = ttk.Checkbutton(frame, text="Accept CDIMDET Terms", variable=tornar_publico_var)
chk_publicar.grid(row=1, column=2, sticky="w")
chk_publicar.configure(state=tk.DISABLED)

# Button to read terms
btn_termos = ttk.Button(frame, text="📜 Read Terms", command=mostrar_termos)
btn_termos.grid(row=1, column=3, sticky="w", padx=10)

# HTML
ttk.Label(frame, text="HTML (index.html):").grid(row=2, column=0, sticky="nw")
text_html = tk.Text(frame, height=8, font=("Consolas", 10), bg="#262626", fg="lightgreen", insertbackground="white")
text_html.grid(row=2, column=1, columnspan=3, sticky="nsew", pady=5)

# CSS
ttk.Label(frame, text="CSS (style.css):").grid(row=3, column=0, sticky="nw")
text_css = tk.Text(frame, height=5, font=("Consolas", 10), bg="#262626", fg="#00ffff", insertbackground="white")
text_css.grid(row=3, column=1, columnspan=3, sticky="nsew", pady=5)

# Java
ttk.Label(frame, text="Java (script.java):").grid(row=4, column=0, sticky="nw")
text_java = tk.Text(frame, height=5, font=("Consolas", 10), bg="#262626", fg="#ffcc00", insertbackground="white")
text_java.grid(row=4, column=1, columnspan=3, sticky="nsew", pady=5)

# Python
ttk.Label(frame, text="Python (logic.py):").grid(row=5, column=0, sticky="nw")
text_python = tk.Text(frame, height=5, font=("Consolas", 10), bg="#262626", fg="#ff7777", insertbackground="white")
text_python.grid(row=5, column=1, columnspan=3, sticky="nsew", pady=5)

# Buttons
btn_publicar = ttk.Button(frame, text="🟢 Make Public", command=tornar_publico)
btn_publicar.grid(row=6, column=3, sticky="e", pady=10)

btn_scram = ttk.Button(frame, text="🔴 Scram (Delete All)", command=scram)
btn_scram.grid(row=6, column=0, sticky="w", pady=10)

# Resize
for i in range(2, 6):
    frame.rowconfigure(i, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)

root.mainloop()
