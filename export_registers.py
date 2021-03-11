import json
import requests
from pathlib import Path

registers = requests.get('https://register.register.gov.uk/records.json')
json = registers.json()
beta_registers=list(json.keys())
FORMATS = ['json', 'csv', 'rsf']

for register in beta_registers:
    Path(register).mkdir(parents=True, exist_ok=True)
    for format in FORMATS:
        if format == 'rsf':
            url = f'https://{register}.register.gov.uk/download-rsf'
        else:
            url = f'https://{register}.register.gov.uk/records.{format}?page-size=5000'
        r = requests.get(url)
        r.encoding='UTF-8'
        with open(f"{register}/records.{format}", "w", encoding='utf-8') as f:
            f.write(r.text)