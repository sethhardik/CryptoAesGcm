# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 13:55:01 2021

@author: Hardik Seth
"""
from Crypto.Random import get_random_bytes
from Crypto.Cipher import AES
import json
from base64 import b64encode,b64decode

# create key with bytes passed  and store the  key in path passed
def AES_GCM_CreateSaveKey(key_location,No_bytes=32):
    try:
        # * bytes * 8 = ** bits (1 byte = 8 bits)
        key = get_random_bytes(No_bytes) 
        # Save the key to a file
        file_out = open(key_location, "wb") # wb = write bytes
        file_out.write(key)
        file_out.close()
        return True
    except:
        return False


def AES_GCM_EncryptData(message,key_location,ret_type = "concat"):
    # check if the message is in  string convert it into bytes as encryption can only be done in bytes
    try:
        message_binary = message.encode('utf-8')
    except AttributeError:
        message_binary = message
    # fetch key from the location and read the values in binary
    try:
        f = open(key_location,"rb")
        key = f.read()
    except FileNotFoundError:
        return (False,"No key found in the path provided")
    # creating new cipher class with key and GCM mode of encryption
    cipher = AES.new(key, AES.MODE_GCM)
    # encryping message using GCM logic 
    ciphertext, tag = cipher.encrypt_and_digest(message_binary)
    if ret_type == "concat":
        # concatinating tag nonce and ciphertext in single variable.
        # tag size is 16bits , nonce is also 16bits and will not change hence can easily be removed from the concated values
        result = tag+cipher.nonce+ciphertext
        result = b64encode(result).decode('utf-8')
        # print(tag,cipher.nonce)
        # return (True, send_data)
    elif ret_type == "json":
        json_k = [ 'nonce', 'ciphertext', 'tag' ]
        json_v = list()
        for x in cipher.nonce, ciphertext, tag:
            json_v.append(b64encode(x).decode('utf-8'))
        result = json.dumps(dict(zip(json_k, json_v)))
        print(result)
    else:
        return (False,"Wrong ret type entered. Accepted input ('concat'/'json')")
    return (True, result)

# function to decrypt the data. you can pass key location, input_type of encrypted data wheather it is concat or json file
def AES_GCM_DecryptData(encrypted_input,key_location):
    # fetch key from the location and read the values in binary
    try:
        f = open(key_location,"rb")
        key = f.read()
    except FileNotFoundError:
        return (False,"No key found in the path provided")
    # checking type of value inputed if type is bytes we use concated logic in encryption and decrypt the function
    if type(encrypted_input) == str:
        try:
            encrypted_input = b64decode(encrypted_input)
            tag = encrypted_input[:16]
            nonce = encrypted_input[16:32]
            ciphertext = encrypted_input[32:]
        except:
            return (False, "not able to unpack the values from concated values")
    # if type is dictionary or string  we use the json data extraction and save the values
    elif type(encrypted_input) == dict:
        try:
            try:
                # if json is passed without loading it loads the json and then proceed forward else run without loading
                b64 = json.loads(encrypted_input)
            except:
                b64 = encrypted_input
            json_k = [ 'nonce', 'ciphertext', 'tag' ]
            jv = {k:b64decode(b64[k]) for k in json_k}
            # saving values in the variables
            nonce = jv['nonce']
            tag = jv['tag']
            ciphertext = jv['ciphertext']
        except:
            return (False,"not able to unpack values from json")
    # if different datatype is found we raise error 
    else:
        return (False,"type(encrypted_input) not allowed, you can pass type(): 'bytes' or 'dict'/'str'")
    
    try:
        cipher = AES.new(key, AES.MODE_GCM, nonce=nonce)
        plaintext = cipher.decrypt_and_verify(ciphertext, tag)
        # converting value into string
        decrypted_result = plaintext.decode("ascii")
        return (True, decrypted_result)
    except ValueError or  KeyError:
        return (False,"Incorrect decryption. Message might be tempered with or corrupted")


# AES_GCM_CreateSaveKey("key.bin")
# encrytped = AES_GCM_EncryptData("My name is hardik seth","key.bin")
# print(encrytped)
# asd = encrytped[1]
# # # # asdf = json.loads(asd)
# # # # print(asdf)
# # # # if asdf ==dict:
# # # #     print("Asdsad it is dict")
# # # # print(type(asd))
# data = AES_GCM_DecryptData(asd,"key.bin")
# print(data)
