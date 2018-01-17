# LetterHelper

Python script to substitute several tags on a template with data for different recipients at the same time.

--------

# Motivation
Have you ever need to create several texts from a template with some fields to customize? With this script you can.

# How does it works
1. Ensure you have installed Python version 2.7.14 or more. Otherwise, go to the [downloads page]( https://www.python.org/downloads/) and install it.
2. Write the text you want on the __*letter_template.txt*__ file and place some *tags* like *[placeholder tag]* or *&lt;placeholder tag&gt;* in the text (whatever string you want).
    ```
    <tag_0>

    Lorem ipsum dolor sit amet, consectetur adipiscing elit.
    Nullam eget tortor odio. <tag_1> Interdum et malesuada fames ac ante
    ipsum primis in faucibus. Aenean vel orci volutpat, varius risus quis,
    accumsan dui. <tag_2>
    ```
3. Copy each different *tag* on the __*tags.txt*__ file, one on each line.
    ```
    <tag_0>
    <tag_1>
    <tag_2>
    ```
4. Write the substitution data on the __*data.txt*__ file, one line for each tag, and as many groups as the number of different recipients.
    ```
    data 0 tag 0
    data 0 tag 1
    data 0 tag 2
    data 1 tag 0
    data 1 tag 1
    data 1 tag 2
    data 2 tag 0
    data 2 tag 1
    data 2 tag 2
    ```
5. Double click __*letterhelper.py*__ file.
6. You will get as many txt files as groups of data you entered on *data.txt* file, named as: number (starting at 1), dot, blank space, and the info of the first *tag*.
    ```
    1. data 0 tag 0.txt
    2. data 1 tag 0.txt
    3. data 2 tag 0.txt
    ```

# License
This script is licensed under [The Unlicense](https://github.com/JAFS6/LetterHelper/blob/master/LICENSE).

# Author
[Juan Antonio Fajardo Serrano](https://www.linkedin.com/in/jafs6)
