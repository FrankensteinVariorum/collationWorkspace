# Collation Chunk-21:

Notes: 
- "plutarchs's lives", the title of the book is weirdly mixed up with other wirtnesses?
    - ```
    	<rdgGrp n="[&#34;plutarch's&#34;]">
			<rdg wit="f1823">&lt;hi
				sID="novel1_letter4_chapter14_div4_div15_p3_hi2"/&gt;Plutarch's</rdg>
		</rdgGrp>
		<rdgGrp n="['plutarchs', 'lives']">
			<rdg wit="fMS">Plutarchs &lt;lb n="c57-0037__main__28"/&gt;lives</rdg>
		</rdgGrp>
		<rdgGrp n="['plutarch’s']">
			<rdg wit="f1818">&lt;hi
				sID="novel1_letter4_chapter14_div4_div15_p3_hi2"/&gt;Plutarch’s</rdg>
			<rdg wit="fThomas">&lt;hi
				sID="novel1_letter4_chapter14_div4_div15_p2_hi2"/&gt;Plutarch’s</rdg>
		</rdgGrp>
		<rdgGrp n="['‘plutarch’s', 'lives,’']">
			<rdg wit="f1831">‘Plutarch’s Lives,’</rdg>
		</rdgGrp>
    ```
Changes:

- [] In Manuscript, I moved the element to be on the same line as the letter
    - ```xml
    	<rdgGrp n="['i', '', '&lt;mdel&gt;e&lt;/mdel&gt;', 'i']">
    		<rdg wit="fMS">I &lt;lb n="c57-0038__main__20"/&gt;&lt;mod
    		sID="c57-0038__main__d4e6490"/&gt; &lt;mdel&gt;e&lt;/mdel&gt; &lt;sga-add
    		place="intralinear" sID="c57-0038__main__d4e6494"/&gt;i</rdg>
    	</rdgGrp>
        ```
        
- [] app has &lt; three reading witnesses, BUT looks valid  to the according files. Wrapped longToken around "to the beings concerning whom I" in according editions
    - ```xml
        <rdgGrp n="['to']">
	       <rdg wit="f1823">to</rdg>
	       <rdg wit="f1831">to</rdg>
	   </rdgGrp>
	   ```	