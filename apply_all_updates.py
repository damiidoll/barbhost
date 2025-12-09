#!/usr/bin/env python3
"""
Match products and update them with Length and Lace Size.
"""
import json
import re

# Load update data
with open('product_updates.json', 'r') as f:
    updates = json.load(f)

# Load products from CSV mapping
with open('products_length_lace.json', 'r') as f:
    csv_data = json.load(f)

# Create mapping: product name -> update data
# Product names in Wix are like "Glo ✦ 16\" 5x5 HD Lace"
# We need to extract the base name "Glo" and match it

name_to_update = {}
for handle_id, data in csv_data.items():
    # Extract base name from product name like "Amber ✦ 12\" 5X5 HD Lace"
    name = data['name']
    # Extract the part before "✦"
    base_name = name.split('✦')[0].strip().lower()
    name_to_update[base_name] = {
        'handle_id': handle_id,
        'length': data['length'],
        'lace_size': data['lace_size'].replace(' HD Lace', '').lower()
    }

print(f"Created mapping for {len(name_to_update)} products")
print(f"\nSample mappings:")
for i, (name, data) in enumerate(list(name_to_update.items())[:5]):
    print(f"  '{name}' -> Length: {data['length']}, Lace Size: {data['lace_size']}")

# Save the mapping for use in API calls
with open('product_name_mapping.json', 'w') as f:
    json.dump(name_to_update, f, indent=2)

print(f"\nSaved mapping to product_name_mapping.json")

