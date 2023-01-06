

### Weighted_Transformation

---

#### 1. `Transform(T, n, s = 1/2, t=1/2, isometry = true)` : iterate n times for transformation.

- Parameters
    
    `T (numpy.Matrix)` : Matrix

    `n (int)` : Number of iteration

    `s (int)`  : Weight of `T` 
    
    `t (int)`  : Weight of `|T|U` 

    `isometry (bool)` : select U is isometry or not(unitary) 

 
#### 2. `Transfomation.Normal_calculator()` : Norm and Normality Calculation Function.

where norm is *Frobenius norm*(https://en.wikipedia.org/wiki/Matrix_norm#Frobenius_norm).

- `Transfomation.norm_info` : A list in which the norm of the Transformation is stored.
   
- `Transfomation.normal_info` : A list in which normal characteristic is stored.

---

#### 3.` Transformation.Process(k, digit = 4)` : You can check the calculation process of a specific part.
    
- Parameters

   `k (int)` : purpose number of repetitions 

    `digit (int)` : digit of output matrices 

- Return

    Yield process from `k-1` step to `k` step$

---

#### 4. `Transformation.Plot()` : plotting of normal characteristic.
   
- axis X : number of iteration(`n`)
   
- axis Y : normal characteristic for transformations.

---
*Min Woo Park : Graduate School of Data Science, Seoul National University* - alsdn0110@snu.ac.kr 

*Ji Eun Lee : Department of Mathematics and Statistics, Sejong university* - jieunlee@sejong.ac.kr


==========================================================================================


### General_Transformation

---

#### 1. `Transform(T, n, isometry = true)` : iterate n times for each transforms (Aluthge, Duggal and Mean).

- Parameters
    
    `T (numpy.Matrix)` : Matrix

    `n (int)` : Number of iteration

    `isometry (bool)` : select U is isometry or not(unitary) 


---

#### 2. `Transfomation.Normal_calculator()` : Norm and Normality Calculation Function.

where norm is *Frobenius norm*(https://en.wikipedia.org/wiki/Matrix_norm#Frobenius_norm).

- `Transfomation.norm_info` : A list in which the norm of the Transformation is stored.
   
- `Transfomation.normal_info` : A list in which normal characteristic is stored.

---

#### 3. `Transformation.Process(k,Type, digit = 4)` : You can check the calculation process of a specific part.
    
- Parameters
    
    `k (int)` : purpose number of repetitions ($1\leq k\leq n$)
    
    `Type (str)` : `"Aluthge"`, `"Duggal"` or `"Mean"`

    `digit (int)` : digit of output matrices 


- Return

    Yield process from `k-1` step to `k` step$

---

#### 4. ```Transformation.Plot()``` : plotting of normal characteristic.
   
   - axis X : number of iteration(`n`)
   
   - axis Y : normal characteristic for each transforms.

---

*Min Woo Park : Graduate School of Data Science, Seoul National University* - alsdn0110@snu.ac.kr 

*Ji Eun Lee : Department of Mathematics and Statistics, Sejong university* - jieunlee@sejong.ac.kr

==========================================================================================

Last Update : 2023-01-04








