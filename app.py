
import streamlit as st
import pandas as pd
import numpy as np
import joblib

st.set_page_config(
    page_title="Dubai Estates | AI Valuation",
    page_icon="🏙️",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------- LUXURY DUBAI VILLAS ----------
st.markdown("""
<div style="
    background:
        linear-gradient(90deg, rgba(11,18,32,0.65), rgba(11,18,32,0.15)),
        url('https://images.unsplash.com/photo-1613490493576-7fde63acd811');
    background-size: cover;
    background-position: center;
    height: 280px;
    border-radius: 18px;
    margin-bottom: 25px;
    border: 1px solid rgba(216,181,109,0.45);
    display: flex;
    align-items: flex-end;
    padding: 25px;
    box-sizing: border-box;
">
    <div style="color: white;">
        <div style="
            color: #D8B56D;
            font-size: 12px;
            letter-spacing: 3px;
        ">
            EXCLUSIVE RESIDENCES
        </div>
        <div style="font-size: 27px; font-weight: 800;">
            Luxury Dubai Villas
        </div>
        <div style="font-size: 14px;">
            Discover premium residential properties
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

# ---------- PREMIUM DESIGN ----------
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&display=swap');

:root {
    --gold: #D8B56D;
    --navy: #0B1220;
    --panel: #131E30;
    --muted: #AAB5C7;
}

.stApp {
    background:
        radial-gradient(ellipse at 15% 0%, #1B2D46 0%, transparent 45%),
        linear-gradient(145deg, #0B1220, #101827 65%, #0B1220);
    font-family: 'Inter', sans-serif;
}

.block-container {
    max-width: 1250px;
    padding-top: 2rem;
    padding-bottom: 3rem;
}

#MainMenu, footer, header {visibility: hidden;}

.hero {
    padding: 28px 30px;
    border: 1px solid rgba(216,181,109,.32);
    border-radius: 22px;
    background: linear-gradient(120deg, #17253A, #111B2B 70%);
    box-shadow: 0 15px 50px rgba(0,0,0,.2);
    margin-bottom: 22px;
}

.brand {
    color: var(--gold);
    font-size: 13px;
    font-weight: 800;
    letter-spacing: 4px;
}

.hero-title {
    color: #F7F8FC;
    font-size: clamp(30px, 4vw, 48px);
    font-weight: 800;
    line-height: 1.15;
    margin: 15px 0 10px 0;
    animation: shimmer 5s ease-in-out infinite;
}

.hero-description {
    color: #B9C4D5;
    font-size: 15px;
    line-height: 1.8;
    max-width: 750px;
}

@keyframes shimmer {
    0%, 100% { text-shadow: 0 0 0 rgba(216,181,109,0); }
    50% { text-shadow: 0 0 20px rgba(216,181,109,.35); }
}

.section-title {
    color: #F3F5FA;
    font-size: 22px;
    font-weight: 700;
    margin: 8px 0 4px;
}

.section-subtitle {
    color: var(--muted);
    font-size: 13px;
    margin-bottom: 18px;
}

div[data-testid="stVerticalBlockBorderWrapper"] {
    background: rgba(19,30,48,.84);
    border: 1px solid rgba(180,195,220,.15);
    border-radius: 18px;
    padding: 20px;
}

label, .stMarkdown p {
    color: #D6DEEA;
}

div[data-baseweb="select"] > div,
div[data-baseweb="input"] > div {
    background: #0D1727;
    border: 1px solid #34445C;
    border-radius: 10px;
}

div[data-baseweb="select"] * {
    color: #F3F5FA;
}

input {
    color: #FFFFFF !important;
}

div[data-testid="stFormSubmitButton"] button {
    background: linear-gradient(100deg, #D8B56D, #F1D9A0);
    color: #101827;
    font-weight: 800;
    border: none;
    border-radius: 11px;
    min-height: 48px;
    width: 100%;
    transition: all .25s ease;
}

div[data-testid="stFormSubmitButton"] button:hover {
    box-shadow: 0 0 24px rgba(216,181,109,.45);
    transform: translateY(-2px);
    color: #101827;
}

.result-card {
    border: 1px solid rgba(216,181,109,.7);
    border-radius: 18px;
    padding: 25px;
    margin-top: 20px;
    background: linear-gradient(120deg, #1A2A3D, #101827);
    box-shadow: 0 0 28px rgba(216,181,109,.12);
    animation: appear .7s ease-out;
}

@keyframes appear {
    from {opacity: 0; transform: translateY(12px);}
    to {opacity: 1; transform: translateY(0);}
}

.result-label {
    color: #D8B56D;
    font-size: 12px;
    letter-spacing: 2px;
    font-weight: 800;
}

.result-price {
    color: #FFFFFF;
    font-size: clamp(30px, 4vw, 46px);
    font-weight: 800;
    margin: 12px 0;
    overflow-wrap: anywhere;
}

.result-note {
    color: #AAB5C7;
    font-size: 12px;
    line-height: 1.7;
}

.footer {
    text-align: center;
    color: #8391A6;
    font-size: 12px;
    margin-top: 35px;
}

div[data-testid="stAlert"] {
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)


# ---------- LOAD MODEL AND DATA ----------
@st.cache_resource
def load_model():
    return joblib.load("model_b_log_price.joblib")


@st.cache_data
def load_data():
    data = pd.read_csv("model_data_deploy.csv")
    data["area_name_en"] = (
        data["area_name_en"].astype("string").str.strip()
    )
    return data


try:
    model = load_model()
    df = load_data()
except Exception as error:
    st.error("Could not load the model or dataset.")
    st.code(str(error))
    st.stop()


# ---------- HERO HEADER ----------
st.markdown("""
<div class="hero">
    <div class="brand">◆ DUBAI ESTATES &nbsp; | &nbsp; AI LAB</div>
    <div class="hero-title">Discover your property's value.</div>
    <div class="hero-description">
        A smarter way to estimate residential property prices in Dubai.
        Enter the property details below to generate an AI-powered
        price estimate in UAE dirhams.
    </div>
</div>
""", unsafe_allow_html=True)


# ---------- SUMMARY CARDS ----------
c1, c2, c3 = st.columns(3)

with c1:
    st.markdown("""
    <div style="background:#131E30;border:1px solid #293A50;
    border-radius:14px;padding:18px;">
    <div style="color:#AAB5C7;font-size:12px;">MODEL</div>
    <div style="color:#D8B56D;font-size:20px;font-weight:800;">
    Linear Regression</div>
    <div style="color:#AAB5C7;font-size:11px;">Log-price model</div>
    </div>
    """, unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div style="background:#131E30;border:1px solid #293A50;
    border-radius:14px;padding:18px;">
    <div style="color:#AAB5C7;font-size:12px;">TEST R² SCORE</div>
    <div style="color:#D8B56D;font-size:20px;font-weight:800;">
    0.808</div>
    <div style="color:#AAB5C7;font-size:11px;">Previously evaluated test set</div>
    </div>
    """, unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div style="background:#131E30;border:1px solid #293A50;
    border-radius:14px;padding:18px;">
    <div style="color:#AAB5C7;font-size:12px;">DATASET</div>
    <div style="color:#D8B56D;font-size:20px;font-weight:800;">
    Dubai, UAE</div>
    <div style="color:#AAB5C7;font-size:11px;">Residential transactions</div>
    </div>
    """, unsafe_allow_html=True)

# ---------- PROPERTY MARKET DASHBOARD ----------
st.markdown('<div class="section-title">Dubai Property Market Dashboard</div>',
            unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Explore the transaction data available in your dataset.</div>',
    unsafe_allow_html=True
)


# ---------- DASHBOARD DATA AND FILTERS ----------

market_data = df.copy()

market_data["actual_worth"] = pd.to_numeric(
    market_data["actual_worth"], errors="coerce"
)

market_data["instance_date"] = pd.to_datetime(
    market_data["instance_date"], errors="coerce"
)

market_data = market_data.dropna(
    subset=["actual_worth", "area_name_en"]
)

# Create three interactive filters
st.subheader("Filter Property Market Data")

filter1, filter2, filter3 = st.columns(3)

with filter1:
    communities = sorted(
        market_data["area_name_en"].dropna().unique().tolist()
    )
    selected_community = st.selectbox(
        "Community",
        ["All Communities"] + communities
    )

with filter2:
    property_types = sorted(
        market_data["property_sub_type_en"]
        .dropna()
        .unique()
        .tolist()
    )
    selected_type = st.selectbox(
        "Property Type",
        ["All Property Types"] + property_types
    )

with filter3:
    years = sorted(
        market_data["instance_date"].dropna().dt.year.unique().tolist(),
        reverse=True
    )
    selected_year = st.selectbox(
        "Transaction Year",
        ["All Years"] + years
    )

# Apply selected filters
filtered_data = market_data.copy()

if selected_community != "All Communities":
    filtered_data = filtered_data[
        filtered_data["area_name_en"] == selected_community
    ]

if selected_type != "All Property Types":
    filtered_data = filtered_data[
        filtered_data["property_sub_type_en"] == selected_type
    ]

if selected_year != "All Years":
    filtered_data = filtered_data[
        filtered_data["instance_date"].dt.year == selected_year
    ]

# Dashboard summary figures update with the filters
st.subheader("Filtered Market Summary")

total_transactions = len(filtered_data)
total_value = filtered_data["actual_worth"].sum()
median_price = filtered_data["actual_worth"].median()

m1, m2, m3 = st.columns(3)

m1.metric("Recorded Transactions", f"{total_transactions:,}")
m2.metric("Total Recorded Value", f"AED {total_value:,.0f}")
m3.metric(
    "Median Sale Price",
    f"AED {median_price:,.0f}" if total_transactions else "No data"
)

# Most active communities
st.subheader("Most Active Communities")

if not filtered_data.empty:
    top_communities = filtered_data["area_name_en"].value_counts().head(10)
    st.bar_chart(top_communities)
else:
    st.info("No transactions match these filters.")

# Historical transaction trend
st.subheader("Historical Transaction Trend")

# Property Price Comparison by Community
st.subheader("Average Property Price by Community")

if not filtered_data.empty:
    community_prices = (
        filtered_data.groupby("area_name_en")["actual_worth"]
        .mean()
        .sort_values(ascending=False)
        .head(10)
    )

    community_prices = community_prices.round(0)

    st.bar_chart(community_prices)

    st.caption(
        "Showing the 10 communities with the highest average "
        "recorded transaction values in the filtered dataset."
    )
else:
    st.info("No property prices are available for these filters.")

dated_data = filtered_data.dropna(subset=["instance_date"]).copy()
dated_data["sale_year"] = dated_data["instance_date"].dt.year

yearly_transactions = (
    dated_data.groupby("sale_year")
    .size()
    .rename("Transactions")
)

if not yearly_transactions.empty:
    st.line_chart(yearly_transactions)
else:
    st.info("No valid transaction dates match these filters.")



st.markdown('<div class="section-title">Property details</div>',
            unsafe_allow_html=True)
st.markdown(
    '<div class="section-subtitle">Complete the fields to estimate the sale price.</div>',
    unsafe_allow_html=True
)

communities = sorted(
    df["area_name_en"].dropna().astype(str).unique().tolist()
)

# Match the original model's room categories
room_values = (
    df["rooms_en"].dropna().astype(str).unique().tolist()
)
room_values = sorted(room_values)
room_options = ["Unknown"] + room_values

with st.container(border=True):
    with st.form("property_form"):
        left, right = st.columns(2, gap="large")

        with left:
            community = st.selectbox(
                "📍 Community",
                communities
            )

            property_type = st.selectbox(
                "🏢 Property type",
                ["Flat", "Villa"]
            )

            rooms = st.selectbox(
                "🛏️ Rooms",
                room_options
            )

            area_sqft = st.number_input(
                "📐 Property area (sq ft)",
                min_value=100.0,
                max_value=50000.0,
                value=1000.0,
                step=50.0
            )

        with right:
            parking = st.selectbox(
                "🚗 Parking availability",
                ["1", "0"],
                format_func=lambda value:
                    "Available" if value == "1" else "Not available"
            )

            registration_type = st.selectbox(
                "🏷️ Property status",
                ["Existing Properties", "Off-Plan Properties"]
            )

            sale_year = st.selectbox(
                "📅 Sale year",
                list(range(2020, 2026)),
                index=5
            )

            sale_month = st.selectbox(
                "🗓️ Sale month",
                list(range(1, 13)),
                index=9,
                format_func=lambda month:
                    pd.Timestamp(
                        year=2020, month=month, day=1
                    ).strftime("%B")
            )

        submitted = st.form_submit_button(
            "✦  ESTIMATE PROPERTY VALUE"
        )


# ---------- PREDICTION ----------
if submitted:
    input_data = pd.DataFrame([{
        "area_name_en": community,
        "property_sub_type_en": property_type,
        "rooms_en": rooms,
        "has_parking": parking,
        "reg_type_en": registration_type,
        "area_sqft": area_sqft,
        "sale_year": sale_year,
        "sale_month": sale_month
    }])

    try:
        with st.spinner("Analyzing property details..."):
            predicted_log_price = model.predict(input_data)[0]
            predicted_price = float(np.exp(predicted_log_price))

        if not np.isfinite(predicted_price) or predicted_price <= 0:
            st.error("The model returned an invalid price. Try different inputs.")
        else:
            st.markdown(f"""
            <div class="result-card">
                <div class="result-label">✦ AI-ESTIMATED PROPERTY VALUE</div>
                <div class="result-price">AED {predicted_price:,.0f}</div>
                <div class="result-note">
                    {community} &nbsp; • &nbsp; {property_type}
                    &nbsp; • &nbsp; {area_sqft:,.0f} sq ft<br>
                    Estimate generated from your trained machine-learning model.
                    This is not a formal property valuation or a guaranteed sale price.
                </div>
            </div>
            """, unsafe_allow_html=True)

            st.caption(
                "Model limitation: this estimate depends on the training data "
                "and may be less reliable for unusual or luxury properties."
            )

            
            st.subheader("📊 Historical Property Price Comparison")

            
            historical = pd.read_csv("model_data_deploy.csv")


            historical["sale_year"] = pd.to_datetime(
                historical["instance_date"], errors="coerce"
            ).dt.year

            comparison = historical[
                (historical["area_name_en"] == community) &
                (historical["property_sub_type_en"] == property_type)
            ].copy()

            comparison = comparison.dropna(
                subset=["sale_year", "actual_worth"]
            )

            if not comparison.empty:
                chart_data = (
                    comparison.groupby("sale_year")["actual_worth"]
                    .median()
                    .div(1_000_000)
                    .reset_index()
                )

                chart_data["sale_year"] = chart_data["sale_year"].astype(str)

                st.line_chart(
                    chart_data.set_index("sale_year")["actual_worth"]
                )

                st.caption(
                    "Median historical sale price by year, in millions of AED."
                )
            else:
                st.info(
                    "No matching historical sales were found for this "
                    "community and property type."
                )


    except Exception as error:
        st.error("The prediction could not be completed.")
        st.code(str(error))


st.markdown("""
<div class="footer">
    DUBAI ESTATES AI LAB · EDUCATIONAL PROJECT<br>
    Powered by Python, Streamlit and Scikit-learn
</div>
""", unsafe_allow_html=True)
