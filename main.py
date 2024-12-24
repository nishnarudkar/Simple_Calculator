import streamlit as st

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "🚫 Error: Division by zero is not allowed."
    return n1 / n2


operations = {
    "➕ Addition": add,
    "➖ Subtraction": subtract,
    "✖️ Multiplication": multiply,
    "➗ Division": divide,
}

if "result" not in st.session_state:
    st.session_state.result = None

st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;
    }
    h1 {
        color: #4caf50;
        font-family: Arial, sans-serif;
    }
    .stButton>button {
        background-color: #4caf50;
        color: white;
        border-radius: 8px;
        font-size: 16px;
        height: 50px;
        width: 150px;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🧮 Calculator App")
st.markdown("A simple and **visually enhanced** calculator built with Streamlit! 🚀")

st.header("Input Section")
if st.session_state.result is None:
    first_number = st.number_input("Enter the first number:", step=0.01, key="first_number")
else:
    st.markdown(f"**Current Result: `{st.session_state.result}`**")
    first_number = st.session_state.result

operation = st.selectbox(
    "Select an Operation:",
    list(operations.keys()),
    key="operation"
)

second_number = st.number_input("Enter the second number:", step=0.01, key="second_number")

col1, col2 = st.columns(2) 

with col1:
    if st.button("✨ Calculate"):
        selected_operation = operations[operation]
        result = selected_operation(first_number, second_number)
        st.session_state.result = result 
        st.success(f"🎉 Result: `{first_number} {operation.split()[1]} {second_number} = {result}`")

st.markdown("---")
st.markdown(
    "✨ *Thank you for using this app! Built with 💻 by Nishant Narudkar.*"
)
