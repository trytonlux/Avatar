#!/usr/bin/env python3

import gi
gi.require_version('Rsvg', '2.0')

from gi.repository import Rsvg
import cairo

FILENAME_BASE = "avatar"
INPUT_FILE = FILENAME_BASE + ".svg"

def convert(size):
    img = cairo.ImageSurface(cairo.FORMAT_ARGB32, size, size)
    ctx = cairo.Context(img)

    # Scale the SVG to the new size
    ctx.scale(size/512, size/512)

    handle = Rsvg.Handle()
    svg = handle.new_from_file(INPUT_FILE)
    svg.render_cairo(ctx)

    img.write_to_png(str(size) + "x.png")

if __name__ == "__main__":
    sizes = [32, 64, 128, 264, 512]

    for size in sizes:
        convert(size)
