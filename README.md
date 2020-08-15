# Using NLP to build auto correction words engine
<div style="width:image width px; font-size:100%; text-align:center;"><img src='auto-correct.png' alt="alternate text" width="width" height="height" style="width:300px;height:250px;" /> Figure 1 </div>

Data source :
- Text based on https://norvig.com/big.txt
- https://norvig.com/spell-correct.html as reference for this project

The goal of this spell check model is to compute the following probability: $$P(c|w) = \frac{P(w|c)\times P(c)}{P(w)}$$ (known as Bayes rule)