import streamlit as st

st.title("About")

with st.expander("Our Story"):
    st.write("""
    We are a team of passionate innovators dedicated to revolutionizing industries through cutting-edge robotics and automation solutions. Our mission is to empower businesses with the latest technological advancements, enabling them to overcome challenges, maximize efficiency, and pave the way for a more sustainable and prosperous future.
    
    Born out of a deep understanding of the complexities and labor-intensive nature of various business operations, we have combined our expertise in robotics, computer vision, and artificial intelligence to develop intelligent and autonomous systems that streamline processes, reduce manual labor, and optimize resource utilization.
    """)

with st.expander("Our Approach"):
    st.write("""
    Our solutions are tailored to meet the unique needs of each client, offering customizable and scalable automation solutions that seamlessly integrate into existing operations. From precision manufacturing and logistics to data-driven decision-making and remote monitoring, our range of services empowers businesses to make informed decisions, increase productivity, and minimize environmental impact.
    """)

with st.expander("Vision and Mission", expanded=True):
    st.write("""
    Our vision is to create a future where robotics and automation empower businesses across industries, leading to increased efficiency, reduced waste, and a more sustainable future.
    
    Our mission is to develop and deploy innovative robotic and automation solutions that address real-world challenges faced by our clients, helping them achieve their goals and stay ahead of the competition.
    """)