import requests
import string

url_base = "https://lit-lessons-cdn.duolingo.com/printables/duolingo_abc_{}_printable.pdf"

save_path = "C:/Users/adeli/Downloads/duo_printables"

## Realised after writing the script, you can
# justr download the whole thing from the duolingo website
for letter in string.ascii_lowercase:
    url = url_base.format(letter)
    r = requests.get(url)

    if r.status_code != 200:
        print(f"Error geting letter {letter}: Status Code {r.status_code}")
        break
    else:
        print(f"Got letter {letter} successfully.")
        with open(f"{save_path}/duolingo_abc_{letter}.pdf", "wb") as f:
            f.write(r.content) 
        print(f"Saved {letter} to disk.")