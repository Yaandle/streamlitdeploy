import streamlit as st


st.title("About our app.")
with st.expander("Our Story"):
        st.write(
            """
            At MiFood, we are a team of passionate innovators dedicated to revolutionizing the horticultural industry through cutting-edge robotics and automation solutions. Our mission is to empower farmers and growers with the latest technological advancements, enabling them to overcome challenges, maximize efficiency, and pave the way for a more sustainable and prosperous future.

            Born out of a deep respect for the vital role agriculture plays in our lives, we understand the complexities and labor-intensive nature of horticultural operations. By combining our expertise in robotics, computer vision, and artificial intelligence, we develop intelligent and autonomous systems that streamline processes, reduce manual labor, and optimize resource utilization.
            """
        )

with st.expander("Our Approach"):
        st.write(
            """
            Our solutions are tailored to meet the unique needs of each client, offering customizable and scalable automation solutions that seamlessly integrate into existing operations. From precision planting and harvesting to crop monitoring and management, our range of services empowers growers to make informed decisions, increase yields, and minimize environmental impact.
            """
        )

with st.expander("Vision and Mission", expanded=True):
        st.write("""
            Our vision is to create a future where robotics empowers the
            horticultural industry, leading to increased productivity, reduced
            waste, and a more sustainable food system. Our mission is to develop
            and deploy innovative robotic solutions that address real-world
            challenges faced by farmers and growers.
        """)
        
st.header("Use Cases")
st.write("Check out how different companies and businesses are using our platform.")

use_cases = st.container()
with use_cases:
    cols = st.columns(2)
    
    with cols[0]:
        st.subheader("MyActionImages")
        st.write("Our platform helps the business save time.")
        st.write("**Key Features:**")
        st.write("- Automatic data sorting")
        st.write("- Product pipeline improvement")
        st.write("- Demand forecasting and inventory planning")
        
    with cols[1]:
        st.subheader("MiFood")
        st.write("Our platform helps agricultural businesses monitor crop health and optimize yield.")
        st.write("**Key Features:**")
        st.write("- Plant disease detection and classification")
        st.write("- Crop yield estimation")
        st.write("- Precision farming and resource optimization")
        
    cols = st.columns(2)
    
    with cols[0]:
        st.subheader("Manufacturing")
        st.write("Our platform helps manufacturers improve quality control and productivity.")
        st.write("**Key Features:**")
        st.write("- Defect detection and classification")
        st.write("- Predictive maintenance")
        st.write("- Workflow optimization")
        
    with cols[1]:
        st.subheader("Healthcare")
        st.write("Our platform helps healthcare providers improve patient outcomes and operational efficiency.")
        st.write("**Key Features:**")
        st.write("- Medical image analysis and diagnosis")
        st.write("- Remote patient monitoring")
        st.write("- Supply chain optimization")
