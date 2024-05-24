#!/usr/bin/env python3

def get_info(filename):
    res = []
    with open(filename, "r", encoding = "utf-8") as file_:
        try:
            for line in file_:
                name, login = line.split(";")
                name = name.strip()
                login = login.strip()
                res.append({
                    "name": name,
                    "login": login, 
                })
        except ValueError as err:
            raise "incorrect file"
    return res

def main():
    filename="data/data.txt"
    return get_info(filename)

if __name__ == "__main__":
   print(main())
