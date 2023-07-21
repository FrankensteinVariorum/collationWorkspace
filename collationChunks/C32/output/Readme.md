# chunk 32 notes
- [X] Misalignment. 'existence' in manuscript should be in the following app node.
    ```
	<app>
		<rdgGrp n="['real', '&lt;del&gt;ly&lt;/del&gt;', 'exist', 'ence,', '']">
			<rdg wit="fMS">real &lt;del rend="strikethrough"
				xml:id="c57-0168__main__d4e33145"&gt;ly&lt;/del&gt; exist &lt;sga-add hand="#pbs"
				place="intralinear" sID="c57-0168__main__d4e33148"/&gt;ence, &lt;sga-add
				eID="c57-0168__main__d4e33148"/&gt;</rdg>
		</rdgGrp>
		<rdgGrp n="['really']">
			<rdg wit="f1818">really</rdg>
			<rdg wit="f1823">really</rdg>
			<rdg wit="fThomas">really</rdg>
			<rdg wit="f1831">really</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['existence!']">
			<rdg wit="f1823">existence!</rdg>
			<rdg wit="f1831">existence!</rdg>
		</rdgGrp>
		<rdgGrp n="['existence;']">
			<rdg wit="f1818">existence;</rdg>
			<rdg wit="fThomas">existence;</rdg>
		</rdgGrp>
	</app>
    ```	
    - 2023-07-19: Wrapped longToken around "Such a monster has then really existence! I" in all versions.
- [X] Misalignment. 'formation' should be in the following app.
    ```
	<app>
		<rdgGrp n="['creature’s']">
			<rdg wit="f1818">creature’s</rdg>
			<rdg wit="f1823">creature’s</rdg>
			<rdg wit="fThomas">creature’s</rdg>
			<rdg wit="f1831">creature’s</rdg>
		</rdgGrp>
		<rdgGrp n="['formation']">
			<rdg wit="fMS">formation</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['formation:']">
			<rdg wit="f1831">formation:</rdg>
		</rdgGrp>
		<rdgGrp n="['formation;']">
			<rdg wit="f1818">formation;</rdg>
			<rdg wit="f1823">formation;</rdg>
			<rdg wit="fThomas">formation;</rdg>
		</rdgGrp>
	</app>
    ```	
    - 2023-07-19: Wrapped longToken around "From Frankenstein the particulars of his creature’s formation; but on this point he was impenetrable" in all versions.
- [X] Misaligned. 
    ```
	<app>
		<rdgGrp n="['demoniacal', 'enemy?']">
			<rdg wit="f1818">demoniacal enemy?</rdg>
			<rdg wit="f1823">demoniacal enemy?</rdg>
			<rdg wit="fThomas">demoniacal enemy?</rdg>
			<rdg wit="f1831">demoniacal enemy?</rdg>
		</rdgGrp>
		<rdgGrp n="['dæmonic', 'al', 'ene', '', '&lt;mdel&gt;n&lt;/mdel&gt;', 'm', '', 'y']">
			<rdg wit="fMS">dæmonic &lt;sga-add place="sublinear"
				sID="c57-0169__main__d4e33212"/&gt;al &lt;sga-add
				eID="c57-0169__main__d4e33212"/&gt;&lt;lb n="c57-0169__main__6"/&gt;ene &lt;mod
				sID="c57-0169__main__d4e33217"/&gt; &lt;mdel&gt;n&lt;/mdel&gt; &lt;sga-add
				place="intralinear" sID="c57-0169__main__d4e33221"/&gt;m &lt;sga-add
				eID="c57-0169__main__d4e33221"/&gt;&lt;mod eID="c57-0169__main__d4e33217"/&gt;
				y</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['or', 'to', 'what', 'do']">
			<rdg wit="f1818">Or to what do</rdg>
			<rdg wit="fThomas">Or to what do</rdg>
			<rdg wit="fMS">or to what do</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['your', 'questions']">
			<rdg wit="f1818">your questions</rdg>
			<rdg wit="fThomas">your questions</rdg>
		</rdgGrp>
		<rdgGrp n="['&lt;del&gt;es&lt;/del&gt;', 'your', 'questions']">
			<rdg wit="fMS">&lt;del rend="strikethrough"
				xml:id="c57-0169__main__d4e33225"&gt;es&lt;/del&gt; your questions</rdg>
		</rdgGrp>
	</app>
    ```	
    - 2023-07-19: Wrap all versions of "the world a demoniacal enemy?"/"the world a demoniacal enemy? Or to what do your questions tend?" in longToken
