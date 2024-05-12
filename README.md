<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://i.imgur.com/6wj0hh6.jpg" alt="Project logo"></a>
</p>

<h3 align="center">Project Title</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/issues)
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)](https://github.com/kylelobo/The-Documentation-Compendium/pulls)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

## Transportation Problem Solver

This application helps solve the transportation problem, a type of optimization problem where the goal is to determine the most cost-effective way to distribute a product from several suppliers to various consumers to satisfy demand at the lowest cost. Here’s how it works:

1. **Input Data**: You will input the cost of transporting units from each supply point (row) to each demand point (column) along with the available supplies and required demands.

2. **Balancing the Problem**: If the total supply does not equal the total demand, the app automatically adjusts by adding a 'dummy' supplier or consumer with zero transportation cost to balance the equation. This ensures the problem remains solvable under standard assumptions of the transportation problem.

3. **Calculating the Solution**: The app uses Vogel's Approximation Method (VAM) to find an initial feasible solution by minimizing transportation costs. This method prioritizes the highest cost-differences between the cheapest and second-cheapest routes to quickly identify cost-effective transportation routes.

4. **View Results**: After computing, the app displays the optimal allocation of resources from suppliers to consumers and the minimum transportation cost. You will see a matrix showing how much each supplier should send to each consumer to minimize costs.

5. **Adjustments and Re-calculation**: You can adjust input values and re-calculate as needed to see how changes affect the transportation costs and allocations.

This tool is designed for logistics professionals, supply chain analysts, and anyone involved in distribution and logistics planning, helping to make informed decisions about resource allocation and cost minimization.
