# chunk 27 notes
## initial schema review
- [] These nodes are fine. However, it may be cleaner to longToken each one and put them in a single &lt;app&gt; group.
	 ```xml
        <app>
		<rdgGrp n="['that', 'faintly', 'reminds']">
			<rdg wit="f1818">&lt;pb xml:id="F1818_v3_074" n="070"/&gt;that faintly reminds</rdg>
			<rdg wit="fThomas">&lt;pb xml:id="F1818_v3_074" n="070"/&gt;that faintly reminds</rdg>
			<rdg wit="fMS">that &lt;lb n="c57-0120__main__8"/&gt;faintly reminds</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['me']">
			<rdg wit="f1818">me</rdg>
			<rdg wit="fThomas">me</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['of', 'the', 'anguish', 'of']">
			<rdg wit="f1818">of the anguish of</rdg>
			<rdg wit="fThomas">of the anguish of</rdg>
			<rdg wit="fMS">of the anguish of</rdg>
		</rdgGrp>
	</app>
	```
- [] This chunk is misaligned. Any variation of 'characterize' are in all versions of Frankenstein. Should be under one &lt;app&gt; node.  
	 ```xml
        <app>
		<rdgGrp n="['']">
			<rdg wit="fMS">&lt;sga-add eID="c57-0121__main__d4e22479"/&gt;&lt;mod
				eID="c57-0121__main__d4e22468"/&gt;</rdg>
		</rdgGrp>
		<rdgGrp n="['characterise']">
			<rdg wit="f1831">characterise</rdg>
		</rdgGrp>
		<rdgGrp n="['characterixe']">
			<rdg wit="f1818">characterixe</rdg>
			<rdg wit="fThomas">characterixe</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['characterize']">
			<rdg wit="f1823">characterize</rdg>
			<rdg wit="fMS">characterize</rdg>
		</rdgGrp>
	</app>	
	```
    - I put longTokens around each variation of 'characterize'. 	
- [] This section is fine. However, 'sir' is split in two different tokens. 
	 ```
	 	<app>
		<rdgGrp n="['', '&lt;mdel&gt;s&lt;/mdel&gt;', 's', '', 'ir,']">
			<rdg wit="fMS">&lt;mod sID="c57-0122__main__d4e22561"/&gt; &lt;mdel&gt;s&lt;/mdel&gt;
				&lt;sga-add place="intralinear" sID="c57-0122__main__d4e22565"/&gt;S &lt;sga-add
				eID="c57-0122__main__d4e22565"/&gt;&lt;mod eID="c57-0122__main__d4e22561"/&gt;
				ir,</rdg>
		</rdgGrp>
		<rdgGrp n="['sir?&#34;']">
			<rdg wit="f1818">Sir?”</rdg>
			<rdg wit="f1823">Sir?”</rdg>
			<rdg wit="fThomas">Sir?”</rdg>
			<rdg wit="f1831">sir?”</rdg>
		</rdgGrp>
	</app>
	```
- [] This section is not necessarily misaligned. But all the tokens are mixed up and are hard to read. May be easier to align by wrapping a longToken for each phrase.
	 ```xml
	<app>
		<rdgGrp n="['be']">
			<rdg wit="f1818">be</rdg>
			<rdg wit="f1823">be</rdg>
			<rdg wit="fThomas">be</rdg>
			<rdg wit="f1831">be</rdg>
		</rdgGrp>
		<rdgGrp n="['all', 'be']">
			<rdg wit="fMS">all be</rdg>
		</rdgGrp>
	</app>

	<app>
		<rdgGrp n="['all', 'true,']">
			<rdg wit="f1818">all true,</rdg>
			<rdg wit="f1823">all true,</rdg>
			<rdg wit="fThomas">all true,</rdg>
			<rdg wit="f1831">all true,</rdg>
		</rdgGrp>
		<rdgGrp n="['true', '–']">
			<rdg wit="fMS">true –</rdg>
		</rdgGrp>
	</app>
	```
