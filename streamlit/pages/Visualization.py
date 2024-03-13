import streamlit as st

st.set_page_config(
    page_title="Visualization",
    page_icon="🧊",
    layout="wide"
)

st.markdown("""<style>
            h1 {
              display: flex;
              justify-content: center;
              margin-left: auto;
              margin-right: auto; 
              text-align: center;
            }
            </style>
            """, unsafe_allow_html=True)

tab1, tab2, tab3, tab4 = st.tabs(["Distribution", "Correlation", "Learning From Correlations", "Model Training"])

with tab1:
  tab1.title("Distributions")

  col1, col2 = st.columns(2)
  col1.markdown("""
  **All features of the dataset:**
                
  As we can see, the distribution of distance travelled by vehicle is very skewed, with 75% of the data lying beneath 3000 km pr month, with quite a few outliers being outragerously above the median. This might still be an accurate representation though, since some individuals just might travel that much. 
  We'll keep it for the variance of the data.
  """)

  col1.image("./graphs/outliers.png")

  col2.markdown("""
  **Features of the dataset with a correlation higher than 0.1:**
                
  The carbon emissions, which is our target value follows a skewed normal distribution, which might be useful for model training.
  The rest of the features are either categorical, or does not follow a similar pattern, and might need to be transformed for better model performance.
  """)
  col2.image("./graphs/distributions.png")
  
  st.text("")

  st.markdown(
  """
  #### From the frequency distribution we can see that there are no significant differences between Male and Female, almost a 50/50 split.
  """
  )

  st.image("./graphs/frequency_sex.png")

  st.text("")
  st.markdown(
      """
      #### In the sample data, the majority of people dont own a car (around 60% ), and more then 33% travel by bike/walk. 
      """
  )  

  col1, col2 = st.columns(2)

  col1.image("./graphs/frequency_vehicletype.png")
  col2.image("./graphs/frequency_transport.png")

with tab2:
  tab2.title("Correlation Analysis")
  st.markdown(
      """
      Heatmap of the correlation between the different lifestyle factors and the total carbon emissions.
      This helps us to assess the strength of the relationship between the different factors and the carbon emissions. We can use this information to discover important
      factors for further research and analysis.
      """
  )
  st.image("./graphs/heatmap.png")

  st.markdown(
      """
      ## Gender Differences
      Correlation differences males and females seems to be about the same:
      """
  )

  col1, col2 = st.columns(2)

  col1.markdown(
      """
      ## Male
      """
  )
  col1.image("./graphs/male_correlation.png")

  col2.markdown(
      """
      ## Female
      """
  )
  col2.image("./graphs/female_correlation.png")

  st.markdown(
      """
      From the correlation matrix, we can see that one of the most important factors for carbon emissions is the vehicle monthly distance km.
      This is also supported by the scatter plot below, where we can see a clear positive correlation between the vehicle monthly distance km and the carbon emissions.
      """
  )
  st.image("./graphs/scatter_vehicle_monthly_distance_km_vs_carbon_emission.png")

  st.markdown("""
  Other high correlation factors:
              
      - Vehicle Type (0.5)
              
      - Transport (0.4)
              
      - Frequency of Traveling by Air (0.3)
              
  Lesser correlating factors:
      
      - Waste bag weekyl count (0.2)
              
      - How many new clothes a month (0.2)
              
  Since vehicle type, Transport method and monthly distance are naturally highly correlated, we will focus primarily on the vehicle monthly distance km among these 3.
  """)

  st.markdown("""
  ## Internet Usage
              
  The correlation between internet usage and carbon emissions is very low at 0.1, and the histogram below shows no clear correlation between the two.
  """)
  st.image("./graphs/CarbonEmissionVsHowLongInternetDailyHour.png")

