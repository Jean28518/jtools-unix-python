# jtools-unix-python
Useful python tools for unix systems.

**Disclamer:** I am beginner to python developing in combination to unix systems.
Don't expect too much!

## How to use jtools in your python project:
- place the e.g.  `jfiles.py` file in the same folder as your own .py file.
- add the line e.g. `import jfiles` for adding functionality of jfiles.py into your own .py file
- call a funtion by writing `jfiles.does_file_exist("my/path")`

## Modules

### jfiles
Easy file handling

- `does_file_exist(string: file_path)` returns true or false
- `get_all_lines_from_file(file_path)` - Returns an array of strings.
    Every string has a `\n` sign in the end.
- `append_line_to_file(file_path, line)` - `\n` signs are added automaticly.
    If file doesn't exist, file will be created.


- `remove_all_lines_with_phrase_from_file(file_path, phrase)` - returns false, if an error occurs, otherwise true. Also returns true, if no line was removed.
- `replace_lines_in_file(file_path, line_to_replace, new_line)` - returns false, if an error occurs, otherwise true.lso returns true, if no line was changed.
- `remove_lines_from_file(file_path, lines)` - Removes the given lines (array of strings, no `\n` needed) from the file.


- `get_line_numbers_with_phrase(file_path, phrase)` - Returns an array of ints, in which lines the given phrase are located.
- `remove_line_numbers_from_file(file_path, line_numbers)` - Removes the given lines_numbers (array of ints) from the file.
- `get_line_numbers_from_lines_in_file(file_path, lines)` - returns an array of numbers, where the specific lines are. lines is an array of strings. This function can search for mutliple lines in one run. Returns an empty array, if nothing was found. No `\n` needed.
- `set_line_numbers_to_line_in_file(file_path, line_numbers, new_line)` - replaces the given line numbers (array of ints) with the string in new_line. Returns false, if no file was found. If some line number are bigger than the current lines in the file `\n` will be inserted, until the given line(s) where reached. new_line doesn't need `\n`.
