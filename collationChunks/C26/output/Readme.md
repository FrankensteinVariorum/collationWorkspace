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

- [ ] ### apps with less than 5 rdgs

- [ ] ```xml
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
  ```

- [x] ```xml
  <!-- search `had not hesitated` to locate -->
  <app>
      <rdgGrp n="['selfishness']">
          <rdg wit="f1818">selfishness</rdg>
          <rdg wit="f1823">selfishness</rdg>
          <rdg wit="fThomas">selfishness</rdg>
          <rdg wit="f1831">selfishness</rdg>
      </rdgGrp>
  </app>
  ```
  
- [x] ```xml
  <app>
      <rdgGrp n="['solemn']">
          <rdg wit="f1818">solemn</rdg>
          <rdg wit="f1823">solemn</rdg>
          <rdg wit="fThomas">solemn</rdg>
          <rdg wit="f1831">solemn</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['the', 'sickening', 'oppression', 'of']">
          <rdg wit="f1818">the sickening oppression of</rdg>
          <rdg wit="f1823">the sickening oppression of</rdg>
          <rdg wit="fThomas">the sickening oppression of</rdg>
          <rdg wit="f1831">the sickening oppression of</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `Do you dare` to locate -->
  <app>
      <rdgGrp n="['to']">
          <rdg wit="f1818">to</rdg>
          <rdg wit="f1823">to</rdg>
          <rdg wit="fThomas">to</rdg>
          <rdg wit="f1831">to</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['of', 'scotland.']">
          <rdg wit="f1823">of Scotland.</rdg>
          <rdg wit="fThomas">of Scotland.</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `create another like` to locate -->
  <app>
      <rdgGrp n="['i']">
          <rdg wit="f1818">I</rdg>
          <rdg wit="f1823">I</rdg>
          <rdg wit="fThomas">I</rdg>
          <rdg wit="f1831">I</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `in vice` to locate -->
  <app>
      <rdgGrp n="['a']">
          <rdg wit="f1818">a</rdg>
          <rdg wit="f1823">a</rdg>
          <rdg wit="fThomas">a</rdg>
          <rdg wit="f1831">a</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `detestation and scorn` to locate -->
  <app>
      <rdgGrp n="['man!']">
          <rdg wit="f1823">Man!</rdg>
          <rdg wit="f1831">Man!</rdg>
      </rdgGrp>
      <rdgGrp n="['man,']">
          <rdg wit="f1818">Man,</rdg>
          <rdg wit="fThomas">Man,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `my imagination conjured` to locate -->
  <app>
      <rdgGrp n="['while']">
          <rdg wit="f1818">while</rdg>
          <rdg wit="f1823">while</rdg>
          <rdg wit="fThomas">while</rdg>
          <rdg wit="f1831">while</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `again I thought` to locate -->
  <app>
      <rdgGrp n="['again']">
          <rdg wit="f1818">again</rdg>
          <rdg wit="f1823">again</rdg>
          <rdg wit="fThomas">again</rdg>
          <rdg wit="f1831">again</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `or to see those` to locate -->
  <app>
      <rdgGrp n="['whom']">
          <rdg wit="f1818">whom</rdg>
          <rdg wit="f1823">whom</rdg>
          <rdg wit="fThomas">whom</rdg>
          <rdg wit="f1831">whom</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['elapsed']">
          <rdg wit="f1818">elapsed</rdg>
          <rdg wit="f1823">elapsed</rdg>
          <rdg wit="fThomas">elapsed</rdg>
      </rdgGrp>
      <rdgGrp n="['', '&lt;del&gt;passed&lt;/del&gt;', '', '', 'elapsed']">
          <rdg wit="fMS">&lt;mod sID="c57-0110__main__d4e20178"/&gt; &lt;del rend="strikethrough"
              xml:id="c57-0110__main__d4e20180"&gt;passed&lt;/del&gt; &lt;sga-add
              place="sublinear" sID="c57-0110__main__d4e20183"/&gt; &lt;metamark
              function="insert"&gt;^&lt;/metamark&gt; &lt;sga-add
              eID="c57-0110__main__d4e20183"/&gt;&lt;sga-add place="superlinear"
              sID="c57-0110__main__d4e20189"/&gt;elapsed</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['since', 'we', 'had', 'quitted']">
          <rdg wit="f1818">since we had quitted </rdg>
          <rdg wit="f1823">since we had quitted </rdg>
          <rdg wit="fThomas">since we had quitted </rdg>
          <rdg wit="fMS">&lt;sga-add eID="c57-0110__main__d4e20189"/&gt;&lt;mod
              eID="c57-0110__main__d4e20178"/&gt;since we had quitted</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['switzerland']">
          <rdg wit="fMS">Switzerland</rdg>
      </rdgGrp>
      <rdgGrp n="['switzerland,']">
          <rdg wit="f1818">Switzerland,</rdg>
          <rdg wit="f1823">Switzerland,</rdg>
          <rdg wit="fThomas">Switzerland,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['and', 'france', 'was', 'yet', 'unvisited.']">
          <rdg wit="f1818">and France was yet unvisited.</rdg>
          <rdg wit="f1823">and France was yet unvisited.</rdg>
          <rdg wit="fThomas">and France was yet unvisited.</rdg>
          <rdg wit="fMS">&lt;lb n="c57-0110__main__2"/&gt;and France was yet unvisited.</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['in', 'a', 'week', 'from']">
          <rdg wit="f1818">in a week from</rdg>
          <rdg wit="f1823">in a week from</rdg>
          <rdg wit="fThomas">in a week from</rdg>
          <rdg wit="fMS">in a week from</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `we might` to locate -->
  <app>
      <rdgGrp n="['time']">
          <rdg wit="fMS">&lt;lb n="c57-0110__main__5"/&gt;time</rdg>
      </rdgGrp>
      <rdgGrp n="['time,']">
          <rdg wit="f1818">time,</rdg>
          <rdg wit="f1823">time,</rdg>
          <rdg wit="fThomas">time,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['when']">
          <rdg wit="f1818">when</rdg>
          <rdg wit="f1823">when</rdg>
          <rdg wit="fThomas">when</rdg>
          <rdg wit="fMS">when</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['the', 'plan', 'of', 'our', 'future', 'proceedings.']">
          <rdg wit="f1818">the plan of our future proceedings.</rdg>
          <rdg wit="f1823">the plan of our future proceedings.</rdg>
          <rdg wit="fThomas">the plan of our future proceedings.</rdg>
      </rdgGrp>
      <rdgGrp
              n="['&lt;del&gt;our&lt;/del&gt;', 'the', 'plan', 'of', 'our', 'future', 'proceedings.']">
          <rdg wit="fMS">&lt;del rend="strikethrough"
              xml:id="c57-0110__main__d4e20205"&gt;our&lt;/del&gt; the plan &lt;lb
              n="c57-0110__main__6"/&gt;of our future proceedings.</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `reflect: I must pack` to locate -->
  <app>
      <rdgGrp n="['up']">
          <rdg wit="f1823">up</rdg>
          <rdg wit="f1831">up</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `could be more complete` to locate -->
  <app>
      <rdgGrp n="['a']">
          <rdg wit="f1818">a</rdg>
          <rdg wit="f1823">a</rdg>
          <rdg wit="fThomas">a</rdg>
          <rdg wit="f1831">a</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `chilled by the north-east` to locate -->
  <app>
      <rdgGrp n="['then']">
          <rdg wit="f1818">then</rdg>
          <rdg wit="f1823">then</rdg>
          <rdg wit="fThomas">then</rdg>
          <rdg wit="f1831">then</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `rising. But` to locate -->
  <app>
      <rdgGrp n="['me,']">
          <rdg wit="f1818">me,</rdg>
          <rdg wit="f1823">me,</rdg>
          <rdg wit="fThomas">me,</rdg>
          <rdg wit="f1831">me,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `or be swallowed up in` to locate -->
  <app>
      <rdgGrp n="['the']">
          <rdg wit="f1818">the</rdg>
          <rdg wit="f1823">the</rdg>
          <rdg wit="fThomas">the</rdg>
          <rdg wit="f1831">the</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['&lt;note&gt;thomas copy: pencil mark joins paragraphs.&lt;/note&gt;']">
          <rdg wit="fThomas">&lt;note resp="#ebb"&gt;Thomas copy: pencil mark joins
              paragraphs.&lt;/note&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['&lt;p-end/&gt;', '&lt;p-start/&gt;']">
          <rdg wit="f1818">&lt;p eID="novel1_letter4_chapter19_div4_div21_p26"/&gt; &lt;p
              sID="novel1_letter4_chapter19_div4_div21_p27"/&gt;</rdg>
          <rdg wit="f1823">&lt;p eID="novel1_letter4_chapter19_div4_div20_p26"/&gt; &lt;p
              sID="novel1_letter4_chapter19_div4_div20_p27"/&gt;</rdg>
          <rdg wit="f1831">&lt;p eID="novel1_letter4_chapter20_div4_div20_p26"/&gt; &lt;p
              sID="novel1_letter4_chapter20_div4_div20_p27"/&gt;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['flood', 'of']">
          <rdg wit="f1818">flood of</rdg>
          <rdg wit="f1823">flood of</rdg>
          <rdg wit="fThomas">flood of</rdg>
          <rdg wit="f1831">flood of</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `It had a` to locate -->
  <app>
      <rdgGrp n="['and']">
          <rdg wit="f1818">and</rdg>
          <rdg wit="f1823">and</rdg>
          <rdg wit="fThomas">and</rdg>
          <rdg wit="f1831">and</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `could most easily procure` to locate -->
  <app>
      <rdgGrp n="['i']">
          <rdg wit="f1818">I</rdg>
          <rdg wit="f1823">I</rdg>
          <rdg wit="fThomas">I</rdg>
          <rdg wit="f1831">I</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `much surprised at my` to locate -->
  <app>
      <rdgGrp n="['very']">
          <rdg wit="f1818">very</rdg>
          <rdg wit="fThomas">very</rdg>
          <rdg wit="fMS">very</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `spoke English` to locate -->
  <app>
      <rdgGrp n="['english;']">
          <rdg wit="f1818">English;</rdg>
          <rdg wit="f1823">English;</rdg>
          <rdg wit="fThomas">English;</rdg>
          <rdg wit="f1831">English;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `therefore addressed` to locate -->
  <app>
      <rdgGrp n="['i']">
          <rdg wit="f1818">I</rdg>
          <rdg wit="f1823">I</rdg>
          <rdg wit="fThomas">I</rdg>
          <rdg wit="f1831">I</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `it is not the custom of` to locate -->
  <app>
      <rdgGrp n="['&#34;surely']">
          <rdg wit="f1818">“surely</rdg>
          <rdg wit="f1823">“surely</rdg>
          <rdg wit="fThomas">“surely</rdg>
          <rdg wit="f1831">“surely</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `in a few` to locate -->
  <app>
      <rdgGrp n="['to']">
          <rdg wit="f1818">to</rdg>
          <rdg wit="f1823">to</rdg>
          <rdg wit="fThomas">to</rdg>
          <rdg wit="f1831">to</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `frightful events` to locate -->
  <app>
      <rdgGrp n="['frightful']">
          <rdg wit="f1818">frightful</rdg>
          <rdg wit="f1823">frightful</rdg>
          <rdg wit="fThomas">frightful</rdg>
          <rdg wit="f1831">frightful</rdg>
      </rdgGrp>
  </app>
  ```
