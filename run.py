import os, sys
try:
    __import__("UA").main()
except Exception as e:
    exit(str(e))
