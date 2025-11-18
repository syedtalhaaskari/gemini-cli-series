# Cricket Scores App

A simple Flask web application that fetches and displays live cricket scores from an RSS feed.

## Features

*   Fetches live cricket scores from Cricinfo's RSS feed.
*   Displays the scores in a clean and simple web interface.

## Technologies Used

*   Python
*   Flask
*   feedparser
*   HTML
*   CSS

## Setup and Installation

1.  **Clone the repository:**
    ```bash
    git clone <repository-url>
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd cricket-scores-app
    ```
3.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    ```
4.  **Activate the virtual environment:**
    *   On Windows:
        ```bash
        venv\Scripts\activate
        ```
    *   On macOS/Linux:
        ```bash
        source venv/bin/activate
        ```
5.  **Install the dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

## Usage

1.  **Run the application:**
    ```bash
    python app.py
    ```
2.  **Open your web browser and navigate to:**
    ```
    http://127.0.0.1:5000
    ```

## Project Structure

```
cricket-scores-app/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
└── templates/
    └── index.html      # HTML template for the scoreboard
```
