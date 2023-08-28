#!/usr/bin/env bash

# Loop through all .md files in the current directory
for input_file in *.md; do
  # Skip if no .md files found
  [[ ! -e $input_file ]] && echo "No .md files found" && continue

  # Generate output filename by replacing .md extension with .org
  output_file="${input_file%.md}.org"

  # Perform the conversion
  sed -e 's/^# \(.*\)$/ * \1/' \
      -e 's/^## \(.*\)$/ ** \1/' \
      -e 's/^### \(.*\)$/ *** \1/' \
      -e 's/\*\*\(.*\)\*\$/*\1*/' \
      -e 's/\*\(.*\)\*\$/\1/' \
      -e 's/^\([ \t]*\)`\{3\}\([^ ]*\)/\1#+BEGIN_SRC \2/' \
      -e 's/^\([ \t]*\)`\{3\}/\1#+END_SRC/' \
      -e 's/\[\([^\]]*\)\]\([^\)]*\)/[[\2][\1]]/' \
      "$input_file" > "$output_file"
done
