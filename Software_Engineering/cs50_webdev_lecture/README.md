Harvard CS50 html, css,javascript lecture: https://www.youtube.com/watch?v=alnzFK-4xMY

Notes:
  * [Override trick](https://www.youtube.com/watch?v=alnzFK-4xMY&t=7640s)
  * document type declartion: 
    * Implicit indicator to the browser of the latest version
  * **Tags**
    * `ex: <html></html>` Symetrical
    * Hieararchy can be referred to as child parent
    * `<pr>` Provides some more semantic meaning for breaks
    * `<br>` doesn't require a closing tag
    * **The indentation is for humans & readability**

  * Attribute:
    * Modifies the behavior of a tag. Similar to a parameter in a function
    * Define properties of the element. Added to the opening tag. 
    * ex: `lang='en'`
  * element:
    * Everything related to the open and close tag
    * The HTML element is everything from the start tag to the end tag:
    * `<tagname>Content goes here...</tagname>`
    * More [here](https://www.w3schools.com/html/html_elements.asp)
  * Document Model:
    * Represents the structure of the doucment in a tree-like hierarchy of objects. It is stored in memory. 
    * Scripts execute top to bottom, left to right
    * Inside the CPU memory it will build this tree based data structure. 
  * Javascript:
    * Javascript creates dynamic behavior and can change behavior programatically. 
    * Javascript can dynamically add or remove from the tree. Like gmail one doesn't need to reload the page to see new email. Manipulates the DOM
  * CSS:
    * "cascading" -> Children and grandchildren inherit properties. "Cascade"
    * stylesheet is a code sheet that contain lots of styles or properties
    * class selector -> `.` means this is a class

* Protocol - A protocol is a set of rules and standards that govern the communication between devices on a network. It defines the format of data being transmitted, as well as the methods for error detection and correction. Examples of commonly used protocols include TCP/IP, HTTP, and FTP.
  * `curl -I http://harvard.edu` `curl -I https://harvard.edu`
* Classes - Attributes that define a specific group or category of an element. They are used to apply styles to multiple elemnets using CSS
  * Selectors:
    * type selector
      * type selector in CSS is used to select all elements of a given type. It is written as the name of the element, such as p or div. For example, to select all <p> elements on a page, you could use the type selector p { … }. Type selectors can be combined with other selectors, such as class selectors or ID selectors, to target specific elements within a page.
      * ID selector
        * An ID selector in CSS is used to select an element based on its ID attribute. It is written as a name preceded by a hash character (#) and can be used to select a single element on a page [1]. For example, if you had an HTML element with an ID of "myElement", you could select it with the following CSS:
        * #myElement { /* CSS styles go here */ }
      * attribute selector
        * An attribute selector in CSS is a selector that is used to select elements based on the presence or value of a given attribute [1]. For example, you could use the [rel="noopener"] attribute selector to select all anchor elements with the rel attribute set to "noopener". Attribute selectors are useful for targeting elements that have certain attributes or attribute values.
frameworks -> 
  Boostrap -> whole bunch of files with javascript and CSS

