from cx_Freeze import setup, Executable


base = "Win32GUI"
executable = [Executable("main.py ", targetName='DSA.exe', base=base)]

setup(name='DSA',
      version='1.0',
      description="Digital Signature Algorithm",
      executables=executable)
