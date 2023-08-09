- [x] misalignment:

```xml
<app>
    <rdgGrp n="['chap. 9', '', 'on']">
        <rdg wit="fMS">&lt;longToken&gt;Chap. 9&lt;/longToken&gt; &lt;shi
            rend="sup"&gt;&lt;/shi&gt; &lt;anchor xml:id="c56-0073.05"/&gt;&lt;lb
            n="c56-0073__main__2"/&gt;On</rdg>
    </rdgGrp>
    <rdgGrp n="['chapter vi.']">
        <rdg wit="f1818">&lt;head&gt;CHAPTER VI.&lt;/head&gt;</rdg>
        <rdg wit="f1823">&lt;head&gt;CHAPTER VI.&lt;/head&gt;</rdg>
        <rdg wit="fThomas">&lt;head&gt;CHAPTER VI.&lt;/head&gt;</rdg>
    </rdgGrp>
    <rdgGrp n="['chapter vii.']">
        <rdg wit="f1831">&lt;head&gt;CHAPTER VII.&lt;/head&gt;</rdg>
    </rdgGrp>
</app>
<app>
    <rdgGrp n="['&lt;p-start/&gt;']">
        <rdg wit="f1818">&lt;p sID="novel1_letter4_chapter6_div4_div6_p1"/&gt;</rdg>
        <rdg wit="f1823">&lt;p sID="novel1_letter4_chapter6_div4_div6_p1"/&gt;</rdg>
        <rdg wit="fThomas">&lt;p sID="novel1_letter4_chapter6_div4_div6_p1"/&gt;</rdg>
        <rdg wit="f1831">&lt;p sID="novel1_letter4_chapter7_div4_div7_p1"/&gt;</rdg>
    </rdgGrp>
</app>
<app>
    <rdgGrp n="['o n ,']">
        <rdg wit="f1823">O&lt;hi sID="novel1_letter4_chapter6_div4_div6_p1_hi1"/&gt;N&lt;hi
            eID="novel1_letter4_chapter6_div4_div6_p1_hi1"/&gt;,</rdg>
    </rdgGrp>
    <rdgGrp n="['o n']">
        <rdg wit="f1818">O&lt;hi sID="novel1_letter4_chapter6_div4_div6_p1_hi1"/&gt;N&lt;hi
            eID="novel1_letter4_chapter6_div4_div6_p1_hi1"/&gt;</rdg>
        <rdg wit="fThomas">O&lt;hi sID="novel1_letter4_chapter6_div4_div6_p1_hi1"/&gt;N&lt;hi
            eID="novel1_letter4_chapter6_div4_div6_p1_hi1"/&gt;</rdg>
        <rdg wit="f1831">O&lt;hi sID="novel1_letter4_chapter7_div4_div7_p1_hi1"/&gt;N&lt;hi
            eID="novel1_letter4_chapter7_div4_div7_p1_hi1"/&gt;</rdg>
    </rdgGrp>
</app>
```

merge apps:

