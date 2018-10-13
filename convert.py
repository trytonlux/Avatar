#!/usr/bin/env python3

import gi
gi.require_version('Rsvg', '2.0')

from gi.repository import Rsvg
import cairo

FILENAME_BASE = "avatar"
INPUT_FILE = FILENAME_BASE + ".svg"

# Because we're not a perfect square. Use ratio to get height for whatever
# size we want (height/width).
SIZE_RATIO = 280/264

def convert(size):
    img = cairo.ImageSurface(cairo.FORMAT_ARGB32, size, int(size * SIZE_RATIO))
    ctx = cairo.Context(img)

    # Scale the SVG to the new size
    scale_ratio = size/264
    ctx.scale(scale_ratio, scale_ratio)

    handle = Rsvg.Handle()
    svg = handle.new_from_file(INPUT_FILE)
    svg.render_cairo(ctx)

    img.write_to_png(str(size) + "x.png")

if __name__ == "__main__":
    sizes = [32, 64, 128, 264, 512]

    for size in sizes:
        convert(size)
