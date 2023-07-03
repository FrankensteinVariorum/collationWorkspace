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