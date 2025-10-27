# Boundary-Dominant Probability Optimization Models

This repository contains the Python source code, experimental simulations, and numerical verifications used in the paper titled **“Boundary-Dominant Optimization in Discrete Probabilistic Allocation Models”**.

The article mathematically and experimentally demonstrates why **internal optima remain saddle point in nature** and why **true optimal behavior emerges at the boundary conditions** in discrete probability models (e.g., ball-drawing problems from two bags).

---

## 📄 Article Information

**Article Title:** Boundary-Dominant Optimization: A Closed-Form Framework for Efficient Resource Allocation  
**Author:** Kaan Gökalp  
**Status:** Preprint available on *arXiv (coming soon)*  
**Field:** Applied Probability, Optimization Theory, Mathematical Modeling  

---

## 📁 Repository Structure
```bash
├── model1/
│ ├── model1_boundary_plots.py # Model 1: Boundary behavior simulations
│ ├── model1_results.png # Output plots for Model 1
│
├── model2/
│ ├── model2_limit_simulation.py # Model 2: Asymmetric case limit analysis
│ ├── model2_results.png
│
├── model3/
│ ├── model3_lagrange_solver.py # Model 3: Lagrange solution and heatmap
│ ├── model3_heatmap.png
│
├── supplementary/
│ ├── appendix_hessian_example.py # Appendix A: Tangent-space Hessian example
│ ├── appendix_gap_bound_check.py # Appendix C: Gap bound computation
├── Makale.pdf # Main article
├── Supplementary_Material.pdf # Additional proofs and derivations
└── requirements.txt # Python dependencies
```
## ⚙️ Running Instructions
Clone the repository:
```bash
git clone https://github.com/Kaan-Gokalp/BagProbability-Optimization-Models.git
cd BagProbability-Optimization-Models
  ```
Install the required dependencies:
```bash
pip install -r requirements.txt
```
Run a sample experiment:
```bash
python model3/model3_lagrange_solver.py
```
All graphs and outputs will be automatically saved to the /results/ folder.

## 🧪 Experimental Outputs
The code reproduces all figures presented in the paper:  
**Model 1**: Probability change along the boundary (monotonic analysis)  
**Model 2**: Limit histograms in asymmetric cases  
**Model 3**: Realization of the global optimum under AM–GM conditions (heatmap)  
**Supplementary Material**: Hessian signature analysis, gap bound verifications  

## 📘 Citation
If you use this work, please cite it as follows:  
```
Kaan Gökalp, Boundary-Dominant Optimization: A Closed-Form Framework for Efficient Resource Allocation, arXiv:xxxx.xxxxx (2025).
```
## 📜 License
MIT License © 2025 Kaan Gökalp  
The code is freely available for academic research and educational purposes only.

## 📧 Contact
For questions, comments, or contributions:  
📩 kaangokalp6@gmail.com
