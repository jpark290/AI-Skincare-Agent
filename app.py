import streamlit as st
from pipeline import run_pipeline

st.title("AI Skincare Multi-Agent System")

# 1) General Question
query = st.text_input(
    "Enter your skincare question:",
    ""
)

# 2) Skin type
skin_type = st.selectbox(
    "Skin Type",
    ["", "oily", "dry", "combination", "normal", "sensitive"]
)

# 3) Product type
product_type = st.selectbox(
    "Product Type",
    ["", "cleanser", "serum", "moisturizer", "sunscreen", "other"]
)

# 4) Budget
min_price = st.number_input("Min Price", min_value=0, value=0)
max_price = st.number_input("Max Price", min_value=0, value=0)

# 5) Main Skin Concern
main_concerns = st.multiselect(
    "Main Skin Concerns (choose up to 3)",
    ["acne", "redness", "hydration", "dark spots", "wrinkles", "sensitivity"]
)

if len(main_concerns) > 3:
    main_concerns = main_concerns[:3]

# 6) Age Range
age_range = st.selectbox(
    "Age Range",
    ["", "less_than_18", "18_to_25", "25_to_35", "35_to_45", "45_plus"]
)

# Ask the need to prioritize for sensible skin
needs_sensitive = st.checkbox(
    "Prioritize products suitable for sensitive skin",
    value=True
)


filters = {
    "skin_type": skin_type,
    "product_type": product_type,
    "min_price": min_price,
    "max_price": max_price,
    "main_concerns": main_concerns,
    "age_range": age_range,
    "needs_sensitive": needs_sensitive
}

if st.button("Run Consultation"):
    if len(main_concerns) == 0:
        st.warning("Please select at least one main concern.")
    else:
        summary, recs, score = run_pipeline(query, filters)

        st.subheader("Summary")
        st.write(summary)

        st.subheader("Recommendations")
        for r in recs:
            st.markdown(r)

      