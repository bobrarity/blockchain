# Blockchain API with Flask

🔗 A simple blockchain implementation in Python, with a Flask API for interacting with the blockchain.

## 📜 Overview

This project demonstrates a basic blockchain system where:
- Transactions can be added.
- Blocks can be mined.
- The full blockchain can be retrieved.
- Nodes can be registered.
- Conflicts between chains can be resolved using a consensus algorithm.

## 🚀 Features

- **Blockchain Implementation**: The core blockchain logic is implemented in Python.
- **Proof of Work**: A simple Proof of Work algorithm to secure the blockchain.
- **Consensus Algorithm**: Ensures all nodes in the network agree on a single version of the blockchain.
- **REST API**: Interact with the blockchain using HTTP requests.

## 📂 Project Structure

```
.
├── .gitignore              # Ignore the unnecessary files
├── app.py                  # Flask API for interacting with the blockchain
├── blockchain.py           # Core blockchain implementation
├── requirements.txt        # Python dependencies
└── README.md               # Project documentation
```

### Files Explained

- **`blockchain.py`**: Contains the `Blockchain`, `Block`, and `Transaction` classes which handle the core blockchain logic.
- **`app.py`**: A Flask application that provides an API to interact with the blockchain.
- **`requirements.txt`**: Lists the Python libraries needed to run the project.

## ⚙️ Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/bobrarity/blockchain.git
   cd blockchain
   ```

2. **Create a Virtual Environment** (optional but recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Flask Application**:
   ```bash
   python app.py
   ```

5. **Access the API**:
   - Visit `http://127.0.0.1:5000/` in your web browser or use tools like `curl` or Postman to interact with the API.

## 📬 API Endpoints

### 1. Mine a New Block
   - **URL**: `/mine`
   - **Method**: `GET`
   - **Description**: Mines a new block and adds it to the blockchain.

### 2. Create a New Transaction
   - **URL**: `/transactions/new`
   - **Method**: `POST`
   - **Description**: Adds a new transaction to be included in the next mined block.
   - **Body**: JSON containing `sender`, `receiver`, and `amount`.

### 3. View the Full Blockchain
   - **URL**: `/chain`
   - **Method**: `GET`
   - **Description**: Retrieves the entire blockchain.

### 4. Register New Nodes
   - **URL**: `/nodes/register`
   - **Method**: `POST`
   - **Description**: Registers new nodes to the blockchain network.
   - **Body**: JSON containing a list of node URLs.

### 5. Consensus Algorithm
   - **URL**: `/nodes/resolve`
   - **Method**: `GET`
   - **Description**: Resolves conflicts between different chains to ensure consensus.

## 🧩 How It Works

### Proof of Work
The Proof of Work algorithm ensures that blocks can only be added to the blockchain after a valid proof has been found, requiring significant computational effort.

### Consensus Algorithm
The consensus mechanism ensures all nodes in the network agree on a single version of the blockchain, replacing shorter chains with the longest valid chain.

## 🛠️ Built With

- [Python](https://www.python.org/) - Core language for blockchain logic.
- [Flask](https://flask.palletsprojects.com/) - Micro web framework for building the API.

