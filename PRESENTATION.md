# History
* The Feistel Cipher is a block cipher that recursively applies a round function.
* Feistel cipher first gained respect when it was adopted by the US Government, and used within the National Security Agency.
* The recursion of the feistel cipher makes the hardware for the cipher easier to implement.
* While research shows that 3 rounds are enough for pseudorandom encryption, 4 rounds are enough for "strong" pseudorandom encryption. 

# Strengths
* Involution Property
* Similar encryption and decryption algorithms
* F does not have to be invertible

# Weaknesses
* Weak and semi-weak keys nat ve ysed. Block ciphers (Feistel cipher is the structure from which many block ciphers developed from) are often used in hash modes where the key input can be chosen by hackers in an attempt to find collisions.
* Differential attack (if one is possible). Differential attack is the study of how differences in input can be reflected in the differences of output. In the case of a block cipher, it refers to tracing differences through the network of transformation, discovering where the cipher exhibits non-random behavior, and exploiting such properties to recover the key.
* The parallelism of Feistel Cipher is about half of an equivalent substitution permutation network (SPN). SPN has more “inherent parallelism,” which means SPN can be computed much faster than Feistel Cipher. But the difference in computing time is more obvious when the computer has a CPU with many execution units.

# Variations
* DES (Data Encryption Standard): 16 rounds, 64-bit block size, 64-bit key though effective key length is only 56 bits (extra 8 bits as check bits)
* Twofish: 16 rounds, 128-bit block size, key size up to 256 bits (128, 192, 256 bits)
