# citation-network-app
This is the citation application I created which searches an author's most referenced papers.
# Methodology
1. Database setup  
    1. Created local mysql database
    2. Used python notebook to filter needed data into csv files
    3. Created tables in mysql database to hold necessary information
    4. Loaded data from the csv files into the corresponding tables  
    Table structure:  
    authors: authorId, NormalizedName  
    paperauthoraffiliations: paperId, authorId  
    paperreferences: paperId, paperReferenceId  
2. Flask API creation  
Created Flask API which takes in a name in the url and queries the database. The queries utilize joins on the tables in order to get the necessary information. This can be seen in the main.py file.  
3. React FrontEnd  
Created a react application from scratch which uses axios to send a get request to my flask backend. The react app has a simple search bar and sends the request and displays the resulting list of most common papers and the number of times they were referenced.  
# Progress  
This application fulfills all the requirements proposed, but could definitely be extended further with more time, such as also loading the papers table from which we could obtain more information about the papers and making the react front end look nicer.  
