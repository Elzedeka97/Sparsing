#!/usr/bin/env python3
"""parse module
get_info parses data/data.txt, example:
    Vadim ; Vadim97
    Denis ;Elzedeka97
"""
import requests

def get_info(filename: str, url: str="https://github.com/") -> str:
    """get name and logins from file filename
    Args:
        path to file with name and logins filename.
    Returns:
        list of dicts with "name" and "login" parsed filename
        Example:
        [
            {'name': 'Vadim', 'login': 'Vadim97'},
            {'name': 'Denis', 'login': 'Elzedeka97'}
        ]
    Raises:
        ValueError: if bad file format - no ":" in line
        RuntimeError: if no login found at github.com

    """
    res = []
    with open(filename, "r", encoding = "utf-8") as file_:
        for line in file_:
            try:
                name, login = line.split(";")
                name = name.strip()
                login = login.strip()
                res.append({
                    "name": name,
                    "login": login,
                })
                repo_url = f"{url}{login}"
                responce = requests.get(repo_url)
                if responce.status_code != 200:
                    raise RuntimeError("no such user")
            except ValueError as err:
                raise ValueError(f"Cannot parse file: {err}") from err
    return res

def main():
    """main func
    """
    filename="data/data.txt"
    return get_info(filename)

if __name__ == "__main__":
    print(main())
