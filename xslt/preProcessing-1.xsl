<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
    xmlns:xs="http://www.w3.org/2001/XMLSchema"
    xmlns:math="http://www.w3.org/2005/xpath-functions/math"
    exclude-result-prefixes="xs math"
    version="3.0">
    
    <xsl:mode on-no-match="shallow-copy"/>
    <!-- 2023-08-09 ebb with yxj and nlh: This pre-processing stage 1 raises unwisely flattened note elements so that we may treat them as longTokens. 
     -->
 
    
    <xsl:template match="note[@sID]">
        <note xml:id="{@sID}">
            <xsl:for-each select="following::node()[following::note[@eID = current()/@sID]]">
                <xsl:copy select="current()"/>
            </xsl:for-each>         
        </note>
    </xsl:template>
    
  <xsl:template match="(* | text())[not(self::note)][preceding-sibling::note[1][@sID]]"/>
    
    <xsl:template match="note[@eID]"/>
     
</xsl:stylesheet>