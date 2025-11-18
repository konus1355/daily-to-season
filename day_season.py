import streamlit as st

# Page config
st.set_page_config(
    page_title="Season-long to Max Daily Catch Converter",
    page_icon="🦋",
    layout="centered"
)

st.title("Season-long to Max Daily Catch Converter")

st.write(
    "Convert season-long catch into an estimated range of maximum daily catch "
    "using the relationship from Onufrieva & Onufriev (2018)."
)

# Inputs
season_long = st.number_input(
    "Season-long catch",
    min_value=0.0,
    step=1.0,
    format="%.0f"
)

flight_weeks = st.number_input(
    "Flight duration (weeks)",
    min_value=0.0,
    step=1.0,
    format="%.1f"
)

# Calculate button
if st.button("Calculate"):
    if flight_weeks <= 0:
        st.error("Flight duration must be greater than 0 weeks.")
    elif season_long < 0:
        st.error("Season-long catch cannot be negative.")
    else:
        # Original formulas:
        # answer1 = a / (2.87 * x)
        # answer2 = a / (0.96 * x)
        a = season_long
        x = flight_weeks

        answer1 = a / (2.87 * x)
        answer2 = a / (0.96 * x)

        finalans1 = round(answer1, 2)
        finalans2 = round(answer2, 2)

        st.success(
            f"Estimated max daily catch range: **{finalans1} – {finalans2}** moths/trap/day"
        )

# About section
with st.expander("About this tool"):
    st.markdown(
        """
        **Programmed originally by:** Andrei Onufriev  
        **Adapted for web deployment by:** Ksenia & ChatGPT 🥒  

        Based on:

        Onufrieva, K. S. & A. V. Onufriev. 2018.  
        *Linear relationship between peak and season-long abundances in insects.*  
        PLOS ONE 13: e0193110. doi:10.1371/journal.pone.0193110.
        """
    )
