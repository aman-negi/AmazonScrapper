Problem Statement -> Web Scrappe through the multiple amazon website and extract the required Fields

Bonus Problem -> ByPass the amazon Captcha 

Before choosing the library to use we need to first see that what kind of errors might occur while scrapping the 
amazon website.
1. Amazon being a tech giant won't easily allow crawlers/bots to scrappe their data for multiple reason, one being
    website overloading.
2. Amazon at times can show captcha to prevent bots to override other thing. (Bonus Problem)
3. Amazon might have multiple way of formating multiple category of items.Specially books.

How to override these problems.

1. Their are multiple ways to prevent websites to know that a bot is scrapping the data.
    a. Spoofing : Use multiple proxy headers/user agent on website so that they blacklist one specific agent,
        you can use multiple others, and by switching between them, you can prevent user agents to 
        getting blacklisted.
        Advantages : You can use multithreading to fasten your work without getting blacklisted, as 
                     by using multithreading you can scrappe multiple urls at a time, which can reduce
                     the speed by multiple x.
        Drawback : To scrappe for a huge amount of data you should have 100's of multiple proxies, so 
                    you can get them only by paying for them.
                    If we are planning to use multithreading we should have to take in the factor of 
                    high system requirement, increasing more cost.
    b.  Pretend to be normal User : By staying at a url for random amaount of time you can prevent the 
        websites from knowing that you are using a bot. Also add on multiple error handlers to bypass the 
        bot checking system.
        Advantages : Cost Effective(Not in aspect of time)
        Drawbacks : It will take a lot of time and specific handling of errors to get the work done.

2. You can add all the precautionary and handling methods for any captcha or bot detection.

3. Amazon mainly have same structure accross multiple regions but mainly have difference of formatting the websites
    between books and other item. Also in pricing as fashion has variable and sometime items might be out of stock so
    their might be no tag for pricing, so we need to consider that fact too.

Our Approach :

1. For prevention we randomized the time spend on each website so that our bot won't be easily detected. Also use selenium
    over bs4 as it can help at overriding the problems and will be able to help the bot preventing detection as compared to 
    static search(based on trials and errors). So, we used selenium for our project.

2. So we used time.sleep method of python for making our programm wait for a random amt of time for prevention.

3. For formatting we searched accross various categories for specific search and Xpath over id as it may include id too
    but can take other aspect to for better specification

4. (Bonus Problem)As amazon has specific captcha so we can easily override it. As it is an image we can use OCR technique to detect the 
    text in the image and fill the captcha form and submit it using selenium.

Installation Required for project

pip install pandas
pip install selenium
pip install torch torchvision torchaudio
pip install easyocr
pip uninstall opencv-python-headless==4.5.5.62
pip install opencv-python-headless==4.5.2.52
pip install datetime

Also you need to install webbrowser driver for you project