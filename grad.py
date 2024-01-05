import streamlit as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt

# Fonction pour générer le nuage de mots
def generate_wordcloud(text):
    wordcloud = WordCloud(width=800, height=400, random_state=21, max_font_size=110, background_color='white').generate(text)
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.imshow(wordcloud, interpolation="bilinear")
    ax.axis('off')
    st.pyplot(fig)

# Interface utilisateur avec Streamlit
def main():
    st.title("Nuage de mots avec Streamlit")

    # Zone de texte pour saisir le texte
    text_input = st.text_area("Entrez votre texte ici:", "Saisissez votre texte...")

    # Bouton pour générer le nuage de mots
    if st.button("Générer le nuage de mots"):
        generate_wordcloud(text_input)

# Exécuter l'application Streamlit
if __name__ == "__main__":
    main()
