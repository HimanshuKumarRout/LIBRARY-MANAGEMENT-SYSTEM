
<div align="center">
  <h1>📚 Library Management System</h1>
  <p>
    <strong>A Python-based GUI application for efficient library record management using Tkinter and MySQL.</strong>
  </p>
  <p>
    <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&amp;logo=python&amp;logoColor=white" />
    <img src="https://img.shields.io/badge/Tkinter-GUI-blue?style=for-the-badge" />
    <img src="https://img.shields.io/badge/MySQL-4479A1?style=for-the-badge&amp;logo=mysql&amp;logoColor=white" />
    <img src="https://img.shields.io/badge/Database-Connected-green?style=for-the-badge" />
  </p>
</div>

<br />

## 🌟 Overview

The **Library Management System** is a desktop-based application built with **Python (Tkinter)** and **MySQL** to simplify library operations.

It provides an intuitive graphical interface for managing **members, books, and transactions**, making it ideal for small to medium-scale libraries or academic projects.

---

## 🚀 Key Features

- 📥 **Add Records** – Insert new member and book details  
- 🔄 **Update Data** – Modify existing records  
- ❌ **Delete Records** – Remove outdated entries  
- 🔍 **Search Functionality** – Find books and members easily  
- 📋 **Display Records** – View complete database entries  
- 📅 **Auto Date Management** – Borrow & due dates generation  
- 💰 **Fine Calculation** – Late return penalty system  
- 🧾 **Table View** – Organized data display  
- 🔄 **Reset & Exit** – Clear form or close app instantly  

---

## 🛠️ Tech Stack

- **Python 3.x**
- **Tkinter** (GUI Framework)
- **MySQL** (Database)
- **mysql-connector-python**

---

## 📁 Project Structure

```text
library-management-system/
├── library.py        # Main application (Tkinter GUI)
├── database.sql      # Database schema (optional)
└── README.md         # Documentation
````

---

## 🗄️ Database Setup

Create the database:

```sql
CREATE DATABASE library_management_system;
```

### 📘 Books Table

```sql
CREATE TABLE books (
    BookID INT PRIMARY KEY,
    BookTitle VARCHAR(255),
    Author VARCHAR(255),
    Price INT
);
```

### 📗 Library Table

```sql
CREATE TABLE library (
    Member VARCHAR(50),
    PRN_NO VARCHAR(50) PRIMARY KEY,
    ID VARCHAR(50),
    FirstName VARCHAR(100),
    LastName VARCHAR(100),
    Address1 VARCHAR(200),
    Address2 VARCHAR(200),
    Postcode VARCHAR(20),
    Mobile VARCHAR(20),
    BookID VARCHAR(50),
    BookTitle VARCHAR(200),
    Author VARCHAR(200),
    DateBorrowed VARCHAR(50),
    DateDue VARCHAR(50),
    DaysOnBook VARCHAR(20),
    LateReturnFine VARCHAR(20),
    DateOverDue VARCHAR(20),
    ActualPrice VARCHAR(20)
);
```

---

## ⚙️ Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/HimanshuKumarRout/library-management-system.git
cd library-management-system
```

### 2️⃣ Install Dependencies

```bash
pip install mysql-connector-python
```

### 3️⃣ Configure Database

Update credentials in your Python file:

```python
host = "localhost"
user = "root"
password = "yourpassword"
database = "library_management_system"
```

### 4️⃣ Run the Application

```bash
python library.py
```

---

## 🖥️ Application Interface

The application includes:

* 📌 Member Information Panel
* 📚 Book Selection Section
* 📊 Data Display Panel
* 🎛️ CRUD Operation Buttons
* 📋 Database Record Table

---

## 📌 Functional Modules

| Module    | Description                   |
| --------- | ----------------------------- |
| Add Data  | Insert new member/book record |
| Update    | Modify existing data          |
| Delete    | Remove records                |
| Show Data | Display selected details      |
| Reset     | Clear all fields              |
| Exit      | Close the application         |

---

## 🔮 Future Enhancements

* 🔐 Login Authentication System
* 🔄 Book Return Management
* 📊 Advanced Search & Filters
* 📷 Barcode Scanner Integration
* 📤 Export to Excel/PDF
* 🌐 Web Version (Django / Flask)

---

## 👨‍💻 Author

**Himanshu Kumar Rout**

* GitHub: [https://github.com/himanshukumarrout](https://github.com/himanshukumarrout)
* LinkedIn: [https://www.linkedin.com/in/himanshurout](https://www.linkedin.com/in/himanshurout)

---

## ⭐ Support

If you like this project, please **star ⭐ the repository** and share it!

---

<p align="center">Built with ❤️ using Python & MySQL</p>
