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
https://user-images.githubusercontent.com/68334628/93126233-b86a2b80-f6e9-11ea-964a-c409b42ac8c1.jpg
Wordcloud:
https://user-images.githubusercontent.com/68334628/93126251-ba33ef00-f6e9-11ea-9355-2c6af8020215.jpg


Sample website 2:
https://user-images.githubusercontent.com/68334628/93126254-bacc8580-f6e9-11ea-96d7-873b82460966.jpg
Wordcloud:
https://user-images.githubusercontent.com/68334628/93126256-bb651c00-f6e9-11ea-86d9-bbc58342e78f.jpg


Sample website 3:
https://user-images.githubusercontent.com/68334628/93301724-80acd200-f816-11ea-8bf8-aff44fbae82c.png
Wordcloud:
https://user-images.githubusercontent.com/68334628/93301786-9621fc00-f816-11ea-8419-28dcf6f0f271.png
