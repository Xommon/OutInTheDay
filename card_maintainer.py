# Micheal Quentin
# 01. July 2025
# Card Maintainer

import json
import os
import time

# Variables
cards_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), "OITD_cards.json")

def save_custom_format(data, path):
    with open(path, "w", encoding="utf-8") as f:
        f.write("[\n")
        for idx, card in enumerate(data):
            f.write("  {\n")
            fields = []
            if "title" in card:
                fields.append(f'    "title": "{card["title"]}"')
            if "url" in card and card["url"]:
                fields.append(f'    "url": "{card["url"]}"')
            if "image" in card and card["image"]:
                fields.append(f'    "image": "{card["image"]}"')
            if "location" in card and card["location"]:
                fields.append(f'    "location": {json.dumps(card["location"], ensure_ascii=False)}')
            if "type" in card and card["type"]:
                fields.append(f'    "type": {json.dumps(card["type"], ensure_ascii=False)}')
            if "identity" in card and card["identity"]:
                fields.append(f'    "identity": {json.dumps(card["identity"], ensure_ascii=False)}')
            if "time" in card and card["time"]:
                fields.append(f'    "time": {json.dumps(card["time"], ensure_ascii=False)}')
            if "vibe" in card and card["vibe"]:
                fields.append(f'    "vibe": {json.dumps(card["vibe"], ensure_ascii=False)}')
            f.write(",\n".join(fields))
            f.write("\n  }")
            if idx < len(data) - 1:
                f.write(",\n")
            else:
                f.write("\n")
        f.write("]\n")

while True:
    # Main menu
    print('0: Add Card')
    print('1: Delete Card')
    selection = input('Select an option: ')

    with open(cards_json, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if selection == '0':  # Add card
        # Gather card information
        card_title = input('\nTitle: ').strip()
        card_url = input('URL: ').strip()
        card_image = input('Image: ').strip()
        card_location = [s.strip() for s in input('Location: ').split('|') if s.strip()]
        card_type = [s.strip() for s in input('Type: ').split('|') if s.strip()]
        card_identity = [s.strip() for s in input('Identity: ').split('|') if s.strip()]
        card_time = [s.strip() for s in input('Time: ').split('|') if s.strip()]
        card_vibe = [s.strip() for s in input('Vibe: ').split('|') if s.strip()]

        # Create the new card with only non-empty fields
        new_card = {}
        if card_title:
            new_card["title"] = card_title
        if card_url:
            new_card["url"] = card_url
        if card_image:
            new_card["image"] = card_image
        if card_location:
            new_card["location"] = card_location
        if card_type:
            new_card["type"] = card_type
        if card_identity:
            new_card["identity"] = card_identity
        if card_time:
            new_card["time"] = card_time
        if card_vibe:
            new_card["vibe"] = card_vibe

        # Append the new card
        data.append(new_card)

        # Save using custom formatting
        save_custom_format(data, cards_json)
        print(card_title, 'added to cards.\n')
        time.sleep(2)
