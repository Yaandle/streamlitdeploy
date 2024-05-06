import streamlit as st

def run():
    st.set_page_config(page_title="Industry Automation Solutions")
    st.title("The Automation Revolution: Transforming Industries")

    st.subheader("Addressing Industry Challenges with Robotics and AI")
    with st.expander("Labor Shortages and Rising Costs"):
        st.write(
            """
            Finding and retaining skilled labor has become increasingly difficult, leading to rising labor costs and impacting production capacity. The COVID-19 pandemic further exacerbated this issue, forcing many businesses to operate with limited workforces.
            
            Automation through robotics and intelligent systems can help reduce the dependency on manual labor, allowing companies to maintain productivity and efficiency even with a smaller workforce. These technologies can take on repetitive or hazardous tasks, freeing up human workers to focus on higher-value, creative tasks.
            """
        )

    with st.expander("Inefficient Manual Processes"):
        st.write(
            """
            Manual tasks often involve slow speeds, inconsistent quality, and potential product damage. This leads to increased risk of waste, safety hazards, and reduced profitability.
            
            Automated systems can operate with consistent speed and precision, improving throughput, reducing waste, and enhancing product quality. Robotic solutions can handle delicate or complex tasks with greater accuracy and reliability than human workers, minimizing errors and defects.
            """
        )

    with st.expander("Human Error and Fatigue"):
        st.write(
            """
            Mistakes due to fatigue or human error can result in product defects, safety issues, and operational disruptions. Manual work also exposes employees to risks like musculoskeletal injuries and health concerns.
            
            Automated systems can perform tasks in challenging environments, mitigating the risk of accidents and exposure to health hazards for human workers. This not only improves workplace safety but also plays a vital role in maintaining hygiene and limiting the spread of diseases like COVID-19.
            """
        )

    with st.expander("Sustainability Concerns"):
        st.write(
            """
            Traditional industrial practices can contribute to environmental challenges such as resource depletion, pollution, and high carbon footprints. There is a growing demand for sustainable solutions that minimize the impact on the planet.
            
            Data-driven automation and precision technologies enable more efficient use of resources, lower energy consumption, and reduced environmental impact. Automated systems can optimize processes, minimize waste, and support the transition towards a more sustainable industrial landscape.
            """
        )

    st.subheader("The Promise of Automation")
    st.write(
        """
        Robotics, artificial intelligence, and related technologies hold immense potential to address these challenges and transform industries across the board. By embracing these transformative solutions, businesses can unlock a wide range of benefits:
        """
    )

    benefits_cols = st.columns(2)
    with benefits_cols[0]:
        st.write(
            """
            - Increased Productivity and Efficiency
            - Reduced Labor Costs and Dependency
            - Improved Product Quality and Consistency
            """
        )

    with benefits_cols[1]:
        st.write(
            """
            - Enhanced Workplace Safety and Hygiene
            - Improved Sustainability and Environmental Impact
            - Competitive Advantage in Changing Markets
            """
        )

    st.subheader("The Future of Industry")
    st.write(
        """
        While challenges remain in terms of accessibility, affordability, and seamless integration, the future of industry appears increasingly automated. Embracing these transformative technologies is crucial for creating more sustainable, efficient, and resilient businesses that can thrive in the face of evolving market demands and environmental pressures.
        
        As industries continue to undergo this digital and robotic revolution, those that can effectively harness the power of automation will be poised to gain a significant competitive advantage and lead the way into the future. The businesses that invest in automation solutions today will be better equipped to navigate the complexities of the modern industrial landscape and stay ahead of the curve.
        """
    )

   # st.subheader("Explore Our Automation Solutions")
    # st.write(
      #  """
       # Learn more about our robotic and AI-powered automation services
       # """
    # )
   ## st.page_link("pages/Service.py")             Add YKS Site

if __name__ == "__main__":
    run()