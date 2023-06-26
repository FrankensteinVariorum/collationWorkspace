- [x] Misalignment: In MS, it is `One evening I sat` while in other editions it is `I sat one evening`. This difference cause `One everning` in MS going up. 

  - Wrapping longToken around `One evening I sat` in MS

  ```xml
  <app>
  		<rdgGrp n="['']">
  			<rdg wit="f1818">&lt;pb xml:id="F1818_v3_044" n="040"/&gt;</rdg>
  			<rdg wit="f1823">&lt;pb xml:id="F1823_v2_401" n="128"/&gt;</rdg>
  			<rdg wit="fThomas">&lt;pb xml:id="F1818_v3_044" n="040"/&gt;</rdg>
  			<rdg wit="f1831">&lt;pb xml:id="F1831_v_162" n="146"/&gt;</rdg>
  		</rdgGrp>
  		<rdgGrp n="['&lt;p-start/&gt;', 'one', 'evening']">
  			<rdg wit="fMS">&lt;milestone unit="tei:p-START"/&gt; &lt;lb
  				n="c57-0102__main__24"/&gt;One evening</rdg>
  		</rdgGrp>
  	</app>
  	<app>
  		<rdgGrp n="['chapter iii.']">
  			<rdg wit="f1818">&lt;head&gt;CHAPTER III.&lt;/head&gt;</rdg>
  			<rdg wit="fThomas">&lt;head&gt;CHAPTER III.&lt;/head&gt;</rdg>
  		</rdgGrp>
  		<rdgGrp n="['chapter viii.']">
  			<rdg wit="f1823">&lt;head&gt;CHAPTER VIII.&lt;/head&gt;</rdg>
  		</rdgGrp>
  		<rdgGrp n="['chapter xx.']">
  			<rdg wit="f1831">&lt;head&gt;CHAPTER XX.&lt;/head&gt;</rdg>
  		</rdgGrp>
  	</app>
  	<app>
  		<rdgGrp n="['&lt;p-start/&gt;']">
  			<rdg wit="f1818">&lt;p sID="novel1_letter4_chapter19_div4_div21_p1"/&gt;</rdg>
  			<rdg wit="f1823">&lt;p sID="novel1_letter4_chapter19_div4_div20_p1"/&gt;</rdg>
  			<rdg wit="fThomas">&lt;p sID="novel1_letter4_chapter19_div4_div21_p1"/&gt;</rdg>
  			<rdg wit="f1831">&lt;p sID="novel1_letter4_chapter20_div4_div20_p1"/&gt;</rdg>
  		</rdgGrp>
  	</app>
  	<app>
  		<rdgGrp n="['i', 'sat']">
  			<rdg wit="f1818">I &lt;hi sID="novel1_letter4_chapter19_div4_div21_p1_hi1"/&gt;SAT&lt;hi
  				eID="novel1_letter4_chapter19_div4_div21_p1_hi1"/&gt;</rdg>
  			<rdg wit="f1823">I &lt;hi sID="novel1_letter4_chapter19_div4_div20_p1_hi1"/&gt;SAT&lt;hi
  				eID="novel1_letter4_chapter19_div4_div20_p1_hi1"/&gt;</rdg>
  			<rdg wit="fThomas">I &lt;hi
  				sID="novel1_letter4_chapter19_div4_div21_p1_hi1"/&gt;SAT&lt;hi
  				eID="novel1_letter4_chapter19_div4_div21_p1_hi1"/&gt;</rdg>
  			<rdg wit="f1831">I &lt;hi sID="novel1_letter4_chapter20_div4_div20_p1_hi1"/&gt;SAT&lt;hi
  				eID="novel1_letter4_chapter20_div4_div20_p1_hi1"/&gt;</rdg>
  			<rdg wit="fMS">I sat</rdg>
  		</rdgGrp>
  	</app>
  ```

- [x] merge two apps by wrapping `sufficient light` by longToken in 1818, 1823, Thomas, and 1831:

```xml
<app>
    <rdgGrp n="['sufficient']">
        <rdg wit="f1818">sufficient</rdg>
        <rdg wit="f1823">sufficient</rdg>
        <rdg wit="fThomas">sufficient</rdg>
        <rdg wit="f1831">sufficient</rdg>
    </rdgGrp>
    <rdgGrp n="['light', 'sufficient']">
    	<rdg wit="fMS">&lt;lb n="c57-0102__main__27"/&gt;light sufficient</rdg>
    </rdgGrp>
</app>

<app>
    <rdgGrp n="['light']">
        <rdg wit="f1818">light</rdg>
        <rdg wit="f1823">light</rdg>
        <rdg wit="fThomas">light</rdg>
        <rdg wit="f1831">light</rdg>
    </rdgGrp>
</app>
```