- [X] This section is fine. However, it may be more appropritae to put these nodes under a single app node
    ```
	<app>
		<rdgGrp n="['his', 'shattered']">
			<rdg wit="f1818">his shattered</rdg>
			<rdg wit="f1823">his shattered</rdg>
			<rdg wit="fThomas">his shattered</rdg>
			<rdg wit="f1831">his shattered</rdg>
			<rdg wit="fMS">his shattered</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['', '&lt;del&gt;mind&lt;/del&gt;', '', '']">
			<rdg wit="fMS">&lt;mod sID="c57-0169__main__d4e33444"/&gt; &lt;del rend="strikethrough"
				xml:id="c57-0169__main__d4e33446"&gt;mind&lt;/del&gt; &lt;sga-add place="sublinear"
				sID="c57-0169__main__d4e33449"/&gt; &lt;metamark
				function="insert"&gt;^&lt;/metamark&gt;</rdg>
		</rdgGrp>
		<rdgGrp n="['spirit']">
			<rdg wit="f1823">spirit</rdg>
			<rdg wit="f1831">spirit</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['feelings']">
			<rdg wit="f1818">feelings</rdg>
			<rdg wit="fThomas">feelings</rdg>
			<rdg wit="fMS">&lt;sga-add eID="c57-0169__main__d4e33449"/&gt;&lt;sga-add
				place="superlinear" sID="c57-0169__main__d4e33455"/&gt;feelings</rdg>
		</rdgGrp>
	</app>
    ```
    - 2023-07-19: Wrapped longToken around all versions of "compose his shattered spirit"/"compose his shattered feelings"
- [X] Not necessarily misaligned, but the rdgGrps have less than four witnesses.
    ```
	<app>
		<rdgGrp n="['but', 'the']">
			<rdg wit="f1818">but the</rdg>
			<rdg wit="f1823">but the</rdg>
			<rdg wit="fThomas">but the</rdg>
			<rdg wit="f1831">but the</rdg>
			<rdg wit="fMS">but the</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['real']">
			<rdg wit="f1818">real</rdg>
			<rdg wit="fThomas">real</rdg>
			<rdg wit="fMS">real</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['beings']">
			<rdg wit="f1818">beings</rdg>
			<rdg wit="f1823">beings</rdg>
			<rdg wit="fThomas">beings</rdg>
			<rdg wit="f1831">beings</rdg>
			<rdg wit="fMS">beings</rdg>
		</rdgGrp>
	</app>
    ```	
    - 2023-07-19: Wrapped longToken around all versions of "fancy, but the beings themselves"
- [X] misaligned?
    ```
	<app>
		<rdgGrp n="['believed', 'myself']">
			<rdg wit="f1823">believed myself</rdg>
			<rdg wit="f1831">believed myself</rdg>
		</rdgGrp>
		<rdgGrp n="['felt', 'as', 'if', 'i']">
			<rdg wit="f1818">felt as if I</rdg>
			<rdg wit="fThomas">felt as if I</rdg>
			<rdg wit="fMS">felt as if I</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['was']">
			<rdg wit="fMS">was</rdg>
		</rdgGrp>
		<rdgGrp n="['were']">
			<rdg wit="f1818">were</rdg>
			<rdg wit="fThomas">were</rdg>
		</rdgGrp>
	</app>
    ```	
    - Wrapped all versions of "I believed myself destined for some great enterprise." in longToken
- [X] Misalignment
    ```
	<app>
		<rdgGrp n="['merits;']">
			<rdg wit="f1818">merits;</rdg>
			<rdg wit="f1823">merits;</rdg>
			<rdg wit="fThomas">merits;</rdg>
			<rdg wit="f1831">merits;</rdg>
		</rdgGrp>
		<rdgGrp n="['sake', '–and']">
			<rdg wit="fMS">sake –and</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['and']">
			<rdg wit="f1823">and</rdg>
			<rdg wit="f1831">and</rdg>
		</rdgGrp>
		<rdgGrp n="['and,']">
			<rdg wit="f1818">and,</rdg>
			<rdg wit="fThomas">and,</rdg>
		</rdgGrp>
	</app>
    ```
    - Wrapped longToken around all versions of "own merits; and"/"own sake –and"