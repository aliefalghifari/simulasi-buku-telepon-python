import json #import modul json untuk mengakses file json

class Database:
    def __init__(self, file):
        self.file = file

    def read(self): #fungsi untuk membaca file database.json
        with open(self.file, 'r') as f:
            data = json.load(f)
        return data

    def write(self, data): #fungsi untuk menulis data ke file database.json
        with open(self.file, 'w') as f:
            json.dump(data, f, indent=4)
    
    def add_contact(self, name, number):#fungsi untuk menambahkan kontak baru ke database.json
        data = self.read()
        data[name] = number
        self.write(data)
    
    def get_contact(self, name): #fungsi untuk mengambil kontak dari database.json
        data = self.read()
        return data.get(name, "Contact not found")
    
    def list_contacts(self): #fungsi untuk menampilkan daftar kontak dari database.json
        data = self.read()
        return list(data.keys())
