from rich.console import Console
from rich.layout import Layout
from rich.live import Live
from rich.panel import Panel
from rich.text import Text
from rich.markup import escape
import pytchat
import twitchio
import os
import time

def clear_screen():
    # Check the operating system name and run the appropriate command
    if os.name == 'nt':
        _ = os.system('cls') # Windows
    else:
        _ = os.system('clear') # Linux/macOS/Posix





print("Overlay for chat is starting...\n please link your video ID for your youtube live stream")
video_id = input("╰─▸")
print("clearing text in 3 seconds...") 
time.sleep(1)
clear_screen()

header_text = Text("My Application Header", justify="center", style="bold white on blue")
header_panel = Panel(header_text, height=3)

log_area = Text()
content_panel = Panel(log_area, title="Logs", height=15)

# 3. Create a Layout object to structure the console
layout = Layout()

# Define the layout structure: one top pane, one bottom pane
layout.split_column(
    Layout(header_panel, name="header", size=3),
    Layout(content_panel, name="main")
)
author = []
messages = []
log_area = []
chat = pytchat.create(video_id=video_id)

console = Console()
with Live(layout, screen=True, redirect_stderr=False, redirect_stdout=False) as live:
    # Continuously add new lines to the log area
    while chat.is_alive():
        # 1. Check for New Chat Messages (Non-Blocking)
        for c in chat.get().sync_items():
            
            author_name = c.author.name if c.author.name else "Unknown User"
            
            msg = f"[{c.author.name}]: {c.message}"
            log_area.append(escape(msg)+ "\n")
            if len(log_area) > 10: log_area.pop(0)
        #if len(log_area) >= (content_panel.height or 20) - 2:
           #log_area.pop(0) 
           
     
     
        # Update the content panel with the new text
        layout["main"].update(Panel("".join(log_area), title="Logs"))
        #layout["main"].update(Panel(log_area, title="Logs"))
        # Manually refresh the screen with the new layout
        live.refresh()
        
        time.sleep(0.5)

    # Keep the output visible after the loop finishes
    time.sleep(5)

#print("Overlay for chat is starting...\n please link your video ID for your youtube live stream")
#video_id = input("╰─▸") 
#print("clearing text in 3 seconds...")
#time.sleep(3)
#clear_screen()
#print("┏━°⌜ CHAT ⌟°━┓")                         
#chat = pytchat.create(video_id=video_id)
#while chat.is_alive():
    #for c in chat.get().sync_items():
        #print(f"{c.datetime} [{c.author.name}]- {c.message}")
        # Here you can add code to overlay the chat message on your video stream
        # This could involve using a graphics library to render the text on screen
