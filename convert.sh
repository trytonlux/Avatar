#!/bin/sh

check_rsvg()
{
    if ! type "rsvg-convert" > /dev/null; then
        echo "missing dependency: librsvg"
        exit
    fi
}

check_rsvg