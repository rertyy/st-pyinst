# app.py
import os

import streamlit as st


def main():

    st.title("My Streamlit App")
    st.write("Hello, Streamlit!")
    st.write("# Read 1")
    try:
        with open("./test.txt", "r") as f:
            st.write(f.read())
    except FileNotFoundError:
        st.write("File not found")
    st.write("# Write 1")
    with open("./test.txt", "w") as f:
        f.write("hello world")
    st.write("# Read 2")
    with open("./test.txt", "r") as f:
        st.write(f.read())
    st.write("# delete and read")
    os.remove("./test.txt")
    try:
        with open("./test.txt", "r") as f:
            st.write(f.read())
    except FileNotFoundError:
        st.write("File not found")


if __name__ == "__main__":
    main()