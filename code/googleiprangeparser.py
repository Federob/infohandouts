import requests
import argparse

def scarica_json(url):
    """
    Scarica e restituisce il contenuto JSON dall'URL specificato.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Genera un'eccezione se la richiesta non ha successo
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

def scrivi_file(ip_ranges, nome_file):
    """
    Scrive i range IP in un file di testo, uno per riga.
    Se il file non esiste, lo crea; altrimenti lo sovrascrive.
    """
    try:
        with open(nome_file, "w") as file:
            for ip_range in ip_ranges:
                file.write(ip_range + "\n")
        print(f"File '{nome_file}' scritto correttamente.")
    except IOError as e:
        print("Errore durante la scrittura del file:", e)

def main():
    parser = argparse.ArgumentParser(
        description="Scarica i range IP da goog.json e li salva su file."
    )
    parser.add_argument(
        "--output",
        required=True,
        help="Percorso e nome del file di output (es. docs/ip_ranges.txt)"
    )
    args = parser.parse_args()

    url = "https://www.gstatic.com/ipranges/goog.json"
    
    # Scarica il JSON dal server
    data = scarica_json(url)
    if data is None:
        return

    # Estrai i range IP dal JSON
    ip_ranges = estrai_range_ip(data)
    
    # Scrivi i range IP sul file specificato (crea o sovrascrive)
    scrivi_file(ip_ranges, args.output)

if __name__ == "__main__":
    main()