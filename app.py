import streamlit as st
import sympy as sp

# Access the API key from Streamlit secrets
api_key = st.secrets["api_key"]

# Example usage (This is just a demonstration, use the API key where necessary in your app)
#st.write(f"Your API key is: {api_key}")

# App title and description
st.title("Maximizing Profit with Calculus! 📈")
st.write("""
Ever wondered how companies determine the best price for their products? It’s not just guesswork—there’s a fascinating science behind it, and it involves calculus! 📊✨

Let’s dive into a case study to understand how derivatives can help us find the optimal price for a new smartphone.
""")

# Developer credit
st.write("**Developed By: Irfan Ullah Khan**")

# Inputs for fixed and variable costs
st.subheader("Step 1: Input Your Cost Structure")
fixed_cost = st.number_input("Fixed Costs ($)", value=2000, step=100)
variable_cost_per_unit = st.number_input("Variable Cost per Unit ($)", value=20, step=1)

# Inputs for demand curve and revenue function
st.subheader("Step 2: Input Your Demand and Revenue Function")
max_price = st.number_input("Maximum Price ($)", value=200, step=10)
max_units = st.number_input("Maximum Units Sold", value=1000, step=50)

# Profit equation
st.subheader("Step 3: Setting Up the Profit Equation")
st.write("We assume the profit function is a quadratic equation based on the price of the smartphone.")

price = sp.Symbol('x')
revenue = price * (max_units - (max_units / max_price) * price)
cost = fixed_cost + variable_cost_per_unit * (max_units - (max_units / max_price) * price)
profit = revenue - cost

st.latex(f"P(x) = {sp.simplify(profit)}")

# Derivative and critical points
st.subheader("Step 4: Applying Derivatives")
derivative = sp.diff(profit, price)
st.write("The derivative of the profit function is:")
st.latex(f"P'(x) = {sp.simplify(derivative)}")

critical_points = sp.solve(derivative, price)
optimal_price = critical_points[0]

st.write(f"The optimal price to maximize profit is: ${optimal_price:.2f}")

# Validate and test the pricing strategy
st.subheader("Step 5: Testing Your Price")
st.write(f"Based on our calculations, the price of **${optimal_price:.2f}** per smartphone should maximize your profit.")
