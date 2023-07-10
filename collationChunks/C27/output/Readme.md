# chunk 27 notes
## initial schema review
- [X] This chunk is misaligned. Any variation of 'characterize' are in all versions of Frankenstein. Should be under one &lt;app&gt; node.  
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
- [X] This section is fine. However, 'sir' is split in two different tokens. 
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
- [x] This section is not necessarily misaligned. But all the tokens are mixed up and are hard to read. May be easier to align by wrapping a longToken for each phrase.
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
    - Put longToken around each variation. "be all true,"/"all be true -"	
    - I am pretty sure.this is 	
    - Honestly I think this is fine but, this needs to be looked at by someone else. 	
- [X] This section (specifically the manuscript) is misaligned. 'siezed immedietely' should be in the next &lt;app&gt; node. 
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
    - Put longToken around 'seized immediately' in all versions.	
- [X] This section is misaligned. Ernest should be in next &lt;app&gt; node. 
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
    - put a longToken around 'Ernest.' in all versions 
- [X] This section is fine, I think. However, the it is quite messy and one of the &lt;app&gt; groups only have two witnesses.
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
    - I will wrap 'I was on/in' in manuscript.	
- [X] This section is fine, however it is a bit awkward.
	 ```xml
	<app>
		<rdgGrp n="['an', 'agitation']">
			<rdg wit="f1818">an agitation</rdg>
			<rdg wit="f1823">an agitation</rdg>
			<rdg wit="fThomas">an agitation</rdg>
			<rdg wit="f1831">an agitation</rdg>
		</rdgGrp>
		<rdgGrp n="['too', 'great', 'an', 'agitation']">
			<rdg wit="fMS">too great &lt;lb n="c57-0127__main__25"/&gt;an agitation</rdg>
		</rdgGrp>
	</app>

	<app>
		<rdgGrp n="['too', 'great']">
			<rdg wit="f1818">too great</rdg>
			<rdg wit="f1823">too great</rdg>
			<rdg wit="fThomas">too great</rdg>
			<rdg wit="f1831">too great</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['to', 'be', 'endured', 'in', 'my', 'weak']">
			<rdg wit="f1818">to be endured in my weak</rdg>
			<rdg wit="f1823">to be endured in my weak</rdg>
			<rdg wit="fThomas">to be endured in my weak</rdg>
			<rdg wit="f1831">to be endured in my weak</rdg>
			<rdg wit="fMS">to be endured in my &lt;lb n="c57-0127__main__26"/&gt;weak</rdg>
		</rdgGrp>
	</app>
	```
    - Wrapped longToken around 'was too great an agitation to be' in all versions . 
- [X] At the near bottom of the collation chunk, a large section of the 1831 version is completely reworked, compared to the others.
    - I wrapped the entire rewritten section in a longToken. 
- [X] This section is misaligned. 'death' should be in the next &lt;app&gt;
	 ```xml
	<app>
		<rdgGrp n="['in']">
			<rdg wit="f1818">in</rdg>
			<rdg wit="f1823">in</rdg>
			<rdg wit="fThomas">in</rdg>
			<rdg wit="f1831">in</rdg>
		</rdgGrp>
		<rdgGrp n="['of', 'death']">
			<rdg wit="fMS">of death</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['death,']">
			<rdg wit="f1818">death,</rdg>
			<rdg wit="fThomas">death,</rdg>
		</rdgGrp>
		<rdgGrp n="['death.']">
			<rdg wit="f1823">death.</rdg>
			<rdg wit="f1831">death.</rdg>
		</rdgGrp>
	</app>
	```	
    - put longToken around 'death' in manuscript. 
        - this did not work
    - 2023-07-06: Wrapping all variations of "in death."/"in death,"/"of death". I do not think this will work since "of" and "in" are different works, and the punctuation at the end varies. But who knwows it may work.  
        - major w
- [X] This section is fine. However, the schema marks it as yellow on the file. It is annoying.
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
    - Wrap each 'that faintly reminds me of the anguish of recognition.' in a longToken
