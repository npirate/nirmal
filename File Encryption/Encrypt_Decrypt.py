import pyAesCrypt
bufferSize = 6 * 1024
password = 'password'

pyAesCrypt.encryptFile('test.csv','test.csv.aes',password,bufferSize)
