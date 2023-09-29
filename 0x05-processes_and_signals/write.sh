#!/usr/bin/env bash

text="#!/usr/bin/env bash"

for file in *; do
    if [[ -f $file && $(head -n 1 "$file") != "$text" ]]; then
        echo "$text" | cat - "$file" > temp && mv temp "$file"
        echo "Added '$text' to $file"
    fi
done
