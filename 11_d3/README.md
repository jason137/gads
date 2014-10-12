# D3.js

we will add to this definition as we go along:

    what is d3?
        def1: a library for rendering interactive visualizations in the browser

note: familiarize yourself with the tools for viewing page source & the
javascript console in your favorite browser

another note: this is a quick intro from the perspective of a data scientist, not
a web developer!

## The DOM

what is a webpage?
- implementation of various **web standards** (specifications & definitions for web design)
- **html** defines structure
    - set off with *body* tags
    - [do-nothing html](http://bost.ocks.org/mike/d3/workshop/hello-world.html)
- **css** defines aesthetics
    - set off with *style* tags
    - [html with css](http://bost.ocks.org/mike/d3/workshop/hello-css.html)
- **javascript** defines behavior, interactivity 
    - set off with *script* tags
    - [html with js](http://bost.ocks.org/mike/d3/workshop/hello-javascript.html)

(view source & console in above examples)

the logical structure of a webpage is defined in terms of a set of parent-child
relationships between html elements or **nodes**
- this element hierarchy is called the **document object model**, or **DOM**

the central goal of d3 is to make data-driven visualization easier *without*
introducing a new way of representing an image in html (eg, by using existing standards only)
- the task of creating a viz boils down to **constructing a DOM from a dataset**
- *each data point will have a corresponding DOM elt*

## SVG

d3 relies on **svg** (scalable vector graphics), a popular web standard for representing
2d images
- [some basic svg examples](http://www.w3schools.com/svg/svg_examples.asp)

pixel-based graphics (not like svg) are made up of pixels with specific location & color assignments

vector graphics (like svg) are made up of lines, curves, points that are described mathematically
- svg advantages include zoomability, smaller file size, better display performance, more flexibility for web developers
- represented by xml

with this knowledge, here's a better answer to our original question:

    what is d3?
        def1: a library for rendering interactive visualizations in the browser
        def2: a javascript library capable of building interactive viz's (using the svg standard)
              by directly manipulating the DOM

## From Data to DOM

the name D3 stands for **data-driven documents**
- "documents" refers to the DOM as above
- the "data-driven" part refers to the fact that the dataset becomes the
  *backbone* of our DOM
    - **D3 explicitly maps recs from the dataset into DOM elts**
    - [basic d3 svg example](http://alignedleft.com/content/03-tutorials/01-d3/110-drawing-svgs/3.html)

```
what is d3?
    def1: a library for rendering interactive visualizations in the browser
    def2: a javascript library capable of building interactive viz's (using the svg standard)
          by directly manipulating the DOM
    def3: a js library capable of building interactive viz's by binding data to html elements
```
## Selectors

the basic strategy for interactivity in d3 is to perform operations on
selections of DOM elts; d3 does this by borrowing a powerful tool from css called the **selector**

a selector is a method that takes an input pattern as a parameter, operates on
DOM elements, and returns an array of elements matching the input pattern (the
*selection*).
- data is represented by an *array*
- selection returns array, on which another selection can be called
    - **method chaining**
    - [selector syntax example](http://alignedleft.com/content/03-tutorials/01-d3/110-drawing-svgs/3.html)

## The Data-Join
[circles]

## Loading Data
data loading is always an **asynchronous** process
- data-dependent code must be invoked via **callback**
    - yikes
    - d3 has convenience methods called d3.csv, d3.tsv, d3.json which wrap
      more primitive data loader
        - these are useful, but need to make sure you use the right loader for your
        data file!
    - due to the asynchronous nature of code execution, the loader func is analogous to a main func

## Interactive Behavior

interactive behavior is added via **event handlers**, which can easiliy be implemented by
attaching an **event listener** to a node (or a selection of nodes), and by defining the event handling behavior
[circles]

## some cool examples:
[svg swarm](http://bl.ocks.org/mbostock/2647924)  
[canvas swarm](http://bl.ocks.org/mbostock/2647922)  
[choropleth](http://bl.ocks.org/mbostock/3306362)  
[streamgraph](http://bl.ocks.org/mbostock/4060954)  
[binary tree](http://prcweb.co.uk/lab/d3-tree/)  
[layout tree (w edge bundling)](http://mbostock.github.io/d3/talk/20111018/tree.html)

[force-directed graph](http://bl.ocks.org/mbostock/4062045)
[network cooc mtx](http://bost.ocks.org/mike/miserables/)

[realtime](http://bost.ocks.org/mike/path/)  
[interactive](http://bl.ocks.org/mbostock/4063663)  
[transitions](http://www.newyorker.com/sandbox/business/subway.html)

[iris scatterplot](https://gist.github.com/mbostock/3887118)  
many more in the gallery!
