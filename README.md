<h2>DOCUMENTATION OF CAR PRICE PREDICTION
</h2>

<ul>
    THERE ARE STEP BY STEP PROCESS
    <li type="bullet">CHANGE UNSTRUCTURED TO STRUCURED DATA
        Unstructured data</li>
    <li>Imported the necessary library such as( pandas,numpy,..etc)
    </li>
    <li>Imported excel files which are given and read the each files
        The unstructured data is given of dictionary format
    </li>
</ul>


Eg: {'it': 0, 'ft': 'Petrol', 'bt': 'Hatchback', 'km': '1,20,000', 'transmission': 'Manual', 'ownerNo': 3, 'owner': '3rd
Owner', 'oem': 'Maruti', 'model': 'Maruti Celerio', 'modelYear': 2015, 'centralVariantId': 3979, 'variantName': 'VXI',
'price': '₹ 4 Lakh', 'priceActual': '', 'priceSaving': '', 'priceFixedText': None, 'trendingText': {'imgUrl':
'https://stimg.cardekho.com/used-cars/common/icons/trending.svg', 'heading': 'Trending Car!', 'desc': 'High chances of
sale in next 6 days'}}


<ul>
    structured data


    <li>For extracting the data from unstructured data by using simple python code of control statement( loop)
    </li>
    <li>The file were looks like after extraction
    </li>
</ul>

Eg:
it,ft,bt,km,transmission,ownerNo,owner,oem,model,modelYear,centralVariantId,variantName,price,priceActual,priceSaving,priceFixedText,trendingText,
0,Petrol,Hatchback,"1,20,000",Manual,3,3rd Owner,Maruti,Maruti Celerio,2015,3979,VXI,₹ 4 Lakh,,,,"

<ul>
    <li>After the extraction converted all file(xlsx to csv) for file handling
    </li>
    <li>Imported the all csv files for analysis and files were concated
    </li>
</ul>

<h2>DATA-PREPROCESSING
</h2>
<h4>Handling nan values:</h4>
<li> Removed the above 50% of nan values in the dataset </li>
<li> Filling nan values on each columns using (mean , mode) </li>
<li> After completed these columns should be presented the 100% percentage non nan- value </li>
<h4>Standardising Data:</h4>
<li> data point has string formats like 70 kms, then remove the unit ‘kms’ and change the data type from string to
    integers
    for understanding the machine </li>


<h4>Encoding the data:
</h4>


<li>Encode the each every column which are the datatype is object to numerical by using (label encoder and
    one-hot-encoded)

    <h4>Data visualization:</h4>
<li> Descriptive statistic were done first in the visualization process</li>
<li> Import the necessary library for visualization (matplotlib , seaborn)</li>
<li> Identify the distribution of each column and visualiszed</li>
<li> Finding the outliers for this distribution and removed by using(z-score)</li>
<li> Visualiszed the columns after the change in distribution using (boxplot)</li>
<li> For feature selection correlation were done in visualization by using (heatmap)</li>
<h4>Normalization:</h4>
<li> Find the final distribution of dataset and normalizing the columns using (Min-Max Scaling)</li>


<h4>MODEL BUILDING
</h4>

<li> Import the necessary library for model build(train-test-spilt, linear regression ,random forest regressor)</li>
<li> Train the model with spilt ratio of 80-20</li>
<li> Trained with linear regression but the performance of very low</li>
<li> For better performance used another method of randan forest regressor. In this method is more efficient then linear
</li>
<h4>regression</h4>
<li> Given the user input of given trained columns</li>