- [X] This section is fine. But it may look cleaner and remove the schema marker if 'which to me was' was pushed into the neighboring &lt;app&gt;
	```
	<app>
		<rdgGrp n="['be', 'let', 'loose']">
			<rdg wit="f1818">be let loose</rdg>
			<rdg wit="fThomas">be let loose</rdg>
			<rdg wit="fMS">be &lt;lb n="c57-0124__main__5"/&gt;let loose</rdg>
		</rdgGrp>
		<rdgGrp n="['remain', 'in a world which to me was replete with wretchedness.']">
			<rdg wit="f1823">remain &lt;longToken&gt;in a world which to me was replete with
				wretchedness.&lt;/longToken&gt;</rdg>
			<rdg wit="f1831">remain &lt;longToken&gt;in a world which to me was replete with
				wretchedness.&lt;/longToken&gt;</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['in a world replete with &lt;del&gt;whrect&lt;/del&gt;   wretchedness.', '']">
			<rdg wit="fMS">&lt;longToken&gt;in a world replete with &lt;del rend="strikethrough"
				xml:id="c57-0124__main__d4e22942"&gt;whrect&lt;/del&gt; &lt;lb
				n="c57-0124__main__6"/&gt; &lt;sga-add hand="#pbs" place="superlinear"
				sID="c57-0124__main__d4e22947"/&gt;wretchedness.&lt;/longToken&gt; &lt;sga-add
				eID="c57-0124__main__d4e22947"/&gt;&lt;anchor xml:id="c57-0124.02"/&gt;</rdg>
		</rdgGrp>
		<rdgGrp n="['in a world replete with wretchedness.']">
			<rdg wit="f1818">&lt;longToken&gt;in a world replete with
				wretchedness.&lt;/longToken&gt;</rdg>
			<rdg wit="fThomas">&lt;longToken&gt;in a world replete with
				wretchedness.&lt;/longToken&gt;</rdg>
		</rdgGrp>
	</app>
	```
    - longToken around 'in a world replete with wretchedness.' for all versions
    - 2023-07-04: As of this timemark, the current changes to this section failed to align appropriately.
    - 2023-07-06: Putting longToken around variations of "to bet let loose" and "to remain". Is this an appropriate method? Will it even work???
        - No. It isn't a good method and it did not work. I am going to remove all longTokens from this section and start over. 
    -  2023-07-07: lengthening and combining longTokens
- [X] This section is really weird. I think it is misaligned. Most variations are the same except for the manuscript.
	```
	<app>
		<rdgGrp n="['the']">
			<rdg wit="f1818">the</rdg>
			<rdg wit="f1823">the</rdg>
			<rdg wit="fThomas">the</rdg>
			<rdg wit="f1831">the</rdg>
		</rdgGrp>
		<rdgGrp n="['&lt;del&gt;w&lt;/del&gt;', 'life', 'would', 'afford', 'the']">
			<rdg wit="fMS">&lt;del rend="strikethrough"
				xml:id="c57-0124__main__d4e22959"&gt;w&lt;/del&gt; life would afford the</rdg>
		</rdgGrp>
	</app>

	<app>
		<rdgGrp n="['law,', 'less', 'innocent', 'than', 'poor', 'justine', 'had', 'been.']">
			<rdg wit="f1818">law, less innocent than poor Justine had been.</rdg>
			<rdg wit="f1823">law, less innocent than poor Justine had been.</rdg>
			<rdg wit="fThomas">law, less innocent than poor Justine had been.</rdg>
			<rdg wit="f1831">law, less innocent than poor Justine had been.</rdg>
		</rdgGrp>
		<rdgGrp n="['only', 'consolation', 'that', 'i', 'was', 'capable', 'of', 'receiving.']">
			<rdg wit="fMS">only &lt;w ana="start"/&gt;consola&lt;lb
				n="c57-0124__main__10"/&gt;tion&lt;w ana="end"/&gt; that I was capable of
				receiving.</rdg>
		</rdgGrp>
	</app>
	```
    - Wrap all witnesses of 'of the law' in each variation. 	
- [X] This section is misaligned. variations of shuddering should be pushed down. 
	```
	<app>
		<rdgGrp n="['remembered']">
			<rdg wit="f1818">remembered</rdg>
			<rdg wit="f1823">remembered</rdg>
			<rdg wit="fThomas">remembered</rdg>
			<rdg wit="fMS">&lt;w ana="start"/&gt;remem&lt;lb n="c57-0131__main__13"/&gt;bered&lt;w
				ana="end"/&gt;</rdg>
		</rdgGrp>
		<rdgGrp n="['remembered,', 'shuddering,']">
			<rdg wit="f1831">remembered, shuddering,</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['shuddering']">
			<rdg wit="f1818">shuddering</rdg>
			<rdg wit="f1823">shuddering</rdg>
			<rdg wit="fThomas">shuddering</rdg>
		</rdgGrp>
		<rdgGrp n="['with', 'shuddering']">
			<rdg wit="fMS">with shuddering</rdg>
		</rdgGrp>
	</app>
	```
    - 2023-07-06: I am going to wrap all varations of "remembered, shuddering,"/"remembered shuddering"/"remembered with shuddering".	
## Pass 1 notes
- The chunk's initial alignment passing is done. Ready for review.
- [x] 2023-07-10 ebb: Correcting/simplifying alignment around three-witness section: 
   "you, but you will be hanged/hung when the next session comes"
- [x] 1831 "Immediately upon your being taken ill" passage: wrap in longTokens to line up witnesses, which come back together at: 
   "that I might discover some trace"
- [x] longToken for all witnesses except fMS at "endeavoured by dwelling" to "abode of cheerfulness"
      Witnesses reunite at "What a place"
- [x] long 1831 passage near the end out of alignment: MOVE longToken back further "restrain me from...committing..."
- [x] Fix chapter heading alignments so MS joins the rest of the editions.

## Hand Edit (later)
2023-07-10 ebb: This passage in 1831 needs to be moved far down. It's a second longToken sitting after another longToken:

```
&lt;longToken&gt;&lt;pb
				xml:id="F1831_v_180" n="164"/&gt;It was midnight. I lay on the deck, looking at the
				stars,&lt;/longToken&gt;
```				