with tab3:
  tab3.title("Learning from correlations")         

  col1, col2 = st.columns(2)
  st.markdown(
      """
      ## Air travel Frequency
      """
  )
  col1, col2 = st.columns(2)
  col1.markdown(
      """
      Frequency of traveling by air, with nearly all 4 categories having a similar frequency (25% ish).
      Theres a small majority of people flying very frequently, and a small minority of people flying rarely.
      """
  )
  col1.image("./graphs/frequency_of_traveling_by_air.png")


  col2.markdown(
      """
      ##
      ##
      Mean carbon emissions for people who identify with each category of frequency of traveling by air.
      """)
  col2.image("./graphs/frequency_of_traveling_by_air_mean.png")

  col1, col2 = st.columns(2)

  st.markdown("""
                
  **The mean and total sum of carbon emissions for each flight frequence category**
                
  <div>
  <style scoped>
      .dataframe tbody tr th:only-of-type {
          vertical-align: middle;
      }

      .dataframe tbody tr th {
          vertical-align: top;
      }

      .dataframe thead th {
          text-align: right;
      }
  </style>
  <table border="1" class="dataframe">
    <thead>
      <tr style="text-align: right;">
        <th></th>
        <th>Frequency of Traveling by Air</th>
        <th>mean</th>
        <th>sum</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th>0</th>
        <td>frequently</td>
        <td>2362.866482</td>
        <td>5963875</td>
      </tr>
      <tr>
        <th>1</th>
        <td>never</td>
        <td>1716.337129</td>
        <td>4220473</td>
      </tr>
      <tr>
        <th>2</th>
        <td>rarely</td>
        <td>1945.872830</td>
        <td>4819927</td>
      </tr>
      <tr>
        <th>3</th>
        <td>very frequently</td>
        <td>3026.455906</td>
        <td>7687198</td>
      </tr>
    </tbody>
  </table>
  </div>
  """, unsafe_allow_html=True)

  st.text("")

  st.markdown("""
  The carbon emissions are around 25% higher on average, for people who fly very frequently, compared to the mean across all categories. 
  """)

  st.text("")

  st.markdown("""
  ## Declared Energy Efficiency
              
  We can see that people thah categorize themselves as energy efficient, generally tend to have a little bit lower carbon emission in total, but the difference really is only about 1,5% lower than the 'No' category.

  The total sum of carbon emissions seems to be higher by people declaring that they're being energy efficient,
  indicating that a lot more people think they are being efficient than not, while not really making any difference in the emitted carbon dioxide!
  """)

  col1, col2 = st.columns(2)

  col1.image("./graphs/mean_energy_effi.png")
  col2.image("./graphs/sum_energy_effi.png")



