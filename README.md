# Academic-Data-Drift-amp-Copy-Behaviour-Analyzer
Project Description
The project is a simulated database that contains academic information about a university. This database will be used to compare the effects of various types of copies (Shallow Copy & Deep Copy) on data integrity.

Objective
* Randomly generate student details
* Store data in nested dictionaries
* Conversion of data to Pandas DataFrame
* Statistical analysis by NumPy
* Mathematical operations by math library
* Comparison between Shallow Copy & Deep Copy
* Data drift analysis
* Determine if the system is stable
  
Data Structure

A single piece of data looks like this:
python
{
    "id": integer,
    "marks": integer,
    "attendance": integer,
    "scores": [internal, assignment]
}

Tools
* Python
* NumPy
* Pandas
* random module
* math module
* copy module

Workflow
1.Data generation
Random generation of 10-15 student details

2. Copy creation
Creates
* Shallow Copy
* Deep Copy

3. Data mutation
Mutation happens only on copy:
* Marks will be updated as per:
  `marks = marks + sqrt(marks)`
* Reduction in attendance
* Scores will be updated

4. Analysis
* Mean, Median, Standard Deviation (NumPy)
* Mean Calculated Manually
* Data Normalization
* Detecting Drift:
  `drift = abs(original_mean - modified_mean)`

5. Classification
Classification based on drift value and consistency of data:

* Stable Data
* Minor Drift in Data
* Critical Drift in Data
* Failure in Copying of Data
  
Personalization Logic
Roll number is: **2**
Rule: Mutation is done on those values which are divisible by `(roll_no % 3)`
So mutation will be performed on values whose index is:

  Indices → 0, 2, 4, 6, ...

Important Concept - Shallow vs. Deep Copy
Shallow Copy
* Only outer structure is copied
* Inner structures are shared
* Modifying inner structures affects the original data
* Results in **Copy Failure**
Deep Copy
* Independent copy created
* No reference sharing
* Safe from modification

Sample Output
Original DataFrame
Shallow Copy DataFrame
Deep Copy DataFrame
Drift
Tuple Output `(Mean, Drift, Standard deviation)`

Learning Outcomes
* Recognized the distinction between shallow copy and deep copy
* Learnt about the phenomenon of data drift in practical scenarios
* Received practical training in using NumPy and Pandas libraries
* Used mathematical operations in Python code
* Wrote modular code by using functions

How to Run
```bash
pip install numpy pandas
python your_file_name.py

Conclusion
In conclusion, the current assignment underscores the significance of data management practices. This is because the example presented here shows how data can be easily corrupted by shallow copy, but deep copy prevents such an occurrence.
