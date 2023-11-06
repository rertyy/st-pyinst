# -*- mode: python ; coding: utf-8 -*-


datas = [("venv/Lib/site-packages/streamlit/runtime", "./streamlit/runtime"), ("venv/Lib/site-packages/streamlit/static", "./streamlit/static"), ("application", "./application")]
hiddenimports=["streamlit"]

block_cipher = None


a = Analysis(
    ['run_main.py'],
    pathex=[],
    binaries=[],
    datas=datas,
    hiddenimports=["streamlit"],
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
