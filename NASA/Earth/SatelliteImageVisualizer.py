import tkinter as tk
from PIL import ImageTk, Image
import aiohttp
import asyncio
from io import BytesIO

"""
Diese Klasse müsst ihr nicht anfassen. (Insbesondere der asynchrone Download ist trotzdem interessant)
"""


class SatelliteImageVisualizer:
    def __init__(self, root, image_urls, dates):
        self.root = root
        self.image_urls = image_urls
        self.dates = dates
        self.current_index = 0
        self.image_buffer = []  # Store downloaded images

        self.root.title("Darmstadt Over Time")  # Change window title

        self.image_label = tk.Label(root)
        self.image_label.pack()

        self.date_label = tk.Label(root, text="Date: " + self.dates[self.current_index])
        self.date_label.pack()

        self.prev_button = tk.Button(root, text="Previous", command=self.show_previous_image)
        self.prev_button.pack(side=tk.LEFT)

        self.next_button = tk.Button(root, text="Next", command=self.show_next_image)
        self.next_button.pack(side=tk.RIGHT)

        self.loop = asyncio.get_event_loop()
        self.loop.run_until_complete(self.download_images())  # Download images asynchronously on startup
        self.show_image()

    async def download_image(self, session, url):
        print("Downloading " + url)
        async with session.get(url) as response:
            image_data = await response.read()
            image = Image.open(BytesIO(image_data))
            image = image.resize((600, 600), Image.LANCZOS)  # Use LANCZOS filter for antialiasing
            self.image_buffer.append(image)
            print("Downloaded " + url + "\n\n")

    async def download_images(self):
        async with aiohttp.ClientSession() as session:
            tasks = [self.download_image(session, url) for url in self.image_urls]
            await asyncio.gather(*tasks)

    def show_image(self):
        image = self.image_buffer[self.current_index]
        photo = ImageTk.PhotoImage(image)
        self.image_label.configure(image=photo)
        self.image_label.image = photo
        self.date_label.config(text="Date: " + self.dates[self.current_index])

    def show_next_image(self):
        if self.current_index < len(self.image_urls) - 1:
            self.current_index += 1
            self.show_image()

    def show_previous_image(self):
        if self.current_index > 0:
            self.current_index -= 1
            self.show_image()


def display_satellite_images(image_urls, dates):
    root = tk.Tk()
    app = SatelliteImageVisualizer(root, image_urls, dates)
    app.root.mainloop()
