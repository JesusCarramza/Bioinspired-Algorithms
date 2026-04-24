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

### [02_Genetic_Programming](./02_Genetic_Programming)
**Practice 2: Symbolic Regression (GPLearn & DEAP)**
* **Description:** Implementation of Symbolic Regression using the GPLearn and DEAP libraries. The practice involves implementing standard examples and modifying the DEAP algorithm to approximate a specific 2-variable mathematical function.
* **Key Concepts:** Genetic Programming, Symbolic Regression, GPLearn, DEAP framework.
* **Documentation:** [Read the practice instructions here](./02_Genetic_Programming/Practice_2.md).

### [03_Particle_Swarm_Optimization](./03_Particle_Swarm_Optimization)
**Practice 3: Particle Swarm Optimization (PSO) - Global Topology**
* **Description:** Minimization of a 2D mathematical function using Particle Swarm Optimization. The implementation uses a global topology, tracking the position, velocity, personal best (pbest), and global best (gbest) for a swarm of 20 particles over 50 iterations.
* **Key Concepts:** Particle Swarm Optimization, Global Topology, Swarm Intelligence, Inertia weight, Cognitive and Social learning factors.
* **Documentation:** [Read the practice instructions here](./03_Particle_Swarm_Optimization/Practice_3.md).

### [4_Ant_Colony_Optimization](./4_Ant_Colony_Optimization)
**Practice 4: Ant Colony Optimization (ACO)**
* **Description:** Implementation of the Ant Colony Optimization algorithm to find optimal paths. It involves calculating transition probabilities based on heuristic information and pheromone trails, as well as applying pheromone update rules (evaporation and deposit) after each iteration.
* **Key Concepts:** Ant Colony Optimization, Swarm Intelligence, Pheromone Update, Transition Probability.
* **Documentation:** [Read the practice instructions here](./4_Ant_Colony_Optimization/Practice_4.md).



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