```xml
<app>
    <rdgGrp n="['father.', '', 'to v. frankenstein  geneva – june 2', '            d– 17—', 'my']">
        <rdg wit="fMS">father. &lt;lb n="c56-0073__main__4"/&gt; &lt;longToken&gt;To V.–Frankenstein &lt;lb n="c56-0073__main__5"/&gt;Geneva – June 2&lt;shi rend="sup"&gt; d&lt;/shi&gt;– 17—&lt;/longToken&gt; &lt;lb n="c56-0073__main__6"/&gt;My</rdg>
    </rdgGrp>
    <rdgGrp n="['father:—', '&lt;p-end/&gt;']">
        <rdg wit="f1818">father:— &lt;p eID="novel1_letter4_chapter6_div4_div6_p1"/&gt;</rdg>
        <rdg wit="f1823">father:— &lt;p eID="novel1_letter4_chapter6_div4_div6_p1"/&gt;</rdg>
        <rdg wit="fThomas">father:— &lt;p eID="novel1_letter4_chapter6_div4_div6_p1"/&gt;</rdg>
        <rdg wit="f1831">father:— &lt;p eID="novel1_letter4_chapter7_div4_div7_p1"/&gt;</rdg>
    </rdgGrp>
</app>
<app>
    <rdgGrp n="['&#34;to', 'v.', 'frankenstein.']">
        <rdg wit="f1818">&lt;ab sID="novel1_letter4_chapter6_div4_div6_ab1"/&gt;&lt;hi sID="novel1_letter4_chapter6_div4_div6_ab1_hi1"/&gt;”To&lt;hi eID="novel1_letter4_chapter6_div4_div6_ab1_hi1"/&gt; V. F&lt;hi sID="novel1_letter4_chapter6_div4_div6_ab1_hi2"/&gt;RANKENSTEIN&lt;hi eID="novel1_letter4_chapter6_div4_div6_ab1_hi2"/&gt;.&lt;ab eID="novel1_letter4_chapter6_div4_div6_ab1"/&gt;</rdg>
        <rdg wit="f1823">&lt;ab sID="novel1_letter4_chapter6_div4_div6_ab1"/&gt;&lt;hi sID="novel1_letter4_chapter6_div4_div6_ab1_hi1"/&gt;”To&lt;hi eID="novel1_letter4_chapter6_div4_div6_ab1_hi1"/&gt; V. F&lt;hi sID="novel1_letter4_chapter6_div4_div6_ab1_hi2"/&gt;RANKENSTEIN&lt;hi eID="novel1_letter4_chapter6_div4_div6_ab1_hi2"/&gt;.&lt;ab eID="novel1_letter4_chapter6_div4_div6_ab1"/&gt;</rdg>
    </rdgGrp>
    <rdgGrp n="['&lt;del&gt;  &#34;to v. frankenstein. &lt;/del&gt;']">
        <rdg wit="fThomas">&lt;del rend="strikethrough" medium="pencil"&gt; &lt;ab sID="novel1_letter4_chapter6_div4_div6_del1_ab1"/&gt; &lt;hi sID="novel1_letter4_chapter6_div4_div6_del1_ab1_hi1"/&gt;”To&lt;hi eID="novel1_letter4_chapter6_div4_div6_del1_ab1_hi1"/&gt; V. F&lt;hi sID="novel1_letter4_chapter6_div4_div6_del1_ab1_hi2"/&gt;RANKENSTEIN&lt;hi eID="novel1_letter4_chapter6_div4_div6_del1_ab1_hi2"/&gt;.&lt;ab eID="novel1_letter4_chapter6_div4_div6_del1_ab1"/&gt; &lt;/del&gt;</rdg>
    </rdgGrp>
</app>
<app>
    <rdgGrp n="['&lt;p-start/&gt;', '&#34;my']">
        <rdg wit="f1818">&lt;p sID="novel1_letter4_chapter6_div4_div6_p2"/&gt; “&lt;hi sID="novel1_letter4_chapter6_div4_div6_p2_hi1"/&gt;MY</rdg>
        <rdg wit="f1823">&lt;p sID="novel1_letter4_chapter6_div4_div6_p2"/&gt; “&lt;hi sID="novel1_letter4_chapter6_div4_div6_p2_hi1"/&gt;MY</rdg>
        <rdg wit="fThomas">&lt;p sID="novel1_letter4_chapter6_div4_div6_p2"/&gt; “&lt;hi sID="novel1_letter4_chapter6_div4_div6_p2_hi1"/&gt;MY</rdg>
        <rdg wit="f1831">&lt;p sID="novel1_letter4_chapter7_div4_div7_p2"/&gt; “My</rdg>
    </rdgGrp>
</app>
```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['only']">
          <rdg wit="f1818">only</rdg>
          <rdg wit="f1823">only</rdg>
          <rdg wit="fThomas">only</rdg>
          <rdg wit="f1831">only</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['a', 'few']">
          <rdg wit="f1818">a few</rdg>
          <rdg wit="f1823">a few</rdg>
          <rdg wit="fThomas">a few</rdg>
          <rdg wit="f1831">a few</rdg>
          <rdg wit="fMS">a few</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge these apps:

  ```xml
  <app>
      <rdgGrp n="['&#34;last', 'thursday', '(may']">
          <rdg wit="f1818">“Last Thursday (May</rdg>
          <rdg wit="f1823">“Last Thursday (May</rdg>
          <rdg wit="fThomas">“Last Thursday (May</rdg>
          <rdg wit="f1831">“Last Thursday (May</rdg>
      </rdgGrp>
      <rdgGrp
              n="['last', 'thurday', '(may &lt;del&gt;26&lt;/del&gt; 28th)', 'i;', '', '&lt;del&gt;your my  &lt;/del&gt;', '', '&lt;del&gt;cousin&lt;/del&gt;']">
          <rdg wit="fMS">&lt;lb n="c56-0074__main__1"/&gt;Last thurday &lt;longToken&gt;(May
              &lt;del rend="strikethrough" xml:id="c56-0074__main__d5e15491"&gt;26&lt;/del&gt;
              28&lt;shi rend="underline"&gt;th&lt;/shi&gt;)&lt;/longToken&gt; I; &lt;mod
              sID="c56-0074__main__d5e15497"/&gt; &lt;del rend="strikethrough"
              xml:id="c56-0074__main__d5e15499"&gt;your &lt;sga-add place="superlinear"
              sID="c56-0074__main__d5e15501"/&gt;my &lt;sga-add
              eID="c56-0074__main__d5e15501"/&gt; &lt;/del&gt; &lt;mod
              eID="c56-0074__main__d5e15497"/&gt; &lt;del rend="strikethrough"
              xml:id="c56-0074__main__d5e15507"&gt;cousin&lt;/del&gt;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['7th)']">
          <rdg wit="f1818">7th)</rdg>
          <rdg wit="f1823">7th)</rdg>
          <rdg wit="fThomas">7th)</rdg>
      </rdgGrp>
      <rdgGrp n="['7th),']">
          <rdg wit="f1831">7th),</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['i,']">
          <rdg wit="f1818">I,</rdg>
          <rdg wit="f1823">I,</rdg>
          <rdg wit="fThomas">I,</rdg>
          <rdg wit="f1831">I,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge these apps:

  ```xml
  <app>
      <rdgGrp n="['came', '&lt;del&gt;up&lt;/del&gt;', 'and enquired', 'for']">
          <rdg wit="fMS">came &lt;del rend="strikethrough"
              xml:id="c56-0074__main__d5e15565"&gt;up&lt;/del&gt; &amp;&lt;lb
              n="c56-0074__main__12"/&gt;enquired for</rdg>
      </rdgGrp>
      <rdgGrp n="['came,', 'and']">
          <rdg wit="f1818">came, and</rdg>
          <rdg wit="f1823">came, and</rdg>
          <rdg wit="fThomas">came, and</rdg>
          <rdg wit="f1831">came, and</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['enquired']">
          <rdg wit="f1831">enquired</rdg>
      </rdgGrp>
      <rdgGrp n="['inquired']">
          <rdg wit="f1818">inquired</rdg>
          <rdg wit="f1823">inquired</rdg>
          <rdg wit="fThomas">inquired</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['if', 'we', 'had', 'seen']">
          <rdg wit="f1818">if we had seen</rdg>
          <rdg wit="f1823">if we had seen</rdg>
          <rdg wit="fThomas">if we had seen</rdg>
          <rdg wit="f1831">if we had seen</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs

  ```xml
  <app>
      <rdgGrp n="['when', 'i', 'thought']">
          <rdg wit="f1818">when I thought</rdg>
          <rdg wit="f1823">when I thought</rdg>
          <rdg wit="fThomas">when I thought</rdg>
          <rdg wit="f1831">when I thought</rdg>
          <rdg wit="fMS">when I thought</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['that']">
          <rdg wit="f1818">that</rdg>
          <rdg wit="f1823">that</rdg>
          <rdg wit="fThomas">that</rdg>
          <rdg wit="f1831">that</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['miniature']">
          <rdg wit="f1818">miniature</rdg>
          <rdg wit="f1823">miniature</rdg>
          <rdg wit="fThomas">miniature</rdg>
          <rdg wit="f1831">miniature</rdg>
          <rdg wit="fMS">miniature</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['that']">
          <rdg wit="f1818">that</rdg>
          <rdg wit="f1823">that</rdg>
          <rdg wit="fThomas">that</rdg>
          <rdg wit="f1831">that</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['the', 'despair', 'that', 'succeeded', 'to', 'the', 'joy', 'i']">
          <rdg wit="f1818">the despair that succeeded to the joy I</rdg>
          <rdg wit="f1823">the despair that succeeded to the joy I</rdg>
          <rdg wit="fThomas">the despair that succeeded to the joy I</rdg>
          <rdg wit="f1831">the despair that succeeded to the joy I</rdg>
          <rdg wit="fMS">the despair that succeeded to the joy &lt;lb
              n="c56-0076__main__27"/&gt;I</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['at', 'first']">
          <rdg wit="f1818">at first</rdg>
          <rdg wit="f1823">at first</rdg>
          <rdg wit="fThomas">at first</rdg>
          <rdg wit="f1831">at first</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge the two rdgGrp by remove the space after `new` in MS

  ```xml
  <!-- search `receiving` to locate -->
  <app>
      <rdgGrp n="['new', 's', '']">
          <rdg wit="fMS">new &lt;sga-add hand="#pbs" place="intralinear"
              sID="c56-0076__main__d5e16085"/&gt;s &lt;sga-add
              eID="c56-0076__main__d5e16085"/&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['news']">
          <rdg wit="f1818">news</rdg>
          <rdg wit="f1823">news</rdg>
          <rdg wit="fThomas">news</rdg>
          <rdg wit="f1831">news</rdg>
      </rdgGrp>
  </app>
  ```

- [x] word fusion: henryendeavoured in `MS`

  - add a space after `henry`

  ```xml
  <app>
      <rdgGrp n="['walk', '&lt;del&gt;c&lt;/del&gt;', 'henryendeavoured ']">
          <rdg wit="fMS">walk &lt;del rend="strikethrough"
              xml:id="c56-0077__main__d5e16236"&gt;C&lt;/del&gt; Henry&lt;w
              ana="start"/&gt;endeav&lt;lb n="c56-0077__main__14"/&gt;oured&lt;w
              ana="end"/&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['walk,', 'clerval', 'endeavoured']">
          <rdg wit="f1818">walk, Clerval endeavoured</rdg>
          <rdg wit="f1823">walk, Clerval endeavoured</rdg>
          <rdg wit="fThomas">walk, Clerval endeavoured</rdg>
          <rdg wit="f1831">walk, Clerval endeavoured</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['said']">
          <rdg wit="f1818">said</rdg>
          <rdg wit="f1823">said</rdg>
          <rdg wit="fThomas">said</rdg>
          <rdg wit="f1831">said</rdg>
          <rdg wit="fMS">said</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['he,']">
          <rdg wit="f1818">he,</rdg>
          <rdg wit="f1823">he,</rdg>
          <rdg wit="fThomas">he,</rdg>
          <rdg wit="f1831">he,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge two apps:

  ```xml
  <app>
      <rdgGrp n="['&#34;dear', 'lovely', 'child,']">
          <rdg wit="f1831">“dear lovely child,</rdg>
      </rdgGrp>
      <rdgGrp n="['&#34;that', 'dear']">
          <rdg wit="f1818">“that dear</rdg>
          <rdg wit="f1823">“that dear</rdg>
          <rdg wit="fThomas">“that dear</rdg>
          <rdg wit="fMS">"that dear</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&#34;child']">
          <rdg wit="fMS">&lt;lb n="c56-0077__main__18"/&gt;"child</rdg>
      </rdgGrp>
      <rdgGrp n="['child;']">
          <rdg wit="f1818">child;</rdg>
          <rdg wit="f1823">child;</rdg>
          <rdg wit="fThomas">child;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs: 

  ```xml
  <app>
      <rdgGrp n="['rest']">
          <rdg wit="fMS">rest</rdg>
      </rdgGrp>
      <rdgGrp
              n="['rest.', 'the', 'pang', 'is', 'over,', 'his', 'sufferings', 'are', 'at', 'an', 'end', 'for', 'ever.']">
          <rdg wit="f1831">rest. The pang is over, his sufferings are at an end for ever.</rdg>
      </rdgGrp>
      <rdgGrp n="['rest:']">
          <rdg wit="f1818">rest:</rdg>
          <rdg wit="f1823">rest:</rdg>
          <rdg wit="fThomas">rest:</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['he', 'does', 'not', 'now', 'feel', 'the']">
          <rdg wit="f1818">he does not &lt;pb xml:id="F1818_v1_153" n="141"/&gt;now feel the</rdg>
          <rdg wit="f1823">he does not &lt;pb xml:id="F1823_v1_160" n="141"/&gt;now feel the</rdg>
          <rdg wit="fThomas">he does not &lt;pb xml:id="F1818_v1_153" n="141"/&gt;now feel
              the</rdg>
          <rdg wit="fMS">he does not now feel the</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&#34;murderers', 'grasp', '–']">
          <rdg wit="fMS">&lt;lb n="c56-0077__main__21"/&gt;"murderers grasp –</rdg>
      </rdgGrp>
      <rdgGrp n="['murderer’s', 'grasp;']">
          <rdg wit="f1818">murderer’s grasp;</rdg>
          <rdg wit="f1823">murderer’s grasp;</rdg>
          <rdg wit="fThomas">murderer’s grasp;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['no', 'longer', 'be', 'a']">
          <rdg wit="f1818">no longer be a</rdg>
          <rdg wit="f1823">no longer be a</rdg>
          <rdg wit="fThomas">no longer be a</rdg>
          <rdg wit="f1831">no longer be a</rdg>
          <rdg wit="fMS">no longer be a</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['fit']">
          <rdg wit="f1818">fit</rdg>
          <rdg wit="f1823">fit</rdg>
          <rdg wit="fThomas">fit</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge these apps: 1831 misses a long content.

  ```xml
  <app>
      <rdgGrp n="['pity', 'his', '&#34;survivors']">
          <rdg wit="fMS">pity his &lt;lb n="c56-0077__main__24"/&gt;"survivors</rdg>
      </rdgGrp>
      <rdgGrp n="['pity;']">
          <rdg wit="f1818">pity;</rdg>
          <rdg wit="f1823">pity;</rdg>
          <rdg wit="fThomas">pity;</rdg>
          <rdg wit="f1831">pity;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['the', 'survivors']">
          <rdg wit="f1818">the survivors</rdg>
          <rdg wit="f1823">the survivors</rdg>
          <rdg wit="fThomas">the survivors</rdg>
      </rdgGrp>
      <rdgGrp n="['we', 'must', 'reserve']">
          <rdg wit="f1831">we must reserve</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['are', 'the', 'greatest']">
          <rdg wit="f1818">are the greatest</rdg>
          <rdg wit="f1823">are the greatest</rdg>
          <rdg wit="fThomas">are the greatest</rdg>
          <rdg wit="fMS">are the greatest</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['sufferers']">
          <rdg wit="fMS">sufferers</rdg>
      </rdgGrp>
      <rdgGrp n="['sufferers,']">
          <rdg wit="f1818">sufferers,</rdg>
          <rdg wit="f1823">sufferers,</rdg>
          <rdg wit="fThomas">sufferers,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['and']">
          <rdg wit="f1818">and</rdg>
          <rdg wit="f1823">and</rdg>
          <rdg wit="fThomas">and</rdg>
          <rdg wit="fMS">and</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&#34;for']">
          <rdg wit="fMS">&lt;lb n="c56-0077__main__25"/&gt;"for</rdg>
      </rdgGrp>
      <rdgGrp n="['for']">
          <rdg wit="f1818">for</rdg>
          <rdg wit="f1823">for</rdg>
          <rdg wit="fThomas">for</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['them', 'time', 'is', 'the']">
          <rdg wit="f1818">them time is the</rdg>
          <rdg wit="f1823">them time is the</rdg>
          <rdg wit="fThomas">them time is the</rdg>
          <rdg wit="fMS">them time is the</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['only', 'consolation.']">
          <rdg wit="f1818">only consolation.</rdg>
          <rdg wit="f1823">only consolation.</rdg>
          <rdg wit="fThomas">only consolation.</rdg>
      </rdgGrp>
      <rdgGrp n="['&lt;del&gt;ir&lt;/del&gt;', 'only', 'consolation.']">
          <rdg wit="fMS">&lt;del rend="vertical_line"
              xml:id="c56-0077__main__d5e16288"&gt;ir&lt;/del&gt; only consolation.</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['&#34;those']">
          <rdg wit="fMS">&lt;lb n="c56-0077__main__26"/&gt;"Those</rdg>
      </rdgGrp>
      <rdgGrp n="['those']">
          <rdg wit="f1818">Those</rdg>
          <rdg wit="f1823">Those</rdg>
          <rdg wit="fThomas">Those</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['maxims', 'of', 'the']">
          <rdg wit="f1818">maxims of the</rdg>
          <rdg wit="f1823">maxims of the</rdg>
          <rdg wit="fThomas">maxims of the</rdg>
          <rdg wit="fMS">maxims of the</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['stoics']">
          <rdg wit="fMS">stoics</rdg>
      </rdgGrp>
      <rdgGrp n="['stoics,']">
          <rdg wit="f1818">Stoics,</rdg>
          <rdg wit="f1823">Stoics,</rdg>
          <rdg wit="fThomas">Stoics,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['that', 'death']">
          <rdg wit="f1818">that death</rdg>
          <rdg wit="f1823">that death</rdg>
          <rdg wit="fThomas">that death</rdg>
          <rdg wit="fMS">that death</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&#34;was']">
          <rdg wit="fMS">&lt;lb n="c56-0077__main__27"/&gt;"was</rdg>
      </rdgGrp>
      <rdgGrp n="['was']">
          <rdg wit="f1818">was</rdg>
          <rdg wit="f1823">was</rdg>
          <rdg wit="fThomas">was</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['no']">
          <rdg wit="f1818">no</rdg>
          <rdg wit="f1823">no</rdg>
          <rdg wit="fThomas">no</rdg>
          <rdg wit="fMS">no</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['evil']">
          <rdg wit="fMS">evil</rdg>
      </rdgGrp>
      <rdgGrp n="['evil,']">
          <rdg wit="f1818">evil,</rdg>
          <rdg wit="f1823">evil,</rdg>
          <rdg wit="fThomas">evil,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['and']">
          <rdg wit="f1818">and</rdg>
          <rdg wit="f1823">and</rdg>
          <rdg wit="fThomas">and</rdg>
          <rdg wit="fMS">and</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['that']">
          <rdg wit="f1818">that</rdg>
          <rdg wit="f1823">that</rdg>
          <rdg wit="fThomas">that</rdg>
          <rdg wit="f1831">that</rdg>
          <rdg wit="fMS">that</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['for']">
          <rdg wit="f1831">for</rdg>
      </rdgGrp>
      <rdgGrp n="['the', 'mind', 'of', 'man']">
          <rdg wit="f1818">the mind of man</rdg>
          <rdg wit="f1823">the mind of man</rdg>
          <rdg wit="fThomas">the mind of man</rdg>
          <rdg wit="fMS">the mind of man</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&#34;ought']">
          <rdg wit="fMS">&lt;lb n="c56-0077__main__28"/&gt;"ought</rdg>
      </rdgGrp>
      <rdgGrp n="['ought']">
          <rdg wit="f1818">ought</rdg>
          <rdg wit="f1823">ought</rdg>
          <rdg wit="fThomas">ought</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['to', 'be', 'superior', 'to']">
          <rdg wit="f1818">to be superior to</rdg>
          <rdg wit="f1823">to be superior to</rdg>
          <rdg wit="fThomas">to be superior to</rdg>
          <rdg wit="fMS">to be superior to</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['despair']">
          <rdg wit="f1818">despair</rdg>
          <rdg wit="f1823">despair</rdg>
          <rdg wit="fThomas">despair</rdg>
      </rdgGrp>
      <rdgGrp n="['&lt;del&gt;that&lt;/del&gt;', 'despair']">
          <rdg wit="fMS">&lt;del rend="strikethrough"
              xml:id="c56-0077__main__d5e16300"&gt;that&lt;/del&gt; despair</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['&#34;on']">
          <rdg wit="fMS">&lt;lb n="c56-0077__main__29"/&gt;"on</rdg>
      </rdgGrp>
      <rdgGrp n="['on']">
          <rdg wit="f1818">on</rdg>
          <rdg wit="f1823">on</rdg>
          <rdg wit="fThomas">on</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['the', 'eternal', 'absence', 'of', 'a', 'beloved']">
          <rdg wit="f1818">the eternal absence of a beloved</rdg>
          <rdg wit="f1823">the eternal absence of a beloved</rdg>
          <rdg wit="fThomas">the eternal absence of a beloved</rdg>
          <rdg wit="fMS">the eternal absence of a beloved</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&#34;object']">
          <rdg wit="fMS">&lt;lb n="c56-0077__main__30"/&gt;"object</rdg>
      </rdgGrp>
      <rdgGrp n="['object,']">
          <rdg wit="f1818">object,</rdg>
          <rdg wit="f1823">object,</rdg>
          <rdg wit="fThomas">object,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['ought', 'not', 'to', 'be']">
          <rdg wit="f1818">ought not to be</rdg>
          <rdg wit="f1823">ought not to be</rdg>
          <rdg wit="fThomas">ought not to be</rdg>
          <rdg wit="fMS">ought not to be</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['urged', '–']">
          <rdg wit="fMS">urged –</rdg>
      </rdgGrp>
      <rdgGrp n="['urged.']">
          <rdg wit="f1818">urged.</rdg>
          <rdg wit="f1823">urged.</rdg>
          <rdg wit="fThomas">urged.</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['even']">
          <rdg wit="f1818">Even</rdg>
          <rdg wit="f1823">Even</rdg>
          <rdg wit="fThomas">Even</rdg>
          <rdg wit="fMS">even</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&#34;cato']">
          <rdg wit="fMS">&lt;lb n="c56-0077__main__31"/&gt;"Cato</rdg>
      </rdgGrp>
      <rdgGrp n="['cato']">
          <rdg wit="f1818">Cato</rdg>
          <rdg wit="f1823">Cato</rdg>
          <rdg wit="fThomas">Cato</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['wept', 'over', 'the', 'dead', 'body', 'of']">
          <rdg wit="f1818">wept over the dead body of</rdg>
          <rdg wit="f1823">wept over the dead body of</rdg>
          <rdg wit="fThomas">wept over the dead body of</rdg>
          <rdg wit="fMS">wept over the dead body of</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['not', 'be']">
          <rdg wit="f1818">not be</rdg>
          <rdg wit="f1823">not be</rdg>
          <rdg wit="fThomas">not be</rdg>
          <rdg wit="f1831">not be</rdg>
          <rdg wit="fMS">&lt;lb n="c56-0078__main__26"/&gt;not be</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['the']">
          <rdg wit="f1818">the</rdg>
          <rdg wit="f1823">the</rdg>
          <rdg wit="fThomas">the</rdg>
          <rdg wit="f1831">the</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge two apps:

  ```xml
  <app>
      <rdgGrp n="['child.']">
          <rdg wit="f1831">child.</rdg>
      </rdgGrp>
      <rdgGrp n="['child:']">
          <rdg wit="f1818">child:</rdg>
          <rdg wit="f1823">child:</rdg>
          <rdg wit="fThomas">child:</rdg>
      </rdgGrp>
      <rdgGrp n="['child–', 'dear', 'mountains']">
          <rdg wit="fMS">child– Dear mountains</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&#34;dear', 'mountains!']">
          <rdg wit="f1818">“Dear mountains!</rdg>
          <rdg wit="f1823">“Dear mountains!</rdg>
          <rdg wit="fThomas">“Dear mountains!</rdg>
          <rdg wit="f1831">“Dear &lt;pb xml:id="F1831_v_076" n="60"/&gt;mountains!</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['the', 'sky', 'and', 'lake', 'are', 'blue']">
          <rdg wit="f1818">the sky and lake are blue</rdg>
          <rdg wit="f1823">the sky and lake are blue</rdg>
          <rdg wit="fThomas">the sky and lake are blue</rdg>
          <rdg wit="f1831">the sky and lake are blue</rdg>
          <rdg wit="fMS">the sky and lake &lt;lb n="c56-0079__main__19"/&gt;are blue</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['and', 'placid.']">
          <rdg wit="f1818">and placid.</rdg>
          <rdg wit="f1823">and placid.</rdg>
          <rdg wit="fThomas">and placid.</rdg>
          <rdg wit="f1831">and placid.</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less then 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['or', 'to', 'mock']">
          <rdg wit="f1818">or to mock</rdg>
          <rdg wit="f1823">or to mock</rdg>
          <rdg wit="fThomas">or to mock</rdg>
          <rdg wit="f1831">or to mock</rdg>
          <rdg wit="fMS">&lt;lb n="c56-0079__main__20"/&gt;or to mock</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['at']">
          <rdg wit="f1818">at</rdg>
          <rdg wit="f1823">at</rdg>
          <rdg wit="fThomas">at</rdg>
          <rdg wit="f1831">at</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['grief', 'and', 'fear']">
          <rdg wit="f1818">grief and fear</rdg>
          <rdg wit="f1823">grief and fear</rdg>
          <rdg wit="fThomas">grief and fear</rdg>
          <rdg wit="f1831">grief and fear</rdg>
          <rdg wit="fMS">grief and &lt;lb n="c56-0080__main__2"/&gt;fear</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['again']">
          <rdg wit="f1818">again</rdg>
          <rdg wit="f1823">again</rdg>
          <rdg wit="fThomas">again</rdg>
          <rdg wit="f1831">again</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['sky']">
          <rdg wit="f1818">sky</rdg>
          <rdg wit="f1823">sky</rdg>
          <rdg wit="fThomas">sky</rdg>
          <rdg wit="f1831">sky</rdg>
      </rdgGrp>
      <rdgGrp n="['', '&lt;del&gt;night&lt;/del&gt;', 'sky']">
          <rdg wit="fMS">&lt;mod sID="c56-0081__main__d5e16932"/&gt; &lt;del rend="strikethrough"
              xml:id="c56-0081__main__d5e16934"&gt;night&lt;/del&gt; &lt;sga-add hand="#pbs"
              place="superlinear" sID="c56-0081__main__d5e16937"/&gt;sky</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['']">
          <rdg wit="fMS">&lt;sga-add eID="c56-0081__main__d5e16937"/&gt;&lt;mod
              eID="c56-0081__main__d5e16932"/&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['above ']">
          <rdg wit="fThomas">&lt;add place="margin"&gt;above &lt;/add&gt;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge two apps:

  ```xml
  <app>
      <rdgGrp
              n="['', '&lt;del&gt;very fine&lt;/del&gt;', 'serene', '', 'and', '', '&lt;del&gt;unable&lt;/del&gt;']">
          <rdg wit="fMS">&lt;mod sID="c56-0081__main__d5e16941"/&gt; &lt;del rend="strikethrough"
              xml:id="c56-0081__main__d5e16943"&gt;very fine&lt;/del&gt; &lt;sga-add hand="#pbs"
              place="superlinear" sID="c56-0081__main__d5e16946"/&gt;serene &lt;sga-add
              eID="c56-0081__main__d5e16946"/&gt;&lt;mod eID="c56-0081__main__d5e16941"/&gt; and
              &lt;lb n="c56-0081__main__6"/&gt; &lt;del rend="strikethrough"
              xml:id="c56-0081__main__d5e16953"&gt;unable&lt;/del&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['serene;']">
          <rdg wit="f1818">serene;</rdg>
          <rdg wit="f1823">serene;</rdg>
          <rdg wit="fThomas">serene;</rdg>
          <rdg wit="f1831">serene;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&lt;del&gt;and,&lt;/del&gt;']">
          <rdg wit="fThomas">&lt;del rend="strikethrough"&gt;and,&lt;/del&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['and,']">
          <rdg wit="f1818">and,</rdg>
          <rdg wit="f1823">and,</rdg>
          <rdg wit="f1831">and,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] word  fusion: the `lb` is treated as a part of the word in MS

  - Add a space after `he` in MS

  ```xml
  <app>
      <rdgGrp n="['he was']">
          <rdg wit="fMS">He&lt;lb n="c56-0083__left_margin__6"/&gt;was</rdg>
      </rdgGrp>
      <rdgGrp n="['he', 'was']">
          <rdg wit="f1818">&lt;hi sID="novel1_letter4_chapter6_div4_div6_p29_hi1"/&gt;He&lt;hi
              eID="novel1_letter4_chapter6_div4_div6_p29_hi1"/&gt; was</rdg>
          <rdg wit="f1823">&lt;hi sID="novel1_letter4_chapter6_div4_div6_p29_hi1"/&gt;He&lt;hi
              eID="novel1_letter4_chapter6_div4_div6_p29_hi1"/&gt; was</rdg>
          <rdg wit="fThomas">&lt;hi sID="novel1_letter4_chapter6_div4_div6_p29_hi1"/&gt;He&lt;hi
              eID="novel1_letter4_chapter6_div4_div6_p29_hi1"/&gt; was</rdg>
          <rdg wit="f1831">&lt;hi sID="novel1_letter4_chapter7_div4_div7_p29_hi1"/&gt;He&lt;hi
              eID="novel1_letter4_chapter7_div4_div7_p29_hi1"/&gt; was</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge these apps:

  ```xml
  <app>
      <rdgGrp n="['mont', 'salêve,', 'a', 'hill', 'that', 'bounds', 'plainpalais', 'on']">
          <rdg wit="f1818">Mont Salêve, a hill that bounds Plainpalais on</rdg>
          <rdg wit="f1823">Mont Salêve, a hill that bounds Plainpalais on</rdg>
          <rdg wit="fThomas">Mont Salêve, a hill that bounds Plainpalais on</rdg>
          <rdg wit="f1831">Mont Salêve, a hill that bounds Plainpalais on</rdg>
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
      <rdgGrp n="['mont-salêve;']">
          <rdg wit="fMS">Mont-Salêve;</rdg>
      </rdgGrp>
      <rdgGrp n="['south.']">
          <rdg wit="f1818">south.</rdg>
          <rdg wit="f1823">south.</rdg>
          <rdg wit="fThomas">south.</rdg>
          <rdg wit="f1831">south.</rdg>
      </rdgGrp>
  </app>
  ```

