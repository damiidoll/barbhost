#!/usr/bin/env python3
"""
Script to apply updates to all Ready Units products.
This script will:
1. Load the product update data
2. Fetch all products from Wix
3. Match products by exportProductId
4. Update each product with Length and Lace Size info sections
"""
import json

# Load the update payloads
with open('product_updates.json', 'r') as f:
    update_payloads = json.load(f)

# Create a lookup dictionary by handle_id
updates_by_handle = {payload['handle_id']: payload for payload in update_payloads}

print(f"Loaded {len(update_payloads)} update payloads")
print(f"\nSample updates:")
for i in range(min(5, len(update_payloads))):
    payload = update_payloads[i]
    print(f"  {payload['handle_id']}: Length={payload['length']}, Lace Size={payload['lace_size']}")

# Example API call format for one product
example_handle = "vx_buss-down-shawty"
if example_handle in updates_by_handle:
    example_update = updates_by_handle[example_handle]
    print(f"\nExample API call for {example_handle}:")
    print(f"  URL: https://www.wixapis.com/stores/v1/products/{{product_id}}")
    print(f"  Method: PATCH")
    print(f"  Body: {json.dumps({'additionalInfoSections': example_update['additionalInfoSections']}, indent=2)}")

print(f"\n\nReady to update {len(update_payloads)} products!")
print("Note: The API updates may need to be applied manually or through a different method")
print("if the MCP tool is not applying the changes correctly.")

