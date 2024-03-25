import socket
from tkinter import *

def find_ip():
    url = url_entry.get()
    try:
        ip_address = socket.gethostbyname(url)
        ip_entry.delete(0, END)
        ip_entry.insert(0, ip_address)
    except socket.gaierror:
        ip_entry.delete(0, END)
        ip_entry.insert(0, "Invalid URL")

root = Tk()
root.title("IP Finder")
url_label = Label(root, text="Enter URL:")
url_label.pack()
url_entry = Entry(root)
url_entry.pack()
ip_label = Label(root, text="IP Address:")
ip_label.pack()
ip_entry = Entry(root)
ip_entry.pack()
find_button = Button(root, text="Find IP", command=find_ip)
find_button.pack()

root.mainloop()
