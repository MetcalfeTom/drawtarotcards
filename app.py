import os
import random
from datetime import datetime

import streamlit as st

st.set_page_config(page_title="drawtarot.cards")


def main():
    st.title("drawtarot.cards")

    # List of tarot cards with their indices
    # we get these by listing the ./cards directory
    # and extracting the index and card name from the filename.  The files are named {index} {name}.jpg
    files = os.listdir("cards")

    tarot_cards = []

    for file in files:
        split_name = file.removesuffix(".jpg").split(" ")
        tarot_cards.append((int(split_name[0]), " ".join(split_name[1:])))

    # Generate seed from current date and time
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    seed = hash(current_time) % (2**32)  # Limiting the seed to 32-bit integer range
    random.seed(seed)

    # Number of cards to display
    num_cards = random.choice([1, 2])

    selected_cards = random.sample(tarot_cards, num_cards)

    # Extracting the card names for the message
    card_names = [card[1] for card in selected_cards]

    # Message about the drawn cards
    if num_cards == 1:
        st.write(f"You drew '{card_names[0]}'.")
        # Using the provided directory structure './cards' and file naming convention
        image_path = os.path.join(
            "cards", f"{selected_cards[0][0]} {selected_cards[0][1]}.jpg"
        )
        # Display the image
        st.image(image_path, caption=card_names[0], use_column_width=True)
    else:
        st.write(f"You drew '{card_names[0]}' and '{card_names[1]}'.")
        col1, col2 = st.columns(2)
        with col1:
            image_path1 = os.path.join(
                "cards", f"{selected_cards[0][0]} {selected_cards[0][1]}.jpg"
            )
            col1.image(image_path1, caption=card_names[0], use_column_width=True)
        with col2:
            image_path2 = os.path.join(
                "cards", f"{selected_cards[1][0]} {selected_cards[1][1]}.jpg"
            )
            col2.image(image_path2, caption=card_names[1], use_column_width=True)

    st.write(
        f"Discover more with [Nébula the Tarot Cat](https://apps.apple.com/us/app/nebula-tarot-cat/id6449970544) 🐈"
    )


if __name__ == "__main__":
    main()
