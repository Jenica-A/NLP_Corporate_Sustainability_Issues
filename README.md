## Using Natural Language Processing Techniques to Understand Corporate Sustainability Issues
### Unsupervised NLP Project Write-Up

by Jenica Andersen

June 13, 2022


**Abstract**
Corporate sustainability practices have increasingly become an important focus of enterprises as they aim to stabilize and grow their bottom line amid an ever-changing, significantly interconnected global economy. According to the [Harvard Business Review](https://hbr.org/2016/10/the-comprehensive-business-case-for-sustainability), "Embedded sustainability efforts clearly result in a positive impact on business performance." They drive a competitive advantage through stakeholder engagement, improve risk management, foster innovation, improve financial performance, increase customer loyalty, and attract and engage employees. Companies wishing to be viewed as adopters of beneficial sustainability practices publish public sustainability reports. Sometimes lengthy reports espouse aggressive policies, but come with little follow-through. In other instances, stakeholders call on leaders to simply take tougher action. Ceres.org is an organization that tracks the sustainability reporting of companies and gathers shareholder resolutions filed by investment network members. These resolutions are part of broader investor efforts to encourage companies to address the full scope of environmental, social and governance (ESG) issues. 

In this project, I used Natural Language Processing techniques to model the major topics and terms within a corpus of 923 shareholder resolution documents. I found that the top occuring topics in the corpus of resolutions includes:
    '1. Climate emissions targets', 
    '2. Activism/Lobbying', 
    '3. Female Wage Disparity',
    '4. Campaign Contributions', 
    '5. ESG management and corporate policies', 
    '6. Plastic Polution and the Ocean',
    '7. human rights impact assessments',
Results of this project will benefit consultants, companies, investors or activists who wish to understand the current state of sustainability practices and wish to learn from and apply the best practices to their own operations.

#### **Design:**
This project is modeled after a paper in the journal *Sustainability* by [Raghupathi, V. et. al (2020)](https://www.mdpi.com/2071-1050/12/11/4753), and largely follows a generally similar NLP path, but this project specifically aimed to answer these key questions of interest:
- What topics (in what frequency) occur in shareholder sustainability resolutions? 
- Do proposed resolutions have positive, negative or neutral sentiment scores? 
- If there is a variety of sentiments, What topics are associated with each sentiment type? 

To do this, I obtained the data from ceres.org, removed a standard list of english stop words as well as a handful of custom words that occured in high enough frequency that they did not conntribute to results in any significant manner, but were still infrequent enough to not be culled by max_df 0.99 removal. I also removed special characters, and stemmed the words in the documents relying on the most aggressive stemmer (Porter), but loosely comparing the other stemmers, Lancaster and SnowBall for significant differences in results. Once the documents were processed, a document term matrix was created for uni-gram, bi-gram, and tri-gram analysis. Non-negative matrix factorization was then applied to determine the top topics. Raghupathi et al used seven topics for their research, and this project found via trial and error this was a suitable number of topics. Having a higher number of topics resulted in overlap between topics, but it did produce less frequent but novel topics results as well. This project aslo analyzed the sentiment of the entire corpus using Vader sentiment analyzer. 

#### **Data Description:**
Ceres.org hosts an ["Engagement Tracker" database](https://engagements.ceres.org/?_ga=2.198336172.281927745.1653500401-1839935729.1653500401) that contains 2,860 resolution entries, dating from 2009 to 2022. I attempted to but was not successful at scraping the database using python selenium. I manually gathered 923 documents, which contained about 410,000 words.

#### **Algorithms/Tools**
Algorithms used include, Regex removal of special characters and punctuation, removal of stopwords via lambda function and countvectorizor, stemming using Porter, Lancaster, and Snowball for comparison (porter went with), clustering and dimensionality reduction using non-negative matrix factorization and vader sentiment analysis. I used matplotlib and wordcloud to create visualizations.

#### **Communnications**
In addition to the slides and visuals presented, my code for this project is posted on github.


#### **References:**
Raghupathi, V.; Ren, J.; Raghupathi, W. Identifying Corporate Sustainability Issues by Analyzing Shareholder Resolutions: A Machine-Learning Text Analytics Approach. Sustainability 2020, 12, 4753. https://doi.org/10.3390/su12114753




