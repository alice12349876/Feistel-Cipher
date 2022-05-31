# Feistel Cipher 

## History
* The Feistel Cipher is a block cipher that recursively applies a round function.
* Feistel cipher first gained respect when it was adopted by the US Government, and used within the National Security Agency.
* The recursion of the feistel cipher makes the hardware for the cipher easier to implement.
* While research shows that 3 rounds are enough for pseudorandom encryption, 4 rounds are enough for "strong" pseudorandom encryption.

## Security Strength
* Key Size: A larger key size means more security.
* Block Size: A larger block size means more security.
* Subkey Generation: Increasing the complexity in how the subkeys are generated from the key increases security.
* Rounds: Increasing the number of rounds, or the number of times a round function is applied, increases security.

## Data Encryption Standard (DES)
* The Data Encryption Standard is the most famous type of Feistel Cipher, and was the most popular encryption method in the 1970s-1990s.
* 64 bit input block
* 64 bit output block
* 64 bit key
* 16 rounds

## Basic Structure
![Feistel Cipher Structure](img/BasicStructure.png)
<center>Data Encryption Standard Basic Structure</center>

\
![Initial and Final Permutation Table](img/PermutationTables.png)
<center>Initial and Final Permutation Tables</center>

\
![One Round](img/OneRound.png)
<center>One Feistel Round</center>

\
![f function](img/ffunction.png)
<center>F Function</center>

\
![Expansion D Box](img/expansionBox.png)
<center>Expansion D-Box</center>

\
![S Boxes](img/sBox.png)
<center>S Box</center>

\
![Straight D-Box](img/straightPermutation.png)
<center>Straight D-Box (Straight Permutation)</center>

\
![Key Generation](img/KeyGeneration.png)
<center>Key Generation</center>

\
![Parity Drop](img/parityDrop.png)
<center>Parity-Drop Permutation Table</center>

\
![Key Compression](img/keyCompression.png)
<center>Compression D-Box</center>

## Strengths
* Involution Property
* Similar encryption and decryption algorithms
* F does not have to be invertible

## Weaknesses
* Weak and semi-weak keys: Block ciphers are often used in hash modes where the key input can be chosen by hackers in an attempt to find collisions.
* Existence of differential attack (if one is possible): Differential attack/cryptanalysis the study of how differences in input can be reflected in the differences of output. The discovery of non-random behavior can be exploited to recover the key.
* Less parallelism: Substitution permutation network (SPN) has more “inherent parallelism,” which means SPN can be computed much faster than Feistel Cipher. But the difference in computing time is more obvious when the computer has a CPU with many execution units.

## Variations
* DES (Data Encryption Standard): 16 rounds, 64-bit block size, 64-bit key with an effective key length of 56 bits (extra 8 bits as parity bits)
* Twofish: 16 rounds, 128-bit block size, key size up to 256 bits (128, 192, 256 bits)
