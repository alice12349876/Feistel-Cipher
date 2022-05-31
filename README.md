## Feistel Cipher
This project covers the history, strengths, and weaknesses of Feistel Cipher. In addition, this project dives deeper into the structure and algorithms of Feistel Cipher, with an encoder and decoder. \

## How to Use This
The Feistel Cipher encoder and decoder (encoder.py and decoder.py respectively) are coded in Python, and they can be found in the code directory. There is no need to install third-party libraries. \
To run encoder.py, make sure you are in the right directory and run the following command:
```
python3 encoder.py [Plain Text] [Key of length 64 bits]
```
The ciphertext will be written to cipheredText.txt in binary string, and this file can be found in the same directory as encoder.py. \
To run decoder.py, make sure you are in the right directory and run the following command:
```
python3 decoder.py [Key of length 64 bits]
```
decoder.py will read in ciphertext from cipheredText.txt and can successfully decode the ciphertext if the same key used for encryption is provided. \
## Other Resources
[Presentation](PRESENTATION.md) \
[Homework](HOMEWORK.md)