with tab4:
  tab4.title("Model Training")
  st.markdown(
      """
      ## Predicton And Model Training:

      We have used machnie learning models to try to predict the carbon emissions based on the different lifestyle factors.

      We have applied 8 different machine learning models to the data to see which one performs the best,
      including classification, regression, clustering and ANN models.
      """
  )

  st.markdown(
      """
  ### Regression Models:

  Data was scaled using a StandardScaler, and the models was trained using a 80/20 train/test split.

  The XGBoost model looks to have the best accuracy, with a score of 0.9747 on the test set, with only a MAE of 123.98.

      
  Regression results:
  <div>
  <style scoped>
      .dataframe tbody tr th:only-of-type {
          vertical-align: middle;
      }

      .dataframe tbody tr th {
          vertical-align: top;
      }

      .dataframe thead th {
          text-align: right;
      }
  </style>
  <table border="1" class="dataframe">
    <thead>
      <tr style="text-align: right;">
        <th></th>
        <th>ML models</th>
        <th>r2</th>
        <th>MAE</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <th>0</th>
        <td>XGBRegressor</td>
        <td>0.974770</td>
        <td>123.986466</td>
      </tr>
      <tr>
        <th>1</th>
        <td>LinearRegression</td>
        <td>0.605501</td>
        <td>524.908445</td>
      </tr>
      <tr>
        <th>2</th>
        <td>SVR</td>
        <td>0.105251</td>
        <td>725.583154</td>
      </tr>
    </tbody>
  </table>
  </div><br>
      """
  , unsafe_allow_html=True)

  st.image("./graphs/XGB.png")

  st.markdown("""
  ### Artificial Neural Network:

  We used a Sequential ANN model from the Keras library.
  We experimented with different layers and nodes, and the model was trained using a 80/20 train/test split.
  """)

  st.markdown("""
  #### Results
              
  The results show that the accuracy of the model increases with the number of layers and neurons.
  We can see that the accuracy of the model is 0.9819 with 4 layers (256, 512, 512, 512 neurons) The test loss is 109.2275 and the mean absolute error is 75.5905.
  This is the best result we have achieved with the neural network.
  We can also conclude that the neural network has better results the our XGBoost model, that 'only' got an accuracy of 0.9747 and a MAE of 123.9864.

  An overview of the different ANN models and their performance:

  __[x1,... xn] means the numbers of neurons for each layer in the network__

  <table><tr>
  <td>

  |Layers                      | Epochs | Accuracy | Test Loss | MAE     |
  |----------------------------| -------| -------- | ----------| --------|
  |1 lay [32]                  | 50     | 0.6514   | 485.4101  | 488.3452|
  |1 lay [64]                  | 50     | 0.6794   | 458.6350  | 457.2778|
  |1 lay [128]                 | 50     | 0.7634   | 360.0965  | 358.2312|
  |1 lay [256]                 | 50     | 0.8073   | 314.0002  | 303.8010|
  |1 lay [512]                 | 50     | 0.8387   | 277.7811  | 267.3893|


  </td><td>

  |Layers                      | Epochs | Accuracy | Test Loss | MAE     |
  |----------------------------| -------| -------- | ----------| --------|
  |2 lay [32, 64]              | 50     | 0.8260   | 305.7189  | 287.4525|
  |2 lay [64, 128]             | 50     | 0.8519   | 280.6377  | 259.1389|
  |2 lay [128, 256]            | 50     | 0.9222   | 195.7561  | 177.1057|
  |2 lay [256, 512]            | 50     | 0.9588   | 154.8777  | 133.3263|

  </td></tr>

  <tr>
  <td>

  |Layers                      | Epochs | Accuracy | Test Loss | MAE     |
  |----------------------------| -------| -------- | ----------| --------|
  |3 lay [32, 64, 128]         | 50     | 0.8919   | 219.7377  | 210.3670|
  |3 lay [64, 128, 256]        | 50     | 0.9469   | 167.5058  | 152.9221|
  |3 lay [128, 256, 512]       | 50     | 0.9755   | 126.4031  | 104.1510|
  |3 lay [256, 512, 512]       | 50     | 0.9800   | 115.4065  | 81.7558 |

  </td><td>

  |Layers                      | Epochs | Accuracy | Test Loss | MAE     |
  |----------------------------| -------| -------- | ----------| --------|
  |4 lay [32, 64, 128, 256]    | 50     | 0.9787   | 117.9240  | 108.2563|
  |4 lay [64, 128, 256, 512]   | 50     | 0.9792   | 117.7210  | 94.6650 |
  |4 lay [128, 256, 512, 512]  | 50     | 0.9713   | 134.8475  | 80.8660 |
  |4 lay [256, 512, 512, 512]  | 50     | 0.9819   | 109.2275  | 75.5905 |

  </td></tr></table><br>
  """, unsafe_allow_html=True)

  st.markdown("""
  ## Alternative Models

  We used a clustering model to see if we could find any patterns in the data, but the results were not very promising.
  The data seems to be too complex to be clustered into any clear groups.
              
  We also used a classification model to see if we could predict the different categories of carbon emissions, but the model was not very suited
  for this purpose, and are mostly for demonstrative puposes.
  """)

  st.markdown("""
  ### Clustering Model:

  We tried different methods to indentify clusters in the data, for example using dendograms an elbow method to find the optimal number of clusters.
  The results were not very promising, and we could not find any clear clusters in the data.
  We tried to do a PCA to reduce the dimensionality of the data, but this did not help to give any clear information either.
              

  """)
  st.image("./graphs/dendrogram_hierarchical-clustering.png")
  st.image("./graphs/3d_cluster.png")

  st.markdown("""
  ## Classification
              
  For demonstrative purposes, we tried to train different classification models without much success.
  We normalized the data to a gaussian distribution, with the mean at 0.
              
              
  Then the target feature got binned into 4 categories, divided by the quartiles of the data.
  The most succesful classification model, was a Random Forest Classifier with n_estimators at 300 and max depth at 13 layers.
              
  The model was not very useful, since while it got a decent accuracy at 67%, the predictions it made did not have much informational value,
  since the categorizations of the data made the targets vague.
              
  This is the result of the model testing:

                precision    recall  f1-score   support

                  0       0.74      0.79      0.77       356
                  1       0.63      0.53      0.58       395
                  2       0.59      0.57      0.58       367
                  3       0.71      0.80      0.75       382
          accuracy                           0.67      1500
          macro avg       0.67      0.68      0.67      1500
      weighted avg       0.67      0.67      0.67      1500
  """)

st.markdown(
"""
    ## Conclusion


In conclusion of our research, we can say it is definetely possible to predict carbon emissions from lifestyle factors.
We found correlating features which has a big impact on the carbon output, transport choices being among the top.
We have created a simple frontend application with streamlit, where a user can get predictions from our models, by inputting their own lifestyle factors

- **H0**
This hypothesis is definetely false, since there is clear correlation between lifestyle factors and carbon emissions

- **H1**
We can conclude that given the same formatted inputs, we can train regression and ANN models to predict an individuals carbon emissions
with a model accuracy of around 97% to 98%

- **H2**
According to our discoveries, the most significant factor
for individual carbon emissions is style of transport (i. e public or private vehicles) and how many kilometers driven in a private vehicle a month. 

- **H3**
Out of all the factors we have available in our data, many of the factors had very little correlation to the total carbon emission output, and a few had a little correlation, and even fewer had a strong correlation.
This gives insight in how the different factors weigh more or less in the total output of carbon emissions, which might be useful for interested parts

- **H4**
We have used 10000 entries of synthetically generated data from research papers, and we have used standard recognized methods of data-analysis for our models, which gives us accuracy of around 97% for predictions. We believe our conclusions accurately represents reality.

- **H5**
We have found a small correlation of daily internet usage, with total carbon output, but we have been unable to find any clear tendency between people who spend a lot of time on the internet, and people who emit a lot of carbon. We therefore conclude, that theres no significant impact from this factor.

"""
)