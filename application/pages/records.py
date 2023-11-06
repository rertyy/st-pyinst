import os
import platform

import streamlit as st

os_platform = platform.system()
st.write(os_platform)
localappdata = os.getenv("LOCALAPPDATA")
st.write(localappdata)
program_dir = os.path.join(localappdata, "streamlit-app")
os.makedirs(program_dir, exist_ok=True)
st.write(program_dir)
file_loc = os.path.join(program_dir, "output.txt")

write_value = st.text_area("Enter text here")

write_button = st.button("write output")
if write_button:
    with open(file_loc, "w") as f:
        f.write(write_value)
        st.success(f'Text {write_value} has been written to output.txt')

read_button = st.button("read output")
if read_button:
    try:
        with open(file_loc, "r") as f:
            read_value = f.read()
            st.success(f'Text {read_value} has been read from output.txt')
    except FileNotFoundError:
        st.error("File not found")

delete_button = st.button("Delete file")
if delete_button:
    try:
        os.remove(file_loc)
        st.success(f'File output.txt has been deleted')
    except FileNotFoundError:
        st.error("File not found")



