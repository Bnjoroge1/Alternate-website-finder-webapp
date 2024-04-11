from googlesearch import search
import streamlit as st  
import time

## set page

st.set_page_config(
    page_title="Alternate Website Finder",
    page_icon="🌐",
    initial_sidebar_state="collapsed"
)

###  side bar
SideBar = st.sidebar

with SideBar:
    st.write("## 🌐 Alternate Website")
    st.write("Developer: Nishant Maity")
    st.write("---")
    st.subheader("Social links")
    st.markdown(
        """
        <ul>
            <li><a href="https://www.linkedin.com/in/nishantmaity">Linkedin</a></li>    
            <li><a href="https://github.com/Nishant43S/">Github</a></li>
            <li><a href="https://www.instagram.com/invites/contact/?i=1kgck1bm2send&utm_content=m95jbmo">instagram</a></li>
        </ul>
        """,
        unsafe_allow_html=True
    )

FrontPageText = """
Find the alternative websites with this webapp.
Github link of this project [Alternate Website finder](https://github.com/Nishant43S/Alternate-website-finder-webapp.git)
"""

st.header("Alternate Website Finder")  ### main Title
st.write(FrontPageText)


Form = st.form(border=False,key="Form")   ########  input fields
with Form:
    SearchWebsite = st.text_input(
        label="",type="default",
        placeholder="Search Website Hear",
        disabled=False,
        label_visibility="hidden"
    )

    Number_of_Results = st.slider(
            label="Number of Results",min_value=1,
            max_value=150,value=15,
            step=1
        )
    
    GenerateBtn , InputResults = st.columns([4,6])

    with GenerateBtn:

        GetResults = st.form_submit_button("Generate Links",use_container_width=True)
        

    with InputResults:
        if GetResults:
                GeneratedResult = f"ㅤWebsite: {SearchWebsite}ㅤㅤㅤResults: {Number_of_Results}"
                def stream_data1():
                    for word in GeneratedResult.split(" "):
                        yield word + " "
                        time.sleep(0.02)
                st.write_stream(stream_data1)
    
        
##########  main logic of app

if GetResults:
    if SearchWebsite == "":
        st.warning("Enter Website Name")
    else:
        with st.spinner("Generating Results..."):
            time.sleep(3)

        st.toast(SearchWebsite)
        ResultText = f"List of alternate Websites of {SearchWebsite}"
        def stream_data2():
            for word in ResultText.split(" "):
                yield word + " "
                time.sleep(0.03)
        st.write_stream(stream_data2)
        st.write("---")
        if __name__=="__main__":
            try:
                Query = (f"related:{SearchWebsite}.com")
                Results = search(
                    Query,
                    num_results=Number_of_Results,
                    sleep_interval=5,timeout= 2,
                    advanced=True
                )
                for i in Results:
                    Title = (f"Title: {i.title}")
                    Description = (f"Description: {i.description}")
                    Url = (f"Link: {i.url}")
                    st.write(Title)
                    st.write(Description)
                    st.write(Url)
                    st.text("")


            except Exception as err:
                Error = f"Too many requests{err}"
                st.info(Error)
                st.info("use after some time or refresh the web page")