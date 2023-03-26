import os, sys
try:
    __import__("ua").main()
except Exception as e:
    exit(str(e))
