# Crypto Aes GCM

`CryptoAesGcm` package is a Wrapper for `Cypto.Aes` package and makes encryption and decryption easier.


Links to understand basics of AES and GCM algorithms:
1. <https://acodez.in/data-encryption-algorithms/>
2. <https://www.tutorialspoint.com/cryptography/block_cipher.html>
3. <https://www.tutorialspoint.com/cryptography/advanced_encryption_standard.html>.



## what you can do:

* Generate **Encryption Key**
* Using Encryption Key, Encrypt string and get O/P in json/concat String format
* Decrypt already encrypted string back to plain text format

## Installation

```
pip install CryptoAesGcm
```

## Usage

Example - Generate Key :
```python
>>> from CryptoAesGcm import AES_GCM_CreateSaveKey

# pass location where you want key to saved at 

>>> print(AES_GCM_CreateSaveKey(key_location,No_bytes=32))  # by default No_bytes = 32
True
```

Example - Encrypt text:
```python
>>> from CryptoAesGcm import AES_GCM_EncryptData

# for ret_type = "json"
>>> ret = AES_GCM_EncryptData("Random text data","key.bin",ret_type = "json")  # by default ret_type =  "concat")
>>> print(ret)
(True, '{"nonce": "plgyFSJ3+DCQdsVT/T+Nsg==", "ciphertext": "1iMBFpaJoDmuT3LgtYsbz79MPYRMbQ==", "tag": "T3Ivn95YHSK8Z25VXT0+zQ=="}')

# for  default ret_type = "concat"
>>> ret = AES_GCM_EncryptData("Random text data","key.bin")
>>> print(ret)
(True, '1f8GuiS+Tn2X1rKKryDth0B96RkLBFl+vSX2TfqdW6/yTjgOVJDKF2RmyfQO5q5YI2IhK/ru')
```

Example - Decrypt text:
```python
>>> from CryptoAesGcm import AES_GCM_DecryptData

# you can pass both concatinated and json format as input 
# function will itself find the best way to decrypt and return the O/P
>>> ret = AES_GCM_DecryptData("encrypted text","key.bin")
>>> print(ret)
(True, 'Random text data')

```


###### Note: Function returns tuple if code fails to execute 1st element will be False else it will be True.