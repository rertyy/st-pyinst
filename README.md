Proof of concept of accessing local files using Streamlit and Pyinstaller.

(If there is an easier way to do it please let me know)

- See https://github.com/whitphx/stlite#limitations
- Electron uses Emscripten, an in-memory file server to store files. Hence, written files do not persist after closing the app if Javascript is not used. See https://pyodide.org/en/stable/usage/file-system.html
- Accessing the internet: https://github.com/whitphx/stlite#example-2-pyodidehttppyfetch

Following tutorial by @charlesmyu at https://discuss.streamlit.io/t/using-pyinstaller-or-similar-to-create-an-executable/902/73
1. Copy whole application, including any `./pages` into `./application`
2. install Pyinstaller using your dependency management system eg `pip install pyinstaller`
3. `touch run_main.py` and modify the code as required, especially `./application/main.py`  for entry point to application
```import os
import streamlit.web.bootstrap

if __name__ == "__main__":
    os.chdir(os.path.dirname(__file__))

    flag_options = {
        "server.port": 8501,
        "global.developmentMode": False,
    }

    streamlit.web.bootstrap.load_config_options(flag_options=flag_options)
    flag_options["_is_running_with_streamlit"] = True
    streamlit.web.bootstrap.run(
        "./application/main.py", # modify this as required
        "streamlit run",
        [],
        flag_options,
    )
```
4. `touch ./hooks/hook-streamlit.py`
```from PyInstaller.utils.hooks import copy_metadata
datas = copy_metadata('streamlit')
```
5. Run command `pyi-makespec --onefile --additional-hooks-dir=./hooks run_main.py`. This should return a `run_main.spec`
6. Modify run_main.spec so it looks something like the following. 
- Add the top few lines, and then change the `datas=datas` and `hiddenimports=hiddenimports`
- Make sure the `/venv/Lib/site-packages` follows appropriate dependency management system.
- For Windows the Pipenv venv looks like
`C:\Users\<name>\.virtualenvs\<venv>\Lib\site-packages`
```
from PyInstaller.utils.hooks import collect_data_files
from PyInstaller.utils.hooks import copy_metadata

# -*- mode: python ; coding: utf-8 -*-

datas = [("venv/Lib/site-packages/streamlit/runtime", "./streamlit/runtime"), ("venv/Lib/site-packages/streamlit/static", "./streamlit/static"), ("application", "./application")]
hiddenimports = ["streamlit"]

block_cipher = None


a = Analysis(
    ['run_main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=hiddenimports,
    hookspath=['./hooks'],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    noarchive=False,
)
pyz = PYZ(a.pure)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='run_main',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
```
7. Now run
`pyinstaller run_main.spec --clean`
8. This generates  `/dist/run_main.exe` which can then be run