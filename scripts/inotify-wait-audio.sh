#!/bin/sh

inotifywait -m -e MOVED_TO --format "%f" --include '\.wav$' . 2> /dev/null | while read -r audio_file; do  whisper -f txt --language pt "$audio_file" -o teste/ ; done
