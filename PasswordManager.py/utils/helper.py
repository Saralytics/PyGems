import json


class Helper:
    def __init__(self, tkinter_entry, data_path):
        self.entry_text_field = tkinter_entry
        self.data_path = data_path

    def search(self):
        # input:
        search_term = self.entry_text_field.get()

        # load the data to search : err handling: what if file doesn't exist
        try:
            with open(self.data_path, "r") as file:
                data = json.load(file)
        except FileNotFoundError:
            raise FileNotFoundError
        else:
            # find the value corresponding to the key (search term)
            if search_term in data:
                email = data[search_term]['email']
                pwd = data[search_term]['password']
                return search_term, email, pwd
            else:
                return None

    def save(self, entry):
        try:
            with open(self.data_path, "r") as file:
                data = json.load(file)
                data.update(entry)
            with open(self.data_path, "w") as file:
                json.dump(data, file, indent=4)

        except FileNotFoundError:
            with open(self.data_path, "w") as file:
                json.dump(entry, file, indent=4)