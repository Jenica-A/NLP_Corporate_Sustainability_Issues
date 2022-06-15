## Using Natural Language Processing Techniques to Understand Corporate Sustainability Issues
### Unsupervised NLP Project Proposal

by Jenica Andersen

May 27, 2022

Corporate sustainability practices have increasingly become an important focus of enterprises that aim to stabilize and grow their bottom line. According to the [Harvard Business Review](https://hbr.org/2016/10/the-comprehensive-business-case-for-sustainability), "Embedded sustainability efforts clearly result in a positive impact on business performance." They drive a competitive advantage through stakeholder engagement, improve risk management, foster innovation, improve financial performance, increase customer loyalty, and attract and engage employees.  

Companies wishing to be viewed as adopters of beneficial sustainability practices publish public sustainability reports. Sometimes lengthy reports espouse aggressive policies, but come with little follow-through. In other instances, stakeholders call on leaders to simply take tougher action. 

Ceres.org is an organization that tracks the sustainability reporting of companies and gathers shareholder resolutions filed by investment network members. These resolutions are part of broader investor efforts to encourage companies to address the full scope of environmental, social and governance (ESG) issues.

#### **Question/Need:**
I aim to use Natural Language Processing techniques to review the proposed sustainability resolutions found in a database at Ceres.org, to answer these main questions: 
- What topics (in what frequency) occur in shareholder sustainability resolutions? 
- Do proposed resolutions have positive, negative or neutral sentiment scores? 
- If there is a variety of sentiments: 
    - What topics are associated with each sentiment type? 
    - What is the financial performance of the companies associated with each sentiment type? 

This project is modeled off of a [paper by Raghupathi, V. et. al (2020)](https://www.mdpi.com/2071-1050/12/11/4753), who list the two key questions in their research as: 
- What is the variance in resolutions and practices between sectors, and 
- Do shareholder resolutions reflect corporate sustainability concerns in terms of environmental, social, and governance aspects?

If time permits, I would also like to address these questions and compare my findings to theirs (reproducibility of results was mentioned as a point of interest in their paper. How closely will my results match their 2020 results?)

Results of this project will benefit consultants, companies, investors or activists who wish to understand the current state of sustainability practices and wish to learn from and apply the best practices to their own operations.

#### **Data Description:**
Ceres.org hosts an ["Engagement Tracker" database](https://engagements.ceres.org/?_ga=2.198336172.281927745.1653500401-1839935729.1653500401) that contains 2,860 resolution entries, dating from 2009 to 2022. I will scrape the database using python selenium to gather the documents. An individual sample/unit of analysis in this project is a resolution proposal. I will tokenize the documents by word, di-gram and tri-gram for further analysis.

#### **Tools:**
The tools I will use for this project are listed in the Metis unsupervised NLP project introduction and include:
- Python text processing libraries/tools required for data handling (such as NLTK for natural language processing, sklearn to convert text documents to matrices, VADER for sentiment analysis, gensim for topic modeling).
- Acquisition tools that could include web scraping via python selenium 
- Storage tools that could include SQL or noSQL (e.g. MongoDB) databases
- Processing tools that could include Google Cloud or Amazon Web Services for cloud computing resources
- Visualization tools that could include python libraries such as Bokeh and Plotly or resources outside of python such as Tableau
- Production tools that could include Flask or other web app libraries/technologies

#### **MVP Goal:**
A minimum viable product for this project will be a successfully scraped corpus of documents and a plot of sentiment scores across documents in the corpus. If possible, it may include a rough, preliminary list of topics recovered from the corpus.

#### **References:**
Raghupathi, V.; Ren, J.; Raghupathi, W. Identifying Corporate Sustainability Issues by Analyzing Shareholder Resolutions: A Machine-Learning Text Analytics Approach. Sustainability 2020, 12, 4753. https://doi.org/10.3390/su12114753
