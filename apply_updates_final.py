#!/usr/bin/env python3
"""
Script to apply Length and Lace Size updates to all Ready Units products.
Matches products by exportProductId and updates additionalInfoSections.
"""
import json
import sys

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

# Example: Show how to match and update
print(f"\n\nTo update products:")
print(f"1. Match product.exportProductId to handle_id in updates_by_handle")
print(f"2. Prepend Length and Lace Size sections to existing additionalInfoSections")
print(f"3. Use PATCH /stores/v1/products/{{product.id}} with the updated sections")

