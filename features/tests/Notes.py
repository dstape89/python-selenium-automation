"""
.py file interacts with gherkin file?


XPath Notes
 XPath in Selenium is an XML path used for navigation through the HTML structure of the page.
 It is a syntax or language for finding any element on a web page using XML path expression.
 XPath can be used for XML and HTML documents to find the location of any element on a webpage using HTML DOM structure

 XPath format:

 Xpath=//tagname[@Attribute='Value']

 // = Select current node
 tagname = Tagname like input, div, img etc.
 @ = Selects attribute
 Attribute = Attribute name
 Value = Value of attribute

 To find the element on web pages accurately there are different types of locators:
 ID = Find element by ID
 Classname = By classname
 Name = By name
 Link text = By text of the link
 XPath = Required for finding the dynamic element and traverse between various elements of the webpage
 CSS Path = Locates elements having no name, class or ID

 Two types of XPath:
 Absolute and Relative

 Absolute = Direct way to find the element, but if there are any changes made in the path of the element then that XPath gets failed.

 The key characteritic of XPath is that it begins with the single forward slash, which means you can select the element from the root node

Ex = /html/body/div[2]/div[1]/div/h4[1]/b etc.

Relative XPath = Starts from the middle of HTML DOM structure. It starts with double forward slash. It can search elements anywhere on the webpage, means no need to write a ong xpath and you can start from the middle of HTML DOM Structure. Relative Xpath is always preferreed as it is not a complete path from the root element

Ex =  //div[@class='featured-box columnsize1']//h4[1]//b[1]

Xpath axes - search different nodes in XML document from current context node. XPath Axes are the methods to find dynamic elements, wihch otherwise might not be posisble by normal XPath method having no ID, classname, name etc.


$x("//a[contains(@href, 'link here')]")

best paths to use: xpath, css selectors, id

$x("//div[@CLASS='help-content']/h1")
    - / at the end links to a direct child. If you go down multiple children, you use //
"""