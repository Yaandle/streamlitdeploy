import streamlit as st

def about_mifood():
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

if __name__ == "__main__":
    about_mifood()
