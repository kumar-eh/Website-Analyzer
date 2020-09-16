# Website-Analyzer
When given a url it checks whether its a valid url or not. If it's a valid url it will search for all the links in the website and store it in a array(remove duplicates).
Prints the number of distinct links in the output. Then for the specified website it will extract clean text without style tags , html tags etc...
Then parsing the text ie. removing punctuations , stop words and other data cleaning methods like stemming etc...
The word cloud is created for the clean text which has only the key terms based on the frequency.
The output contains total number of words of the website , number of distinct links , number of pages at top level.
The top 9 keywords of the clean text is displayed. If the button 'Generate word cloud' is clicked the word cloud for the 20 terms will be displayed.
If the button 'display links of the website' is clicked all the links of the website will be displayed in the frame below with the scrolling bar.
The screenshots of the output are on the issues section. To run the program copy the program in the Python IDLE and save it in the same directory as the cloud mask 
and logo. Then while executing the program you will get the output.
The website analyzer does the the following functions as above and display the word cloud.

Sample website 1:

Wordcloud:



Sample website 2:
![image](https://user-images.githubusercontent.com/68334628/93303657-76400780-f819-11ea-92c4-246ab394203a.png)
Wordcloud:
![image](https://user-images.githubusercontent.com/68334628/93303642-70e2bd00-f819-11ea-84e4-3b36e58a3cac.png)


Sample website 3:
![image](https://user-images.githubusercontent.com/68334628/93303204-c2d71300-f818-11ea-9c6e-0f52123c825d.png)
Wordcloud:
![image](https://user-images.githubusercontent.com/68334628/93303555-47c22c80-f819-11ea-8381-169efd577a9b.png)

