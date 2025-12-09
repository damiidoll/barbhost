#!/usr/bin/env python3
"""
Script to update all Ready Units products with Length and Lace Size info sections.
Extracts lace size without "HD Lace" suffix (e.g., "2x6" instead of "2x6 HD Lace")
"""
import json
import re

# Load the parsed CSV data
with open('products_length_lace.json', 'r') as f:
    csv_data = json.load(f)

def extract_lace_size(lace_size_str):
    """Extract just the size part (e.g., '2x6' from '2x6 HD Lace' or '5X5 HD Lace')"""
    # Remove "HD Lace" and any extra whitespace, convert to lowercase
    cleaned = lace_size_str.replace('HD Lace', '').strip()
    # Normalize case (make lowercase for consistency)
    return cleaned.lower()

# Prepare update payloads for all products
update_payloads = []

for handle_id, product_info in csv_data.items():
    length = product_info['length']  # Already has quotes, e.g., "12\""
    lace_size_full = product_info['lace_size']  # e.g., "5X5 HD Lace" or "2x6 HD Lace"
    lace_size = extract_lace_size(lace_size_full)  # Extract just "5x5" or "2x6"
    
    # Create the two info sections
    additional_info_sections = [
        {
            "title": "Length",
            "description": length
        },
        {
            "title": "Lace Size",
            "description": lace_size
        }
    ]
    
    update_payloads.append({
        "handle_id": handle_id,
        "length": length,
        "lace_size": lace_size,
        "additionalInfoSections": additional_info_sections
    })

# Save the update payloads to a JSON file
with open('product_updates.json', 'w') as f:
    json.dump(update_payloads, f, indent=2)

print(f"Generated {len(update_payloads)} product update payloads")
print(f"\nSample update payload:")
print(json.dumps(update_payloads[0], indent=2))
print(f"\nSample lace size extraction:")
for i in range(min(5, len(update_payloads))):
    payload = update_payloads[i]
    print(f"  {payload['handle_id']}: Length={payload['length']}, Lace Size={payload['lace_size']}")

