import streamlit as st
import ollama
import json
import uuid
from pathlib import Path

st.set_page_config(page_title="Local ChatGPT Clone", page_icon="🤖", layout="wide")

DATA_FILE = Path("chats.json")


def load_chats():
    if DATA_FILE.exists():
        return json.loads(DATA_FILE.read_text())
    return {}

def save_chats(chats):
    DATA_FILE.write_text(json.dumps(chats, indent=2))


chats = load_chats()

if "chat_id" not in st.session_state:

    if chats:
        st.session_state.chat_id = list(chats.keys())[0]

    else:
        new_chat = str(uuid.uuid4())
        chats[new_chat] = []
        save_chats(chats)
        st.session_state.chat_id = new_chat


st.sidebar.title("💬 Conversations")

if st.sidebar.button("➕ New Chat"):

    new_chat = str(uuid.uuid4())
    chats[new_chat] = []

    save_chats(chats)

    st.session_state.chat_id = new_chat
    st.rerun()


# Display existing chats
for cid in chats.keys():

    messages = chats[cid]

    if messages:
        title = messages[0]["content"][:30]
    else:
        title = "New Chat"

    if st.sidebar.button(title, key=cid):
        st.session_state.chat_id = cid
        st.rerun()


# Delete chat
st.sidebar.divider()

if st.sidebar.button("🗑 Delete Current Chat"):

    chats.pop(st.session_state.chat_id)

    if chats:
        st.session_state.chat_id = list(chats.keys())[0]
    else:
        new_chat = str(uuid.uuid4())
        chats[new_chat] = []
        st.session_state.chat_id = new_chat

    save_chats(chats)
    st.rerun()


st.sidebar.divider()

model = st.sidebar.selectbox(
    "Model",
    ["llama3.2:3b", "llama3.2:1b", "phi3", "mistral"]
)

temperature = st.sidebar.slider(
    "Temperature",
    0.0,
    1.0,
    0.7
)


current_chat = chats.get(st.session_state.chat_id, [])


st.title("🤖 Local ChatGPT Clone")

for msg in current_chat:

    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])


prompt = st.chat_input("Send a message")

if prompt:

    current_chat.append({
        "role": "user",
        "content": prompt
    })

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):

        placeholder = st.empty()
        full_response = ""

        try:

            stream = ollama.chat(
                model=model,
                messages=current_chat,
                stream=True,
                options={"temperature": temperature}
            )

            for chunk in stream:

                content = chunk["message"]["content"]

                full_response += content

                placeholder.markdown(full_response + "▌")

            placeholder.markdown(full_response)

        except Exception as e:

            full_response = f"Error: {e}"
            placeholder.error(full_response)

    current_chat.append({
        "role": "assistant",
        "content": full_response
    })

    chats[st.session_state.chat_id] = current_chat

    save_chats(chats)