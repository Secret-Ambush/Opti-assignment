import streamlit as st
import pandas as pd

# Define a function to calculate the transportation problem
def transportation_solver(cost_matrix, supply, demand, INF=10**3):
    cost_matrix = cost_matrix.astype(float).values.tolist()
    total_supply = sum(supply)
    total_demand = sum(demand)
    
    if total_supply == total_demand:
        st.info("It's a BALANCED Transportation Problem")
        
    else:
        st.info("It's a UNBALANCED Transportation Problem")
        if total_supply > total_demand:
            for row in cost_matrix:
                row.append(0)
            demand.append(total_supply - total_demand)
            st.info("Adding a column")
        elif total_demand > total_supply:
            cost_matrix.append([0] * len(demand))
            supply.append(total_demand - total_supply)
            st.info("Adding a row")
        
    n = len(cost_matrix)
    m = len(cost_matrix[0])
    
    allocations = [[0]*m for _ in range(n)]
    result_cost = 0
    while any(supply) and any(demand):
        row_penalties = []
        col_penalties = []

        # Calculate row penalties
        for row in cost_matrix:
            sorted_costs = sorted(set(row))
            if len(sorted_costs) > 1:
                penalty = sorted_costs[1] - sorted_costs[0]
            else:
                penalty = 0
            row_penalties.append(penalty)

        # Calculate column penalties
        for j in range(m):
            col_costs = [cost_matrix[i][j] for i in range(n)]
            sorted_costs = sorted(set(col_costs))
            if len(sorted_costs) > 1:
                penalty = sorted_costs[1] - sorted_costs[0]
            else:
                penalty = 0
            col_penalties.append(penalty)

        # Find the highest penalty
        if max(row_penalties) > max(col_penalties):
            i = row_penalties.index(max(row_penalties))
            sorted_row = sorted((cost_matrix[i][j], j) for j in range(m))
            j = sorted_row[0][1]
        else:
            j = col_penalties.index(max(col_penalties))
            sorted_col = sorted((cost_matrix[i][j], i) for i in range(n))
            i = sorted_col[0][1]

        # Allocate as much as possible
        allocation = min(supply[i], demand[j])
        allocations[i][j] += allocation
        result_cost += allocation * cost_matrix[i][j]
        supply[i] -= allocation
        demand[j] -= allocation

        # If supply or demand is zero, replace the costs with INF
        if supply[i] == 0:
            for j in range(m):
                cost_matrix[i][j] = INF
        if demand[j] == 0:
            for i in range(n):
                cost_matrix[i][j] = INF

    return result_cost, allocations


# Streamlit app interface
st.title("Transportation Problem Solver")   

footer="""<style>
a:link , a:visited{
color: blue;
background-color: transparent;
text-decoration: underline;
}

a:hover,  a:active {
color: red;
background-color: transparent;
text-decoration: underline;
}

.footer {
position: fixed;
left: 0;
bottom: 0;
width: 100%;
background-color: transparent;
color: white;
text-align: center;
}
</style>
<div class="footer">
<p></p>
<p>Developed by Riddhi Goswami ✨</p>
</div>
"""

co1, co2 = st.columns([3,1])
co1.markdown("""
Hey there! ✨ This app optimizes the distribution of products from multiple suppliers to various consumers at the lowest possible cost. Here’s how you can use this tool:

1. **Input Costs and Quantities**: Enter the transportation costs from each supplier to each consumer, along with the available supplies and required demands.
2. **Automatic Balancing**: If the total supply and demand are unequal, the app adds a 'dummy' point with zero cost to balance the problem, ensuring solvability.
3. **Optimal Allocation**: Using Vogel's Approximation Method, the app calculates the most cost-effective distribution strategy and displays the optimal allocation matrix and the total transportation cost.
""")
co2.image("giphy.gif")

st.subheader("Enter details on cost matrix size")
num_rows = st.number_input("Enter number of rows (supply points):", min_value=1, key="num_rows")
num_cols = st.number_input("Enter number of columns (demand points):", min_value=1, key="num_cols")

# Initialize the session state to keep track of changes after submission
if 'submit' not in st.session_state:
    st.session_state['submit'] = False

# Submit button
if st.button('Submit'):
    st.session_state['submit'] = True

# This block will execute after the user clicks submit and state is True
st.write("\n\n")
if st.session_state['submit']:
    column_names = ['w{}'.format(i + 1) for i in range(num_cols)]
    
    st.subheader("Input your data below:")
    st.write("Cost matrix")
    column_names = ['w{}'.format(i+1) for i in range(num_cols)]
    input_data = pd.DataFrame(index=range(num_rows), columns=column_names)
    input_data = input_data.fillna(0)
    edited_data = st.data_editor(input_data)
    
    col3,col4 = st.columns([1,1])
    col3.write("🚛 SUPPLIES:")
    supplies = [col3.number_input(f"Enter supply for ROW s{i + 1}:", key=f"supply_{i}") for i in range(num_rows)]
    col4.write("🛍️ DEMAND:")
    demands = [col4.number_input(f"Enter demand for COLUMN {column_names[j]}:", key=f"demand_{j}") for j in range(num_cols)]
    
    col_1, col_2, col_3 = st.columns([1,1,1])
    if col_2.button("Solve Transportation Problem"):
        cost_matrix = edited_data.values.tolist()
        allocations = None
        result, allocations = transportation_solver(edited_data, supplies, demands)
        st.success("Done!")
        st.subheader("Results 🧐")
        st.markdown(f"The basic feasible solution cost is: `{result} units`")
        st.write("Final Allocations:")
        st.dataframe(allocations)

st.markdown(footer,unsafe_allow_html=True)

