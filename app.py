import streamlit as st
#from factorial import fact

def fact(n):
    if n == 0 or n == 1:
        result = 1
    else: 
        result = n * fact(n-1)
    return result


def main():
    st.title("Factorial Calculation")
    number = st.number_input("Enter a number: ", min_value = 0, max_value = 900)
    if st.button("Calculate"):
        result = fact(number)
        st.write(f"The result of {number} factorial is {result}")

if __name__ == "__main__":
    main()