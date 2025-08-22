import streamlit as st
import pandas as pd
import numpy as np
import pickle
import time

# Load the model and data with error handling
try:
    model = pickle.load(open('gamerecfinal.pkl', 'rb'))
    df = pd.read_csv("preprocessed_games3000.csv")
except Exception as e:
    st.error(f"Error loading model or dataset: {e}")
    st.stop()
with open("ui.html", "r") as f:
    html = f.read()
st.markdown(html, unsafe_allow_html=True)

# Function to get game details
def get_game_details(game_index):
    try:
        game_data = df.loc[df['title-1'] == game_index].iloc[0]
        return game_data['title'], game_data['description'], game_data['price_final']
    except IndexError:
        return "Game not found", "", 0

# Main function for the app
def main():

    top_30_tags_list = ['Indie', 'Singleplayer', 'Action', 'Adventure', 'Casual',
                        '2D', 'Simulation', 'Strategy', 'Atmospheric', 'RPG',
                        'Puzzle', 'Story Rich', 'Multiplayer', '3D', 'Pixel Graphics',
                        'Exploration', 'Colorful', 'Cute', 'First-Person', 'Early Access',
                        'Fantasy', 'Funny', 'Free to Play', 'Horror', 'Anime',
                        'Arcade', 'Shooter', 'Retro', 'Female Protagonist', 'Family Friendly']

    st.title("hello there!")

    if 'user_input' not in st.session_state:
        st.session_state['user_input'] = {tag: False for tag in top_30_tags_list}
    st.markdown("""
<style>
/* Fix background for streamlit's root */
.stApp {
    background: linear-gradient(135deg, #ff9bcc, #91c3f1);
    background-attachment: fixed;
    background-size: cover;
    font-family: 'Comic Sans MS', cursive;
    color: #fff2e8;
}

/* Style the buttons to be glow-up queens */
div.stButton > button {
    background-color: #ff80b3;
    color: white;
    border: 2px dotted #ffe0f0;
    border-radius: 12px;
    box-shadow: 0 4px 12px rgba(255, 0, 128, 0.6);
    padding: 10px 20px;
    margin: 8px 4px;
    font-size: 14px;
    font-weight: bold;
    text-shadow: 1px 1px 2px #d63f8d;
    transition: all 0.3s ease-in-out;
}

div.stButton > button:hover {
    background-color: #ff4da6;
    transform: scale(1.07);
    box-shadow: 0 0 18px rgba(255, 0, 128, 0.9);
    cursor: pointer;
}

/* Make all markdown text black for readability */
h1, h2, h3, p, div, span, label {
    color: #fff2e8 !important;
}
</style>
""", unsafe_allow_html=True)



    st.subheader("Choose da tags, leave the rest for AI:")

    # Display the tag buttons in 5 columns
    cols = st.columns(5)
    for i, tag in enumerate(top_30_tags_list):
        with cols[i % 5]:
           if st.button(tag, key=tag):
              st.session_state['user_input'][tag] = not st.session_state['user_input'][tag]


    # Here's the BIG MAIN PREDICT BUTTON inside the Game Picker 3000 box
    if st.button("Predict Game", key="main_predict"):
        input_data = [int(st.session_state['user_input'][tag]) for tag in top_30_tags_list]
        input_df = pd.DataFrame([input_data], columns=top_30_tags_list)

        prediction = model.predict(input_df)[0]
        game_name, description, price = get_game_details(prediction)

        typing_text = f" Predicted Game: {game_name}"
        typed_output = st.empty()
        for i in range(len(typing_text) + 1):
            typed_output.text(typing_text[:i])
            time.sleep(0.05)

        if game_name != "Game not found":
            st.success(f"{game_name}\n\n {description}\n\n Price: ${price:.2f}")
        else:
            st.error(" No matching game found. Try different tags!")

    # Reset Button
    if st.button(" Reset"):
        st.session_state['user_input'] = {tag: False for tag in top_30_tags_list}
        st.success("Selections reset. Start fresh!")

    # Show current selected tags
    st.markdown("### 🔍 Current Selections:")
    st.write(", ".join([tag for tag, selected in st.session_state['user_input'].items() if selected]) or "None")


if __name__ == "__main__":
    main()
