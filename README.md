Here’s a polished **GitHub-style `README.md`** with badges, sections, and a more professional open-source feel:

---

# 🤖 Local ChatGPT Clone

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Streamlit](https://img.shields.io/badge/Streamlit-App-red.svg)
![Ollama](https://img.shields.io/badge/Ollama-LLM-black.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)

A ChatGPT-like web application that runs **locally** using **Streamlit** and **Ollama**.
It supports multiple conversations, real-time streaming responses, and persistent chat history — all without relying on external APIs.

---

## ✨ Features

* 💬 Multi-chat conversation system
* 🧠 Local LLM execution (via Ollama)
* ⚡ Streaming responses (real-time typing effect)
* 🗂 Persistent storage using JSON
* ➕ Create new chats
* 🗑 Delete conversations
* 🎛 Adjustable model & temperature
* 🧾 Clean Streamlit chat interface

---


## 🛠 Tech Stack

| Layer      | Technology |
| ---------- | ---------- |
| Frontend   | Streamlit  |
| Backend    | Python     |
| LLM Engine | Ollama     |
| Storage    | JSON       |

---

## ⚙️ Installation

### 1️⃣ Clone Repository

```bash
git clone https://github.com/your-username/local-chatgpt-clone.git
cd local-chatgpt-clone
```

---

### 2️⃣ Setup Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate       # Windows
source venv/bin/activate    # Mac/Linux
```

---

### 3️⃣ Install Dependencies

```bash
pip install streamlit ollama
```

---

### 4️⃣ Setup Ollama

Install Ollama:
👉 [https://ollama.com](https://ollama.com)

Pull required models:

```bash
ollama pull llama3.2:3b
ollama pull llama3.2:1b
ollama pull phi3
ollama pull mistral
```

---

## ▶️ Run the App

```bash
streamlit run app.py
```

---

## 📂 Project Structure

```bash
.
├── app.py          # Main application
├── chats.json      # Chat storage
└── README.md
```

---

## 🧠 How It Works

* Each chat is assigned a unique `chat_id`
* Messages are stored in `chats.json`
* Ollama handles local LLM responses
* Streaming API provides real-time output
* Sidebar manages chat threads

---

## 🎛 Configuration

| Setting     | Description                                           |
| ----------- | ----------------------------------------------------- |
| Model       | Select LLM (llama, mistral, phi3)                     |
| Temperature | Controls randomness (0 → deterministic, 1 → creative) |

---

## 🚀 Future Improvements

* 🔍 Chat search
* 🏷 Rename chats
* 📤 Export chats (PDF / TXT)
* 🎤 Voice assistant
* 🌐 Deploy with API fallback
* 🧠 Long-term memory support

---

## ⚠️ Important Notes

* Ollama must be running locally
* Large models require sufficient RAM
* `chats.json` grows over time



## 👨‍💻 Author

**Muhammad Adeel**
