import urllib.request
import urllib.parse
import numpy as np
import re

def to_search():
    '''
    This function asks the user to input the search strings, and then returns the url list to the caller
    '''
    query_string = urllib.parse.urlencode({"search_query" : input("Search: ")})
    html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
    search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())

    #the list that contains the links of all the searches
    search_results = ["http://www.youtube.com/watch?v=" + i for i in search_results]

#now, we are going to ask the user for the songs that they wish to download, and form a list out of them
choice = 'y';  #choice variable

final_download_list = []
while (choice == 'y' or choice == 'Y'):
    links = serach();   #asks the user to input which video he wants to download

    #looping through links
    no = 0  #counter that holds the index of the current url in the loop
    for url in links:
        video = pafy.new(url)   #creating a new video instane
        print(no+1, ". ", url)
        no+=1

    int vid_choice = input("Enter index of the video(-1 to cancel)")

    if(vid_choice == -1)    #skipping the song
        continue;

    final_download_list.append(links[vid_choice])

    choice = input("Add more songs?(y/n)")

#now, we loop through the final_download_list and download the best audiostream available