<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    exclude-result-prefixes="xs math"
    version="3.0">
    
    <xsl:mode on-no-match="shallow-copy"/>
    <!-- 2023-06-11 ebb: Adding a patch to correct msColl zone markers in margins. The full ids were not added to the Trojan markers in earlier stages. 
        This results in multiple pairs of zone-markers with the same too-simple ids, and that prevents the msColl edition from being reconstructed in the postCollation pipeline. 
        We correct that here. TO BE DEVELOPED. NOTE LIKELY TROUBLE with ambiguous rule matches b/c of template matching on zone[@eID][preceding-sibling::*[1] ! name() ne 'w'].
    Do you need to try to run the zone recrunching first and store in a variable to continue processing afterwards? 
    -->
    
    <!-- 2023-05-17 ebb and nlh: This is an XSLT late pre-processing stage added just for the collationWorkspace. 
        We don't want to overwrite existing longToken markup. 
        Instead, we are: 
        * Transforming the source XML files, however marked, by adding handling for delSpan anchors,
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
    
    <xsl:template match="/"><!-- Added on 2023-06-11 -->
        <xsl:variable name="repaired-zoneTrojans">
            <xsl:apply-templates/>
        </xsl:variable>
        <xsl:apply-templates select="$repaired-zoneTrojans" mode="laterCorrections"/>
    </xsl:template>
    
    <!-- 2023-06-13 ebb Notes: 
        Sometimes there are nested margin zones. These must be processed from the inside out.
        Test with this XPath: //zone[contains(@corresp, '.')][following::zone[1][not(@eID)]]
        There is one instance in C11. The first following zone has an @sID, but has no corresp attribute (probably because this doesn't have an anchor insertion mark in the main text. It's an insertion inside an insertion!
        There aren't any of these in C18. 
        
       OBJECTIVE: CONTROL THE PROCESSING ORDER. 
       First, process ONLY the elements that have first-following zones that match. Since it won't happen all the time, it's conditional.   
        --> 
    
    <xsl:template match="zone[contains(@corresp, '.')][following::zone[1][@eID]]"><!-- Added on 2023-06-11. This template matches on margin zones with @corresp attributes pointing to anchor elements for insertion points in the main text. -->
        <!-- ebb: Process the simple ones with no nested zones first. -->
        <xsl:variable name="repairedID" as="xs:string" select="tokenize(@sID, '__')[1] || '.' || tokenize(@corresp, '.')[2] || '__' || substring-after(@sID, '__')"/>
    <xsl:element name="{name()}">
          <xsl:attribute name="corresp" select="@corresp"/>
        <xsl:attribute name="type" select="@type"/>
          <xsl:attribute name="sID">
              <xsl:value-of select="$repairedID"/>
          </xsl:attribute>
        <xsl:apply-templates select="following::zone[1][@eID]" mode="fixEndID">
            <xsl:with-param name="reapiredID" as="xs:string" select="$repairedID"/>
        </xsl:apply-templates>
    </xsl:element>
    </xsl:template>
    
    <xsl:template match="zone[@eID]" mode="fixEndID">
        <xsl:param name="repairedID"/>
        <xsl:element name="{name()}">
            <xsl:attribute name="eID">
                <xsl:value-of select="$repairedID"/>
            </xsl:attribute>
        </xsl:element> 
       

    </xsl:template>
    
    
    
    
    <xsl:template match="anchor[@xml:id = preceding::delSpan/substring-after(@spanTo, '#')]" mode="laterCorrections">
        <delSpan anchor="{@xml:id}"/>
    </xsl:template>  
    
    <xsl:template match="zone[@eID][preceding-sibling::*[1] ! name() ne 'w']" mode="laterCorrections">
        <xsl:text> &#10;</xsl:text>
        <xsl:copy><xsl:apply-templates select="node()|@*" mode="laterCorrections"/></xsl:copy> 

    </xsl:template>
    
    <xsl:template match="(head | del | mdel | add | note | longToken)/text()" mode="laterCorrections">
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