from typing import TypedDict, Optional
from tkinter import *
import tkinter.font as tkFont

class Key(TypedDict):
    label: str
    # Refer to Tkinter keycodes:
    # https://stackoverflow.com/a/32289245
    codes: list[str]
    x: int
    y: int
    width: Optional[int]
    height: Optional[int]

KEYS: list[Key] = [
    {
        "label": "W",
        "codes": ["W", "w"],
        "x": 1,
        "y": 0,
        "width": None,
        "height": None
    },
    {
        "label": "A",
        "codes": ["A", "a"],
        "x": 0,
        "y": 1,
        "width": None,
        "height": None
    },
    {
        "label": "S",
        "codes": ["S", "s"],
        "x": 1,
        "y": 1,
        "width": None,
        "height": None
    },
    {
        "label": "D",
        "codes": ["D", "d"],
        "x": 2,
        "y": 1,
        "width": None,
        "height": None
    },
    {
        "label": "Jump",
        "codes": ["<space>"],
        "x": 0,
        "y": 2,
        "width": 3,
        "height": 0.5
    },
]

KEY_WIDTH = 64
KEY_HEIGHT = 64
KEY_TEXT_SIZE = 24
KEY_MARGIN = 2

root = Tk(screenName="Bikey", baseName="Bikey", className='Tk', useTk=1)
canvas = Canvas(root, background='black')
canvas.grid(column=0, row=0, sticky=(N, W, E, S))

font = tkFont.Font(family="Arial", size=KEY_TEXT_SIZE)

def render_key(key: Key, bg_fill, fg_fill):
    label = key.get("label")
    
    x0 = key.get("x") * KEY_WIDTH + KEY_MARGIN
    y0 = key.get("y") * KEY_HEIGHT + KEY_MARGIN
    
    width = key.get("width") or 1
    height = key.get("height") or 1
    
    real_width = width * KEY_WIDTH
    real_height = height * KEY_HEIGHT
    
    x1 = x0 + real_width - KEY_MARGIN
    y1 = y0 + real_height - KEY_MARGIN
    
    canvas.create_rectangle(
        x0,
        y0,
        x1,
        y1,
        fill=bg_fill
    )
    
    text_width = font.measure(label)
    
    canvas.create_text(
        x0 + real_width / 2,
        y0 + real_height / 2,
        text=label,
        fill=fg_fill,
        justify="center",
        font=font
    )

for key in KEYS:
    render_key(key, "white", "black")
    
    def on_pressed(event: Event, key=key):
        render_key(key, "yellow", "black")
    
    for keycode in key.get("codes"):
        root.bind(keycode, on_pressed)

canvas.pack()
root.mainloop()
