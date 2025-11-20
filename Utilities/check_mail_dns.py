import subprocess
import sys
from rich.console import Console
from rich.table import Table

def check_spf(domain):
    spf_record = subprocess.run(['dig', '+short', 'TXT', domain], capture_output=True, text=True).stdout.strip()
    if not spf_record:
        return "No SPF record found."
    return spf_record

def check_dmarc(domain):
    dmarc_record = subprocess.run(['dig', '+short', 'TXT', f'_dmarc.{domain}'], capture_output=True, text=True).stdout.strip()
    if not dmarc_record:
        return "No DMARC record found."
    return dmarc_record

def check_dkim(domain):
    dkim_selectors = subprocess.run(['dig', '+short', 'TXT', domain], capture_output=True, text=True).stdout.strip()
    if not dkim_selectors:
        return "No DKIM selectors found."

    selectors = []
    for line in dkim_selectors.split('\n'):
        if 'v=DKIM1' in line:
            selector = line.split('p=')[1].split(';')[0]
            selectors.append(selector)

    if not selectors:
        return "No DKIM selectors found."

    dkim_records = {}
    for selector in selectors:
        dkim_record = subprocess.run(['dig', '+short', 'TXT', f'{selector}._domainkey.{domain}'], capture_output=True, text=True).stdout.strip()
        if not dkim_record:
            dkim_records[selector] = "No DKIM record found."
        else:
            dkim_records[selector] = dkim_record

    return dkim_records

def main():
    if len(sys.argv) != 2:
        print("Usage: python check_records.py <domain>")
        sys.exit(1)

    domain = sys.argv[1]

    spf_record = check_spf(domain)
    dmarc_record = check_dmarc(domain)
    dkim_records = check_dkim(domain)

    console = Console()

    table = Table(title=f"DNS Records for {domain}")
    table.add_column("Record Type", style="cyan")
    table.add_column("Record Value", style="magenta")

    table.add_row("SPF", spf_record)
    table.add_row("DMARC", dmarc_record)

    if isinstance(dkim_records, str):
        table.add_row("DKIM", dkim_records)
    else:
        for selector, record in dkim_records.items():
            table.add_row(f"DKIM ({selector})", record)

    console.print(table)

if __name__ == "__main__":
    main()