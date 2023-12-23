# HFM
Host-File-Modifier (HFM) ~~ Version 1.0

This script is used to generate a custom script that will modify the contents of the hosts file with the given input. The generated script can then be sent to anybody, and upon execution, the generated script will modify the hosts file's content.

The current version only works for Windows (The script can be generated using any operating system, as long as Python is installed, but the generated script will only execute on Windows). I'm working on a Linux version.

The current version triggers UAC. I'm working on a solution.

Not to be used for malicious purposes.

Example input: -website: example.com -redirect IP: 1.1.1.1
This example will redirect 'example.com' to '1.1.1.1'.(Basically nowhere).

If you encounter any issues, please contact me.
