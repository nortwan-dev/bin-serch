# ∧_∧ Twin Bunny Predictors: Interactive Binary Search Game

A lightweight, highly optimized interactive terminal game written in Python. The script utilizes the **Binary Search** algorithm to guess a hidden number chosen by the user within a custom range (up to 1,000,000,000). 

Before starting, the program mathematically predicts the maximum number of attempts required using logarithmic complexity.

---

## ⚡ Technical Highlights & Optimization

* **$O(1)$ Memory Complexity:** Unlike naive implementations that generate massive arrays using `list(range())` or loops, this version works entirely on pure mathematical boundaries (`low` and `high` variables). It allocates **zero extra RAM**, allowing it to handle ranges up to billions seamlessly without triggers like Out of Memory (OOM) errors.
* **Logarithmic Time Complexity (O(log n)):** The game guarantees finding the target within the exact mathematical limit calculated via $\lceil\log_2(\text{count})\rceil$.
* **Robust Input Validation:** Built-in safeguards handle deceptive user behavior (e.g., inputting `y` when the guess is mathematically incorrect) and invalid inputs without breaking the search loop.

---

## 🎮 Preview

```text
 ∧_∧   ∧_∧
( ◍’꒳’ ))`ᵕ’◍) ~♡  < [AI Predictors]
/     づ⊂    ヽ

Hi! Enter count of numbers (max count 1000000000 numbers):
> 1000000
Enter a number (1-1000000), and we will guess it.
> 42

We are analyzing the parameters...
[AI]: Easy! We will guess your number in 20 attempts at most.
Starting binary search...

---

# 🚀 How to Run
1.Clone this repository or download the script.

2.Ensure you have Python 3 installed.

3.Run the script via your terminal:
