"""
Contains the random generation code for functions, variables, and data
"""

import random

randomFirstChar = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_'
randomVarChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
randomChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-'
encChars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-!@#$%^&*()+=[]{}|:;\'/?<>.,'

# Generate a random function
def genFunc(randomFuncSize):
  firstFuncChar = ''.join(random.SystemRandom().choice(randomFirstChar) for _ in xrange(1))
  remFuncChar = ''.join(random.SystemRandom().choice(randomVarChars) for _ in xrange(randomFuncSize-1))
  return firstFuncChar + remFuncChar

# Generate a random variable
def genVar(randomVarSize):
  firstVarChar = ''.join(random.SystemRandom().choice(randomFirstChar) for _ in xrange(1))
  remVarChar = ''.join(random.SystemRandom().choice(randomVarChars) for _ in xrange(randomVarSize-1))
  return firstVarChar + remVarChar

# Generate random data
def genData(dataLen):
  return ''.join(
      random.SystemRandom().choice(randomChars) for _ in xrange(dataLen))

# Generate an encryption key
def genKey(encKeyLen):
  return ''.join(
      random.SystemRandom().choice(encChars) for _ in xrange(encKeyLen))

# Generate an IV for encryption
def genIv(encIvLen):
  return ''.join(
      random.SystemRandom().choice(encChars) for _ in xrange(encIvLen))