import subprocess
import requests
from bs4 import BeautifulSoup

def get_installed_libraries():
    result = subprocess.run(['pip', 'list'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    installed_libraries = result.stdout.decode('utf-8').split('\n')
    return [lib.split()[0] for lib in installed_libraries[2:] if lib]

def search_library_online(library_name):
    url = f"https://pypi.org/pypi/{library_name}/json"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("info", {}).get("summary", "No description available.")
    else:
        return "Description not found."

def create_library_info():
    libraries = get_installed_libraries()
    library_info = {}
    for lib in libraries:
        description = search_library_online(lib)
        library_info[lib] = description
    return library_info

if __name__ == "__main__":
    library_info = create_library_info()
    for lib, desc in library_info.items():
        print(f"{lib}: {desc}")



