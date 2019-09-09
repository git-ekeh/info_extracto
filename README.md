# info_extracto

Info_extracto is an open-source pythonic tool that accesses both the Requests and BeautifulSoup libraries to pull text inbetween specified HTML tags from websites to populate text files. Info_extracto populates text files, while elegantly stripping the text of any existing html tags.

## Installation

The first step to installing this code locally is to download Python 3 from https://www.python.org/downloads/windows/. Once you reach this website, you will be faced with versions of python for various operating systems. Download the version of python that is compatible with your local operating system. To avoid future complications when trying to access python's wealth of open-source libraries, select the "Download with pip" option at the beginning of the download. Pip is the standard package manager for python that allows you access various open-source python libraries that are not apart of python's standard library. 
The second step is to use Python to install Beautiful Soup 4.4.0 Library. The installation can be done through copying pip install beautifulsoup4 into your commandline terminal.  
The third and final step is to use Python to install the Requests Library. The intallation cna be completed through copying pip install requests into your commandline terminal. 


## Usage

The purpose of this tool is to use the populated text files to train a machine learning algorithm to recommend a set of options to an end-user based on their input. The text of the populated text files acts as data that machine learning algorithms can learn to predict or find underlying patterns in. 

## Break Down

![import descriptions](https://github.com/git-ekeh/screenshots/blob/master/data_capture00.PNG) The first line in the code is called a "shebang". It is used to ensure that the script will be executed from the shell. In line 5 I access the BeautifulSoup Library- a library used primarily for scraping the web for various types of data. In line 6 I access the Requests Library- a python library that allows users to send HTTP/1.1 (HyperText Tranfer Protocol) requests. HTTP/1.1 requests happen when an HTTP client(the info_extracto tool) sends a request message to an HTTP server. If the request is approved by the server, the client is allowed to pull information from the server into their preferred domain. I shorten request to rs, using the "as" simplifier syntax for efficiency purposes.   

![function](https://github.com/git-ekeh/screenshots/blob/master/data_capture01.PNG) On line 9, I define a function called data_scrape() and do not give it any parameters. Line 10 describes my process of retrieving information from a URL. I used the City of Toronto's Open Data's URL to retrieve the data I was interested. To retrieve the data I use the requests library method get. The syntax is requests.get(url) because I simplified requests to rs line 10 looks like rs.get(url). In Line 10, I scrape the content of City of Toronto URL and store it in a variable named webapge. I use the requests library's method titled content to complete this task. 

![beautifulsoup structures](https://github.com/git-ekeh/screenshots/blob/master/data_capture02.PNG) Line 12 invokes the beautifulsoup library, where I create the BeautifulSoup Object. I call BeautifulSoup, which takes two parameters: the variable created using requests- webpage and an HTML parser. There are various parsers available to use, I chose the html parser because the focus of the function is primarily to extract text from URLs written in HTML. Line 13 uses the beautifulsoup method "find_all". Within a Google Chrome Brower and on a website of your choice, right click and scroll down the list of options and choose "Inspect". After following these instructions you should be exposed to the underlying html tags of the website. For this tool, I wanted to extract the text in paragraph form. To do this I found that <p> are HTML tags that are used to store and represent paragraphs of text on website. Therefore, I used the find_all() method to instruct the function to find all instances of the <p> HTML tag and stored it in the variable page_links.  
  
 ![data structures](https://github.com/git-ekeh/screenshots/blob/master/data_capture03.PNG) Line 13-17 describe the process I used to create a text file with the paragraph content from the City of Toronto URL I chose. On line 14, I used the open("file", "w+") method built-in to Python 3 to create a text file titled training_file prepended with ".txt" to ensure a text file is created. The second parameter "w+", indicates write and the plus sign means it will create the file if it is non-existent in the directory. 
