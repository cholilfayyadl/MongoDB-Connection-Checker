# Flask MongoDB Connection Checker

This project is a simple Flask application to check the connection to a MongoDB database. It uses Bootstrap 5 for styling and displays messages about the connection status.

## Features
- Connects to a MongoDB Atlas cluster.
- Displays success or error messages regarding the database connection.
- Styled with Bootstrap 5 for a modern and responsive UI.

## Prerequisites

- Python 3.7+
- MongoDB Atlas account
- Installed Python packages (listed in `requirements.txt`)

## Project Structure
```
project/
├── app/
│   ├── __init__.py
│   ├── db_checker.py
│   ├── templates/
│   │   └── check_db.html
├── .env
├── requirements.txt
└── run.py
```

## Setup Instructions

### 1. Clone the Repository
```bash
git clone <repository-url>
cd <repository-directory>
```

### 2. Set Up a Virtual Environment
```bash
python3 -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure the `.env` File
Create a `.env` file in the root directory and add your MongoDB connection string:

```
DB_URI=mongodb+srv://<username>:<password>@<cluster-address>/?retryWrites=true&w=majority
```

Replace `<username>`, `<password>`, and `<cluster-address>` with your MongoDB Atlas credentials.

### 5. Run the Application
```bash
python run.py
```

The application will be available at `http://127.0.0.1:5000/`.

### 6. Access the Database Checker
- Navigate to `http://127.0.0.1:5000/check_db` to check the database connection status.

## Dependencies
- Flask
- pymongo
- python-dotenv
- Bootstrap 5 (via CDN)

## Example Output

- **Successful Connection:**
  ![Success Message](https://via.placeholder.com/600x200.png?text=Database+Connected+Successfully)

- **Failed Connection:**
  ![Error Message](https://via.placeholder.com/600x200.png?text=Error+Connecting+to+Database)

## Troubleshooting

### SSL Certificate Error
If you encounter an SSL certificate error:
1. Update Python certificates:
   ```bash
   /Applications/Python\ 3.x/Install\ Certificates.command
   ```
2. Use the `certifi` library to specify the CA file:
   ```bash
   pip install certifi
   ```
   Update the `DB_URI` with `tlsCAFile`:
   ```
   DB_URI=mongodb+srv://<username>:<password>@<cluster-address>/?retryWrites=true&w=majority&tlsCAFile=/path/to/certifi/cacert.pem
   ```

### Invalid Credentials
Ensure your MongoDB Atlas connection string, username, and password are correct.

## License
This project is licensed under the MIT License.
