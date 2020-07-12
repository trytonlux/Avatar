#!/bin/sh

check_rsvg()
{
    if ! type "rsvg-convert" > /dev/null; then
        echo "missing dependency: librsvg"
        exit
    fi
}

convert_svg()
{
    # Converts avatar.svg to a PNG with given size
    rsvg-convert --height="$1" --width="$1" --output "x$1.png" avatar.svg
}

check_rsvg
convert_svg 512
convert_svg 256
convert_svg 128
convert_svg 64