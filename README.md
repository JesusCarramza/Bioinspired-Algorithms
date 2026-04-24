# Bioinspired-Algorithms 🧬💻

Welcome to the **Bioinspired-Algorithms** repository. This project is a structured collection of artificial intelligence algorithms inspired by nature, biological evolution, and swarm behavior. 

The primary goal of this repository is to translate biological concepts into computational heuristics. By implementing these algorithms from scratch in Python, this project demonstrates the core mathematical and logical mechanics behind Evolutionary Computing, focusing on solving complex optimization and search problems.

> 🚧 **Work in Progress:** This repository is currently under active development. It is an ongoing academic and personal project that will be continuously updated with new practices, algorithms, and modules over the next 2 months.

## 🗂️ Repository Structure & Practices

Currently, the repository contains the following implementations:

### [01_Genetic_Algorithm](./01_Genetic_Algorithm)
**Practice 1: The Knapsack Problem (Weasleys' Wizard Wheezes)**
* **Description:** An implementation of a Genetic Algorithm to solve a constrained variation of the classic Knapsack Problem. The goal is to maximize the profit of items placed in a knapsack with a specific weight limit and mandatory inventory minimums.
* **Key Concepts:** Rejection sampling for initial population, Roulette Wheel Selection, Uniform Crossover, Uniform Mutation, and Generational Replacement with elitism.
* **Documentation:** [Read the full explanation here](./01_Genetic_Algorithm/README_Practice1.md).

*(More practices will be added here soon...)*



## 🚀 How to Run

**1. Clone the repository:**
```bash
git clone https://github.com/JesusCarramza/Bioinspired-Algorithms.git
```

**2. Create a Virtual Enviroment**
```bash
python -m venv my_virtual_enviorment
```

**3. Activate the Virtual Enviroment**
```bash
# Windows
my_virtual_enviorment\Scripts\activate

# Linux/Mac
source my_virtual_enviorment/bin/activate
```

**4. Install requirements**
```bash
pip install -r requirements.txt
```

**5. Navigate to the specific practice folder:**
```bash
cd 01_Genetic_Algorithm
```

**6. Execute the main script:**
```bash
python solution_practice_1.py
```