- [x] word fusion: wrapping `&amps;` with longToken in MS.

  ```xml
  <app>
      <rdgGrp n="['murderer', 'and cause']">
          <rdg wit="fMS">murderer &amp;&lt;lb n="c56-0084__main__16"/&gt;cause</rdg>
      </rdgGrp>
      <rdgGrp n="['murderer,', 'and', 'cause']">
          <rdg wit="f1818">murderer, and cause</rdg>
          <rdg wit="f1823">murderer, and cause</rdg>
          <rdg wit="fThomas">murderer, and cause</rdg>
          <rdg wit="f1831">murderer, and cause</rdg>
      </rdgGrp>
  </app>
  ```

- [x] extra space: move `.` into `w` element in MS

  ```xml
  <!-- search `impenetrable` to locate -->
  <app>
      <rdgGrp n="['darkness .']">
          <rdg wit="fMS">&lt;sga-add eID="c56-0083__main__d5e17657"/&gt;&lt;mod
              eID="c56-0083__main__d5e17643"/&gt;&lt;w ana="start"/&gt;dark&lt;lb
              n="c56-0083__main__17"/&gt;ness&lt;w ana="end"/&gt;.</rdg>
      </rdgGrp>
      <rdgGrp n="['darkness.']">
          <rdg wit="f1818">darkness.</rdg>
          <rdg wit="f1823">darkness.</rdg>
          <rdg wit="fThomas">darkness.</rdg>
          <rdg wit="f1831">darkness.</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge two apps:

  ```xml
  <app>
      <rdgGrp n="['revolved']">
          <rdg wit="f1818">revolved</rdg>
          <rdg wit="f1823">revolved</rdg>
          <rdg wit="fThomas">revolved</rdg>
          <rdg wit="f1831">revolved</rdg>
      </rdgGrp>
      <rdgGrp n="['revolved', 'in', 'my', 'mind', '&lt;del&gt;i', 'revolved']">
          <rdg wit="fMS">revolved in my mind &lt;delSpan rend="strikethrough"
              spanTo="#c56-0083.07"/&gt;I revolved</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['in', 'my', 'mind']">
          <rdg wit="f1818">in my mind</rdg>
          <rdg wit="f1823">in my mind</rdg>
          <rdg wit="fThomas">in my mind</rdg>
          <rdg wit="f1831">in my mind</rdg>
      </rdgGrp>
      <rdgGrp n="['in', 'my', 'mind', '&lt;/del&gt;i', 'resolved', 'in', 'my', 'mind']">
          <rdg wit="fMS">in &lt;lb n="c56-0083__main__18"/&gt;my mind &lt;delSpan
              anchor="c56-0083.07"/&gt;&lt;anchor xml:id="c56-0083.10"/&gt;&lt;lb
              n="c56-0083__left_margin__1"/&gt;&lt;sga-add hand="#pbs"
              sID="c56-0083__left_margin__d5e17681"/&gt;I resolved in my mind</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['elude']">
          <rdg wit="f1818">elude</rdg>
          <rdg wit="f1823">elude</rdg>
          <rdg wit="fThomas">elude</rdg>
          <rdg wit="f1831">elude</rdg>
      </rdgGrp>
      <rdgGrp
              n="['&lt;del&gt;elude all the &lt;unclear&gt;us&lt;/unclear&gt; &lt;/del&gt;', 'elude']">
          <rdg wit="fMS">&lt;del rend="strikethrough" xml:id="c56-0084__main__d5e18094"&gt;elude
              all the &lt;unclear&gt;us&lt;/unclear&gt; &lt;/del&gt; &lt;lb
              n="c56-0084__main__27"/&gt;elude</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['all']">
          <rdg wit="f1818">all</rdg>
          <rdg wit="f1823">all</rdg>
          <rdg wit="fThomas">all</rdg>
          <rdg wit="f1831">all</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge these apps:

  ```xml
  <app>
      <rdgGrp n="['']">
          <rdg wit="fThomas">&lt;pb xml:id="F1818_v1_163" n="151"/&gt;</rdg>
          <rdg wit="fMS">&lt;sga-add eID="c56-0084__main__d5e18134"/&gt;&lt;anchor
              xml:id="c56-0084.07"/&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['and then']">
          <rdg wit="f1831">&lt;longToken&gt;And then&lt;/longToken&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['besides,']">
          <rdg wit="f1818">&lt;pb xml:id="F1818_v1_163" n="151"/&gt;Besides,</rdg>
          <rdg wit="f1823">Besides,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&lt;del&gt;besides&lt;/del&gt;']">
          <rdg wit="fThomas">&lt;del rend="strikethrough"&gt;Besides&lt;/del&gt;</rdg>
      </rdgGrp>
      <rdgGrp
              n="['–', '&lt;del&gt;the com&lt;/del&gt;', '&lt;del&gt;mon', 'people', 'would', 'believe', 'it', 'to', 'be', 'a', 'real', 'devil']">
          <rdg wit="fMS">– &lt;del rend="strikethrough" xml:id="c56-0084__main__d5e18152"&gt;the
              com&lt;/del&gt; &lt;lb n="c56-0085__main__1"/&gt;&lt;delSpan
              spanTo="#c56-0085.02"/&gt;mon people would believe it to &lt;lb
              n="c56-0085__main__2"/&gt;be a real devil</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['and']">
          <rdg wit="fThomas">&lt;add place="margin"&gt;And&lt;/add&gt;</rdg>
          <rdg wit="fMS">and</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="[',']">
          <rdg wit="fThomas">,</rdg>
      </rdgGrp>
      <rdgGrp n="['who', 'could', 'attempt', '&lt;/del&gt;besides']">
          <rdg wit="fMS">who could attempt &lt;delSpan anchor="c56-0085.02"/&gt;&lt;anchor
              xml:id="c56-0085.03"/&gt;&lt;lb n="c56-0085__left_margin__1"/&gt;Besides</rdg>
      </rdgGrp>
  </app>
  ```