- [x] merge two apps by wrapping `me to` by longToken in 1818, 1823, Thomas, and 1831:

```xml
<app>
    <rdgGrp n="['me']">
        <rdg wit="f1818">me</rdg>
        <rdg wit="f1823">me</rdg>
        <rdg wit="fThomas">me</rdg>
        <rdg wit="f1831">me</rdg>
    </rdgGrp>
    <rdgGrp n="['to', 'me']">
        <rdg wit="fMS">to me</rdg>
    </rdgGrp>
</app>

<app>
    <rdgGrp n="['to']">
        <rdg wit="f1818">to</rdg>
        <rdg wit="f1823">to</rdg>
        <rdg wit="fThomas">to</rdg>
        <rdg wit="f1831">to</rdg>
    </rdgGrp>
</app>
```

- [x] the space at the end of the norm in MS. This problem is caused by the line `normalized = RE_WORD_END.sub(' ', normalized)` in collate.py. I wanna add another regex to remove the space at the end of the norm: `normalized = re.sub(r'\s+$', '', normalized)`. 

```xml
<app>
    <rdgGrp n="['already ']">
        <rdg wit="fMS">&lt;w ana="start"/&gt;al&lt;lb n="c57-0103__main__15"/&gt;ready&lt;w
            ana="end"/&gt;</rdg>
    </rdgGrp>
    <rdgGrp n="['already']">
        <rdg wit="f1818">already</rdg>
        <rdg wit="f1823">already</rdg>
        <rdg wit="fThomas">already</rdg>
        <rdg wit="f1831">already</rdg>
    </rdgGrp>
</app>
```

- [x] Misalignment: wrapping longToken around  `the earth from whose form &amp; mind` in MS

```xml
<app>
    <rdgGrp n="['up', 'on']">
        <rdg wit="fMS">&lt;lb n="c57-0103__main__29"/&gt;&lt;sga-add hand="#pbs"
            place="intralinear" sID="c57-0103__main__d4e19003"/&gt;up &lt;sga-add
            eID="c57-0103__main__d4e19003"/&gt;on</rdg>
    </rdgGrp>
    <rdgGrp n="['upon', 'the', 'earth,', 'who', 'might', 'make']">
        <rdg wit="f1818">upon the earth, who might make</rdg>
        <rdg wit="f1823">upon the earth, who might make</rdg>
        <rdg wit="fThomas">upon the earth, who might make</rdg>
        <rdg wit="f1831">upon the earth, who might make</rdg>
    </rdgGrp>
</app>
<app>
    <rdgGrp n="['the']">
        <rdg wit="f1818">the</rdg>
        <rdg wit="f1823">the</rdg>
        <rdg wit="fThomas">the</rdg>
        <rdg wit="f1831">the</rdg>
        <rdg wit="fMS">the</rdg>
    </rdgGrp>
</app>
<app>
    <rdgGrp n="['earth', 'from', 'whose', 'form', 'and', 'mind']">
        <rdg wit="fMS">earth from whose form &amp; mind</rdg>
    </rdgGrp>
    <rdgGrp n="['very', 'existence', 'of', 'the', 'species', 'of']">
        <rdg wit="f1818">very existence of the species of</rdg>
        <rdg wit="f1823">very existence of the species of</rdg>
        <rdg wit="fThomas">very existence of the species of</rdg>
        <rdg wit="f1831">very existence of the species of</rdg>
    </rdgGrp>
</app>
```

- [x] Misalignment: the second app should go up. Wrapping `a right,` with longToken in 1818, 1823, and Thomas

