import requests
import argparse
from datetime import datetime

def scarica_json(url):
    """
    Scarica e restituisce il contenuto JSON dall'URL specificato.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print("Errore durante il download del file JSON:", e)
        return None

def estrai_range_ip(data):
    """
    Estrae i range IP dal dizionario JSON.
    Cerca sia la chiave 'ipv4Prefix' che 'ipv6Prefix' all'interno della lista 'prefixes'.
    """
    ip_ranges = []
    for prefix in data.get("prefixes", []):
        if "ipv4Prefix" in prefix:
            ip_ranges.append(prefix["ipv4Prefix"])
        elif "ipv6Prefix" in prefix:
            ip_ranges.append(prefix["ipv6Prefix"])
    return ip_ranges

def scrivi_file(ip_ranges, nome_file, source_url):
    """
    Scrive i range IP in un file di testo, uno per riga.
    Aggiunge come prima riga un commento con l'URL sorgente e la data/ora di parsing.
    Se il file non esiste, lo crea; altrimenti lo sovrascrive.
    """
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(nome_file, "w") as file:
            # Riga di commento con sorgente e timestamp
            file.write(f"# Source: {source_url} parsed at {timestamp}\n")
            # Scrittura dei range IP
            for ip_range in ip_ranges:
                file.write(ip_range + "\n")
        print(f"File '{nome_file}' scritto correttamente.")
    except IOError as e:
        print("Errore durante la scrittura del file:", e)

def main():
    parser = argparse.ArgumentParser(
        description="Scarica i range IP da goog.json e li salva su file, "
                    "inserendo commento con sorgente e data/ora."
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Percorso e nome del file di output (es. docs/ip_ranges.txt)"
    )
    args = parser.parse_args()

    source_url = "https://www.gstatic.com/ipranges/goog.json"
    
    # Scarica il JSON dal server
    data = scarica_json(source_url)
    if data is None:
        return

    # Estrai i range IP dal JSON
    ip_ranges = estrai_range_ip(data)
    
    # Scrivi i range IP su file (crea o sovrascrive, con header di commento)
    scrivi_file(ip_ranges, args.output, source_url)

if __name__ == "__main__":
    main()
