"""Module to encypt and decrypt data"""


import pyAesCrypt


def encrypt(file, password, output):
    """Encrypt file"""
    pyAesCrypt.encryptFile(file, output, password)


def decrypt(file, password, output):
    """Decrypt file"""
    pyAesCrypt.decryptFile(file, output, password)
