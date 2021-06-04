import pefile

print("Loading File")

pe = pefile.PE('', fast_load=True)

print("File Loaded")
print("Changing Header to prevent memory relocation")

pe.OPTIONAL_HEADER.DllCharacteristics = 0x8120

print("Header Modified")
pe.write(filename='')

print("File Saved!")

# From Here: https://bbs.pediy.com/thread-257743.htm