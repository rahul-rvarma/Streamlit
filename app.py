import streamlit as st

def find_largest(num1, num2, num3):
    largest = max(num1, num2, num3)
    return largest

def main():
    st.title('Find the Largest Number')

    num1 = st.number_input('Enter first number:')
    num2 = st.number_input('Enter second number:')
    num3 = st.number_input('Enter third number:')

    if st.button('Find Largest'):
        largest = find_largest(num1, num2, num3)
        st.success(f'The largest number is: {largest}')

if __name__ == "__main__":
    main()