- [x] extra space: remove the space after `servant ` in MS

  ```xml
  <app>
      <rdgGrp n="['servant', 's']">
          <rdg wit="fMS">servant &lt;sga-add hand="#pbs" place="intralinear"
              sID="c56-0085__main__d5e18255"/&gt;s</rdg>
      </rdgGrp>
      <rdgGrp n="['servants']">
          <rdg wit="f1818">servants</rdg>
          <rdg wit="f1823">servants</rdg>
          <rdg wit="fThomas">servants</rdg>
          <rdg wit="f1831">servants</rdg>
      </rdgGrp>
  </app>
  ```

- [x] extra space: remove the space after `family` in MS

  ```xml
  <app>
      <rdgGrp n="['family', ',', '']">
          <rdg wit="fMS">family &lt;sga-add hand="#pbs" place="intralinear"
              sID="c56-0085__main__d5e18260"/&gt;, &lt;sga-add
              eID="c56-0085__main__d5e18260"/&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['family,']">
          <rdg wit="f1818">family,</rdg>
          <rdg wit="f1823">family,</rdg>
          <rdg wit="fThomas">family,</rdg>
          <rdg wit="f1831">family,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] extra space: remove the space after `rustic` in MS

  ```xml
  <app>
      <rdgGrp n="['rustic', ',']">
          <rdg wit="fMS">rustic &lt;sga-add hand="#pbs" place="intralinear"
              sID="c56-0085__main__d5e18298"/&gt;,</rdg>
      </rdgGrp>
      <rdgGrp n="['rustic,']">
          <rdg wit="f1818">rustic,</rdg>
          <rdg wit="f1823">rustic,</rdg>
          <rdg wit="fThomas">rustic,</rdg>
          <rdg wit="f1831">rustic,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['her', 'and']">
          <rdg wit="fMS">her and</rdg>
      </rdgGrp>
      <rdgGrp
              n="['her.', 'my tale was not one to announce publicly; its astounding horror would be looked upon as madness by the vulgar. did any one indeed exist, except i, the creator, who would believe, unless his senses convinced him, in the existence of the living monument of presumption and rash ignorance which i had let loose upon the world?']">
          <rdg wit="f1831">her. &lt;longToken&gt;My tale was not one to announce publicly; its
              astounding horror would be looked upon as madness by the vulgar. Did any one indeed
              exist, except I, the creator, who would believe, unless his senses convinced him, in
              the existence of the living monument of presumption and rash ignorance which I had
              let loose upon the world?&lt;/longToken&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['her;', 'and,']">
          <rdg wit="f1818">her; and,</rdg>
          <rdg wit="f1823">her; and,</rdg>
          <rdg wit="fThomas">her; and,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['in', 'this']">
          <rdg wit="f1818">in this</rdg>
          <rdg wit="f1823">in this</rdg>
          <rdg wit="fThomas">in this</rdg>
          <rdg wit="fMS">in this</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['assurance']">
          <rdg wit="fMS">assurance</rdg>
      </rdgGrp>
      <rdgGrp n="['assurance,']">
          <rdg wit="f1818">assurance,</rdg>
          <rdg wit="f1823">assurance,</rdg>
          <rdg wit="fThomas">assurance,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['i', 'calmed']">
          <rdg wit="f1818">I calmed</rdg>
          <rdg wit="f1823">I calmed</rdg>
          <rdg wit="fThomas">I calmed</rdg>
          <rdg wit="fMS">I calmed</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['myself']">
          <rdg wit="fMS">&lt;lb n="c56-0089__main__11"/&gt;myself</rdg>
      </rdgGrp>
      <rdgGrp n="['myself,']">
          <rdg wit="f1818">myself,</rdg>
          <rdg wit="f1823">myself,</rdg>
          <rdg wit="fThomas">myself,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['expecting', 'the', 'trial', 'with']">
          <rdg wit="f1818">expecting the trial with</rdg>
          <rdg wit="f1823">expecting the trial with</rdg>
          <rdg wit="fThomas">expecting the trial with</rdg>
          <rdg wit="fMS">expecting the trial with</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['eagerness']">
          <rdg wit="fMS">eagerness</rdg>
      </rdgGrp>
      <rdgGrp n="['eagerness,']">
          <rdg wit="f1818">eagerness,</rdg>
          <rdg wit="f1823">eagerness,</rdg>
          <rdg wit="fThomas">eagerness,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['but', 'without', 'prognosticating', 'an', 'evil', 'result.']">
          <rdg wit="f1818">but without prognosticating an evil result.</rdg>
          <rdg wit="f1823">but without prognosticating an evil result.</rdg>
          <rdg wit="fThomas">but without prognosticating an evil result.</rdg>
          <rdg wit="fMS">&lt;lb n="c56-0089__main__12"/&gt;but without prognosticating an evil
              &lt;lb n="c56-0089__main__13"/&gt;result.</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['elizabeth.', 'time']">
          <rdg wit="f1818">Elizabeth. Time </rdg>
          <rdg wit="f1823">Elizabeth. Time </rdg>
          <rdg wit="fThomas">Elizabeth. Time </rdg>
          <rdg wit="f1831">Elizabeth. Time </rdg>
          <rdg wit="fMS">&lt;sga-add eID="c56-0090__main__d5e19230"/&gt;&lt;mod
              eID="c56-0090__main__d5e19220"/&gt;Elizabeth. Time</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['had']">
          <rdg wit="f1818">had</rdg>
          <rdg wit="f1823">had</rdg>
          <rdg wit="fThomas">had</rdg>
          <rdg wit="fMS">&lt;lb n="c56-0090__main__3"/&gt;had</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['her']">
          <rdg wit="f1818">her</rdg>
          <rdg wit="f1823">her</rdg>
          <rdg wit="fThomas">her</rdg>
          <rdg wit="f1831">her</rdg>
          <rdg wit="fMS">her</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['form']">
          <rdg wit="f1818">form</rdg>
          <rdg wit="f1823">form</rdg>
          <rdg wit="fThomas">form</rdg>
          <rdg wit="fMS">form</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['since', 'i']">
          <rdg wit="f1818">since I</rdg>
          <rdg wit="f1823">since I</rdg>
          <rdg wit="fThomas">since I</rdg>
          <rdg wit="f1831">since I</rdg>
          <rdg wit="fMS">since &lt;lb n="c56-0090__main__4"/&gt;I</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['had']">
          <rdg wit="f1818">had</rdg>
          <rdg wit="f1823">had</rdg>
          <rdg wit="fThomas">had</rdg>
          <rdg wit="fMS">had</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge two apps:

  ```xml
  <app>
      <rdgGrp n="['never']">
          <rdg wit="f1818">never</rdg>
          <rdg wit="f1823">never</rdg>
          <rdg wit="fThomas">never</rdg>
          <rdg wit="f1831">never</rdg>
      </rdgGrp>
      <rdgGrp n="['shall', 'never']">
          <rdg wit="fMS">shall never</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['shall']">
          <rdg wit="f1818">shall</rdg>
          <rdg wit="f1823">shall</rdg>
          <rdg wit="fThomas">shall</rdg>
          <rdg wit="f1831">shall</rdg>
      </rdgGrp>
  </app>
  ```

