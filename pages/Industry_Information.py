import streamlit as st

def run():
    st.title("Industry Information")

    st.subheader("Challenges in the Horticultural Industry")
    with st.expander("Labor Shortages and Rising Costs"):
        st.write(
            """
            Finding and retaining skilled labor has become increasingly difficult, leading to rising labor costs and impacting production capacity. The pandemic further exacerbated this issue, forcing growers to operate with limited workforces.
            """
        )

    with st.expander("Inefficient Harvesting"):
        st.write(
            """
            Manual harvesting often involves long hours, slow picking speeds, and potential damage to produce. This leads to increased risk of food waste and reduced profitability.
            """
        )

    with st.expander("Human Error and Fatigue"):
        st.write(
            """
            Mistakes due to fatigue or human error can result in product damage, inconsistent quality, and even safety hazards for workers. Additionally, manual tasks expose workers to risks like musculoskeletal injuries and potential COVID-19 transmission.
            """
        )

    with st.expander("Sustainability Concerns"):
        st.write(
            """
            Traditional farming practices can contribute to environmental issues like water overuse, soil depletion, and pesticide pollution. There is a growing need for sustainable solutions that minimize environmental impact.
            """
        )

    st.subheader("Technology as a Solution")
    st.write(
        """
        Robotics and related technologies hold immense potential to address these challenges and transform the horticultural industry:
        """
    )

    with st.expander("Robotic Harvesting"):
        st.write(
            """
            Automation through robotic harvesters can improve efficiency, reduce labor dependence, and minimize damage to produce. This leads to higher yields, lower costs, and improved product quality.
            """
        )
        robot_harvester_image = "static/strawberryrobotlarge.jpg"
        if robot_harvester_image:
            st.image(robot_harvester_image, caption="Robotic Harvester")

    with st.expander("Data-Driven Practices"):
        st.write(
            """
            Sensors and data analytics can provide valuable insights into crop health, soil conditions, and environmental factors. This allows for optimization of irrigation, fertilization, and pest control, leading to improved resource efficiency and sustainability.
            """
        )

    with st.expander("Enhanced Safety and Hygiene"):
        st.write(
            """
            Robots can perform repetitive tasks in challenging environments, reducing the risk of accidents and exposure to hazards for human workers. This also plays a vital role in mitigating the spread of diseases like COVID-19.
            """
        )

    with st.expander("Precision Agriculture"):
        st.write(
            """
            Technologies like drones and automated systems enable targeted interventions based on specific data points, maximizing resource utilization and minimizing waste.
            """
        )

    st.subheader("Benefits for Farmers")
    benefits_cols = st.columns(2)
    with benefits_cols[0]:
        st.write(
            """
            - Increased Productivity and Efficiency
            - Reduced Labor Costs
            - Improved Product Quality
            """
        )

    with benefits_cols[1]:
        st.write(
            """
            - Enhanced Sustainability
            - Improved Worker Safety and Well-being
            """
        )

    st.subheader("Looking Ahead")
    st.write(
        """
        While challenges remain in terms of accessibility, affordability, and integration of these technologies, the future of horticulture appears promising. Embracing automation and innovation is crucial for creating a more sustainable, efficient, and resilient agricultural sector that addresses the growing demand for food while ensuring fair labor practices, worker safety, and environmental responsibility.
        """
    )



if __name__ == "__main__":
    run()
