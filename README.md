# Book Reading Website 📚🌙

This is a Django-based web application that allows users to create an account, log in, upload books, and read them in dark mode. 

## Features 🚀
- **User Authentication:** Sign up, log in, and log out securely.
- **Book Upload:** Users can upload books (PDFs, EPUBs, etc.).
- **Dark Mode:** Enhanced reading experience with a dark mode interface.
- **Book Viewing:** Users can read uploaded books directly in the browser.

## Installation 🛠️

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/yourusername/book-reading-website.git
   cd book-reading-website
   ```

2. **Create a Virtual Environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**  
   ```bash
   python manage.py migrate
   ```

5. **Create a Superuser (Optional for Admin Access)**  
   ```bash
   python manage.py createsuperuser
   ```

6. **Run the Development Server**  
   ```bash
   python manage.py runserver
   ```

7. **Access the Website**  
   Open your browser and visit:  
   ```
   http://127.0.0.1:8000/
   ```

## Project Structure 📂
```
book-reading-website/
│── books/               # App for managing books
│── users/               # App for user authentication
│── templates/           # HTML templates
│── static/              # CSS, JavaScript, and other static files
│── media/               # Uploaded books stored here
│── db.sqlite3           # SQLite database
│── manage.py            # Django management script
│── requirements.txt     # Dependencies
│── README.md            # Project documentation
```

## Tech Stack 🏗️
- **Backend:** Django, SQLite
- **Frontend:** HTML, CSS, JavaScript
- **Authentication:** Django Authentication System

## Future Improvements ✨
- [ ] Bookmarking feature 📌
- [ ] AI-powered book summarization 🤖
- [ ] Highlighting & annotation support ✍️

## License 📜
This project is open-source and available under the [MIT License](LICENSE).

---

Enjoy reading your books in dark mode! 🌙📖  
Contributions & suggestions are welcome! 🎉
