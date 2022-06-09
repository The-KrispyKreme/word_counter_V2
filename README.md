# word_counter_V2
## Overview 
---

*Taiwan plays an important role in East Asian politics. The dialogue between the ROC and PRC can be seen, at times, as nationalistic. The goal of this is to provide the framework for a discourse analysis of given transcripts of speeches. This will allow a measurment to see if there has been an increase in nationalism from Chinese Leaders.*

## Features 
---
1. The transcripts will be uploaded along with the appropriate information, such as the title, author, and year. 
2. A word or phrase search will provided in order to find the input what needs to found. 
3. The word count will be presented to show how many times the word is found and in what documents. 
4. The results will be graphed and tabled to see pattern or trends and to do basic statistical analysis. 

## Models
--- 
* Document
    * title (charfield, title of the transcript)
    * year (interger field, year of the transcript)
    * author (charfield, author/speaker)
    * doc (, transcript)

* Word
    * searched_word (charfield, word or phased to be searched)

* WordCount
    * searched_word (foreignkey to Word)
    * doc (foreignkey to Document)
    * present (boolean, `TRUE` if word is present)
    * count (interger field, count of the word in the documents)


## Schedule
---
### Week 1 
- Personal repo completed. 
- Project set up and preparation completion.
- Write Models.

### Week 2 
- Document upload and conversion.
- Styling.
- Charting of data.

### Week 3 