- [] This section (specifically the manuscript) is misaligned. 'siezed immedietely' should be in the next &lt;app&gt; node. 
	 ```xml
	<app>
		<rdgGrp n="['hospitality ;']">
			<rdg wit="fThomas">hospitality&lt;hi
				eID="novel1_letter4_chapter20_div4_div22_p26_hi1"/&gt;;</rdg>
		</rdgGrp>
		<rdgGrp
			n="['hospitality', '&lt;del&gt;but prejudiced against you.&lt;/del&gt;', 'siezed', 'immediately']">
			<rdg wit="fMS">&lt;lb n="c57-0125__main__7"/&gt;hospitality &lt;del rend="strikethrough"
				xml:id="c57-0125__main__d4e23123"&gt;but prejudiced against you.&lt;/del&gt; &lt;lb
				n="c57-0125__main__8"/&gt;Siezed immediately</rdg>
		</rdgGrp>
		<rdgGrp n="['hospitality;']">
			<rdg wit="f1818">hospitality;</rdg>
			<rdg wit="f1823">hospitality;</rdg>
			<rdg wit="f1831">hospitality;</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['seized', 'immediately,']">
			<rdg wit="f1818">seized immediately,</rdg>
			<rdg wit="f1823">seized immediately,</rdg>
			<rdg wit="fThomas">seized immediately,</rdg>
			<rdg wit="f1831">seized immediately,</rdg>
		</rdgGrp>
	</app>
	```
    - Put longToken around 'seized immediately' in manuscript.	
- [] This section is misaligned. Ernest should be in next &lt;app&gt; node. 
	 ```xml
	<app>
		<rdgGrp n="['safe', 'and', 'elizabeth', 'and', 'ernest.']">
			<rdg wit="fMS">&lt;lb n="c57-0127__main__10"/&gt;safe &amp; Elizabeth &amp;
				Ernest.</rdg>
		</rdgGrp>
		<rdgGrp n="['safe—and', 'elizabeth—and']">
			<rdg wit="f1818">safe—and Elizabeth—and</rdg>
			<rdg wit="f1823">safe—and Elizabeth—and</rdg>
			<rdg wit="fThomas">safe—and Elizabeth—and</rdg>
			<rdg wit="f1831">safe—and Elizabeth—and</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['ernest', '?&#34;']">
			<rdg wit="f1823">Ernest ?”</rdg>
		</rdgGrp>
		<rdgGrp n="['ernest?&#34;']">
			<rdg wit="f1818">Ernest?”</rdg>
			<rdg wit="fThomas">Ernest?”</rdg>
			<rdg wit="f1831">Ernest?”</rdg>
		</rdgGrp>
	</app>
	```
    - put a longToken around 'Ernest.' in manuscript 
- [] This section is fine, I think. However, the it is quite messy and one of the &lt;app&gt; groups only have two witnesses.
	 ```xml
	<app>
		<rdgGrp n="['on']">
			<rdg wit="f1818">on</rdg>
			<rdg wit="f1823">on</rdg>
			<rdg wit="fThomas">&lt;hi sID="novel1_letter4_chapter20_div4_div22_p44_hi2"/&gt;on&lt;hi
				eID="novel1_letter4_chapter20_div4_div22_p44_hi2"/&gt;</rdg>
			<rdg wit="f1831">on</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['in']">
			<rdg wit="fThomas">&lt;add place="margin"&gt;in&lt;/add&gt;</rdg>
			<rdg wit="fMS">in</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['the', 'orkney']">
			<rdg wit="f1818">the Orkney</rdg>
			<rdg wit="f1823">the Orkney</rdg>
			<rdg wit="fThomas">the Orkney</rdg>
			<rdg wit="f1831">the Orkney</rdg>
			<rdg wit="fMS">the orkney</rdg>
		</rdgGrp>
	</app>
	```
    - I will wrap 'I was on/in the Orkney' in manuscript.	
