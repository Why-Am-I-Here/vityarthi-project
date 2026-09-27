# Project Statement: Vityarthi Text Obfuscation Tool

## Problem Statement
In an increasingly digital landscape, users often need a lightweight, quick method to obscure plain text messages before sharing them over unsecured communication channels. Heavyweight encryption protocols are often too complex for simple, everyday text obfuscation. 

## Scope of the Project
This project provides a custom, client-side string encryption and decryption command-line interface (CLI) application. It slices strings, reverses character orders, and injects randomized alphanumeric salts to encode standard text. The scope is limited to terminal-based execution using Python's standard libraries, without requiring external database integrations or third-party cryptographic modules.

## Target Users
* Students and developers looking for a fast, local tool to obfuscate strings.
* Individuals wanting to send visually scrambled text messages that can only be decoded by a peer possessing the same Python script.

## High-Level Features
1. **Interactive CLI:** A continuous terminal loop allowing users to easily choose between encrypting and decrypting data without restarting the program.
2. **Custom Slicing Algorithm:** Dynamically splits strings into front and back halves, reversing the sequence to scramble readability.
3. **Randomized Salting:** Injects randomly generated numeric and alphabetic character blocks at the front, middle, and back of the string to alter the final string length and disguise the core data.
4. **Lossless Decryption:** Accurately strips injected random characters and reconstructs the original string based on reverse mathematical slicing.