```xml
<app>
    <rdgGrp n="['a']">
        <rdg wit="f1818">a</rdg>
        <rdg wit="f1823">a</rdg>
        <rdg wit="fThomas">a</rdg>
    </rdgGrp>
    <rdgGrp n="['any', '', 'right', '', '&lt;del&gt;for&lt;/del&gt;']">
        <rdg wit="fMS">&lt;sga-add hand="#pbs" place="superlinear"
            sID="c57-0103__main__d4e19020"/&gt;any &lt;sga-add
            eID="c57-0103__main__d4e19020"/&gt; right &lt;lb n="c57-0103__main__31"/&gt; &lt;del
            rend="strikethrough" xml:id="c57-0103__main__d4e19025"&gt;for&lt;/del&gt;</rdg>
    </rdgGrp>
</app>
<app>
    <rdgGrp n="['right,']">
        <rdg wit="f1818">right,</rdg>
        <rdg wit="f1823">right,</rdg>
        <rdg wit="fThomas">right,</rdg>
        <rdg wit="f1831">right,</rdg>
    </rdgGrp>
</app>
```

- [x] Muddle combination: `beware!your` in MS. Wrapping `beware!` with longToken in MS.

```xml
<app>
    <rdgGrp n="['beware!', 'your']">
        <rdg wit="f1818">beware! Your</rdg>
        <rdg wit="f1823">beware! Your</rdg>
        <rdg wit="fThomas">beware! Your</rdg>
        <rdg wit="f1831">beware! your</rdg>
    </rdgGrp>
    <rdgGrp n="['beware!your']">
        <rdg wit="fMS">beware!&lt;lb n="c57-0107__main__1"/&gt;Your</rdg>
    </rdgGrp>
</app>
```

- [x] Misalignment: caused by a long different paragraph in 1831:

- wrapping with longToken for this paragraph in 1831: 

```xml
he was wearing away his time
            fruitlessly where he was; that letters from the friends he had formed in London desired
            his return to complete the negotiation they had entered into for his Indian enterprise.
            He could not any longer delay his departure; but as his journey to London might be
            followed, even sooner than he now conjectured, by his longer voyage,
```

- [x] Muddle combination in MS:
- expected to add a space after start tag of `<w>` in collate.py
  - This fix might cause an extra space before a norm with a single word, so we should remove the space at the beginning of norm with regex `normalized = re.sub(r'^\s+', '', normalized)`

```xml
<app>
    <rdgGrp n="['was', 'north-east,']">
        <rdg wit="f1818">was north-east,</rdg>
        <rdg wit="f1823">was north-east,</rdg>
        <rdg wit="fThomas">was north-east,</rdg>
        <rdg wit="f1831">was north-east,</rdg>
    </rdgGrp>
    <rdgGrp n="['wasnorth-east ']">
        <rdg wit="fMS">was&lt;w ana="start"/&gt;north-&lt;lb
            n="c57-0112__main__21"/&gt;east&lt;w ana="end"/&gt;</rdg>
    </rdgGrp>
</app>
```

- [x] Misalignment in MS: wrapping ` <sga-add place="superlinear" sID="c57-0112__main__d4e20641"/>made the <sga-add eID="c570112__main__d4e20641"/><mod eID="c57-0112__main__d4e20633"/>` with longToken in MS

```xml
<app>
    <rdgGrp n="['made', 'the']">
        <rdg wit="f1818">made the</rdg>
        <rdg wit="f1823">made the</rdg>
        <rdg wit="fThomas">made the</rdg>
        <rdg wit="f1831">made the</rdg>
    </rdgGrp>
    <rdgGrp n="['', '', 'made', 'the']">
        <rdg wit="fMS">&lt;mod sID="c57-0112__main__d4e20633"/&gt;&lt;sga-add place="sublinear"
            sID="c57-0112__main__d4e20635"/&gt; &lt;metamark
            function="insert"&gt;^&lt;/metamark&gt; &lt;sga-add
            eID="c57-0112__main__d4e20635"/&gt;&lt;sga-add place="superlinear"
            sID="c57-0112__main__d4e20641"/&gt;made the</rdg>
    </rdgGrp>
</app>

<app>
    <rdgGrp n="['']">
        <rdg wit="fMS">&lt;sga-add eID="c57-0112__main__d4e20641"/&gt;&lt;mod
            eID="c57-0112__main__d4e20633"/&gt;</rdg>
    </rdgGrp>
    <rdgGrp n="['attempt,']">
        <rdg wit="f1823">attempt,</rdg>
        <rdg wit="f1831">attempt,</rdg>
    </rdgGrp>
</app>
<app>
    <rdgGrp n="['attempt']">
        <rdg wit="f1818">attempt</rdg>
        <rdg wit="fThomas">attempt</rdg>
        <rdg wit="fMS">attempt</rdg>
    </rdgGrp>
</app>
```

 
