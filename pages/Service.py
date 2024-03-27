import streamlit as st

def run():
    st.title("Our Services")
    st.header("Convenience and Results-Based Solutions")
    st.write(""" At MiFood, our services are designed to offer both convenience and results. We understand the importance of saving your time and increasing production, and our robotics automation solutions are crafted to address these needs effectively. """)

    st.header("Horticultural Harvesting Robotics System")
    st.write(""" Our flagship service revolves around a cutting-edge robotics system tailored for horticultural harvesting. This system harnesses the power of computer vision technology, integrated seamlessly with our advanced robots, to automate fruit harvesting processes. """)

    benefits_cols = st.columns(2)
    with benefits_cols[0]:
        st.subheader("Key Benefits")
        st.write("""
- Increased Efficiency
- Reduced Labor Costs
- Improved Harvest Quality
""")
    with benefits_cols[1]:
        st.subheader("Sustainability")
        st.write("""
- Lowered CO2 Emissions
- Minimized Environmental Impact
- Optimized Resource Utilization
""")

    st.header("Pricing")
    st.write(""" MiFood offers flexible pricing options to suit your needs. Choose the plan that best fits your requirements: """)

    pricing_cols = st.columns(3)
    with pricing_cols[0]:
        st.subheader("Non-Locked-in Contract")
        st.write("""
- **Monthly Fee:** $2,800
- **Cancel Anytime**
""")
    with pricing_cols[1]:
        st.subheader("6-Month Contract")
        st.write("""
- **Monthly Fee:** $2,500
- **Total Cost for 6 months:** $15,000
""")
    with pricing_cols[2]:
        st.subheader("3-Month Contract")
        st.write("""
- **Monthly Fee:** $2,300
- **Total Cost for 3 months:** $6,900
""")

    st.write(""" Our pricing is transparent, providing you with flexibility and value for your horticultural operations. """)

    st.header("Request a Quote")
    with st.form("quote_form"):
        st.write("### Contact Information")
        name = st.text_input("Name")
        email = st.text_input("Email")
        company = st.text_input("Company")

        st.write("### Project Details")
        project_type = st.selectbox("Project Type", ["Horticultural Harvesting", "Other"])
        description = st.text_area("Please describe your project requirements")

        submitted = st.form_submit_button("Request Quote")
        if submitted:
            # Add code to handle form submission (e.g., send email, save to database)
            st.success(f"Thank you, {name}! Our team will review your request and provide you with a quote shortly.")

if __name__ == "__main__":
    run()