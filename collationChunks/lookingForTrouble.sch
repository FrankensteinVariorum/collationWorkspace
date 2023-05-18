<?xml version="1.0" encoding="UTF-8"?>
<sch:schema xmlns:sch="http://purl.oclc.org/dsdl/schematron" queryBinding="xslt3"
    xmlns:sqf="http://www.schematron-quickfix.com/validator/process"
    xmlns="http://purl.oclc.org/dsdl/schematron">
    <ns uri="http://interedition.eu/collatex/ns/1.0" prefix="cx"/>
    
    <pattern>
        <title>Looking for a low number of witnesses</title>
        <rule context="app">
            <report role="info" test=".//rdg => count() &lt; 5">Hey! How come there's less than 5 reading witnesses at this point? Is something out of alignment?</report>
            <report role="warning" test=".//rdg => count() &lt; 3">YIKES! There are fewer than THREE reading witnesses?! What gives?</report>
        </rule>
    </pattern>
   <!-- For a noiser view, when seriously looking for even more trouble, uncomment this pattern! Maybe uncomment this when you think the collation is near complete. 
       <pattern>
        <title>Looking for false alignments</title>
        <rule context="app">
            <report role="info" test="descendant::rdg => count() = 5 and count(child::rdgGrp) = 1 and child::rdgGrp/@n[not(matches(., '\s')) and preceding-sibling::app[1]/descendant::rdg => count() &lt; 5]">
               The collation may be falsely aligned or "snagged" here, because not all the witnesses are present in the app before this one. 
            </report>
            <report role="info" test="descendant::rdg => count() = 5 and count(child::rdgGrp) = 1 and child::rdgGrp/@n[not(matches(., '\s')) and following-sibling::app[1]/descendant::rdg => count() &lt; 5]">
                The collation may be falsely aligned or "snagged" here, because not all the witnesses are present in the app after this one. 
            </report>
        </rule>
    </pattern>
   -->
 
</sch:schema>