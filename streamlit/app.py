import streamlit as st
import pickle
import matplotlib.pyplot as plt


# Open the pickle file in read-binary mode
with open('model.pkl', 'rb') as f:
    # Load the model from the file
    model = pickle.load(f)

# Define custom CSS for background color and font family
custom_css = """
<style>

/* Change background image */
[data-testid="stAppViewContainer"] {
    background-image: url("https://c4.wallpaperflare.com/wallpaper/649/854/518/omega-seamaster-professional-watch-others-wallpaper-preview.jpg");
    background-size: cover;
    background-position: center center;
    background-repeat: no-repeat;
    background-attachment: local;
    }

[data-testid="stHeader"]{
    background: rgba(0,0,0,0); 
    }

[data-testid="stAppViewBlockContainer"]{
    background-color: rgba(64, 64, 64, 0.5)

    }

/* Change font family for all text elements */
body {
    font-family: 'Futura', sans-serif; /* Futura font family */
    font-size: 16px;
}

/* Change font family specifically for headings */
h1, h2, h3, h4, h5, h6 {
    font-family: 'Futura', sans-serif; /* Futura font family */
    font-size: 24px; /* Change to your desired font size */
    text-align: center; /* Center align headings */
}
</style>

/* Change text color to red */
<style>
    h1, h2 {
        color: red;
    }
</style>
"""

# Apply custom CSS
st.markdown(custom_css, unsafe_allow_html=True)

# Title (with center alignment using custom CSS)
st.markdown("<h1 style='text-align: center;'>OMEGA Proofmaster</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align: center; font-weight: normal;'>Need a sense check for your ad?</h2>", unsafe_allow_html=True)
# User input
user_input = st.text_area("Enter text here")

# Prediction
if st.button('Predict'):
    prediction = model.predict_proba([user_input])[0][0]
    prediction_pct = round((1 - prediction) * 100, 1)
    st.write(f'Text is {prediction_pct}% matching with OMEGA')

    # Create Pie Chart
    labels = ['Cartier', 'OMEGA']
    sizes = [100 - prediction_pct, prediction_pct]
    colors = ['#d6dbdf','#C50124']

    # Create the pie chart without the square box and with labels inside
    fig, ax = plt.subplots(figsize=(2,2))
    fig.set_facecolor('#00000000')
    wedges, texts, autotexts = ax.pie(
        sizes, labels=labels, colors=colors,
        autopct='%1.1f%%', startangle=90,
        wedgeprops={'edgecolor': 'none'},  # Remove the edgecolor (square box)
        textprops={'fontsize': 6, 'color': 'white'},
        explode= [0, 0.2]
    )

    # Adjust layout to fit labels inside the circle
    ax.axis('equal')
    plt.setp(autotexts, size=5, weight='bold')  # Set properties for autopct labels

    # Show the pie chart
    st.pyplot(fig)
