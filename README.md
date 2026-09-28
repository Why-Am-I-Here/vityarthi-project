# Text Obfuscation

Text obfuscation takes your input string and randomizes it through various slicing techniques and makes it almost impossible to read without the built in decryption tool.
Vityarthi project for BTech CSE Semester 1.
Reg No. : 26BAI10949
Name: Himanshu Gangwar

## Required Modules/Libraries:

- Python version 3.14.7

- Random (This library is inbuilt with Python so, doesn't require installation)

## Installation:

```
git clone https://github.com/Why-Am-I-Here/vityarthi-project

cd vityarthi-project
```

## Usage Instructions:

- Do place all your files in one directory so that the code can refer to different functions located in different files.
- Users should initiate the file "terminal.py."
- When asked users can input 1 to encrypt the string or 2 to decrypt a string.
- The final encrypted or decrypted text will now be output by the program.

## Testing Instructions:

Here project includes unit tests for testing modules within project using Python in-built unittest framework to ensure all modules working fine.
1. The user has to open the terminal in the project directory.

2. Run it: python -m unittest test_project.py

3. If all the string manipulation logic worked correctly, then terminal should print OK.

## Screenshots:

* Encryption Process: [Encryption](https://ik.imagekit.io/brwwpvjhs/Screenshot%202026-09-28%20000440.png)

* Decryption Process: [Decryption](https://ik.imagekit.io/brwwpvjhs/Screenshot%202026-09-28%20000440.png)

# Note:

- It is recommended to keep only the encrypted text yielded by the code when using the decrypt option to prevent such errors caused by string length limitation.
- Encryption should not be applied to single character words.
