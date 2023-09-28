import streamlit as st

from langchain import PromptTemplate
from langchain.chat_models import ChatOpenAI
from langchain.schema import HumanMessage, SystemMessage

chat_model = ChatOpenAI(temperature=0.8, model_name="gpt-3.5-turbo", verbose=True)

template = """
    Act as an AI that will help convert the text to use proper grammar, professionalism, mannerisms, and be enthusiastic or empathetic. Try to address people by their names if a name is given in the text.

    For context the business is a(n) {business_type}.
    
    Rules:
    --------
    - If the user inputs an already perfect text, tell the user it is great as is.

    - If the user inputs something irrelevant to business texts or the context of the business, tell the user "Please input a business related text."
    --------

    EXAMPLES:
    --------
    Example 1:
    Human: okay i cut hair tomorrow 5
    AI: I can service your haircut tommorow 5 PM. See you then!

    Example 2:
    Human: We can happily schedule an appointment for 3 PM tomorrow for your pedicure. 
    AI: The text is great as is!

    Example 3:
    Human: Who is Donald Trump?
    AI: Please input a business related text.
    --------
"""

st.set_page_config(page_title="FluentFix")
st.header("FluentFix")

st.markdown("This is a quick project inspired to help fix my mom's lacking literacy skills in English. She works as a nail technician and often asks me to write or fix their text to a client she needs to communicate with so why not have [LangChain :parrot::chains:](https://python.langchain.com/) and [OpenAI](https://platform.openai.com/) do that!")

col1, col2 = st.columns(2)

with col1:
   st.markdown("### Business Context")
   option_context = st.selectbox(
       "What type of business is this?",
        ('Nail Salon', 'Barber', 'Hair Salon', 'Restaurant', 'Dry Cleaning'))

st.markdown("## Enter Text To Convert")

def get_text():
    input_text = st.text_area(label="Your Text", placeholder="Your Text", key="text_input", label_visibility="collapsed")
    return input_text

text_input = get_text()

st.markdown("## Your Converted Text:")

if text_input:
    prompt_with_options = template.format(business_type=option_context)

    messages = [SystemMessage(content=prompt_with_options), HumanMessage(content=text_input)]
    output_text = chat_model.predict_messages(messages).content
    output_text = output_text.replace("$", "\$")
    
    print(messages)

    st.write(output_text)