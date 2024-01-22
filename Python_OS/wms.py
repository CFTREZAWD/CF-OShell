import tkinter as tk
from tkinter import ttk
import customtkinter as ctk
import requests
import urllib.parse
import json



def wms():

    ctk.set_appearance_mode('dark')
    window = ctk.CTk()
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
    WMS_Label = ctk.CTkLabel(window, text='WMS', font=('Agency FB', 62))
    WMS_Label.pack()

    url_label = ctk.CTkLabel(window, text='URL:', font=('Agency FB', 24))
    url_label.pack(pady=10)
    url_textbox = ctk.CTkEntry(window, textvariable=url_var)
    url_textbox.pack()

    msg_label = ctk.CTkLabel(window, text='Message:', font=('Agency FB', 24))
    msg_label.pack(pady=10)
    msg_textbox = ctk.CTkEntry(window, textvariable=msg_var)
    msg_textbox.pack()

    send_button = ctk.CTkButton(window, text='Send', command=send_msg, font=('Agency FB', 24))
    send_button.pack(pady=10)

    window.mainloop()
    print("Finished")
