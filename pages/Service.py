import streamlit as st

def run():
   st.title("Our Services")

   st.header("Convenience and Results-Based Solutions")
   st.write("""
       At MiFood, our services are designed to offer both convenience and results. We understand the importance of saving your time and increasing production, and our robotics automation solutions are crafted to address these needs effectively.
   """)

   st.header("Horticultural Harvesting Robotics System")
   st.write("""
       Our flagship service revolves around a cutting-edge robotics system tailored for horticultural harvesting. This system harnesses the power of computer vision technology, integrated seamlessly with our advanced robots, to automate fruit harvesting processes.
   """)

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
   st.write("""
       MiFood offers a flexible pricing model to suit your needs. Our custom leasing service ensures a return on investment (ROI) in under 18 months. Choose the option that best fits your requirements:
   """)

   pricing_cols = st.columns(2)
   with pricing_cols[0]:
       st.subheader("Locked-in 18-month Contract")
       st.write("""
           - **Monthly Fee:** $2,333
           - **Total Cost over 18 months:** $41,994
       """)

   with pricing_cols[1]:
       st.subheader("Non-Fixed Contract")
       st.write("""
                .
           - **Monthly Fee:** $2,600
           - **Cancel Anytime**
       """)

   st.write("""
       Our pricing is transparent, providing you with the flexibility to choose the plan that aligns with your goals. Whether you opt for the locked-in 18-month contract or the non-fixed contract, our services are geared towards delivering tangible value and driving success in your horticultural operations.
   """)

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
