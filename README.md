## Python--Medical-data-extraction-Backend-Project - Etracting pdf to string - fetching FastAPI using Postman

This project is an extraction system to convert pdf medical file to personal text informations and using FastAPI backend server.


## Project Structure

- **backend/**: Contains the FastAPI backend server code, source code
- **tests/**: Contains the test cases for backend by Pytest.
- **requirements.txt**: Lists the required Python packages.
- **README.md**: Provides an overview and instructions for the project.


## Setup Instructions

1. **Clone the repository**:
   ```bash
   git clone https://github.com/tommydoan/Python--Medical-data-extraction-Backend-Project.git
   cd Python--Medical-data-extraction-Backend-Project
   ```
1. **Install dependencies:**:   
   ```commandline
    pip install -r requirements.txt
   ```
1. **Run the FastAPI server:**:   
   ```commandline
    uvicorn Backend/rsc/main:app --reload
   ```
1. **Run the Streamlit app:**:   
   ```commandline
    streamlit run src/main.py
   ```
