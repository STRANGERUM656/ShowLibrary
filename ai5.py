import subprocess
import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor, as_completed

def get_installed_libraries():
    """Restituisce la lista dei pacchetti installati."""
    result = subprocess.run(['pip', 'list'], stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    installed_libraries = result.stdout.decode('utf-8').split('\n')
    return [lib.split()[0] for lib in installed_libraries[2:] if lib]

def fetch_description(lib_name):
    """Recupera la descrizione della libreria da PyPI."""
    url = f"https://pypi.org/project/{lib_name}/"
    try:
        response = requests.get(url, timeout=5)
        soup = BeautifulSoup(response.text, "html.parser")
        desc_tag = soup.find('p', class_='package-description__summary')
        return lib_name, desc_tag.text.strip() if desc_tag else "Descrizione non disponibile"
    except Exception:
        return lib_name, "Errore nel recupero"

def create_library_info(max_workers=10):
    """Crea un dizionario {nome_lib: descrizione} usando richieste parallele."""
    libraries = get_installed_libraries()
    library_info = {}

    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_lib = {executor.submit(fetch_description, lib): lib for lib in libraries}
        for future in as_completed(future_to_lib):
            lib, desc = future.result()
            library_info[lib] = desc

    return library_info

if __name__ == "__main__":
    library_info = create_library_info()
    for lib, desc in sorted(library_info.items()):
        print(f"{lib}: {desc}")


