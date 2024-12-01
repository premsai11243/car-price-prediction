                                  **DOCUMENTATION OF CAR PRICE PREDICTION**
                                   **THERE  ARE  STEP BY STEP PROCESS**
<h2>CHANGE UNSTRUCTURED TO STRUCURED DATA</h2>	
**Unstructured data**
	Imported the necessary library such as( pandas,numpy,..etc)
	Imported excel files which are given and read the each files 
The unstructured data is given of dictionary format

Eg: {'it': 0, 'ft': 'Petrol', 'bt': 'Hatchback', 'km': '1,20,000', 'transmission': 'Manual', 'ownerNo': 3, 'owner': '3rd Owner', 'oem': 'Maruti', 'model': 'Maruti Celerio', 'modelYear': 2015, 'centralVariantId': 3979, 'variantName': 'VXI', 'price': '₹ 4 Lakh', 'priceActual': '', 'priceSaving': '', 'priceFixedText': None, 'trendingText': {'imgUrl': 'https://stimg.cardekho.com/used-cars/common/icons/trending.svg', 'heading': 'Trending Car!', 'desc': 'High chances of sale in next 6 days'}}

**structured data**
	For extracting the data from unstructured data by using simple python code of control statement( loop)
	The file were looks like after extraction
Eg: it,ft,bt,km,transmission,ownerNo,owner,oem,model,modelYear,centralVariantId,variantName,price,priceActual,priceSaving,priceFixedText,trendingText, 
0,Petrol,Hatchback,"1,20,000",Manual,3,3rd Owner,Maruti,Maruti Celerio,2015,3979,VXI,₹ 4 Lakh,,,," 

	After the extraction converted all file(xlsx to csv) for file handling
	Imported the all csv files for analysis and files were concated  

**DATA-PREPROCESSING**

**Handling nan values**:
•	Removed the above 50% of nan values in the dataset
•	Filling nan values on each columns using (mean , mode)
•	After completed these columns should be presented the 100% percentage non nan- value  
       Standardising Data:
•	data point has string formats like 70 kms, then remove the unit ‘kms’ and change the data type from string to integers for understanding the machine 
        

**Encoding the data:**

•	Encode the each every column which are the datatype is object to numerical by using     (label encoder and one-hot-encoded)

**Data visualization:**

•	Descriptive statistic were done first in the visualization process
•	Import the necessary library for visualization (matplotlib , seaborn)
•	Identify the distribution of each column and visualiszed
•	Finding the outliers for this distribution and removed by using(z-score)
•	Visualiszed the columns after the change in distribution using (boxplot)
•	For feature selection correlation were done in visualization by using (heatmap)
**Normalization:**

•	Find the final distribution of dataset and normalizing the columns using (Min-Max Scaling)

**MODEL BUILDING**

•	Import the necessary  library  for  model build(train-test-spilt, linear regression ,random forest regressor)
•	Train the model with spilt ratio of 80-20
•	Trained with linear regression but the performance of very low 
•	For better performance used another method of randan forest regressor. In this method is more efficient then linear regression
•	Given the user input of given trained columns

**DEPLOYMENT METHOD:**

