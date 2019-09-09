# info_extracto

Info_extracto is an open-source information extraction tool that accesses both the Requests and BeautifulSoup libraries to pull text inbetween specified HTML tags from websites to populate text files. Info_extracto populates text files, while elegantly stripping any existing HTML tags using Python 3.

## Installation

The first step to installing this code locally is to download Python 3 from https://www.python.org/downloads/windows/. Once you reach this website, you will be faced with versions of Python for various operating systems. Download the version of Python that is compatible with your local operating system. To avoid future complications when trying to access Python 3's wealth of open-source libraries, select the **Download with pip** option at the beginning of the download. Pip is the standard package manager for python that allows you to access various open-source Python libraries that are not apart of Python 3's standard library. 
The second step is to use Python to install the BeautifulSoup 4.4.0 library. The installation can be done through copying **pip install beautifulsoup4** into your commandline terminal.  
The third and final step is to use Python to install the Requests Library. The intallation can be completed through copying **pip install requests** into your commandline terminal. 


## Usage

The purpose of this tool is to use the populated text files to train a machine learning algorithm to recommend a set of options to an end-user based on their input. The text of the populated text files acts as data that machine learning algorithms can learn to predict or find underlying patterns in. 

## Break Down

![import descriptions](https://github.com/git-ekeh/screenshots/blob/master/data_capture00.PNG) 
The first line in the code is called a "shebang". It is used to ensure that the script will be executed from the shell. In line 5 I access the BeautifulSoup Library- a Python library used primarily for scraping the internet for various types of data. In line 6 I access the Requests Library- a Python library that allows users to send HTTP/1.1 (HyperText Tranfer Protocol) requests. HTTP/1.1 requests happen when an HTTP client(the info_extracto tool) sends a request message to an HTTP server. If the request is approved by the server, the client is allowed to pull information from the server into their preferred domain. I shorten request to rs, using the "as" simplifier syntax for efficiency purposes.   

![function](https://github.com/git-ekeh/screenshots/blob/master/data_capture01.PNG) 
On line 9, I define a function called data_scrape() and do not give it any parameters. Line 10 describes my process of retrieving information from a URL. I used the City of Toronto's Open Data's URL to retrieve the data I was interested. To retrieve the data I use the Requests library method **get()**. The syntax is requests.get(url), however, because I simplified requests to rs line 10 looks like rs.get(url). In Line 10, I scrape the content from the City of Toronto URL and store it in a variable named **webapge**. I use the requests library's method titled **content** to complete this task. 

![beautifulsoup structures](https://github.com/git-ekeh/screenshots/blob/master/data_capture02.PNG) 
Line 12 invokes the BeautifulSoup library, where I create the BeautifulSoup Object and save it in a variable named **soup**. I call BeautifulSoup, which takes two parameters: the variable created using requests- webpage and an HTML parser. There are various parsers available to use, I chose the HTML parser because the focus of the function is primarily to extract text from URLs written in HTML. Line 13 uses the beautifulsoup method **find_all()**. Within a Google Chrome Brower and on a website of your choice, right click and scroll down through the list of options and choose "Inspect". After following these instructions you should be exposed to the underlying HTML tags of the website. For this tool, I wanted to extract all the text on the website that is in paragraph form. To do this I needed to locate all lowercase p's inbetween each '<>'. This symbol represents HTML tags that are used to store and represent paragraphs of text on a website. As a result, I used the find_all() method to identify all instances of the paragraph HTML tags on the webpage and stored it in the variable **page_links**.  
  
![data structures](https://github.com/git-ekeh/screenshots/blob/master/data_capture03.PNG) 
Line 13-17 describe the process I used to create a text file with the paragraph content from the City of Toronto URL I chose. On line 14, I define a variable with the **open("file", "w+")** method built-in to Python 3 to create a text file titled training_file prepended with ".txt" to ensure a text file is created. The second parameter "w+", indicates write and the plus sign means it will create the file if it is non-existent in your local directory. I saved the contents of the text file in a variable titled **train**. On line 15 I used a for loop to iterate through each HTML paragraph tag on the City of Toronto Website, and stored the text in the variable page_links that was defined earlier. Within the for loop, I extract the text in between each HTML paragraph tag by using the BeautifulSoup method **get_text()** and write them into the training_file.txt. When this condition is satisfied the loop is exited and line 17 instructs the program to close training_file.txt file.  Line 19 is needed to call the function defined above. Your end product should be a text file with the content of each paragraph on the City of Toronto website displayed in a text file without any HTML tags. 
 
 Your file should look like this: ![textfile](https://github.com/git-ekeh/screenshots/blob/master/data_capture04.PNG) 
 

