## **FoodieFinders**
> Content-based Restaurants Recommender System using Cosine Similarities.

<center>
    <img src="https://cdn.vox-cdn.com/thumbor/jEOXUWBAr8tQzmXf0ZF1ma66Z0g=/0x432:5174x3019/fit-in/1200x600/cdn.vox-cdn.com/uploads/chorus_asset/file/20100019/shutterstock_1497472160.jpg" width="600" alt="cognitiveclass.ai logo" />
</center>

**Introduction**

The project is a Content-based Restaurant Recommender System using Cosine Similarities. It aims to provide restaurant recommendations to users based on the similarity calculation among restaurants. The similarity is measured based on the content or features of the restaurants, such as their types of cuisine, location (state and city), and average reviews. The objective is to help users discover new restaurants that match their preferences and location.

**Dataset**

The dataset was scraped from the TripAdvisor website and contains restaurant data across 20 cities in Washington, Texas, New York, New Jersey, and California. It includes information such as the restaurant's name, street address, location, type of cuisine served, average rating, number of reviews, comments, contact number, TripAdvisor restaurant URL, menu URL, and price range.

Data Source: https://www.kaggle.com/datasets/siddharthmandgi/tripadvisor-restaurant-recommendation-data-usa

**Workflow**

1. **Preliminary Wrangling:** The data is assessed and cleaned to ensure proper data types, remove irrelevant columns, and handle missing values. The reviews and number of reviews columns are converted to float and int, respectively. The TripAdvisor URL, menu, and price range columns are dropped, and missing rows in the type column are removed. The state and city are extracted from the location, and latitude and longitude are obtained using the OpenStreetMap API.

2. **Build Recommendation System:** The content-based recommender system is constructed using cosine similarities. The restaurant features, such as cuisine types, state, and city, are one-hot encoded. A similarity matrix is generated using cosine similarity, capturing the similarity between each pair of restaurants.

3. **Test Recommendation System:** The system is tested to recommend restaurants based on a given restaurant's name, state, and city. The top similar restaurants are recommended to the user.

**Results**

The content-based recommender system successfully provides restaurant recommendations based on the user's preferences and location. It offers a way for users to discover new restaurants that match their tastes and are located in their desired state and city.

**Deployment Site**
https://davidsonity-restaurants-recommendation-system-app-wqpses.streamlitapp.com/

**Implementation**

The project is implemented using Python and leverages various libraries such as pandas, NumPy, requests, BeautifulSoup, and Folium for visualization. The code follows the standard data preprocessing, similarity matrix generation, and recommendation steps.

**Repository Structure**
The repository structure includes the following files and directories:
```
├── LICENSE
├── clean_data.csv
├── TripAdvisor_RestauarantRecommendation.csv
├── Procfile
├── README.md
├── app.py
├── notebook.ipynb
├── requirements.txt
└── setup.sh
```
- `LICENSE`: File containing the license information for your project.
- `clean_data.csv`: The preprocessed and cleaned dataset after data wrangling.
- `TripAdvisor_RestauarantRecommendation.csv`: The raw dataset containing restaurant information.
- `Procfile`: File specifying the commands to run your application in a hosting environment, such as Heroku.
- `README.md`: Markdown file with project documentation, instructions, or other relevant information.
- `app.py`: Python file containing the main code for deployment.
- `notebook.ipynb`: Jupyter notebook file for exploratory analysis and experiments.
- `requirements.txt`: File listing the required Python libraries and their versions.
- `setup.sh`: Shell script for setting up the project environment or executing necessary setup commands.

**Conclusion**

The TripAdvisor Restaurant Recommendation project successfully builds a content-based recommender system to help users discover new restaurants based on their preferences and location. By leveraging cosine similarities and restaurant features, the system provides relevant and personalized recommendations to users. The project's implementation and results make it a valuable tool for individuals looking for restaurant suggestions in various locations in the USA.
