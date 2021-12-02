import random
import json


class generator:
    def __init__(self):
        self.first_name_list = []
        self.last_name_list = []
        self.address_list = []
        self.preprocess()

    def preprocess(self):
        self.load_names()
        self.load_address()

    def load_names(self):
        with open("names.txt", 'r') as f:
            res = json.load(f)
            self.first_name_list = res['fn']
            self.last_name_list = res['ln']

    def load_address(self):
        with open('data.json', 'r') as f:
            addr_data = json.load(f)
        for i in range(0, 500):
            num = random.randint(1, 9999)
            rd_name = addr_data['r'][random.randint(0, len(addr_data['r']) - 1)]
            suffix = addr_data['e'][random.randint(0, len(addr_data['e']) - 1)]
            zip_code_t = addr_data['z'][random.randint(0, len(addr_data['z']) - 1)]
            zip_code = f"{zip_code_t['detail']} {zip_code_t['name']}"
            res = f"{num} {rd_name}{suffix}, {zip_code}"
            self.address_list.append(res)

    def fetch_one(self):
        fni = random.randint(0, len(self.first_name_list) - 1)
        lni = random.randint(0, len(self.last_name_list) - 1)
        adi = random.randint(0, len(self.address_list) - 1)
        fn = self.first_name_list[fni]
        ln = self.last_name_list[lni]
        adr = self.address_list[adi]
        while fn == ln:
            fni = random.randint(0, len(self.first_name_list) - 1)
            fn = self.first_name_list[fni]
        return fn, ln, self.generate_dob(), adr, random.randint(0, 7)

    @staticmethod
    def generate_dob():
        y = random.randint(1940, 2005)
        m = random.randint(1, 12)
        if m == 2:
            d = random.randint(1, 28)
        elif m in [1, 3, 5, 7, 8, 10, 12]:
            d = random.randint(1, 31)
        else:
            d = random.randint(1, 30)

        return f"{y}-{str(m).zfill(2)}-{str(d).zfill(2)}"
