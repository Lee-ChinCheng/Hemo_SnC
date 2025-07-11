# Hemo_SnC
Stands for "Hemolysis Prediction of Therapeutic Peptides Based on Sequence and Concentration"

Poster Topic: Early Screening of Hemolytic Risk in Functional Peptides via Ensemble AI Using Sequence and Concentration Features

### Main Goal 
Therapeutic Peptides or Antimicrobial peptides (AMPs) with high hemolysis risk are unsuitable as drugs, but experimental validation is costly. Our model enables early in silico screening to filter out hemolytic candidates.

<p align="center">
  <img src="./images/main_concept.png" alt="main_concept" width="688" height="286"/>
</p>

Our web-based AI predictor is accessible at https://axp.iis.sinica.edu.tw/hemolysis/

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

|           | Accuracy | Specificity | Precision | Recall | F1-score | MCC | auROC | auPRC |
|-----------|----------|-------------|-----------|--------|----------|-----|--------|--------|
| TestSet1  | 0.78     | 0.77        | 0.77      | 0.79   | 0.78     | 0.56| 0.86   | 0.85   |
| TestSet2  | 0.88     | 0.98        | 0.88      | 0.52   | 0.65     | 0.61| 0.89   | 0.69   |



TestSet2 comprises 18 peptides designed at 7 different concentrations and experimentally validated using sheep red blood cells.
<p align="center">
  <img src="./images/test2_flowchart.PNG" alt="test2_flowchart" width="900" height="243"/>
</p>
<p align="center">
  <img src="./images/sheepRBC.PNG" alt="sheepRBC" width="900" height="390"/>
</p>


- Concentration-dependent hemolysis risk profile<br>
The model predicted elevated hemolysis risk for the same peptides as concentration increased
<p align="center">
  <img src="./images/test2prediction.PNG" alt="test2_conc_trend" width="576" height="432"/>
</p>

