# 1410. HTML Entity Parser

# HTML entity parser is the parser that takes HTML code as input and replace all the entities of the special characters by the characters itself.

# The special characters and their entities for HTML are:

# Quotation Mark: the entity is &quot; and symbol character is ".
# Single Quote Mark: the entity is &apos; and symbol character is '.
# Ampersand: the entity is &amp; and symbol character is &.
# Greater Than Sign: the entity is &gt; and symbol character is >.
# Less Than Sign: the entity is &lt; and symbol character is <.
# Slash: the entity is &frasl; and symbol character is /.
# Given the input text string to the HTML parser, you have to implement the entity parser.

# Return the text after replacing the entities by the special characters.

 

# Example 1:

# Input: text = "&amp; is an HTML entity but &ambassador; is not."
# Output: "& is an HTML entity but &ambassador; is not."
# Explanation: The parser will replace the &amp; entity by &
# Example 2:

# Input: text = "and I quote: &quot;...&quot;"
# Output: "and I quote: \"...\""

# My solu

class Solution:
    def entityParser(self, text: str) -> str:
        text = text.replace("&gt;", '>')
        text = text.replace("&lt;", '<')
        text = text.replace("&frasl;", '/')
        text = text.replace('&quot;','"')
        text = text.replace("&apos;","'")
        text = text.replace("&amp;", '&')

        return text

# Alt solutions

class Solution:
    def entityParser(self, text: str) -> str:
        dict = {
            "&quot;": "\"",
            "&apos;": "'",

            "&gt;": ">",
            "&lt;": "<",
            "&frasl;": "/", 
            "&amp;": "&"  
        }

        for key, value in dict.items():
            text = text.replace(key, value)
        return text
  
class Solution:
    def entityParser(self, text: str) -> str:
        
        html_symbol = [ '&quot;', '&apos;', '&gt;', '&lt;', '&frasl;', '&amp;']
        formal_symbol = [ '"', "'", '>', '<', '/', '&']
                
        for html_sym, formal_sym in zip(html_symbol, formal_symbol):
            text = text.replace( html_sym , formal_sym )
        
        return text
    