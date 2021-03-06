# Transform 2021 Tutorial <br/>Geothermal Well Test Analysis with Python

This tutorial was developed by Irene Wallis and Katie McLean, industry practitioners with extensive experience in geothermal well logging and testing. It will live-stream to YouTube during the SWUG Transform 2021 conference and will be available through the SWUG YouTube channel for viewing later. 

**The tutorial will cover:** 
- General introduction to geothermal wells
- Overview of the completion test process 
- Introduction to temperature log analysis
- Injectivitly index determination (i.e., well capacity in t/hr.bar)
- Spinner data analysis (i.e., feedzone identification)

Production tests and pressure transient analysis are not covered. 

Python offers us the opportunity to generate a robust and repeatable well test analysis that is easy to audit. This is important given the high-value decisions based on these analyses.
We will demo how the Jupyter Notebook environment enables us to store the steps taken to process and interpret data along with key metadata, things that are difficult to do reliability in Excel.  

**You should attend this tutorial if you are:**
- Interested in geothermal wells and how they are characterised using injection testing and temperature logs
- A practising geothermal reservoir engineer who is interested in using python for well test analysis

The tutorial uses methods at an intermediate python level but, because all code is provided, a novice python user can follow along.    

**For more information,** check out a book co-authored by Katie with Sadiq Zarrouk that covers the theory and practice of geothermal well test analysis https://www.elsevier.com/books/geothermal-well-test-analysis/zarrouk/978-0-12-814946-1
 
***

**Here's how you participate in this event:**

1. Follow this link and register for the Transform 2021 unconference https://softwareunderground.org/events/transform-2021.

2. If you're not already a member, join the [Software Underground slack community](https://softwareunderground.org/slack).

3. Join the tutorial slack channel #t21-thurs-geothermal because this is where you can ask questions during the tutorial and meet others who are attending.

4. Decide how you want to interact with the tutorial. You will be able to read along in Curvenote, try out the method yourself without installing anything by using Google Colaboratory, or instal Anaconda to run the tutorial notebooks locally on your computer. More detailed setup instructions are provided below.  

5. Watch the tutorial live stream to YouTube (https://www.youtube.com/watch?v=VEKrTV89Ln8) **The tutorial livestream will be UTC Thursday 22 April 22:00** but will also be freely available after the event. 

6. After the livestream, come meet Irene and Katie, and other tutorial participants, in the Transform 2021 social and hackathon space that's been built using GatherTown (https://gather.town/). A link to this space is included in the topic of the tutorial slack channel (hover over the bar at the top to reveal the gather.town link). 

***

# Setup instructions

As well as the livestream to YouTube, you will be able to interact with the tutorial in three ways:

- Read the notebooks at Curvenote by following [this link](https://curvenote.com/@swung/geothermal-well-test-analysis-transform-2021). Big thanks to [Steve Purves](https://github.com/stevejpurves) for setting this up for us.

- Follow the Google Colaboratory instructions below to interact with the notebooks without installing anything. Big thanks to [Thomas Martin](https://github.com/ThomasMGeo) for the Google Colab advise. 

- Follow the Anaconda Setup instructions below to run the notebooks locally on your computer. Big thanks to [Martin Bentley](https://github.com/mtb-za) for testing the local instal method and helping with datetime debugging. 


***
## Google Colaboratory Setup Instructions

Google Colab is a way to run the tutorial Jupyter Notebooks (.ipynb) in the cloud. It is free to use but, as is typical of Google products, you have to sign in. We will use the free Google Colab (there is no need to sign up for Google Colab Pro).

1. If you do not already have one, you will need a Google account. If you have a gmail address, you already have a google account.
2. Download the content of this repository by clicking on the green "Code" button above and selecting "Download zip"
3. Unzip the T21-Tutorial-WellTestAnalysis-main.zip 
4. Sign into your [Google Drive](http://www.drive.google.com/) using your Google account details and upload the unzipped T21-Tutorial-WellTestAnalysis-main folder to google drive. Note that you need to upload into the browser google drive, not the local Google Drive on your hard drive (if you happen to have one).
5. Open the T21-Tutorial-WellTestAnalysis-main on Google Drive, right click any file that ends with .ipynb and select "open with". If Google Colaboratory appears in your list, then select this. If Google Colaboratory is not already an option, you need to install this into your Google Drive. To install Google Colaboratory: 1) Right click an .ipynb -> open with -> connect more apps, 2) search the Google Workspace Marketplace for 'Colaboratory', and 3) install Google Colaboratory. Now you will be able to go back to your .ipynb and open with Google Colaboratory.

After you have opened the Jupyter Notebooks (.ipynb) in Colab, you will need to mount your Google Drive (i.e., make Google Drive visible to the notebook) so you can import data. Instructions for how to do this is included in the top of each notebook after the introductory text. 

***
## Anaconda Setup Instructions
 
To run this tutorial, you will need an environment that contains all of the required packages. If you are familiar with setting up your own environment, then go ahead with your usual approach. Otherwise, use the following steps.

Download this tutorial from GitHub using the green 'code' button and unzip to somewhere that is easy to find, such as your Documents folder.
 
Download and instal [Anaconda individual edition](https://www.anaconda.com/products/individual) if you don't already have it. When prompted, accept the default installation settings.

In Windows open the anaconda prompt or in macOS open a terminal. Use the prompt/terminal to navigate to where you have saved this tutorial (hint: use _cd \<path_to_the_tutoral\>_ to change directory)
 
In the tutorial folder, you will find an environment.yml file (hint: use _ls_ in MacOS or _dir_ in Windows to list files in your current directory). We will use this file to create an environment that will run the tutorial. Execute the following command in the prompt/terminal to create the environment:
 
    $ conda env create -f environment.yml
 
You will see a lot of text scroll past in the the prompt/terminal and may need to respond y + ENTER at some point. The environment is automatically named geothrm. Once it has built, we need to activate the environment by executing:
 
    $ conda activate geothrm
 
\(geotherm\) should now appear on the far left of your current line in the prompt/terminal window. Now you are inside the right environment, you can execute the following command to launch a browser window containing Juypter notebook:
 
    $ jupyter notebook
 
Now you can open the tutorial notebooks and use them. 

When you are finished with Juypter Notebook, you can close the browser window and go back to the prompt/terminal to kill the process with CTRL + C.
 
When you come back to the tutorial at a later date, you will probably have to activate the geothrm environment again before launching Juypter Notebook.
 
**Other useful commands**
 
Print a list of your conda environments
  
    $ conda env list
 
Print a list of what is inside your active environment
  
    $ conda list

To install an additional package into the active environment

    $ pip install <PackageName>