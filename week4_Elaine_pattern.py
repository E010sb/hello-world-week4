import math
import sys
from pathlib import Path
from PIL import Image, ImageDraw


SIZE = 1000
SCALE = 4
CURVES = 36
STEPS = 2400
PETALS = 5
BACKGROUND = "white"


def draw_pattern():
    image = Image.new("RGB", (SIZE * SCALE, SIZE * SCALE), BACKGROUND)
    drawing = ImageDraw.Draw(image)

    for curve in range(CURVES):
        progress = curve / (CURVES - 1)
        distance = 90 + progress * 85
        red = round(222 + (111 - 222) * progress)
        green = round(206 + (55 - 206) * progress)
        blue = round(246 + (180 - 246) * progress)
        color = (red, green, blue)
        points = []

        for step in range(STEPS + 1):
            angle = step / STEPS * math.tau
            x = 205 * math.cos(angle) + distance * math.cos((PETALS - 1) * angle)
            y = 205 * math.sin(angle) - distance * math.sin((PETALS - 1) * angle)

            screen_x = (SIZE / 2 + y) * SCALE
            screen_y = (SIZE / 2 - x) * SCALE
            points.append((screen_x, screen_y))

        drawing.line(points, fill=color, width=3)

    return image.resize((SIZE, SIZE), Image.Resampling.LANCZOS)


def main():
    image = draw_pattern()
    output = Path(__file__).with_name("purple_bloom.png")
    image.save(output)

    if "--save-only" not in sys.argv:
        import tkinter as tk
        from PIL import ImageTk

        window = tk.Tk()
        window.title("Purple Bloom - Elaine - Week 4")
        preview = image.resize((760, 760), Image.Resampling.LANCZOS)
        photo = ImageTk.PhotoImage(preview)
        label = tk.Label(window, image=photo, borderwidth=0)
        label.pack()
        window.mainloop()


if __name__ == "__main__":
    main()
