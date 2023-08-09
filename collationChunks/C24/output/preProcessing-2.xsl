<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    exclude-result-prefixes="xs math"
    version="3.0">
    
    <xsl:mode on-no-match="shallow-copy"/>
    <!-- 2023-05-17 ebb and nlh: This is an XSLT late pre-processing stage added just for the collationWorkspace. 
        We don't want to overwrite existing longToken markup. 
        Instead, we are: 
        * Transforming the source XML files, however marked, by aadding handling for delSpan anchors,
        * Removing newline characters from inside the inlineVariationEvent elements handled in the Python script, so we no longer have to backspace manually when creating longTokens,
        and so we have finer control over the handling of deletion and insertion events. 
        
        inlineVariationEvent = ['head', 'del', 'mdel', 'add', 'note', 'longToken']

        About the delSpans:
        delSpan elements are used in the S-GA (msColl) files to represent deletions that cross over multiple lines and sometimes (just occasionally) other deletions/modification events.
        
        Technically they should be a single complete token, representing a deletion event, but they can be complicated when they contain multiple modifications inside.
        Because these do not start out as matching element pairs, we are simply matching them here so we can (we hope) process them later as a completely deleted passage.
        We change the anchor into a matching delSpan with an anchor attribute, intended to substitute for the original <anchor> element so it's distinct from other <anchor> elements
        less meaningful to the collation. 
        
        <delSpan spanTo="#id"/>......<delSpan anchor="id"/>
     -->
    <xsl:template match="anchor[@xml:id = preceding::delSpan/substring-after(@spanTo, '#')]">
        <delSpan anchor="{@xml:id}"/>
    </xsl:template>  
    
    <xsl:template match="zone[@eID][preceding-sibling::*[1] ! name() ne 'w']">
        <xsl:text> &#10;</xsl:text>
        <xsl:copy><xsl:apply-templates select="node()|@*"/></xsl:copy> 

    </xsl:template>
  
     
    <xsl:template match="(head | del | mdel | add | note | longToken)/text()">
        <!--ebb: setting all longToken-style element text nodes on a single line to be processed as a single token:-->
        <xsl:analyze-string select="current()" regex="\n">
            <xsl:matching-substring>
                <!-- nothing here: delete the newline -->
            </xsl:matching-substring>
            <xsl:non-matching-substring>
                <xsl:value-of select="replace(., '\s{2,}', ' ')"/>
                <!-- here, removing extra spaces, replace with single space. -->
            </xsl:non-matching-substring>
            
        </xsl:analyze-string>
    </xsl:template>
     
</xsl:stylesheet>