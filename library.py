import streamlit as st
import json

st.set_page_config(page_title="Unit Converter App", page_icon="🔄", layout="centered")

LIBRARY_FILE = "library.json"

# Load and Save Functions
def load_library():
    try:
        with open(LIBRARY_FILE, "r") as file:
            return json.load(file)
    except:
        return []

def save_library():
    with open(LIBRARY_FILE, "w") as file:
        json.dump(library, file, indent=4)

# Initialize library
library = load_library()

st.title("📚 Personal Library Manager")

st.header("Add a New Book")
title:str = st.text_input("Title")
author:str = st.text_input("Author")
year:int = st.number_input("Publication Year", min_value=0, max_value=2025, step=1)
genre:str = st.text_input("Genre")
read_status:bool = st.checkbox("Read")

if st.button("Add Book") and title and author and genre:
    library.append({"title": title, "author": author, "year": int(year), "genre": genre, "read": read_status})
    save_library()
    st.success(f'"{title}" added!')

# Remove a Book
book_titles = [book["title"] for book in library]
book_to_remove = st.selectbox("Remove a book", book_titles)
if st.button("Remove") and book_to_remove:
    library = [book for book in library if book["title"] != book_to_remove]
    save_library()
    st.success(f'"{book_to_remove}" removed!')

# Search for a Book
search_query = st.text_input("Search by Title or Author")
if search_query:
    results = [book for book in library if search_query.lower() in book["title"].lower() or search_query.lower() in book["author"].lower()]
    for book in results:
        st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
    if not results:
        st.warning("No matches found.")

# Display All Books
st.header("📖 Your Library")
for book in library:
    st.write(f"**{book['title']}** by {book['author']} ({book['year']}) - {book['genre']} - {'Read' if book['read'] else 'Unread'}")
if not library:
    st.write("Your library is empty.")

# Statistics
total_books = len(library)
read_books = sum(1 for book in library if book["read"])
st.write(f"📊 **Total Books:** {total_books}")
st.write(f"📖 **Books Read:** {read_books} ({(read_books/total_books*100) if total_books else 0:.2f}%)")
