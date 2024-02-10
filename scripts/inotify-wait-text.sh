#!/bin/sh
#
inotifywait -m -e create --format "%f" --include '\.txt$' . 2> /dev/null | { while read -r text_file; do cat "$text_file"; done }
