import tkinter as tk
from tkinter import ttk
import requests
import urllib.parse
import json

window = tk.Tk()
window.title("Webhook Message Sender")
window.geometry("700x550")
window.iconbitmap("assets\\discord.ico")

# Variables
url_var = tk.StringVar(window)
msg_var = tk.StringVar(window)

# Functions
def send_msg():
    url_base, _, url_webhook_id = url_var.get().partition("/")
    url = f"{url_base}/{urllib.parse.quote(url_webhook_id)}"
    message = msg_var.get()
    headers = {'Content-Type': 'application/json'}
    data = json.dumps({"content": message})
    try:
        response = requests.post(url, data=data, headers=headers)
        if response.status_code == 204:
            print("Message sent")
        else:
            print(f"Failed to send the message: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")



# Widgets
WMS_Label = ttk.Label(window, text='WMS', font=("Terminal", 62))
WMS_Label.pack()

url_label = ttk.Label(window, text='URL:')
url_label.pack(pady=10)
url_textbox = ttk.Entry(window, textvariable=url_var)
url_textbox.pack()

msg_label = ttk.Label(window, text='Message:')
msg_label.pack(pady=10)
msg_textbox = ttk.Entry(window, textvariable=msg_var)
msg_textbox.pack()

send_button = ttk.Button(window, text='Send', command=send_msg)
send_button.pack(pady=10)

window.mainloop()