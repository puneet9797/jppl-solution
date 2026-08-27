import os

mapping = {
    "gst": "gst-registration",
    "msme": "msme-udyam-registration",
    "fssai": "fssai-food-license",
    "iec": "iec-import-export-code",
    "trademark": "trademark-registration",
    "iso": "iso-certification",
    "zed": "zed-green-certification",
    "gem": "gem-portal-registration",
    "bis": "bis-standards-certification",
    "trade": "trade-licence",
    "factory": "factory-licence",
    "solar": "solar-energy-service",
    "tender": "government-tender-consultancy",
    "dpr": "dpr-project-report-preparation",
    "startup": "startup-india-recognition",
    "web": "website-development-services",
    "marketing": "digital-marketing-services",
    "women": "women-entrepreneur-consultant",
    "financial": "financial-advisory-services",
    "healthcare": "healthcare-services",
    "lab": "lab-corp-services",
    "agriculture": "agriculture-business-services",
    "epr-battery": "epr-battery-registration",
    "epr-tyre": "epr-tyre-registration"
}

if not os.path.exists("services.html"):
    print("ERROR: services.html not found.")
    exit(1)

with open("services.html", "r", encoding="utf-8") as f:
    content = f.read()

for card_id, file_slug in mapping.items():
    card_start = content.find(f'id="{card_id}"')
    if card_start == -1:
        print(f"WARNING: Card ID '{card_id}' not found.")
        continue
    
    body_start = content.find('<div class="accordion-body">', card_start)
    if body_start == -1:
        print(f"WARNING: accordion-body for '{card_id}' not found.")
        continue
    
    # Parse depth to find matching closing div
    depth = 1
    pos = body_start + len('<div class="accordion-body">')
    closing_div_pos = -1
    
    while depth > 0 and pos < len(content):
        next_open = content.find('<div', pos)
        next_close = content.find('</div>', pos)
        
        if next_open != -1 and next_open < next_close:
            depth += 1
            pos = next_open + 4
        else:
            depth -= 1
            pos = next_close + 6
            if depth == 0:
                closing_div_pos = next_close
                break
                
    if depth == 0 and closing_div_pos != -1:
        btn_html = f'\n                                <div class="accordion-btn-wrapper" style="margin-top: 20px; text-align: left;">\n                                    <a href="services/{file_slug}.html" class="btn btn-primary btn-small">Read Detailed Guide & Documents <i class="fa-solid fa-arrow-up-right-from-square" style="font-size: 0.75rem; margin-left: 6px;"></i></a>\n                                </div>\n                            '
        # Only inject if the link is not already there
        if f"services/{file_slug}.html" not in content[body_start:closing_div_pos]:
            content = content[:closing_div_pos] + btn_html + content[closing_div_pos:]
            print(f"SUCCESS: Link injected for '{card_id}' -> 'services/{file_slug}.html'")
    else:
        print(f"ERROR: Could not find matching closing div for card '{card_id}'")

with open("services.html", "w", encoding="utf-8") as f:
    f.write(content)

print("SUCCESS: services.html updated with separate guide links.")
