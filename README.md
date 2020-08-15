# Using NLP to build auto correction words engine
<div style="width:image width px; font-size:100%; text-align:center;"><img src='auto-correct.png' alt="alternate text" width="width" height="height" style="width:300px;height:250px;" /></div>

Data source :
- Text based on https://norvig.com/big.txt
- https://norvig.com/spell-correct.html as reference for this project
<br><br>
The goal of this spell check model is to compute the following probability: ![equation](http://www.sciweavers.org/tex2img.php?eq=P%28w%7Cc%29%3D%20%5Cfrac%7BP%28w%7Cc%29%2AP%28c%29%7D%7BP%28w%29%7D%20&bc=White&fc=Black&im=jpg&fs=12&ff=arev&edit=0) (known as Bayes rule)
