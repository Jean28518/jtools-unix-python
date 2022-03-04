# jtools-unix-python
Useful python tools for unix systems.

**Disclamer:** I am beginner to python developing in combination to unix systems.
Don't expect too much!

## How to use jtools in your python project:
- place the e.g.  `jfiles.py` file in the same folder as your own .py file.
- add the line e.g. `import jfiles` for adding functionality of jfiles.py into your own .py file
- call a funtion by writing `jfiles.does_file_exist("my/path")`

## Modules

### jessentials

- `ensure_root_privileges()` - Checks, if script is running as root user. Otherwise exits with error message
- `is_scirpt_running_as_root` - Returns boolean whether this script is running as root user.

- `does_file_exist(file_paht)` - Returns boolean

- `replace_tilde_to_home(folder_path)` - Turns e.g. `~/Dowloads/file.txt` to `/home/jean/Downloads/file.txt`. Returns the new path as string.

- `run_command(command, print_output=True, return_output=False, enviroment = {})` - Runs the command in foreground
    - `command`: String containing the full command. Example: `apt install firefox -y`
    - `print_output`: If not set to False, the output of the command is printed to the stdout.
    - `return_output`: If set to True, returns the output as array of strings.
    - `enviroment`: Here you can set Inviroment variables in a dict. Example: `{'DEBIAN_FRONTEND': 'noninteractive'}`

- `get_arguments()` - Returns all given arguments in an array of strings
- `get_value_from_arguments(value_key, default=None)` - If user gave argument, then it returns the given value. Otherwise returnes the default value, which you can set optionally. Example for correct argument: `--hostname=192.168.1.1`
- `is_argument_option_given(long_code="", short_code="")` - Checks, if user give an argument without a value. Example: `long_code="recursive", short_code="r"` User: `--recursive` or `-xry` -> then this function returns True, otherwise False.

- `fail(error_message="")` - Exits script imediately and optionally prints given error message.

- `printerr(message)` - Prints an error message to stderr.

- `remove_duplicates(array)` - Returns a array without duplicated elements.
- `is_element_in_array(array, element)` - Returns true if array has given element. Otherwise returns false.

- `get_table_of_csv_file(file_path)` - Reads a csv file and returns a resulting 2 dimensional array.

- `get_accessible_table_of_raw_csv_table(csv_raw_table)` - Input a table like e.g. `[["City", "Distance"], ["Nuremberg", 35], ["Munich", 87,4]]`, returns a table like: `[{"City": "Nuremberg", "Distance": 35} , {"City": "Munich", "Distance": 87,4}]`. You can easily acces such a table through: `table[0]["City"]` *In this example it would return 'Nuremberg'.*

### jfiles
Easy file handling

- `does_file_exist(string: file_path)` returns true or false.
- `copy_file(source_path, destination_path)` - Copies file at source_path to destination_path. May overwrites existing file.
- `get_all_lines_from_file(file_path)` - Returns an array of strings.
    Every string has a `\n` sign in the end.
- `write_lines_to_file(file_path, lines)` - Writes array of strings to given path. May overwrite existing file.
- `append_line_to_file(file_path, line)` - `\n` signs are added automatically.
    If file doesn't exist, file will be created.
---
- `get_value_from_file(file_path, value_key)` - Returns None, if file not found, value not found, or value empty. Otherwise returns a string. File has to have the value in this format: `value_key=value`. `!@/n` will be converted to newlines (`\n`)
- `set_value_in_file(file_path, value_key, value)` - Self explaining. Newlines (`\n`) are converted to `!@/n`.

- `remove_all_lines_with_phrase_from_file(file_path, phrase)` - returns false, if an error occurs, otherwise true. Also returns true, if no line was removed.
- `replace_lines_in_file(file_path, line_to_replace, new_line)` - returns false, if an error occurs, otherwise true.lso returns true, if no line was changed.
- `remove_lines_from_file(file_path, lines)` - Removes the given lines (array of strings, no `\n` needed) from the file.
---
- `get_line_numbers_with_phrase(file_path, phrase)` - Returns an array of ints, in which lines the given phrase are located. Counting starts from 1.
- `remove_line_numbers_from_file(file_path, line_numbers)` - Removes the given lines_numbers (array of ints) from the file.
- `get_line_numbers_from_lines_in_file(file_path, lines)` - returns an array of numbers, where the specific lines are. lines is an array of strings. This function can search for mutliple lines in one run. Returns an empty array, if nothing was found. No `\n` needed.
- `set_line_numbers_to_line_in_file(file_path, line_numbers, new_line)` - replaces the given line numbers (array of ints) with the string in new_line. Returns false, if no file was found. If some line number are bigger than the current lines in the file `\n` will be inserted, until the given line(s) where reached. new_line doesn't need `\n`.



### jfolders
- `touch_folder(folder_path)` - Ensures that given folder path exists. Otherwise it creates all folders to the given path.
- `does_folder_exist(folder_path)` - Returns boolean.
- `replace_tilde_to_home(folder_path)` - Turns e.g. `~/Dowloads/file.txt` to `/home/jean/Downloads/file.txt`. Returns the new path as string.
- `get_folder_entries(folder_path)`- Returns an array of strings with the full path of the entries of a folder.
- `get_folder_entry_names(folder_path)` - As `get_folder_entries(folder_path)`, but only retrives the names of the folder entries, not the whole path.
