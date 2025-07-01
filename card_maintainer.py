# Micheal Quentin
# 01. July 2025
# Card Maintainer

import json
import os
import time

# Variables
cards_json = os.path.join(os.path.dirname(os.path.abspath(__file__)), "OITD_cards.json")

while True:
    # Main menu
    print('0: Add Card')
    print('1: Delete Card')
    selection = input('Selection an option: ')

    with open(cards_json, 'r', encoding='utf-8') as file:
        data = json.load(file)

        if selection == '0': # Add card
            # Gather card information
            card_title = input('\nTitle: ').strip()
            card_url = input('URL: ').strip()
            card_image = input('Image: ').strip()
            card_location = [s.strip() for s in input('Location: ').split('|')]
            card_type = [s.strip() for s in input('Type: ').split('|')]
            card_identity = [s.strip() for s in input('Identity: ').split('|')]
            card_time = [s.strip() for s in input('Time: ').split('|')]
            card_vibe = [s.strip() for s in input('Vibe: ').split('|')]

            # Create the new card
            new_card = {
                "title": card_title,
                "url": card_url,
                "image": card_image,
                "location": card_location,
                "type": card_type,
                "identity": card_identity,
                "time": card_time,
                "vibe": card_vibe
            }

            # Append the new card
            data.append(new_card)

            # Save the JSON
            with open(cards_json, "w", encoding="utf-8") as file:
                json.dump(data, file, ensure_ascii=False, indent=2)
                print(card_title, 'added to cards.\n')
                time.sleep(2)