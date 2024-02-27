import streamlit as st

class Style:
    
    def __init__(self):

        st.set_page_config(
            page_title="Streamlit EDA", 
            layout = 'centered', 
            initial_sidebar_state = 'expanded'
        )

        css_style = """
                    <style>
                        h1 a {
                            visibility: hidden;
                        }

                        .css-4z1n4l {
                            visibility: hidden;
                        }
                        
                        footer {
                            visibility: hidden;
                        }
                        
                        .css-15zrgzn {
                            visibility: hidden;
                        }
                        
                        button:hover {
                            border-color: #076deb !important; 
                            color: #076deb !important; 
                            background: transparent !important; 
                            cursor: pointer;
                        }
                        
                        .css-s1k4sy .st-co {
                            border: 1px solid #076deb !important;
                        }
                        
                        [data-testid="toastContainer"] {
                            position: absolute; 
                            top: 50px; 
                            right: 0;
                        }
                    </style>
                """

        st.markdown(css_style, unsafe_allow_html=True)
