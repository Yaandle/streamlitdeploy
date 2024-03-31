import streamlit as st
from pathlib import Path

def run():
    st.title("About MiFood")
    with st.expander("Our Story"):
        st.write(
            """
            At MiFood, we are a team of passionate innovators dedicated to revolutionizing the horticultural industry through cutting-edge robotics and automation solutions. Our mission is to empower farmers and growers with the latest technological advancements, enabling them to overcome challenges, maximize efficiency, and pave the way for a more sustainable and prosperous future.
            """
        )
        st.write(
            """
            Born out of a deep respect for the vital role agriculture plays in our lives, we understand the complexities and labor-intensive nature of horticultural operations. By combining our expertise in robotics, computer vision, and artificial intelligence, we develop intelligent and autonomous systems that streamline processes, reduce manual labor, and optimize resource utilization.
            """
        )

    with st.expander("Our Approach"):
        st.write(
            """
            Our solutions are tailored to meet the unique needs of each client, offering customizable and scalable automation solutions that seamlessly integrate into existing operations. From precision planting and harvesting to crop monitoring and management, our range of services empowers growers to make informed decisions, increase yields, and minimize environmental impact.
            """
        )
    
    with st.expander("Our Team"):
        st.write(
            """
            MiFood is driven by a diverse and talented team of engineers, scientists, and agricultural experts, united by a shared passion for innovation and a commitment to sustainable practices. Our multidisciplinary approach ensures that our solutions are not only technologically advanced but also deeply rooted in a comprehensive understanding of horticultural processes and challenges.
            """
        )

    st.subheader("Industry Information")
    st.write(
        """
        Stay informed about the latest trends, challenges, and opportunities shaping the horticultural industry. Our dedicated resource center provides in-depth analyses, case studies, and expert insights, empowering you with the knowledge to make informed decisions and stay ahead of the curve.
        """
    )
    st.page_link("pages/Industry_Information.py", label=":blue[Learn More]")
    st.divider()
    st.subheader("Technology")
    st.write(
        """
        At the heart of MiFood's solutions lies a fusion of cutting-edge technologies, including advanced robotics, computer vision, machine learning, and artificial intelligence. Our team of skilled engineers and scientists continuously push the boundaries of innovation, developing proprietary algorithms and hardware systems that redefine the capabilities of automated horticultural operations.
        """
    )
    st.page_link("pages/Technology.py", label=":blue[Learn More]")
    technology_image = Path("images/technology.jpg")
    if technology_image.exists():
        st.image(technology_image, caption="MiFood's advanced robotics technology")

    st.divider()
    st.subheader("Services")
    services_cols = st.columns(1)
    with services_cols[0]:
        st.write(
            """
            Robot Leasing:
            Our flexible robot leasing programs provide cost-effective access to our automated solutions, allowing you to scale your operations and stay ahead of the curve.
            """
            """
            Customized Integration:
            Our team of experts work closely with you to integrate our solutions seamlessly into your existing operations, ensuring a smooth transition and maximizing efficiency.
            """
        )
        
    st.page_link("pages/Service.py", label=":blue[Learn More]")
    st.divider()


    st.subheader("Join the revolution")
    st.write(
        """
        We invite you to join us on this exciting journey as we redefine the future of horticulture. Together, we can unlock new levels of efficiency, productivity, and sustainability, ensuring a secure and abundant food supply for generations to come.
        """
    )

    st.write("MiFood, Australia | Contact: zac@mifood.es")

if __name__ == "__main__":
    run()
