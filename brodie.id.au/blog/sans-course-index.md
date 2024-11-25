```{post} 17 November, 2021
:author: Brodie Blackburn
```
# Creating a SANS course index

Recently I sat a GIAC exam. I followed the advice of [this post](https://tisiphone.net/2015/08/18/giac-testing/) to prepare for the exam. Using coloured tabs to quickly find topics in course books sounded like a great idea.

I documented a course outline in YAML and used a [Python script](https://github.com/eidorb/sans-index) to generate an Excel workbook containing a colourful contents and index.

A detailed contents is equally as useful as an index. If I know the rough location of some topic, I can use the contents to quickly narrow down the search.


## Course outline

While studying the SANS course, I created a course outline in a YAML document. YAML was chosen because I could achieve a minimal outline without having to worry about quoting strings, trailing commas, braces or other special characters. Colons in titles, chapters and topics were avoided because of this.

The root of the document is a sequence of the course's books.

```yaml
- <book>
- <book>
- <book>
```

Books map a book title to a sequence of chapters.

```yaml
- Threat intelligence:
    - <chapter>
    - <chapter>
    - <chapter>
```

Chapters map a chapter name to a sequence of topics/keywords.

```yaml
- Threat intelligence:
    - Case study - Stuxnet:
        - <topic>
        - <topic>
        - <topic>
```

Topics map a page number to topic.

```yaml
- Threat intelligence:
    - Case study - Stuxnet:
        - 10: Stuxnet
        - 10: Case study - Stuxnet
        - 10: Iran's nuclear program
    - Introduction to active defense and incident response:
        - 18: Sliding scale of cyber security
        - 18: Architecture
        - 18: Passive defense
```


## YAML to Excel

I wrote a [Python script](https://github.com/eidorb/sans-index) to convert SANS course content in a YAML document to an Excel workbook with two worksheets: Contents and Index. I chose Excel because the output can be easily tweaked and gave me a lot of print layout options.

Contents maps topics to page numbers, in book order. Index maps topics to page numbers, in alphabetical order.

I liked the idea of using coloured tabs to mark books and chapter locations. I found some suitable coloured sticky tabs at Officeworks.

```{figure} sans-course-index/sticky-tabs.jpeg
:alt: Coloured Post-it notes

Coloured Post-it notes.
```

Each book is assigned a colour. This is the colour of the tab at the top of a book. Chapters are assigned colours too. These are the colours of tabs marking chapters in books.

I found hex colour codes that are close enough to the actual colours. Two of the colours were discarded because they were too similar to other colours.

```python
# Some of the colours are a bit hard to distinguish.
colours = [
    "#FF1493",  # deeppink
    # '#FF69B4',  # hotpink
    "#FFE4E1",  # mistyrose
    "#E6E6FA",  # lavender
    # '#B0E0E6',  # powderblue
    "#7FFFD4",  # aquamarine
    "#ADFF2F",  # greenyellow
    "#FFFFE0",  # lightyellow
    "#FFD700",  # gold
    "#FF7F50",  # coral
]
```


## Output

Here's a snippet of a generated Contents worksheet. You can see topics nested below a chapter with the same colour. Likewise, chapters are nested under a book with the same colour.

```{figure} sans-course-index/contents-worksheet.png
:alt: Contents worksheet
:width: 50%

Contents worksheet.
```

And here's what an Index worksheet looks like:

```{figure} sans-course-index/index-worksheet.png
:alt: Index worksheet

Index worksheet.
```

Here are the course books and chapters identified with coloured sticky tabs.

```{figure} sans-course-index/sans-course-books.jpeg
:alt: SANS course books

SANS course books and chapters marked with Post-it notes.
```

```{update} 17 May, 2024

- Use `figure` directive with captions instead of just images.
- Fix header levels.
```

```{update} 26 November, 2024

- Simplify post's filenames
```
