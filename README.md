# Discrete Mathematics: Railway Network Analyzer

This project is a final assignment for the Discrete Mathematics course at Iran University of Science and Technology. It provides a graphical user interface (GUI) to solve two fundamental graph theory problems related to a network of train stations:
1.  **Finding the minimum number of stations** from a source to all other stations.
2.  **Calculating the shortest path** between a source and a destination station.

The application is developed in Python and uses PyQt for the user interface.


## Features

-   **Minimum Station Count**: Implements an algorithm to find the fewest number of stations required to travel from a designated starting point to all other reachable stations. If a station is unreachable, it is marked accordingly.
-   **Shortest Path Finder**: Utilizes a shortest path algorithm to determine the minimum travel distance between two specified stations and displays the optimal route.
-   **User-Friendly Interface**: A simple GUI built with PyQt allows users to paste input data, view results, and switch between light and dark themes.
-   [cite_start]**Focus on Correctness**: The implementation prioritizes providing the correct solution, as per the project requirements, without a focus on computational efficiency[cite: 16].

## Built With

-   **Python**
-   [cite_start]**PyQt/Qt** for the graphical user interface [cite: 15]

## Installation

1.  Clone the repository to your local machine:
    ```bash
    git clone <your-repository-url>
    ```
2.  Navigate to the project directory:
    ```bash
    cd <project-directory>
    ```
3.  Install the required dependencies:
    ```bash
    pip install PyQt5
    ```

## Usage

1.  Run the main application file from your terminal:
    ```bash
    python main.py
    ```
2.  Select the desired problem (Q1 for minimum stations or Q2 for shortest path).
3.  Paste the input data into the "input" text area.
4.  Click the **Submit** button to see the result in the "output" area.

### [cite_start]Sample Input: Minimum Stations (Q1) [cite: 33]
4 2
Shiraz
Tehran
Isfahan
Mashhad
Shiraz Tehran
Mashhad Isfahan
Mashhad
### [cite_start]Sample Input: Shortest Path (Q2) [cite: 74]
5 4
A
B
C
D
E
E C 136.81
D B 12.74
C B 14.63
B A 60.48
A D 45.63
A
C
## Project Rules & Guidelines

-   [cite_start]The use of C++ and Python is permitted[cite: 15].
-   [cite_start]Any method for graph implementation is acceptable[cite: 19].
-   [cite_start]The "Optimal" algorithm is not required[cite: 17].
-   [cite_start]Code similarity between students is strictly prohibited and will be considered cheating[cite: 14].