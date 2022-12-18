&&: logical and (operate the second command after the first seccessfully executes)
`$((newval - oldval))`: perform arithmetic

Two main types of variables
  1. Environment variables:
       * Global variables shared by all shells and child processes 
  2. Shell variables: 
    * Available in the shell they are defined. (Temporary) 

Commands:
  - `cut` -> cuts vertically by different delimeters. 
    - `c` for characters(eg. `c 1-5`, `-c 6,8,8`, `-c :11`) 
    - `d` for delimeter. (tabs --default, comma, spaces) 
    - `f` for field. (i.e. `-d, -f 1`)
  - `sort` -> row sort
    - o output
    - r reverse
    - u unique
    - k sort by a specific column
    - n sort numerically
  - `uniq`
    - c counts

command flags:
  -v: verbose. Works with most commands
  

