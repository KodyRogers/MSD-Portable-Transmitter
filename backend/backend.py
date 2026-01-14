import ctypes

def process(value):
    # Example function that uses ctypes to call a C library function
    libc = ctypes.CDLL("libc.so.6")
    message = b"Hello from C library!\n"
    libc.printf(message)