import sys

isDebugOn = '-d' in sys.argv
debug     = lambda msg: print(f"• {msg}") if isDebugOn else None