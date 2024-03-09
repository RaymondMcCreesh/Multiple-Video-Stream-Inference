import sys
from PyInstaller.__main__ import run as pyinstaller_run

# path to .py file
name = 'second_pyqt5'
script_path = 'second_pyqt5.py'

# path to save exe
dist_path = 'executable'

exe_name = name + '.exe'

# icon path can be addded

# name of the .spec file
spec_name = name + '.spec'

# Create the .spec file
with open(spec_name, 'w') as f:
    f.write(f'''
block_cipher = None

a = Analysis(
    ['{script_path}'],
    pathex=['{dist_path}'],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)
exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name=os.path.join('{dist_path}', '{exe_name}'),
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=True,
    disable_windowed_traceback=False,
    version_file=None,
    ctypes_compiler_flags=None,
    windows_subsystem_version=5,
)
coll = COLLECT(
    exe,
    Tree('{dist_path}'),
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name=os.path.join('{dist_path}', '{exe_name}'),
)
''')

# Run PyInstaller to create the executable file
pyinstaller_run([
    '--clean',
    '--onefile',
    '--distpath', dist_path,
    '--workpath', 'workpath',
    '--specpath', 'spec',
    '--name', exe_name,
    'second_pyqt5.py',
])