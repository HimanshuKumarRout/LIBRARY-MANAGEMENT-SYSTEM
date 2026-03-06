

# 📚 Library Management System (Python + Tkinter + MySQL)

A **Library Management System** built using **Python**, **Tkinter GUI**, and **MySQL Database**. This application allows library administrators to manage members, issue books, update records, and maintain a digital library database through a graphical interface.

---

## 🚀 Features

* Add new library member records
* Update member and book information
* Delete existing member records
* Display member details
* Fetch book titles directly from MySQL database
* Auto-generate borrowed date and due date
* Late return fine calculation
* Search and display book details
* Table view of all library records
* Reset form and exit system functionality

---

## 🛠️ Technologies Used

* **Python**
* **Tkinter** (GUI)
* **MySQL**
* **mysql-connector-python**

---

## 📂 Project Structure

```
library-management-system/
│
├── library.py        # Main Python GUI application
├── README.md         # Project documentation
└── database.sql      # MySQL database structure (optional)
```

---

## 🗄️ Database Setup

Create a MySQL database named:

```sql
library_management_system
```

### Example Tables

**Books Table**

```sql
CREATE TABLE books (
    BookID INT PRIMARY KEY,
    BookTitle VARCHAR(255),
    Author VARCHAR(255),
    Price INT
);
```

**Library Table**

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
git clone https://github.com/yourusername/library-management-system.git
```

### 2️⃣ Install Dependencies

```bash
pip install mysql-connector-python
```

### 3️⃣ Configure MySQL

Update the database credentials inside the code if needed:

```python
host="localhost"
username="root"
password="yourpassword"
database="library_management_system"
```

### 4️⃣ Run the Application

```bash
python library.py
```

---

## 🖥️ Application Interface

The system includes:

* **Member Information Panel**
* **Book Selection List**
* **Data Display Panel**
* **CRUD Operation Buttons**
* **Database Record Table**

---

## 📌 Functional Modules

| Function  | Description                      |
| --------- | -------------------------------- |
| Add Data  | Add a new member and book record |
| Update    | Modify existing member data      |
| Delete    | Remove a member record           |
| Show Data | Display selected member details  |
| Reset     | Clear all fields                 |
| Exit      | Close the application            |

---

## 🔮 Future Improvements

* Login authentication system
* Book return management
* Fine calculation automation
* Search functionality
* Barcode scanner integration
* Export records to Excel/PDF
* Web-based version using Django or Flask

---

## 👨‍💻 Author

**Himanshu Kumar Rout**

* GitHub: [https://github.com/himanshukumarrout](https://github.com/himanshukumarrout)
* LinkedIn: [https://linkedin.com/himanshukumarrout](www.linkedin.com/in/himanshurout)


---

## ⭐ Support

If you like this project, please **star ⭐ the repository** and share it.

---

✅ If you want, I can also give you a **more professional GitHub README with badges, screenshots, and better formatting** (which looks much better on GitHub).