- [x] extra space: remove the space before `impossible` in MS

  ```xml
  <app>
      <rdgGrp n="['', 'impossible,']">
          <rdg wit="fMS">&lt;sga-add eID="c56-0091__Pt1__main__d5e19515"/&gt;&lt;anchor
              xml:id="c56-0091.02"/&gt; impossible,</rdg>
      </rdgGrp>
      <rdgGrp n="['impossible:']">
          <rdg wit="f1818">impossible:</rdg>
          <rdg wit="f1823">impossible:</rdg>
          <rdg wit="fThomas">impossible:</rdg>
          <rdg wit="f1831">impossible:</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['father', 'alphonse', 'frankenstein', '', '&lt;del&gt;al&lt;/del&gt;', '', '']">
          <rdg wit="fMS">father &lt;lb n="c56-0076__main__21"/&gt;Alphonse Frankenstein &lt;lb
              n="c56-0076__main__22"/&gt; &lt;del rend="smear"
              xml:id="c56-0076__main__d5e16066"&gt;Al&lt;/del&gt; &lt;lb
              n="c56-0076__main__23"/&gt; &lt;metamark
              function="separate"&gt;_______________&lt;/metamark&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['father,', '&lt;p-end/&gt;', '&lt;p-start/&gt;']">
          <rdg wit="f1818">father, &lt;p eID="novel1_letter4_chapter6_div4_div6_p12"/&gt; &lt;p
              sID="novel1_letter4_chapter6_div4_div6_p13"/&gt;</rdg>
          <rdg wit="f1823">father, &lt;p eID="novel1_letter4_chapter6_div4_div6_p12"/&gt; &lt;p
              sID="novel1_letter4_chapter6_div4_div6_p13"/&gt;</rdg>
          <rdg wit="fThomas">father, &lt;p eID="novel1_letter4_chapter6_div4_div6_p12"/&gt; &lt;p
              sID="novel1_letter4_chapter6_div4_div6_p13"/&gt;</rdg>
          <rdg wit="f1831">father, &lt;p eID="novel1_letter4_chapter7_div4_div7_p12"/&gt; &lt;p
              sID="novel1_letter4_chapter7_div4_div7_p13"/&gt;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&#34;a lphonse']">
          <rdg wit="f1831">“A&lt;hi
              sID="novel1_letter4_chapter7_div4_div7_p13_hi1"/&gt;LPHONSE&lt;hi
              eID="novel1_letter4_chapter7_div4_div7_p13_hi1"/&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['a lphonse']">
          <rdg wit="f1818">A&lt;hi
              sID="novel1_letter4_chapter6_div4_div6_p13_hi1"/&gt;LPHONSE&lt;hi
              eID="novel1_letter4_chapter6_div4_div6_p13_hi1"/&gt;</rdg>
          <rdg wit="f1823">A&lt;hi
              sID="novel1_letter4_chapter6_div4_div6_p13_hi1"/&gt;LPHONSE&lt;hi
              eID="novel1_letter4_chapter6_div4_div6_p13_hi1"/&gt;</rdg>
          <rdg wit="fThomas">A&lt;hi
              sID="novel1_letter4_chapter6_div4_div6_p13_hi1"/&gt;LPHONSE&lt;hi
              eID="novel1_letter4_chapter6_div4_div6_p13_hi1"/&gt;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp
              n="['f rankenstein .', '&lt;p-end/&gt;', '&lt;p-start/&gt;', '&#34;geneva,', 'may', '12th,', '17—.&#34;']">
          <rdg wit="f1818">F&lt;hi
              sID="novel1_letter4_chapter6_div4_div6_p13_hi2"/&gt;RANKENSTEIN&lt;hi
              eID="novel1_letter4_chapter6_div4_div6_p13_hi2"/&gt;. &lt;p
              eID="novel1_letter4_chapter6_div4_div6_p13"/&gt; &lt;p
              sID="novel1_letter4_chapter6_div4_div6_p14"/&gt; “Geneva, May 12th, 17—.”</rdg>
          <rdg wit="f1823">F&lt;hi
              sID="novel1_letter4_chapter6_div4_div6_p13_hi2"/&gt;RANKENSTEIN&lt;hi
              eID="novel1_letter4_chapter6_div4_div6_p13_hi2"/&gt;. &lt;p
              eID="novel1_letter4_chapter6_div4_div6_p13"/&gt; &lt;p
              sID="novel1_letter4_chapter6_div4_div6_p14"/&gt; “Geneva, May 12th, 17—.”</rdg>
          <rdg wit="fThomas">F&lt;hi
              sID="novel1_letter4_chapter6_div4_div6_p13_hi2"/&gt;RANKENSTEIN&lt;hi
              eID="novel1_letter4_chapter6_div4_div6_p13_hi2"/&gt;. &lt;p
              eID="novel1_letter4_chapter6_div4_div6_p13"/&gt; &lt;p
              sID="novel1_letter4_chapter6_div4_div6_p14"/&gt; “Geneva, May 12th, 17—.”</rdg>
          <rdg wit="f1831">F&lt;hi
              sID="novel1_letter4_chapter7_div4_div7_p13_hi2"/&gt;RANKENSTEIN&lt;hi
              eID="novel1_letter4_chapter7_div4_div7_p13_hi2"/&gt;. &lt;p
              eID="novel1_letter4_chapter7_div4_div7_p13"/&gt; &lt;p
              sID="novel1_letter4_chapter7_div4_div7_p14"/&gt; “Geneva, May 12th, 17—.”</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['raise', 'my']">
          <rdg wit="f1818">raise my</rdg>
          <rdg wit="f1823">raise my</rdg>
          <rdg wit="fThomas">raise my</rdg>
          <rdg wit="fMS">raise my</rdg>
      </rdgGrp>
      <rdgGrp n="['say', 'a', 'few', 'words']">
          <rdg wit="f1831">say a few words</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['spirits.']">
          <rdg wit="f1818">spirits.</rdg>
          <rdg wit="f1823">spirits.</rdg>
          <rdg wit="fThomas">spirits.</rdg>
      </rdgGrp>
      <rdgGrp n="['spirits–']">
          <rdg wit="fMS">spirits–</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['he', 'did', 'not', 'do', 'this', 'by']">
          <rdg wit="f1818">He did not do this by</rdg>
          <rdg wit="f1823">He did not do this by</rdg>
          <rdg wit="fThomas">He did not do this by</rdg>
          <rdg wit="fMS">He did not &lt;lb n="c56-0077__main__15"/&gt;do this by</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['common', 'topics']">
          <rdg wit="f1818">common topics</rdg>
          <rdg wit="f1823">common topics</rdg>
          <rdg wit="fThomas">common topics</rdg>
      </rdgGrp>
      <rdgGrp n="['the', 'common', 'topics']">
          <rdg wit="fMS">the common topics</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['towards', 'geneva.']">
          <rdg wit="f1818">towards Geneva. </rdg>
          <rdg wit="f1823">towards Geneva. </rdg>
          <rdg wit="fThomas">towards Geneva. </rdg>
          <rdg wit="f1831">towards Geneva. </rdg>
          <rdg wit="fMS">&lt;sga-add eID="c56-0079__main__d5e16616"/&gt;&lt;mod
              eID="c56-0079__main__d5e16601"/&gt;towards Geneva.</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&lt;p-end/&gt;', '&lt;p-start/&gt;']">
          <rdg wit="f1818">&lt;p eID="novel1_letter4_chapter6_div4_div6_p23"/&gt; &lt;p
              sID="novel1_letter4_chapter6_div4_div6_p24"/&gt;</rdg>
          <rdg wit="f1823">&lt;p eID="novel1_letter4_chapter6_div4_div6_p23"/&gt; &lt;p
              sID="novel1_letter4_chapter6_div4_div6_p24"/&gt;</rdg>
          <rdg wit="fThomas">&lt;p eID="novel1_letter4_chapter6_div4_div6_p23"/&gt; &lt;p
              sID="novel1_letter4_chapter6_div4_div6_p24"/&gt;</rdg>
          <rdg wit="f1831">&lt;p eID="novel1_letter4_chapter7_div4_div7_p23"/&gt; &lt;p
              sID="novel1_letter4_chapter7_div4_div7_p24"/&gt;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['from']">
          <rdg wit="f1831">from</rdg>
      </rdgGrp>
      <rdgGrp n="['to', 'the', 'east']">
          <rdg wit="f1818">to the east</rdg>
          <rdg wit="f1823">to the east</rdg>
          <rdg wit="fThomas">to the east</rdg>
          <rdg wit="fMS">&lt;lb n="c56-0081__left_margin__3"/&gt;to the east</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['of']">
          <rdg wit="f1818">of</rdg>
          <rdg wit="f1823">of</rdg>
          <rdg wit="fThomas">of</rdg>
      </rdgGrp>
      <rdgGrp n="['-ward', 'of']">
          <rdg wit="fMS">&lt;lb n="c56-0081__left_margin__4"/&gt;-ward of</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['&#34;she most of all,&#34; said ernest, &#34;']">
          <rdg wit="f1831">&lt;longToken&gt;“She most of all,” said Ernest,
              “&lt;/longToken&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['&#34;she']">
          <rdg wit="f1818">“She</rdg>
          <rdg wit="f1823">“She</rdg>
          <rdg wit="fThomas">“She</rdg>
      </rdgGrp>
      <rdgGrp n="['she']">
          <rdg wit="fMS">&lt;lb n="c56-0086__main__17"/&gt;She</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['indeed']">
          <rdg wit="f1818">indeed</rdg>
          <rdg wit="f1823">indeed</rdg>
          <rdg wit="fThomas">indeed</rdg>
          <rdg wit="fMS">indeed</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge two apps:

  ```xml
  <app>
      <rdgGrp n="['appalling', 'a', 'crime?&#34;']">
          <rdg wit="f1831">appalling a crime?”</rdg>
      </rdgGrp>
      <rdgGrp n="['extremely']">
          <rdg wit="f1818">extremely</rdg>
          <rdg wit="f1823">extremely</rdg>
          <rdg wit="fThomas">extremely</rdg>
          <rdg wit="fMS">&lt;lb n="c56-0087__main__6"/&gt;extremely</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['wicked.&#34;']">
          <rdg wit="fMS">wicked."</rdg>
      </rdgGrp>
      <rdgGrp n="['wicked?&#34;']">
          <rdg wit="f1818">wicked?”</rdg>
          <rdg wit="f1823">wicked?”</rdg>
          <rdg wit="fThomas">wicked?”</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['bed', 'for']">
          <rdg wit="f1831">bed for</rdg>
      </rdgGrp>
      <rdgGrp n="['bed,', 'and']">
          <rdg wit="fMS">bed, and</rdg>
      </rdgGrp>
      <rdgGrp n="['bed;', 'and,']">
          <rdg wit="f1818">bed; and,</rdg>
          <rdg wit="f1823">bed; and,</rdg>
          <rdg wit="fThomas">bed; and,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['after']">
          <rdg wit="f1818">after</rdg>
          <rdg wit="f1823">after</rdg>
          <rdg wit="fThomas">after</rdg>
          <rdg wit="fMS">after</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge two apps:

  ```xml
  <app>
      <rdgGrp n="['altered', 'her', 'since', 'i']">
          <rdg wit="f1831">altered her since I</rdg>
      </rdgGrp>
      <rdgGrp n="['made', 'great', 'alterations', 'in']">
          <rdg wit="f1818">made great alterations in</rdg>
          <rdg wit="f1823">made great alterations in</rdg>
          <rdg wit="fThomas">made great alterations in</rdg>
          <rdg wit="fMS">made great alterations in</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['her form since  i had']">
          <rdg wit="fMS">&lt;longToken&gt;her form since &lt;lb n="c56-0090__main__4"/&gt;I
              had&lt;/longToken&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['her form since i had']">
          <rdg wit="f1818">&lt;longToken&gt;her form since I had&lt;/longToken&gt;</rdg>
          <rdg wit="f1823">&lt;longToken&gt;her form since I had&lt;/longToken&gt;</rdg>
          <rdg wit="fThomas">&lt;longToken&gt;her form since I had&lt;/longToken&gt;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge these apps:

  ```xml
  <app>
      <rdgGrp
              n="['&lt;del&gt;our father looks so sorrowful: this dreadful event seems to have revived in his mind his grief on the death of mamma. poor elizabeth also is quite inconsolable.&#34;&lt;/del&gt;', 'the sense of our misfortune is yet unalleviated; the silence of our father is uninterrupted, and there is something more distressing than tears in his unaltered sadness—while poor elizabeth, seeking solitude and for ever weeping, already begins to feel the effects of incessant grief—for her colour is gone, and her eyes are hollow and lustreless']">
          <rdg wit="fThomas">&lt;del rend="strikethrough"&gt;Our father looks so sorrowful: this
              dreadful event seems to have revived in his mind his grief on the death of Mamma.
              Poor Elizabeth also is quite inconsolable.”&lt;/del&gt; &lt;add&gt;the sense of our
              misfortune is yet unalleviated; the silence of our father is uninterrupted, and
              there is something more distressing than tears in his unaltered sadness—while poor
              Elizabeth, seeking solitude and for ever weeping, already begins to feel the effects
              of incessant grief—for her colour is gone, and her eyes are hollow &amp;
              lustreless&lt;/add&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['our']">
          <rdg wit="f1818">Our</rdg>
          <rdg wit="f1823">Our</rdg>
          <rdg wit="fMS">&lt;sga-add eID="c56-0086__main__d5e18427"/&gt;&lt;sga-add
              place="superlinear" sID="c56-0086__main__d5e18433"/&gt;our</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['father', 'looks', 'so']">
          <rdg wit="f1818">father looks so </rdg>
          <rdg wit="f1823">father looks so </rdg>
          <rdg wit="fMS">&lt;sga-add eID="c56-0086__main__d5e18433"/&gt;&lt;mod
              eID="c56-0086__main__d5e18423"/&gt;father looks so</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['sorrowful', 'and', 'it']">
          <rdg wit="fMS">sorrowful and it</rdg>
      </rdgGrp>
      <rdgGrp n="['sorrowful:', 'this', 'dreadful', 'event']">
          <rdg wit="f1818">sorrowful: this dreadful event</rdg>
          <rdg wit="f1823">sorrowful: this dreadful event</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['seems', 'to', 'have', 'revived', 'in', 'his', 'mind', 'his']">
          <rdg wit="f1818">seems to have revived in his mind his</rdg>
          <rdg wit="f1823">seems to have revived in his mind his</rdg>
          <rdg wit="fMS">seems &lt;lb n="c56-0086__main__6"/&gt;to have revived in his mind
              his</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['grief', 'on']">
          <rdg wit="f1818">grief on</rdg>
          <rdg wit="f1823">grief on</rdg>
      </rdgGrp>
      <rdgGrp n="['sorrow', 'for']">
          <rdg wit="fMS">sorrow &lt;lb n="c56-0086__main__7"/&gt;for</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['the', 'death', 'of']">
          <rdg wit="f1818">the death of</rdg>
          <rdg wit="f1823">the death of</rdg>
          <rdg wit="fMS">the death of</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['mamma', 'and']">
          <rdg wit="fMS">Mamma and</rdg>
      </rdgGrp>
      <rdgGrp n="['mamma.']">
          <rdg wit="f1818">Mamma.</rdg>
          <rdg wit="f1823">mamma.</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['poor']">
          <rdg wit="f1818">Poor</rdg>
          <rdg wit="f1823">Poor</rdg>
          <rdg wit="fMS">poor</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['elizabeth']">
          <rdg wit="f1818">Elizabeth</rdg>
          <rdg wit="fMS">&lt;w ana="start"/&gt;Eliza&lt;lb n="c56-0086__main__8"/&gt;beth&lt;w
              ana="end"/&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['elizabeth,', 'also,']">
          <rdg wit="f1823">&lt;pb xml:id="F1823_v1_172" n="153"/&gt;Elizabeth, also,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['is', 'quite', 'inconsolable.&#34;']">
          <rdg wit="f1823">is quite inconsolable.”</rdg>
          <rdg wit="fMS">is quite inconsolable."</rdg>
      </rdgGrp>
      <rdgGrp n="['also', 'is', 'quite', 'inconsolable.&#34;']">
          <rdg wit="f1818">also is quite inconsolable.”</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge these apps:

  ```xml
  <app>
      <rdgGrp
              n="['&lt;del&gt;but, tell me, how does my father support his misfortunes? and how is&lt;/del&gt;', 'you must assist me in acquiring sufficient calmness to console my father and support']">
          <rdg wit="fThomas">&lt;del rend="strikethrough"&gt;But, tell me, how does my father
              support his misfortunes? and how is&lt;/del&gt; &lt;add&gt;You must assist me in
              acquiring sufficient calmness to console my father and support&lt;/add&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['but']">
          <rdg wit="fMS">&lt;lb n="c56-0086__main__14"/&gt;But</rdg>
      </rdgGrp>
      <rdgGrp n="['but,']">
          <rdg wit="f1818">But,</rdg>
          <rdg wit="f1823">But,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['tell', 'me,', 'how', 'does']">
          <rdg wit="f1818">tell me, how does</rdg>
          <rdg wit="f1823">tell me, how does</rdg>
          <rdg wit="fMS">tell me, How &lt;sga-add hand="#pbs" place="superlinear"
              sID="c56-0086__main__d5e18507"/&gt;does</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['my']">
          <rdg wit="f1818">my </rdg>
          <rdg wit="f1823">my </rdg>
          <rdg wit="fThomas">my </rdg>
          <rdg wit="fMS">&lt;sga-add eID="c56-0086__main__d5e18507"/&gt;my</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['father']">
          <rdg wit="f1818">father</rdg>
          <rdg wit="f1823">father</rdg>
          <rdg wit="fMS">father</rdg>
      </rdgGrp>
      <rdgGrp n="['poor']">
          <rdg wit="fThomas">poor</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['support']">
          <rdg wit="f1818">support</rdg>
          <rdg wit="f1823">support</rdg>
      </rdgGrp>
      <rdgGrp n="['support&lt;del&gt;s', 'it', 'and', 'if']">
          <rdg wit="fMS">support&lt;delSpan rend="strikethrough" spanTo="#c56-0086.06"/&gt;s it
              &lt;lb n="c56-0086__main__15"/&gt;and if</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['elizabeth']">
          <rdg wit="fThomas">Elizabeth</rdg>
          <rdg wit="fMS">Elizabeth</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&lt;/del&gt;']">
          <rdg wit="fMS">&lt;delSpan anchor="c56-0086.06"/&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['&lt;del&gt;?&lt;/del&gt;', '&#34;']">
          <rdg wit="fThomas">&lt;del rend="strikethrough"&gt;?&lt;/del&gt; ”</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['his']">
          <rdg wit="f1818">his</rdg>
          <rdg wit="f1823">his</rdg>
          <rdg wit="fMS">his</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&lt;del&gt;f&lt;/del&gt;', 'misfortunes;']">
          <rdg wit="fMS">&lt;del rend="strikethrough"
              xml:id="c56-0086__main__d5e18517"&gt;f&lt;/del&gt; misfortunes;</rdg>
      </rdgGrp>
      <rdgGrp n="['misfortunes?']">
          <rdg wit="f1818">misfortunes?</rdg>
          <rdg wit="f1823">misfortunes?</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['and', 'how', 'is', 'my', 'poor', 'elizabeth?&#34;']">
          <rdg wit="f1818">and how is my poor Elizabeth?”</rdg>
          <rdg wit="f1823">and how is my poor Elizabeth?”</rdg>
          <rdg wit="fMS">and how &lt;lb n="c56-0086__main__16"/&gt;is my poor Elizabeth?"</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&lt;p-end/&gt;']">
          <rdg wit="f1818">&lt;p eID="novel1_letter4_chapter6_div4_div6_p35"/&gt;</rdg>
          <rdg wit="f1823">&lt;p eID="novel1_letter4_chapter6_div4_div6_p35"/&gt;</rdg>
          <rdg wit="fThomas">&lt;p eID="novel1_letter4_chapter6_div4_div6_p35"/&gt;</rdg>
          <rdg wit="fMS">&lt;milestone unit="tei:p-END"/&gt;</rdg>
      </rdgGrp>
  </app>
  ```


