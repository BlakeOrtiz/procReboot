# procReboot

Simple process monitor and rebooter. Mainly using this for hosted servers that decide to close themselves without warning. Ex: Palworld...

## Usage:
Main functionality is only added for Windows systems (May make it cross-OS supported in the future)
`py procReboot.py <Insert Path with executable>`

OR

`py procReboot.py`
- You will be prompted to enter your full path.

The script will then begin to monitor your entered executable within the TASKLIST. If the executable is seen as not running, it will attempt to run said executable and continue to monitor afterward.
