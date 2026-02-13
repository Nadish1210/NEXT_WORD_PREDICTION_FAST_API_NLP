# streamlit_app.py
import streamlit as st

st.set_page_config(
    page_title="Next Word Predictor by Nadish",
    page_icon="🤖",
    layout="centered"
)

st.markdown("<h1 style='text-align:center; color:#4B0082;'>Next Word Predictor 🤖</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Enter a sentence and get AI to predict the next word!</p>", unsafe_allow_html=True)
st.markdown("---")

user_input = st.text_area("Enter your text here:", placeholder="Type a sentence...", height=100)

def predict_next_word(text):
    """
    Simple dummy next-word prediction function.
    Replace this with your model's logic or ML inference.
    """
    words = text.split()
    if not words:
        return ""
    last_word = words[-1]
    # Example: just return 'example' for demonstration
    # Replace with your trained model's prediction logic
    return last_word[::-1]  # Just reversing last word as dummy prediction

if st.button("Predict Next Word"):
    if user_input.strip() == "":
        st.warning("Please enter some text!")
    else:
        try:
            predicted_word = predict_next_word(user_input)
            st.success(f"Predicted next word: **{predicted_word}**")
        except Exception as e:
            st.error(f"Error predicting next word: {e}")

st.markdown(
    "<div style='text-align:center; margin-top:50px;'><p style='color:gray;'>Assignment Demo using Streamlit (no external API)</p></div>",
    unsafe_allow_html=True
)
