# Hemo_SnC
Stands for "Hemolysis Prediction of Therapeutic Peptides Based on Sequence and Concentration"

Poster Topic: Early Screening of Hemolytic Risk in Functional Peptides via Ensemble AI Using Sequence and Concentration Features

---

### Main Goal 
Therapeutic Peptides or Antimicrobial peptides (AMPs) with high hemolysis risk are unsuitable as drugs, but experimental validation is costly. Our model enables early in silico screening to filter out hemolytic candidates.

<p align="center">
  <img src="./images/main_concept.png" alt="main_concept" width="860" height="358"/>
</p>
---

### Model Architecture

- model1 (PC6 encoding + CNN)<br>
<p align="center">
  <img src="./images/model1.PNG" alt="model1_structure" width="254" height="301"/>
</p>

- model2 (PepBERT encoding + MLP)
<p align="center">
  <img src="./images/model2.PNG" alt="model2_structure" width="358" height="380"/>
</p>

### Test Set Evaluation
We have 2 test sets, TestSet1 (10% dataset) and TestSet2 (our wet-lab validated data)<br>
Our TestSet2 is confidential and is not currently available on GitHub


TestSet2 comprises 18 peptides designed at 7 different concentrations and experimentally validated using sheep red blood cells.
<p align="center">
  <img src="./images/test2_flowchart.PNG" alt="sheepRBC" width="1110" height="300"/>
</p>
<p align="center">
  <img src="./images/sheepRBC.PNG" alt="sheepRBC" width="1110" height="483"/>
</p>


- Concentration-dependent hemolysis risk profile<br>
The model predicted elevated hemolysis risk for the same peptides as concentration increased
<p align="center">
  <img src="./images/test2prediction.PNG" alt="test2_conc_trend" width="576" height="432"/>
</p>

