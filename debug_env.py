import os
import sys

with open("debug_out.txt", "w") as f:
    f.write("System Path: " + str(sys.path) + "\n")
    try:
        from fastapi import FastAPI
        f.write("FastAPI imported successfully\n")
    except Exception as e:
        f.write("FastAPI import failed: " + str(e) + "\n")
