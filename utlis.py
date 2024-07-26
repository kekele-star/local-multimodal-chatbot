import json

def save_chat_history(chat_history, file_path):
    with open(file_path, "w") as f:
        json_data = [message.dict() for message in chat_history.messages]
        json_data = []
        for message in chat_history.messages:
            json_data.append(message(dict()))

        json.dump(json_data, f)