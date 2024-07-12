# Local Multimodal AI Chat: waterbits-chatbot

In this repo, i will build a chatbot in Dialogflow for WaterBits.
It will be an end-to-end project covering Dialogflow basics, building a backend in python and Fastapi, interactions with MySQL database, and much more.
I include Dialogflow fundamentals such as intents, entities, contexts, etc in this project. 

# Getting Started
To get
Got it! Here's an improved version of the "Getting Started" section for the repository using Poetry:

---

# Getting Started
To get started with the Local Multimodal AI Chat for WaterBits, follow these steps:
### 1. Clone the repository: I am using Python 3.12 currently
Clone the repository to your local machine:
```bash
git clone <water-bits>
cd waterbits
```

### 2. Install Poetry ( i am using poetry instead of pip)

Make sure you have Poetry installed. If not, you can install it via pip or pipx:
```bash
pip install poetry
```

### 3. Install dependencies
Use Poetry to install the project dependencies and set up the virtual environment:

```bash
poetry install
```

This command installs all necessary dependencies specified in `pyproject.toml`.

### 4. Activate the virtual environment
```bash
poetry shell
```

Activating the virtual environment ensures that all subsequent commands run within the project's isolated environment.

## Usage

Once you've set up the environment, you can start the Local Multimodal AI Chat application:

```bash
poetry run python app.py
```

Replace `app.py` with the actual entry point of your application if different.

