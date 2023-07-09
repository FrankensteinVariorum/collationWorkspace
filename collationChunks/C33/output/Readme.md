- [x] **Misalignment: ** `august` in MS should go down.

  ```xml
  <app>
      <rdgGrp n="['']">
          <rdg wit="f1818">&lt;anchor type="collate" xml:id="C33"/&gt;</rdg>
          <rdg wit="f1823">&lt;anchor type="collate" xml:id="C33"/&gt;</rdg>
          <rdg wit="fThomas">&lt;anchor type="collate" xml:id="C33"/&gt;</rdg>
          <rdg wit="f1831">&lt;anchor type="collate" xml:id="C33"/&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['august', '']">
          <rdg wit="fMS">&lt;anchor type="collate" xml:id="C33"/&gt;&lt;lb
              n="c57-0172__main__27"/&gt;August &lt;mod sID="c57-0172__main__d4e34287"/&gt;</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['&lt;mdel&gt;27&lt;/mdel&gt;', '31', '', '']">
          <rdg wit="fMS">&lt;mdel&gt;27&lt;/mdel&gt; &lt;sga-add place="intralinear"
              sID="c57-0172__main__d4e34291"/&gt;31 &lt;sga-add
              eID="c57-0172__main__d4e34291"/&gt;&lt;mod eID="c57-0172__main__d4e34287"/&gt;
              &lt;shi rend="sup"&gt;&lt;/shi&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['&lt;p-start/&gt;', 'september', '2d.', '&lt;p-end/&gt;', '&lt;p-start/&gt;']">
          <rdg wit="f1818">&lt;p sID="novel1_letter4_div4_p47"/&gt; September 2d. &lt;p
              eID="novel1_letter4_div4_p47"/&gt; &lt;p sID="novel1_letter4_div4_p48"/&gt;</rdg>
          <rdg wit="f1823">&lt;p sID="novel1_letter4_div4_p47"/&gt; September 2d. &lt;p
              eID="novel1_letter4_div4_p47"/&gt; &lt;p sID="novel1_letter4_div4_p48"/&gt;</rdg>
          <rdg wit="fThomas">&lt;p sID="novel1_letter4_div4_p47"/&gt; September 2d. &lt;p
              eID="novel1_letter4_div4_p47"/&gt; &lt;p sID="novel1_letter4_div4_p48"/&gt;</rdg>
          <rdg wit="f1831">&lt;p sID="novel1_letter4_div4_p49"/&gt; September 2d. &lt;p
              eID="novel1_letter4_div4_p49"/&gt; &lt;p sID="novel1_letter4_div4_p50"/&gt;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge two apps:

```xml
<app>
    <rdgGrp n="['daily']">
        <rdg wit="f1818">daily</rdg>
        <rdg wit="f1823">daily</rdg>
        <rdg wit="fThomas">daily</rdg>
        <rdg wit="f1831">daily</rdg>
    </rdgGrp>
    <rdgGrp n="['declined', 'daily']">
        <rdg wit="fMS">declined daily</rdg>
    </rdgGrp>
</app>

<app>
    <rdgGrp n="['', '&lt;del&gt;his&lt;/del&gt;']">
        <rdg wit="fMS">&lt;lb n="c57-0174__main__11"/&gt; &lt;del rend="strikethrough"
            xml:id="c57-0174__main__d4e34607"&gt;his&lt;/del&gt;</rdg>
    </rdgGrp>
    <rdgGrp n="['declined']">
        <rdg wit="f1818">declined</rdg>
        <rdg wit="f1823">declined</rdg>
        <rdg wit="fThomas">declined</rdg>
        <rdg wit="f1831">declined</rdg>
    </rdgGrp>
</app>
```

- [x] merge apps:

  ```xml
  <app>
      <rdgGrp n="['danger']">
          <rdg wit="f1818">&lt;pb xml:id="F1818_v3_173" n="169"/&gt;danger</rdg>
          <rdg wit="f1823">&lt;pb xml:id="F1823_v2_530" n="257"/&gt;danger</rdg>
          <rdg wit="fThomas">&lt;pb xml:id="F1818_v3_173" n="169"/&gt;danger</rdg>
          <rdg wit="f1831">danger</rdg>
      </rdgGrp>
      <rdgGrp n="['death']">
          <rdg wit="fMS">death</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['and']">
          <rdg wit="f1818">and</rdg>
          <rdg wit="f1823">and</rdg>
          <rdg wit="fThomas">and</rdg>
          <rdg wit="f1831">and</rdg>
          <rdg wit="fMS">&amp;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['danger']">
          <rdg wit="fMS">danger</rdg>
      </rdgGrp>
      <rdgGrp n="['death']">
          <rdg wit="f1818">death</rdg>
          <rdg wit="f1823">death</rdg>
          <rdg wit="fThomas">death</rdg>
          <rdg wit="f1831">death</rdg>
      </rdgGrp>
  </app>
  ```

- [x] **Misalignment:** 

  ```xml
  <app>
      <rdgGrp n="['name']">
          <rdg wit="f1818">name</rdg>
          <rdg wit="fThomas">name</rdg>
      </rdgGrp>
      <rdgGrp n="['names']">
          <rdg wit="f1823">names</rdg>
          <rdg wit="f1831">names</rdg>
          <rdg wit="fMS">names</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['adored']">
          <rdg wit="fMS">&lt;lb n="c57-0175__main__29"/&gt;adored</rdg>
      </rdgGrp>
      <rdgGrp n="['s']">
          <rdg wit="fThomas">&lt;add place="margin"&gt;s&lt;/add&gt;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['adored,']">
          <rdg wit="f1818">adored,</rdg>
          <rdg wit="f1823">adored,</rdg>
          <rdg wit="fThomas">adored,</rdg>
          <rdg wit="f1831">adored,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge two apps:

  ```xml
  <app>
      <rdgGrp n="['exclaimed:']">
          <rdg wit="f1823">exclaimed:</rdg>
          <rdg wit="f1831">exclaimed:</rdg>
      </rdgGrp>
      <rdgGrp n="['exclaimed;']">
          <rdg wit="f1818">exclaimed;</rdg>
          <rdg wit="fThomas">exclaimed;</rdg>
      </rdgGrp>
      <rdgGrp n="['exclaimed—in']">
          <rdg wit="fMS">exclaimed—In</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&#34;in']">
          <rdg wit="f1818">“in</rdg>
          <rdg wit="f1823">“in</rdg>
          <rdg wit="fThomas">“in</rdg>
          <rdg wit="f1831">“in</rdg>
      </rdgGrp>
  </app>
  ```

- [x] **Misalignment: **

  ```xml
  <app>
      <rdgGrp n="['gathered', 'resolution', 'to', 'address']">
          <rdg wit="f1818">gathered resolution to address</rdg>
          <rdg wit="f1823">gathered resolution to address</rdg>
          <rdg wit="fThomas">gathered resolution to address</rdg>
          <rdg wit="f1831">gathered resolution to address</rdg>
      </rdgGrp>
      <rdgGrp n="['said.', 'your', 'repentance', 'is']">
          <rdg wit="fMS">said. Your &lt;lb n="c57-0182__main__22"/&gt;repentance is</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['him']">
          <rdg wit="f1823">him</rdg>
          <rdg wit="f1831">him</rdg>
      </rdgGrp>
      <rdgGrp n="['him,']">
          <rdg wit="f1818">him,</rdg>
          <rdg wit="fThomas">him,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp
              n="['in', 'a', 'pause', 'of', 'the', 'tempest', 'of', 'his', 'passion:', '&#34;your', 'repentance,&#34;', 'i', 'said,', '&#34;is']">
          <rdg wit="f1818">in a pause of the tempest of his passion: “Your repentance,” I said,
              “is</rdg>
          <rdg wit="f1823">in a pause of the tempest of his passion: “Your repentance,” I said,
              “is</rdg>
          <rdg wit="fThomas">in a pause of the tempest of his passion: “Your repentance,” I said,
              “is</rdg>
          <rdg wit="f1831">in a pause of the tempest of his passion: “Your repentance,” I said,
              “is</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge two apps:

  ```xml
  <app>
      <rdgGrp n="['switzerland', '&lt;del&gt;how many', 'ti&lt;/del&gt;', 'heart', 'broken']">
          <rdg wit="fMS">Switzerland &lt;delSpan rend="strikethrough"
              spanTo="#c57-0183.02"/&gt;how&lt;lb n="c57-0183__main__7"/&gt;many ti&lt;delSpan
              anchor="c57-0183.02"/&gt; heart broken</rdg>
      </rdgGrp>
      <rdgGrp n="['switzerland,']">
          <rdg wit="f1818">Switzerland,</rdg>
          <rdg wit="f1823">Switzerland,</rdg>
          <rdg wit="fThomas">Switzerland,</rdg>
          <rdg wit="f1831">Switzerland,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['heart-broken']">
          <rdg wit="f1823">heart-broken</rdg>
          <rdg wit="f1831">heart-broken</rdg>
      </rdgGrp>
      <rdgGrp n="['heartbroken']">
          <rdg wit="f1818">heartbroken</rdg>
          <rdg wit="fThomas">heartbroken</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge two apps:

  ```xml
  <app>
      <rdgGrp n="['kindled', '–', 'wretch']">
          <rdg wit="fMS">&lt;lb n="c57-0183__main__30"/&gt;kindled – Wretch</rdg>
      </rdgGrp>
      <rdgGrp n="['re-kindled']">
          <rdg wit="f1818">re-kindled</rdg>
          <rdg wit="fThomas">re-kindled</rdg>
      </rdgGrp>
      <rdgGrp n="['rekindled']">
          <rdg wit="f1823">rekindled</rdg>
          <rdg wit="f1831">rekindled</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['within', 'me.', '&#34;wretch!&#34;']">
          <rdg wit="f1818">within me. “Wretch!”</rdg>
          <rdg wit="f1823">within me. “Wretch!”</rdg>
          <rdg wit="fThomas">within me. “Wretch!”</rdg>
          <rdg wit="f1831">within me. “Wretch!”</rdg>
      </rdgGrp>
  </app>
  ```

  - [x] **Misalignment: ** 

  ```xml
  <app>
      <rdgGrp n="['&lt;del&gt;of&lt;/del&gt;', 'animal–']">
          <rdg wit="fMS">&lt;del rend="strikethrough"
              xml:id="c57-0184__main__d4e37106"&gt;of&lt;/del&gt; &lt;lb
              n="c57-0184__main__31"/&gt;animal–</rdg>
      </rdgGrp>
      <rdgGrp n="['animal.', 'no']">
          <rdg wit="f1818">animal. No</rdg>
          <rdg wit="f1823">animal. No</rdg>
          <rdg wit="fThomas">animal. No</rdg>
          <rdg wit="f1831">animal. No</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['crime,']">
          <rdg wit="f1818">crime,</rdg>
          <rdg wit="f1823">crime,</rdg>
          <rdg wit="fThomas">crime,</rdg>
      </rdgGrp>
      <rdgGrp n="['guilt,']">
          <rdg wit="f1831">guilt,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['no', 'mischief,', 'no', 'malignity,']">
          <rdg wit="f1818">no mischief, no malignity,</rdg>
          <rdg wit="f1823">no mischief, no malignity,</rdg>
          <rdg wit="fThomas">no mischief, no malignity,</rdg>
          <rdg wit="f1831">no mischief, no malignity,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge two apps:

  ```xml
  <app>
      <rdgGrp n="['to', 'death']">
          <rdg wit="f1818">to death</rdg>
          <rdg wit="f1823">to death</rdg>
          <rdg wit="fThomas">to death</rdg>
          <rdg wit="f1831">to death</rdg>
      </rdgGrp>
      <rdgGrp n="['his', 'throat', 'to', 'death']">
          <rdg wit="fMS">&lt;lb n="c57-0185__main__29"/&gt;his throat to death</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['his', 'throat']">
          <rdg wit="f1818">his throat</rdg>
          <rdg wit="f1823">his throat</rdg>
          <rdg wit="fThomas">his throat</rdg>
          <rdg wit="f1831">his throat</rdg>
      </rdgGrp>
  </app>
  ```

  

## app with less than 5 rdgs

- [x] 

```xml
  <app>
      <rdgGrp n="['&lt;p-end/&gt;']">
          <rdg wit="f1818">&lt;p eID="novel1_letter4_div4_p48"/&gt;</rdg>
          <rdg wit="f1823">&lt;p eID="novel1_letter4_div4_p48"/&gt;</rdg>
          <rdg wit="fThomas">&lt;p eID="novel1_letter4_div4_p48"/&gt;</rdg>
          <rdg wit="f1831">&lt;p eID="novel1_letter4_div4_p50"/&gt;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&lt;p-start/&gt;', 'i', 'write', 'to']">
          <rdg wit="f1818">&lt;p sID="novel1_letter4_div4_p49"/&gt; I write to</rdg>
          <rdg wit="f1823">&lt;p sID="novel1_letter4_div4_p49"/&gt; I write to</rdg>
          <rdg wit="fThomas">&lt;p sID="novel1_letter4_div4_p49"/&gt; I write to</rdg>
          <rdg wit="f1831">&lt;p sID="novel1_letter4_div4_p51"/&gt; I write to</rdg>
          <rdg wit="fMS">&lt;milestone unit="tei:p-START"/&gt; &lt;lb n="c57-0172__main__29"/&gt;I
              write to</rdg>
      </rdgGrp>
  </app>
```

- [x] 

```xml
  <app>
      <rdgGrp n="['whom', 'i']">
          <rdg wit="f1818">whom I</rdg>
          <rdg wit="f1823">whom I</rdg>
          <rdg wit="fThomas">whom I</rdg>
          <rdg wit="f1831">whom I</rdg>
          <rdg wit="fMS">whom I</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['have']">
          <rdg wit="f1818">have</rdg>
          <rdg wit="f1823">have</rdg>
          <rdg wit="fThomas">have</rdg>
          <rdg wit="f1831">have</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 
-
- ```xml
  <app>
      <rdgGrp n="['we', 'may']">
          <rdg wit="f1818">We may</rdg>
          <rdg wit="f1823">We may</rdg>
          <rdg wit="fThomas">We may</rdg>
          <rdg wit="fMS">We may</rdg>
      </rdgGrp>
      <rdgGrp
              n="['yet', 'it', 'is', 'terrible', 'to', 'reflect', 'that', 'the', 'lives', 'of', 'all', 'these', 'men', 'are', 'endangered', 'through', 'me.', 'if', 'we', 'are', 'lost,', 'my', 'mad', 'schemes', 'are', 'the', 'cause.']">
          <rdg wit="f1831">Yet it is terrible to reflect &lt;pb xml:id="F1831_v_208"
              n="192"/&gt;that the lives of all these men are endangered through me. If we are
              lost, my mad schemes are the cause.</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['survive']">
          <rdg wit="fMS">survive</rdg>
      </rdgGrp>
      <rdgGrp n="['survive;']">
          <rdg wit="f1818">survive;</rdg>
          <rdg wit="f1823">survive;</rdg>
          <rdg wit="fThomas">survive;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['and', 'if', 'we', 'do']">
          <rdg wit="f1818">and if we do</rdg>
          <rdg wit="f1823">and if we do</rdg>
          <rdg wit="fThomas">and if we do</rdg>
          <rdg wit="fMS">&amp; if we do</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['not', '–']">
          <rdg wit="fMS">not –</rdg>
      </rdgGrp>
      <rdgGrp n="['not,']">
          <rdg wit="f1818">not,</rdg>
          <rdg wit="f1823">not,</rdg>
          <rdg wit="fThomas">not,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['i', 'will', 'repeat', 'the', 'lessons', 'of', 'my']">
          <rdg wit="f1818">I will repeat the lessons of my</rdg>
          <rdg wit="f1823">I will repeat the lessons of my</rdg>
          <rdg wit="fThomas">I will repeat the lessons of my</rdg>
          <rdg wit="fMS">&lt;lb n="c57-0173__main__6"/&gt;I will repeat the lessons of my</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['seneca']">
          <rdg wit="fMS">Seneca</rdg>
      </rdgGrp>
      <rdgGrp n="['seneca,']">
          <rdg wit="f1818">Seneca,</rdg>
          <rdg wit="f1823">Seneca,</rdg>
          <rdg wit="fThomas">Seneca,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['and', 'die', 'with', 'a', 'good', 'heart.']">
          <rdg wit="f1818">and die with a good heart.</rdg>
          <rdg wit="f1823">and die with a good heart.</rdg>
          <rdg wit="fThomas">and die with a good heart.</rdg>
          <rdg wit="fMS">&amp; die with a &lt;lb n="c57-0173__main__7"/&gt;good heart.</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 

```xml
  <app>
      <rdgGrp n="['yet', 'i', 'cannot', 'forbear', 'recording', 'it.']">
          <rdg wit="f1818">yet I cannot forbear recording it.</rdg>
          <rdg wit="f1823">yet I cannot forbear recording it.</rdg>
          <rdg wit="fThomas">yet I cannot forbear recording it.</rdg>
          <rdg wit="f1831">yet I cannot forbear recording it.</rdg>
      </rdgGrp>
      <rdgGrp n="['my', 'dear', 'margeret,', 'yet', 'i', 'cannot', 'forbear', 'recording', 'it.']">
          <rdg wit="fMS">my dear &lt;lb n="c57-0174__main__5"/&gt;Margeret, yet I cannot forbear
              recording it.</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['&lt;p-end/&gt;', '&lt;p-start/&gt;']">
          <rdg wit="f1818">&lt;p eID="novel1_letter4_div4_p53"/&gt; &lt;p
              sID="novel1_letter4_div4_p54"/&gt;</rdg>
          <rdg wit="f1823">&lt;p eID="novel1_letter4_div4_p53"/&gt; &lt;p
              sID="novel1_letter4_div4_p54"/&gt;</rdg>
          <rdg wit="fThomas">&lt;p eID="novel1_letter4_div4_p53"/&gt; &lt;p
              sID="novel1_letter4_div4_p54"/&gt;</rdg>
          <rdg wit="f1831">&lt;p eID="novel1_letter4_div4_p55"/&gt; &lt;p
              sID="novel1_letter4_div4_p56"/&gt;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 
 
 ```xml
  <app>
      <rdgGrp
              n="['apparent', 'lifelessness.', '&lt;p-end/&gt;', '&lt;p-start/&gt;', 'i', 'mentioned']">
          <rdg wit="f1818">apparent lifelessness. &lt;p eID="novel1_letter4_div4_p54"/&gt; &lt;p
              sID="novel1_letter4_div4_p55"/&gt; I mentioned </rdg>
          <rdg wit="f1823">apparent lifelessness. &lt;p eID="novel1_letter4_div4_p54"/&gt; &lt;p
              sID="novel1_letter4_div4_p55"/&gt; I mentioned </rdg>
          <rdg wit="fThomas">apparent lifelessness. &lt;p eID="novel1_letter4_div4_p54"/&gt; &lt;p
              sID="novel1_letter4_div4_p55"/&gt; I mentioned </rdg>
          <rdg wit="f1831">apparent lifelessness. &lt;p eID="novel1_letter4_div4_p56"/&gt; &lt;p
              sID="novel1_letter4_div4_p57"/&gt; I mentioned </rdg>
          <rdg wit="fMS">&lt;sga-add eID="c57-0174__main__d4e34638"/&gt;&lt;mod
              eID="c57-0174__main__d4e34634"/&gt;apparent lifelessness. &lt;milestone
              unit="tei:p-END"/&gt; &lt;milestone unit="tei:p-START"/&gt; &lt;lb
              n="c57-0174__main__15"/&gt;I mentioned</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['in']">
          <rdg wit="f1818">in</rdg>
          <rdg wit="f1823">in</rdg>
          <rdg wit="fThomas">in</rdg>
          <rdg wit="f1831">in</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 
 
 ```xml
  <app>
      <rdgGrp n="['a']">
          <rdg wit="f1818">a</rdg>
          <rdg wit="f1823">a</rdg>
          <rdg wit="fThomas">a</rdg>
          <rdg wit="f1831">a</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['mutiny.', 'this']">
          <rdg wit="f1818">mutiny. This</rdg>
          <rdg wit="f1823">mutiny. This</rdg>
          <rdg wit="fThomas">mutiny. This</rdg>
          <rdg wit="f1831">mutiny. This</rdg>
          <rdg wit="fMS">mutiny. This</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 
-
- ```xml
  <app>
      <rdgGrp n="['me']">
          <rdg wit="f1818">me</rdg>
          <rdg wit="f1823">me</rdg>
          <rdg wit="fThomas">me</rdg>
          <rdg wit="f1831">me</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['demand', 'which']">
          <rdg wit="fMS">demand which</rdg>
      </rdgGrp>
      <rdgGrp n="['demand,']">
          <rdg wit="f1818">demand,</rdg>
          <rdg wit="fThomas">demand,</rdg>
      </rdgGrp>
      <rdgGrp n="['requisition,']">
          <rdg wit="f1823">requisition,</rdg>
          <rdg wit="f1831">requisition,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['which,']">
          <rdg wit="f1818">which,</rdg>
          <rdg wit="f1823">which,</rdg>
          <rdg wit="fThomas">which,</rdg>
          <rdg wit="f1831">which,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 

```xml
  <app>
      <rdgGrp n="['desired', 'therefore']">
          <rdg wit="fMS">desired therefore</rdg>
      </rdgGrp>
      <rdgGrp n="['desired,']">
          <rdg wit="f1818">desired,</rdg>
          <rdg wit="fThomas">desired,</rdg>
      </rdgGrp>
      <rdgGrp n="['insisted,']">
          <rdg wit="f1823">insisted,</rdg>
          <rdg wit="f1831">insisted,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['therefore,']">
          <rdg wit="f1818">therefore,</rdg>
          <rdg wit="f1823">therefore,</rdg>
          <rdg wit="fThomas">therefore,</rdg>
          <rdg wit="f1831">therefore,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 

```xml
  <app>
      <rdgGrp n="['surrounded']">
          <rdg wit="f1831">surrounded</rdg>
          <rdg wit="fMS">&lt;lb n="c57-0175__main__24"/&gt;surrounded</rdg>
      </rdgGrp>
      <rdgGrp n="['surrounded,']">
          <rdg wit="f1818">surrounded,</rdg>
          <rdg wit="f1823">surrounded,</rdg>
          <rdg wit="fThomas">surrounded,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['it,']">
          <rdg wit="f1831">it,</rdg>
      </rdgGrp>
      <rdgGrp n="['you']">
          <rdg wit="fMS">you</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 

```xml
  <app>
      <rdgGrp n="['and', 'these']">
          <rdg wit="f1818">and these</rdg>
          <rdg wit="f1823">and these</rdg>
          <rdg wit="fThomas">and these</rdg>
          <rdg wit="f1831">and these</rdg>
          <rdg wit="fMS">&amp; these</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['dangers']">
          <rdg wit="f1818">dangers</rdg>
          <rdg wit="fThomas">dangers</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 

```xml
  <app>
      <rdgGrp n="['a']">
          <rdg wit="f1818">a</rdg>
          <rdg wit="f1823">a</rdg>
          <rdg wit="fThomas">a</rdg>
          <rdg wit="f1831">a</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp
              n="['rock.', 'this', 'ice', 'is', 'not', 'made', 'of', 'such', 'stuff', 'as', 'your', 'hearts']">
          <rdg wit="f1818">rock. This ice is not made of such stuff as your hearts</rdg>
          <rdg wit="f1823">rock. This ice is not made of such stuff as your hearts</rdg>
          <rdg wit="fThomas">rock. This ice is not made of such stuff as your hearts</rdg>
          <rdg wit="f1831">rock. This ice is not made of such stuff as your hearts</rdg>
          <rdg wit="fMS">rock. this ice is not made &lt;lb n="c57-0176__main__10"/&gt;of such
              stuff &lt;sga-add hand="#pbs" place="superlinear"
              sID="c57-0176__main__d4e35130"/&gt;as your hearts</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 

```xml
  <app>
      <rdgGrp n="['mutable']">
          <rdg wit="fMS">mutable</rdg>
      </rdgGrp>
      <rdgGrp n="['mutable,']">
          <rdg wit="f1818">mutable,</rdg>
          <rdg wit="f1823">mutable,</rdg>
          <rdg wit="fThomas">mutable,</rdg>
          <rdg wit="f1831">mutable,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['and']">
          <rdg wit="f1831">and</rdg>
          <rdg wit="fMS">&amp;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 
 
 ```xml
  <app>
      <rdgGrp n="['moved', '–they']">
          <rdg wit="fMS">moved –They</rdg>
      </rdgGrp>
      <rdgGrp n="['moved.']">
          <rdg wit="f1818">moved.</rdg>
          <rdg wit="f1823">moved.</rdg>
          <rdg wit="fThomas">moved.</rdg>
      </rdgGrp>
      <rdgGrp n="['moved?']">
          <rdg wit="f1831">moved?</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['they']">
          <rdg wit="f1818">They</rdg>
          <rdg wit="f1823">They</rdg>
          <rdg wit="fThomas">They</rdg>
          <rdg wit="f1831">They</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 

 ```xml
  <app>
      <rdgGrp n="['their', 'courage', 'would', 'return.']">
          <rdg wit="f1818">their courage would return.</rdg>
          <rdg wit="f1823">their courage would return.</rdg>
          <rdg wit="fThomas">their courage would return.</rdg>
          <rdg wit="f1831">their courage would return.</rdg>
          <rdg wit="fMS">their courage &lt;lb n="c57-0176__main__28"/&gt;would return.</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&lt;p-end/&gt;', '&lt;p-start/&gt;']">
          <rdg wit="f1818">&lt;p eID="novel1_letter4_div4_p58"/&gt; &lt;p
              sID="novel1_letter4_div4_p59"/&gt;</rdg>
          <rdg wit="f1823">&lt;p eID="novel1_letter4_div4_p58"/&gt; &lt;p
              sID="novel1_letter4_div4_p59"/&gt;</rdg>
          <rdg wit="fThomas">&lt;p eID="novel1_letter4_div4_p58"/&gt; &lt;p
              sID="novel1_letter4_div4_p59"/&gt;</rdg>
          <rdg wit="f1831">&lt;p eID="novel1_letter4_div4_p60"/&gt; &lt;p
              sID="novel1_letter4_div4_p61"/&gt;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 

 ```xml
  <app>
      <rdgGrp n="['&lt;p-end/&gt;']">
          <rdg wit="f1818">&lt;p eID="novel1_letter4_div4_p62"/&gt;</rdg>
          <rdg wit="f1823">&lt;p eID="novel1_letter4_div4_p62"/&gt;</rdg>
          <rdg wit="fThomas">&lt;p eID="novel1_letter4_div4_p62"/&gt;</rdg>
          <rdg wit="f1831">&lt;p eID="novel1_letter4_div4_p64"/&gt;</rdg>
          <rdg wit="fMS">&lt;milestone unit="tei:p-END"/&gt;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['']">
          <rdg wit="f1818">&lt;pb xml:id="F1818_v3_176" n="172"/&gt;</rdg>
          <rdg wit="f1823">&lt;pb xml:id="F1823_v2_533" n="260"/&gt;</rdg>
          <rdg wit="fThomas">&lt;pb xml:id="F1818_v3_176" n="172"/&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['&lt;p-start/&gt;', '', '']">
          <rdg wit="fMS">&lt;milestone unit="tei:p-START"/&gt; &lt;lb n="c57-0177__main__10"/&gt;
              &lt;milestone spanTo="#c57-0177.04" unit="tei:date"/&gt;</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['&lt;p-start/&gt;']">
          <rdg wit="f1818">&lt;p sID="novel1_letter4_div4_p63"/&gt;</rdg>
          <rdg wit="f1823">&lt;p sID="novel1_letter4_div4_p63"/&gt;</rdg>
          <rdg wit="fThomas">&lt;p sID="novel1_letter4_div4_p63"/&gt;</rdg>
          <rdg wit="f1831">&lt;p sID="novel1_letter4_div4_p65"/&gt;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 

  ```xml
  <app>
      <rdgGrp n="['1', '', '&lt;mdel&gt;7&lt;/mdel&gt;', '2', '', '']">
          <rdg wit="fMS">&lt;mod sID="c57-0177__main__d4e35378"/&gt;&lt;sga-add
              place="intralinear" sID="c57-0177__main__d4e35380"/&gt;1 &lt;sga-add
              eID="c57-0177__main__d4e35380"/&gt; &lt;mdel&gt;7&lt;/mdel&gt; &lt;sga-add
              place="intralinear" sID="c57-0177__main__d4e35385"/&gt;2 &lt;sga-add
              eID="c57-0177__main__d4e35385"/&gt;&lt;mod eID="c57-0177__main__d4e35378"/&gt;
              &lt;shi rend="underline"&gt;&lt;/shi&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['12th']">
          <rdg wit="f1823">12th</rdg>
      </rdgGrp>
      <rdgGrp n="['12th.']">
          <rdg wit="f1818">12th.</rdg>
          <rdg wit="fThomas">12th.</rdg>
          <rdg wit="f1831">12th.</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&lt;p-end/&gt;', '&lt;p-start/&gt;']">
          <rdg wit="f1818">&lt;p eID="novel1_letter4_div4_p63"/&gt; &lt;p
              sID="novel1_letter4_div4_p64"/&gt;</rdg>
          <rdg wit="f1823">&lt;p eID="novel1_letter4_div4_p63"/&gt; &lt;p
              sID="novel1_letter4_div4_p64"/&gt;</rdg>
          <rdg wit="fThomas">&lt;p eID="novel1_letter4_div4_p63"/&gt; &lt;p
              sID="novel1_letter4_div4_p64"/&gt;</rdg>
          <rdg wit="f1831">&lt;p eID="novel1_letter4_div4_p65"/&gt; &lt;p
              sID="novel1_letter4_div4_p66"/&gt;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 

```xml
  <app>
      <rdgGrp n="['and', 'fainted.']">
          <rdg wit="f1818">and fainted.</rdg>
          <rdg wit="f1823">and fainted.</rdg>
          <rdg wit="fThomas">and fainted.</rdg>
          <rdg wit="f1831">and fainted.</rdg>
          <rdg wit="fMS">&amp; fainted.</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&lt;p-end/&gt;', '&lt;p-start/&gt;']">
          <rdg wit="f1818">&lt;p eID="novel1_letter4_div4_p68"/&gt; &lt;p
              sID="novel1_letter4_div4_p69"/&gt;</rdg>
          <rdg wit="f1823">&lt;p eID="novel1_letter4_div4_p68"/&gt; &lt;p
              sID="novel1_letter4_div4_p69"/&gt;</rdg>
          <rdg wit="fThomas">&lt;p eID="novel1_letter4_div4_p68"/&gt; &lt;p
              sID="novel1_letter4_div4_p69"/&gt;</rdg>
          <rdg wit="f1831">&lt;p eID="novel1_letter4_div4_p70"/&gt; &lt;p
              sID="novel1_letter4_div4_p71"/&gt;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 

 ```xml
  <app>
      <rdgGrp n="['but']">
          <rdg wit="f1818">but</rdg>
          <rdg wit="fThomas">but</rdg>
          <rdg wit="fMS">but</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['he', 'breathed', 'with']">
          <rdg wit="f1818">he breathed with</rdg>
          <rdg wit="f1823">he breathed with</rdg>
          <rdg wit="fThomas">he breathed with</rdg>
          <rdg wit="f1831">he breathed with</rdg>
          <rdg wit="fMS">he breathed with</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 
- 
- ```xml
  <!-- search `as far as` to locate -->
  <app>
      <rdgGrp n="['was']">
          <rdg wit="f1818">was</rdg>
          <rdg wit="f1823">was</rdg>
          <rdg wit="fThomas">was</rdg>
          <rdg wit="f1831">was</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['in']">
          <rdg wit="f1818">in</rdg>
          <rdg wit="f1823">in</rdg>
          <rdg wit="fThomas">in</rdg>
          <rdg wit="f1831">in</rdg>
          <rdg wit="fMS">in</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 

 ```xml
  <app>
      <rdgGrp n="['my', 'duties', 'towards']">
          <rdg wit="f1818">My duties towards</rdg>
          <rdg wit="f1823">My duties towards</rdg>
          <rdg wit="fThomas">My duties towards</rdg>
          <rdg wit="f1831">My duties towards</rdg>
          <rdg wit="fMS">My duties towards</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['the', 'beings', 'of']">
          <rdg wit="f1823">the beings of</rdg>
          <rdg wit="f1831">the beings of</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 
 
 ```xml
  <app>
      <rdgGrp n="['had', 'greater', 'claims']">
          <rdg wit="f1818">had greater claims</rdg>
          <rdg wit="f1823">had greater claims</rdg>
          <rdg wit="fThomas">had greater claims</rdg>
          <rdg wit="f1831">had greater claims</rdg>
          <rdg wit="fMS">had greater claims</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['to', 'my', 'attention,']">
          <rdg wit="f1818">to my attention,</rdg>
          <rdg wit="f1823">to my attention,</rdg>
          <rdg wit="fThomas">to my attention,</rdg>
          <rdg wit="f1831">to my attention,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 

 ```xml
  <!-- search `have little chance` to locate -->
  <app>
      <rdgGrp n="['you']">
          <rdg wit="f1818">you</rdg>
          <rdg wit="f1823">you</rdg>
          <rdg wit="fThomas">you</rdg>
          <rdg wit="f1831">you</rdg>
          <rdg wit="fMS">you</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['will']">
          <rdg wit="f1818">will</rdg>
          <rdg wit="f1823">will</rdg>
          <rdg wit="fThomas">will</rdg>
          <rdg wit="f1831">will</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 

 ```xml
  <app>
      <rdgGrp n="['me', 'else']">
          <rdg wit="fMS">me else</rdg>
      </rdgGrp>
      <rdgGrp n="['me;', 'in', 'other']">
          <rdg wit="f1818">me; in other</rdg>
          <rdg wit="f1823">me; in other</rdg>
          <rdg wit="fThomas">me; in other</rdg>
          <rdg wit="f1831">me; in other</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['respects']">
          <rdg wit="f1818">respects</rdg>
          <rdg wit="f1823">respects</rdg>
          <rdg wit="fThomas">respects</rdg>
      </rdgGrp>
      <rdgGrp n="['respects,']">
          <rdg wit="f1831">respects,</rdg>
      </rdgGrp>
  </app>
  ```


- [x] 
  
  ```xml
  <!-- search `only happy one` to locate -->
  <app>
      <rdgGrp n="['which']">
          <rdg wit="f1818">which</rdg>
          <rdg wit="f1823">which</rdg>
          <rdg wit="fThomas">which</rdg>
          <rdg wit="f1831">which</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['i', 'have']">
          <rdg wit="f1818">I have</rdg>
          <rdg wit="f1823">I have</rdg>
          <rdg wit="fThomas">I have</rdg>
          <rdg wit="f1831">I have</rdg>
          <rdg wit="fMS">I have</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 

 ```xml
  <app>
      <rdgGrp n="['and', 'his', 'eyes', 'closed']">
          <rdg wit="f1818">and his eyes closed</rdg>
          <rdg wit="f1823">and his eyes closed</rdg>
          <rdg wit="fThomas">and his eyes closed</rdg>
          <rdg wit="f1831">and his eyes closed</rdg>
          <rdg wit="fMS">&lt;lb n="c57-0180__main__30"/&gt;and his eyes closed</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['for', 'ever,']">
          <rdg wit="f1818">for ever,</rdg>
          <rdg wit="f1823">for ever,</rdg>
          <rdg wit="fThomas">for ever,</rdg>
          <rdg wit="f1831">for &lt;pb xml:id="F1831_v_213" n="197"/&gt;ever,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['while']">
          <rdg wit="f1818">while</rdg>
          <rdg wit="f1823">while</rdg>
          <rdg wit="fThomas">while</rdg>
          <rdg wit="f1831">while</rdg>
          <rdg wit="fMS">while</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['the', 'irradiation', 'of']">
          <rdg wit="f1818">the irradiation of</rdg>
          <rdg wit="f1823">the irradiation of</rdg>
          <rdg wit="fThomas">the irradiation of</rdg>
          <rdg wit="f1831">the irradiation of</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['what']">
          <rdg wit="f1818">what</rdg>
          <rdg wit="f1823">what</rdg>
          <rdg wit="fThomas">what</rdg>
          <rdg wit="f1831">what</rdg>
          <rdg wit="fMS">What</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['comment']">
          <rdg wit="f1818">comment</rdg>
          <rdg wit="f1823">comment</rdg>
          <rdg wit="fThomas">comment</rdg>
          <rdg wit="f1831">comment</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['the', 'tale']">
          <rdg wit="f1818">the tale</rdg>
          <rdg wit="f1823">the tale</rdg>
          <rdg wit="fThomas">the tale</rdg>
          <rdg wit="f1831">the tale</rdg>
      </rdgGrp>
      <rdgGrp n="['i', 'will', 'try', 'for', 'the', 'tale']">
          <rdg wit="fMS">I will try for the tale</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['which']">
          <rdg wit="f1818">which</rdg>
          <rdg wit="f1823">which</rdg>
          <rdg wit="fThomas">which</rdg>
          <rdg wit="f1831">which</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['exclamations', 'of', 'grief']">
          <rdg wit="f1818">exclamations of grief</rdg>
          <rdg wit="f1823">exclamations of grief</rdg>
          <rdg wit="fThomas">exclamations of grief</rdg>
          <rdg wit="f1831">exclamations of grief</rdg>
          <rdg wit="fMS">exclamations of grief</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['and', 'horror,']">
          <rdg wit="f1818">and horror,</rdg>
          <rdg wit="f1823">and horror,</rdg>
          <rdg wit="fThomas">and horror,</rdg>
          <rdg wit="f1831">and horror,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['i', 'called', 'on', 'him', 'to', 'stay.']">
          <rdg wit="f1818">I called on him to stay.</rdg>
          <rdg wit="f1823">I called on him to stay.</rdg>
          <rdg wit="fThomas">I called on him to stay.</rdg>
          <rdg wit="f1831">I called on him to stay.</rdg>
          <rdg wit="fMS">I called on him to stay.</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['&lt;p-end/&gt;', '&lt;p-start/&gt;']">
          <rdg wit="f1818">&lt;p eID="novel1_letter4_div4_p77"/&gt; &lt;p
              sID="novel1_letter4_div4_p78"/&gt;</rdg>
          <rdg wit="f1823">&lt;p eID="novel1_letter4_div4_p77"/&gt; &lt;p
              sID="novel1_letter4_div4_p78"/&gt;</rdg>
          <rdg wit="fThomas">&lt;p eID="novel1_letter4_div4_p77"/&gt; &lt;p
              sID="novel1_letter4_div4_p78"/&gt;</rdg>
          <rdg wit="f1831">&lt;p eID="novel1_letter4_div4_p79"/&gt; &lt;p
              sID="novel1_letter4_div4_p80"/&gt;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['rage', 'of', 'some']">
          <rdg wit="f1818">rage of some</rdg>
          <rdg wit="f1823">rage of some</rdg>
          <rdg wit="fThomas">rage of some</rdg>
          <rdg wit="f1831">rage of some</rdg>
      </rdgGrp>
      <rdgGrp n="['rage.', 'that']">
          <rdg wit="fMS">rage. That</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['uncontrolable']">
          <rdg wit="f1823">uncontrolable</rdg>
      </rdgGrp>
      <rdgGrp n="['uncontrollable']">
          <rdg wit="f1818">uncontrollable</rdg>
          <rdg wit="fThomas">uncontrollable</rdg>
          <rdg wit="f1831">uncontrollable</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['passion.', '&lt;p-end/&gt;', '&lt;p-start/&gt;', '&#34;that']">
          <rdg wit="f1818">passion. &lt;p eID="novel1_letter4_div4_p78"/&gt; &lt;p
              sID="novel1_letter4_div4_p79"/&gt; “That</rdg>
          <rdg wit="f1823">passion. &lt;p eID="novel1_letter4_div4_p78"/&gt; &lt;p
              sID="novel1_letter4_div4_p79"/&gt; “That</rdg>
          <rdg wit="fThomas">passion. &lt;p eID="novel1_letter4_div4_p78"/&gt; &lt;p
              sID="novel1_letter4_div4_p79"/&gt; “That</rdg>
          <rdg wit="f1831">passion. &lt;p eID="novel1_letter4_div4_p80"/&gt; &lt;p
              sID="novel1_letter4_div4_p81"/&gt; “That</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `what does it avail that` to locate -->
  <app>
      <rdgGrp n="['i']">
          <rdg wit="f1818">&lt;pb xml:id="F1818_v3_185" n="181"/&gt;I</rdg>
          <rdg wit="f1823">I</rdg>
          <rdg wit="fThomas">&lt;pb xml:id="F1818_v3_185" n="181"/&gt;I</rdg>
          <rdg wit="f1831">I</rdg>
          <rdg wit="fMS">I</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['now']">
          <rdg wit="f1818">now</rdg>
          <rdg wit="f1823">now</rdg>
          <rdg wit="fThomas">now</rdg>
          <rdg wit="f1831">now</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['who']">
          <rdg wit="f1818">who</rdg>
          <rdg wit="f1823">who</rdg>
          <rdg wit="fThomas">who</rdg>
          <rdg wit="f1831">who</rdg>
          <rdg wit="fMS">who</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['irretrievably']">
          <rdg wit="f1818">irretrievably</rdg>
          <rdg wit="f1823">irretrievably</rdg>
          <rdg wit="fThomas">irretrievably</rdg>
          <rdg wit="f1831">irretrievably</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['he']">
          <rdg wit="f1818">he</rdg>
          <rdg wit="f1823">he</rdg>
          <rdg wit="fThomas">he</rdg>
          <rdg wit="f1831">he</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['cannot']">
          <rdg wit="f1823">cannot</rdg>
          <rdg wit="f1831">cannot</rdg>
      </rdgGrp>
      <rdgGrp n="['may', 'not']">
          <rdg wit="f1818">may not</rdg>
          <rdg wit="fThomas">may not</rdg>
          <rdg wit="fMS">may not</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['again', 'raise', 'my']">
          <rdg wit="f1818">again raise my</rdg>
          <rdg wit="f1823">again raise my</rdg>
          <rdg wit="fThomas">again raise my</rdg>
          <rdg wit="f1831">again raise my</rdg>
      </rdgGrp>
      <rdgGrp n="['look', 'on', 'him']">
          <rdg wit="fMS">look on him</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['eyes', 'to']">
          <rdg wit="f1823">eyes to</rdg>
          <rdg wit="f1831">eyes to</rdg>
      </rdgGrp>
      <rdgGrp n="['looks', 'upon']">
          <rdg wit="f1818">looks upon</rdg>
          <rdg wit="fThomas">looks upon</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['his', 'face,']">
          <rdg wit="f1818">his face,</rdg>
          <rdg wit="f1823">his face,</rdg>
          <rdg wit="fThomas">his face,</rdg>
          <rdg wit="f1831">his face,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['before', 'you']">
          <rdg wit="f1818">before you</rdg>
          <rdg wit="f1823">before you</rdg>
          <rdg wit="fThomas">before you</rdg>
          <rdg wit="f1831">before you</rdg>
          <rdg wit="fMS">before you</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['had']">
          <rdg wit="f1818">had</rdg>
          <rdg wit="f1823">had</rdg>
          <rdg wit="fThomas">had</rdg>
          <rdg wit="f1831">had</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['suffered', 'not']">
          <rdg wit="f1818">suffered not</rdg>
          <rdg wit="f1823">suffered not</rdg>
          <rdg wit="fThomas">suffered not</rdg>
          <rdg wit="f1831">suffered not</rdg>
          <rdg wit="fMS">suffered not</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['more']">
          <rdg wit="f1818">more</rdg>
          <rdg wit="fThomas">more</rdg>
          <rdg wit="fMS">more</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['in']">
          <rdg wit="f1818">in</rdg>
          <rdg wit="f1823">in</rdg>
          <rdg wit="fThomas">in</rdg>
          <rdg wit="f1831">in</rdg>
          <rdg wit="fMS">&lt;lb n="c57-0182__main__30"/&gt;in</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['the', 'consummation', 'of', 'the']">
          <rdg wit="f1818">the consummation of the</rdg>
          <rdg wit="f1823">the consummation of the</rdg>
          <rdg wit="fThomas">the consummation of the</rdg>
          <rdg wit="f1831">the consummation of the</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['deed;—oh!']">
          <rdg wit="f1818">deed;—oh!</rdg>
          <rdg wit="fThomas">deed;—oh!</rdg>
      </rdgGrp>
      <rdgGrp n="['deed—oh!']">
          <rdg wit="f1823">deed—oh!</rdg>
          <rdg wit="f1831">deed—oh!</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['not']">
          <rdg wit="f1818">not</rdg>
          <rdg wit="f1823">not</rdg>
          <rdg wit="fThomas">not</rdg>
          <rdg wit="f1831">not</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['and']">
          <rdg wit="f1818">and</rdg>
          <rdg wit="f1823">and</rdg>
          <rdg wit="fThomas">and</rdg>
          <rdg wit="f1831">and</rdg>
      </rdgGrp>
      <rdgGrp n="['and sympathy', 'and']">
          <rdg wit="fMS">&amp;&lt;lb n="c57-0183__main__3"/&gt;sympathy and</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['sympathy;', 'and,']">
          <rdg wit="f1818">sympathy; and,</rdg>
          <rdg wit="f1823">sympathy; and,</rdg>
          <rdg wit="fThomas">sympathy; and,</rdg>
          <rdg wit="f1831">sympathy; and,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp
              n="['that', 'it', 'should', 'be', 'accomplished.', 'i', 'knew', 'that', 'i', 'was', 'preparing', 'for', 'myself', 'a', 'deadly', 'torture;', 'but', 'i', 'was', 'the', 'slave,', 'not', 'the']">
          <rdg wit="f1818">that it should be accomplished. I knew that I was preparing for myself
              a deadly torture; but I was the slave, not the</rdg>
          <rdg wit="f1823">that it should be accomplished. I knew that I was preparing for myself
              a deadly torture; but I was the slave, not the</rdg>
          <rdg wit="fThomas">that it should be accomplished. I knew that I was preparing for
              myself a deadly torture; but I was the slave, not the</rdg>
          <rdg wit="f1831">that it should be accomplished. I knew that I was preparing for myself
              a deadly torture; but I was the slave, not the</rdg>
      </rdgGrp>
      <rdgGrp n="['to', 'execute', 'it—yet']">
          <rdg wit="fMS">to execute it—Yet</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['master']">
          <rdg wit="f1818">master</rdg>
          <rdg wit="fThomas">master</rdg>
      </rdgGrp>
      <rdgGrp n="['master,']">
          <rdg wit="f1823">master,</rdg>
          <rdg wit="f1831">master,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp
              n="['of', 'an', 'impulse,', 'which', 'i', 'detested,', 'yet', 'could', 'not', 'disobey.', 'yet']">
          <rdg wit="f1818">of an impulse, which I detested, yet could not disobey. Yet</rdg>
          <rdg wit="f1823">of an impulse, which I detested, yet could not disobey. Yet</rdg>
          <rdg wit="fThomas">of an impulse, which I detested, yet could not disobey. Yet</rdg>
          <rdg wit="f1831">of an impulse, which I detested, yet could not disobey. Yet</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `design became an insatiable passion.` to locate -->
  <app>
      <rdgGrp n="['and']">
          <rdg wit="f1818">And</rdg>
          <rdg wit="f1823">And</rdg>
          <rdg wit="fThomas">And</rdg>
          <rdg wit="f1831">And</rdg>
          <rdg wit="fMS">And</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['now']">
          <rdg wit="f1818">now</rdg>
          <rdg wit="f1823">now</rdg>
          <rdg wit="fThomas">now</rdg>
          <rdg wit="f1831">now</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['&lt;p-end/&gt;', '&lt;p-start/&gt;', 'i', 'was']">
          <rdg wit="f1818">&lt;p eID="novel1_letter4_div4_p82"/&gt; &lt;p
              sID="novel1_letter4_div4_p83"/&gt; I was</rdg>
          <rdg wit="f1823">&lt;p eID="novel1_letter4_div4_p82"/&gt; &lt;p
              sID="novel1_letter4_div4_p83"/&gt; I was</rdg>
          <rdg wit="fThomas">&lt;p eID="novel1_letter4_div4_p82"/&gt; &lt;p
              sID="novel1_letter4_div4_p83"/&gt; I was</rdg>
          <rdg wit="f1831">&lt;p eID="novel1_letter4_div4_p84"/&gt; &lt;p
              sID="novel1_letter4_div4_p85"/&gt; I was</rdg>
          <rdg wit="fMS">&lt;milestone unit="tei:p-END"/&gt; &lt;milestone unit="tei:p-START"/&gt;
              &lt;lb n="c57-0183__main__25"/&gt;I was</rdg>
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

- [x] ```xml
  <app>
      <rdgGrp n="['powers', 'of']">
          <rdg wit="f1818">powers of</rdg>
          <rdg wit="f1823">powers of</rdg>
          <rdg wit="fThomas">powers of</rdg>
          <rdg wit="f1831">powers of</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['eloquence']">
          <rdg wit="f1818">eloquence</rdg>
          <rdg wit="f1823">eloquence</rdg>
          <rdg wit="fThomas">eloquence</rdg>
          <rdg wit="f1831">eloquence</rdg>
          <rdg wit="fMS">eloquence</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['the']">
          <rdg wit="f1818">the</rdg>
          <rdg wit="f1823">the</rdg>
          <rdg wit="fThomas">the</rdg>
          <rdg wit="f1831">the</rdg>
      </rdgGrp>
      <rdgGrp n="['', '', 'the']">
          <rdg wit="fMS">&lt;lb n="c57-0183__main__29"/&gt;&lt;sga-add place="sublinear"
              sID="c57-0183__main__d4e36835"/&gt; &lt;metamark function="displacement"
              xml:id="c57-0183.03"&gt;^&lt;/metamark&gt; &lt;lb
              n="c57-0183__left_margin__1"/&gt;&lt;sga-add
              sID="c57-0183__left_margin__d4e36844"/&gt;the</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['lifeless']">
          <rdg wit="f1818">lifeless</rdg>
          <rdg wit="f1823">lifeless</rdg>
          <rdg wit="fThomas">lifeless</rdg>
          <rdg wit="f1831">lifeless</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['still']">
          <rdg wit="f1818">still</rdg>
          <rdg wit="f1823">still</rdg>
          <rdg wit="fThomas">still</rdg>
          <rdg wit="f1831">still</rdg>
          <rdg wit="fMS">still</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['would', 'he', 'be', 'the', 'object,', 'again']">
          <rdg wit="f1818">would he be the object, again</rdg>
          <rdg wit="f1823">would he be the object, again</rdg>
          <rdg wit="fThomas">would he be the object, again</rdg>
          <rdg wit="f1831">would he be the object, again</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['he', 'become', 'the']">
          <rdg wit="f1818">he become the</rdg>
          <rdg wit="f1823">he become the</rdg>
          <rdg wit="fThomas">he become the</rdg>
          <rdg wit="f1831">he become the</rdg>
      </rdgGrp>
      <rdgGrp n="['you', 'persue', 'him', 'with']">
          <rdg wit="fMS">you &lt;lb n="c57-0184__main__4"/&gt;persue him with</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['prey']">
          <rdg wit="f1818">prey</rdg>
          <rdg wit="fThomas">prey</rdg>
      </rdgGrp>
      <rdgGrp n="['prey,']">
          <rdg wit="f1823">prey,</rdg>
          <rdg wit="f1831">prey,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['of']">
          <rdg wit="f1818">of</rdg>
          <rdg wit="f1823">of</rdg>
          <rdg wit="fThomas">of</rdg>
          <rdg wit="f1831">of</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `shadow,` to locate -->
  <app>
      <rdgGrp n="['and']">
          <rdg wit="f1818">and</rdg>
          <rdg wit="f1823">and</rdg>
          <rdg wit="fThomas">and</rdg>
          <rdg wit="f1831">and</rdg>
          <rdg wit="fMS">and</rdg>
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

- [x] ```xml
  <app>
      <rdgGrp n="['i', 'am']">
          <rdg wit="f1818">I am</rdg>
          <rdg wit="f1823">I am</rdg>
          <rdg wit="fThomas">I am</rdg>
          <rdg wit="f1831">I am</rdg>
          <rdg wit="fMS">I am</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['well']">
          <rdg wit="f1818">well</rdg>
          <rdg wit="f1823">well</rdg>
          <rdg wit="fThomas">well</rdg>
          <rdg wit="f1831">well</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['enjoyment.', 'once', 'i']">
          <rdg wit="f1818">enjoyment. Once I</rdg>
          <rdg wit="f1823">enjoyment. Once I</rdg>
          <rdg wit="fThomas">enjoyment. Once I</rdg>
          <rdg wit="f1831">enjoyment. Once I</rdg>
          <rdg wit="fMS">enjoyment. Once &lt;lb n="c57-0184__main__25"/&gt;I</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['falsely']">
          <rdg wit="f1818">falsely</rdg>
          <rdg wit="f1823">falsely</rdg>
          <rdg wit="fThomas">falsely</rdg>
          <rdg wit="f1831">falsely</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['but', 'now']">
          <rdg wit="f1818">But now</rdg>
          <rdg wit="f1823">But now</rdg>
          <rdg wit="fThomas">But now</rdg>
          <rdg wit="f1831">But now</rdg>
          <rdg wit="fMS">But now</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['', '&lt;del&gt;crime&lt;/del&gt;']">
          <rdg wit="fMS">&lt;mod sID="c57-0184__main__d4e37085"/&gt; &lt;del rend="strikethrough"
              xml:id="c57-0184__main__d4e37087"&gt;crime&lt;/del&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['crime']">
          <rdg wit="f1831">crime</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['vice']">
          <rdg wit="f1818">vice</rdg>
          <rdg wit="f1823">vice</rdg>
          <rdg wit="fThomas">vice</rdg>
          <rdg wit="fMS">&lt;anchor xml:id="c57-0184.03"/&gt;&lt;lb
              n="c57-0184__left_margin__1"/&gt;&lt;sga-add
              sID="c57-0184__left_margin__d4e37096"/&gt;vice</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
  		<rdgGrp n="['over', 'the', 'frightful', 'catalogue']">
  			<rdg wit="f1818">over the frightful catalogue</rdg>
  			<rdg wit="f1823">over the frightful catalogue</rdg>
  			<rdg wit="fThomas">over the frightful catalogue</rdg>
  			<rdg wit="f1831">over the frightful catalogue</rdg>
  			<rdg wit="fMS">over the frightful &lt;w ana="start"/&gt;cata&lt;lb
  				n="c57-0184__main__33"/&gt;logue&lt;w ana="end"/&gt;</rdg>
  		</rdgGrp>
  	</app>
  	<app>
  		<rdgGrp n="['of', 'my']">
  			<rdg wit="f1818">of my</rdg>
  			<rdg wit="f1823">of my</rdg>
  			<rdg wit="fThomas">of my</rdg>
  			<rdg wit="f1831">of my</rdg>
  		</rdgGrp>
  	</app>
  	<app>
  		<rdgGrp n="['deeds,']">
  			<rdg wit="f1818">deeds,</rdg>
  			<rdg wit="f1823">deeds,</rdg>
  			<rdg wit="fThomas">deeds,</rdg>
  		</rdgGrp>
  		<rdgGrp n="['sins,']">
  			<rdg wit="f1831">sins,</rdg>
  		</rdgGrp>
  	</app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['visions']">
          <rdg wit="f1818">visions</rdg>
          <rdg wit="f1823">visions</rdg>
          <rdg wit="fThomas">visions</rdg>
          <rdg wit="f1831">visions</rdg>
          <rdg wit="fMS">visions</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['of', 'the', 'beauty', 'and', 'the', 'majesty']">
          <rdg wit="f1818">of the beauty and the majesty</rdg>
          <rdg wit="f1823">of the beauty and the majesty</rdg>
          <rdg wit="fThomas">of the beauty and the majesty</rdg>
          <rdg wit="f1831">of the beauty and the majesty</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['enemy']">
          <rdg wit="f1818">enemy</rdg>
          <rdg wit="f1823">enemy</rdg>
          <rdg wit="fThomas">enemy</rdg>
          <rdg wit="f1831">enemy</rdg>
          <rdg wit="fMS">enemy</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['of', 'god', 'and', 'man']">
          <rdg wit="f1818">of God and man</rdg>
          <rdg wit="f1823">of God and man</rdg>
          <rdg wit="fThomas">of God and man</rdg>
          <rdg wit="f1831">of God and man</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['i', 'am']">
          <rdg wit="f1818">I am</rdg>
          <rdg wit="f1823">I am</rdg>
          <rdg wit="fThomas">I am</rdg>
          <rdg wit="f1831">I am</rdg>
          <rdg wit="fMS">I am</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['quite']">
          <rdg wit="f1818">quite</rdg>
          <rdg wit="fThomas">quite</rdg>
          <rdg wit="fMS">quite</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['he', 'gave']">
          <rdg wit="f1818">he gave</rdg>
          <rdg wit="f1823">he gave</rdg>
          <rdg wit="fThomas">he gave</rdg>
          <rdg wit="f1831">he gave</rdg>
          <rdg wit="fMS">&lt;lb n="c57-0185__main__8"/&gt;he gave</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['you']">
          <rdg wit="f1818">you</rdg>
          <rdg wit="f1823">you</rdg>
          <rdg wit="fThomas">you</rdg>
          <rdg wit="f1831">you</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['am', 'i']">
          <rdg wit="f1818">Am I</rdg>
          <rdg wit="f1823">Am I</rdg>
          <rdg wit="fThomas">Am I</rdg>
          <rdg wit="f1831">Am I</rdg>
      </rdgGrp>
      <rdgGrp n="['and', 'am', 'i']">
          <rdg wit="fMS">And &lt;lb n="c57-0185__main__16"/&gt;am I</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['to', 'be', 'thought']">
          <rdg wit="f1818">to be thought</rdg>
          <rdg wit="f1823">to be thought</rdg>
          <rdg wit="fThomas">to be thought</rdg>
          <rdg wit="f1831">to be thought</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['spurned']">
          <rdg wit="f1818">spurned </rdg>
          <rdg wit="f1823">spurned </rdg>
          <rdg wit="fThomas">spurned </rdg>
          <rdg wit="f1831">spurned </rdg>
          <rdg wit="fMS">&lt;sga-add eID="c57-0185__main__d4e37258"/&gt;spurned</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['at,']">
          <rdg wit="f1818">at,</rdg>
          <rdg wit="f1823">at,</rdg>
          <rdg wit="fThomas">at,</rdg>
          <rdg wit="f1831">at,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `other living thing.` to locate -->
  <app>
      <rdgGrp n="['i']">
          <rdg wit="f1818">I</rdg>
          <rdg wit="f1823">I</rdg>
          <rdg wit="fThomas">I</rdg>
          <rdg wit="f1831">I</rdg>
          <rdg wit="fMS">&lt;lb n="c57-0185__main__30"/&gt;I</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['have']">
          <rdg wit="f1818">have</rdg>
          <rdg wit="f1823">have</rdg>
          <rdg wit="fThomas">have</rdg>
          <rdg wit="f1831">have</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['i', 'loathe', 'myself.', 'fear']">
          <rdg wit="fMS">I loathe myself. &lt;lb n="c57-0186__main__1"/&gt;Fear</rdg>
      </rdgGrp>
      <rdgGrp n="['long', 'for', 'the', 'moment', 'when']">
          <rdg wit="f1818">long for the moment when</rdg>
          <rdg wit="f1823">long for the moment when</rdg>
          <rdg wit="fThomas">long for the moment when</rdg>
          <rdg wit="f1831">long for &lt;pb xml:id="F1831_v_217" n="201"/&gt;the moment when</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['these', 'hands']">
          <rdg wit="f1823">these hands</rdg>
          <rdg wit="f1831">these hands</rdg>
      </rdgGrp>
      <rdgGrp n="['they']">
          <rdg wit="f1818">they</rdg>
          <rdg wit="fThomas">they</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['will', 'meet', 'my', 'eyes,', 'when']">
          <rdg wit="f1818">will meet my eyes, when</rdg>
          <rdg wit="f1823">will meet my eyes, when</rdg>
          <rdg wit="fThomas">will meet my eyes, when</rdg>
          <rdg wit="f1831">will meet my eyes, when</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['it']">
          <rdg wit="f1818">it</rdg>
          <rdg wit="fThomas">it</rdg>
      </rdgGrp>
      <rdgGrp n="['that', 'imagination']">
          <rdg wit="f1823">that imagination</rdg>
          <rdg wit="f1831">that imagination</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['will', 'haunt', 'my']">
          <rdg wit="f1818">will haunt my</rdg>
          <rdg wit="f1823">will haunt my</rdg>
          <rdg wit="fThomas">will haunt my</rdg>
          <rdg wit="f1831">will haunt my</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['thoughts']">
          <rdg wit="f1831">thoughts</rdg>
      </rdgGrp>
      <rdgGrp n="['thoughts,']">
          <rdg wit="f1818">thoughts,</rdg>
          <rdg wit="f1823">thoughts,</rdg>
          <rdg wit="fThomas">thoughts,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['no', 'more.', '&lt;p-end/&gt;', '&lt;p-start/&gt;', '&#34;fear']">
          <rdg wit="f1818">no more. &lt;p eID="novel1_letter4_div4_p86"/&gt; &lt;p
              sID="novel1_letter4_div4_p87"/&gt; “Fear</rdg>
          <rdg wit="f1823">no more. &lt;p eID="novel1_letter4_div4_p86"/&gt; &lt;p
              sID="novel1_letter4_div4_p87"/&gt; “Fear</rdg>
          <rdg wit="fThomas">no more. &lt;p eID="novel1_letter4_div4_p86"/&gt; &lt;p
              sID="novel1_letter4_div4_p87"/&gt; “Fear</rdg>
          <rdg wit="f1831">no more. &lt;p eID="novel1_letter4_div4_p88"/&gt; &lt;p
              sID="novel1_letter4_div4_p89"/&gt; “Fear</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['death']">
          <rdg wit="f1818">death</rdg>
          <rdg wit="f1823">death</rdg>
          <rdg wit="fThomas">death</rdg>
          <rdg wit="f1831">death</rdg>
          <rdg wit="fMS">death</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['is', 'needed']">
          <rdg wit="f1818">is needed</rdg>
          <rdg wit="f1823">is needed</rdg>
          <rdg wit="fThomas">is needed</rdg>
          <rdg wit="f1831">is needed</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['hither,']">
          <rdg wit="f1818">hither,</rdg>
          <rdg wit="f1823">hither,</rdg>
          <rdg wit="fThomas">hither,</rdg>
      </rdgGrp>
      <rdgGrp n="['i']">
          <rdg wit="fMS">I</rdg>
      </rdgGrp>
      <rdgGrp n="['thither,']">
          <rdg wit="f1831">thither,</rdg>
      </rdgGrp>
  </app>
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
  <app>
      <rdgGrp n="['called']">
          <rdg wit="f1818">called</rdg>
          <rdg wit="f1823">called</rdg>
          <rdg wit="fThomas">called</rdg>
          <rdg wit="f1831">called</rdg>
      </rdgGrp>
      <rdgGrp n="['created']">
          <rdg wit="fMS">created</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['me']">
          <rdg wit="f1818">me</rdg>
          <rdg wit="f1823">me</rdg>
          <rdg wit="fThomas">me</rdg>
          <rdg wit="f1831">me</rdg>
          <rdg wit="fMS">me</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['into', 'being;']">
          <rdg wit="f1818">into being;</rdg>
          <rdg wit="f1823">into being;</rdg>
          <rdg wit="fThomas">into being;</rdg>
          <rdg wit="f1831">into being;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <!-- search `remembrance` to locate -->
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
      <rdgGrp n="['very']">
          <rdg wit="f1818">very</rdg>
          <rdg wit="f1823">very</rdg>
          <rdg wit="fThomas">very</rdg>
          <rdg wit="f1831">very</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['and', 'in', 'this']">
          <rdg wit="f1818">and in this</rdg>
          <rdg wit="f1823">and in this</rdg>
          <rdg wit="fThomas">and in this</rdg>
          <rdg wit="f1831">and in this</rdg>
          <rdg wit="fMS">&lt;lb n="c57-0186__main__22"/&gt;And in this</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['condition']">
          <rdg wit="f1818">condition</rdg>
          <rdg wit="f1823">condition</rdg>
          <rdg wit="fThomas">condition</rdg>
          <rdg wit="f1831">condition</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['when', 'the', 'images']">
          <rdg wit="f1818">when the images</rdg>
          <rdg wit="f1823">when the images</rdg>
          <rdg wit="fThomas">when the images</rdg>
          <rdg wit="f1831">when the images</rdg>
          <rdg wit="fMS">when the images</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['which']">
          <rdg wit="f1818">which</rdg>
          <rdg wit="f1823">which</rdg>
          <rdg wit="fThomas">which</rdg>
          <rdg wit="f1831">which</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['and', 'heard', 'the', 'rustling', 'of']">
          <rdg wit="f1818">and heard the rustling of</rdg>
          <rdg wit="f1823">and heard the rustling of</rdg>
          <rdg wit="fThomas">and heard the rustling of</rdg>
          <rdg wit="f1831">and heard the rustling of</rdg>
          <rdg wit="fMS">&amp; heard the rustling of</rdg>
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

- [ ] ```xml
  <app>
      <rdgGrp n="['', '&lt;del&gt;misery&lt;/del&gt;', '', '', 'wretchedness', '']">
          <rdg wit="fMS">&lt;mod sID="c57-0187__main__d4e37537"/&gt; &lt;del rend="strikethrough"
              xml:id="c57-0187__main__d4e37539"&gt;misery&lt;/del&gt; &lt;sga-add
              place="sublinear" sID="c57-0187__main__d4e37542"/&gt; &lt;metamark
              function="insert"&gt;^&lt;/metamark&gt; &lt;sga-add
              eID="c57-0187__main__d4e37542"/&gt;&lt;sga-add place="superlinear"
              sID="c57-0187__main__d4e37548"/&gt;wretchedness &lt;sga-add
              eID="c57-0187__main__d4e37548"/&gt;&lt;mod eID="c57-0187__main__d4e37537"/&gt;</rdg>
      </rdgGrp>
      <rdgGrp
              n="['wretchedness;', 'and', 'if', 'yet,', 'in', 'some', 'mode', 'unknown', 'to', 'me,', 'thou']">
          <rdg wit="f1818">wretchedness; and if yet, in some mode unknown to me, thou</rdg>
          <rdg wit="f1823">wretchedness; and if yet, in some mode unknown to me, thou</rdg>
          <rdg wit="fThomas">wretchedness; and if yet, in some mode unknown to me, thou</rdg>
          <rdg wit="f1831">wretchedness; and if yet, in some mode unknown to me, thou</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['hadst']">
          <rdg wit="f1823">hadst</rdg>
          <rdg wit="f1831">hadst</rdg>
      </rdgGrp>
      <rdgGrp n="['hast']">
          <rdg wit="f1818">hast</rdg>
          <rdg wit="fThomas">hast</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['not']">
          <rdg wit="f1818">not</rdg>
          <rdg wit="f1823">not</rdg>
          <rdg wit="fThomas">not</rdg>
          <rdg wit="f1831">not</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['yet']">
          <rdg wit="f1818">yet</rdg>
          <rdg wit="fThomas">yet</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['ceased']">
          <rdg wit="f1818">ceased</rdg>
          <rdg wit="f1823">ceased</rdg>
          <rdg wit="fThomas">ceased</rdg>
          <rdg wit="f1831">ceased</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['others', 'and now', 'you', 'will']">
          <rdg wit="fMS">others &amp;&lt;lb n="c57-0187__main__6"/&gt;now you will</rdg>
      </rdgGrp>
      <rdgGrp n="['think', 'and', 'feel,', 'thou']">
          <rdg wit="f1818">think and feel, thou</rdg>
          <rdg wit="f1823">think and feel, thou</rdg>
          <rdg wit="fThomas">think and feel, thou</rdg>
          <rdg wit="f1831">think and feel, thou</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['desirest']">
          <rdg wit="f1818">desirest</rdg>
          <rdg wit="fThomas">desirest</rdg>
      </rdgGrp>
      <rdgGrp n="['wouldst']">
          <rdg wit="f1823">wouldst</rdg>
          <rdg wit="f1831">wouldst</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['not']">
          <rdg wit="f1818">not</rdg>
          <rdg wit="f1823">not</rdg>
          <rdg wit="fThomas">not</rdg>
          <rdg wit="f1831">not</rdg>
          <rdg wit="fMS">not</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['desire']">
          <rdg wit="f1823">desire</rdg>
          <rdg wit="f1831">desire</rdg>
          <rdg wit="fMS">desire</rdg>
      </rdgGrp>
  </app>
  ```
  
- [x] ```xml
  <app>
      <rdgGrp n="['of', 'remorse']">
          <rdg wit="f1818">of remorse</rdg>
          <rdg wit="f1823">of remorse</rdg>
          <rdg wit="fThomas">of remorse</rdg>
          <rdg wit="f1831">of remorse</rdg>
      </rdgGrp>
      <rdgGrp n="['that', 'rankles']">
          <rdg wit="fMS">that &lt;lb n="c57-0187__main__10"/&gt;rankles</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['may']">
          <rdg wit="f1818">may</rdg>
          <rdg wit="fThomas">may</rdg>
      </rdgGrp>
      <rdgGrp n="['will']">
          <rdg wit="f1823">will</rdg>
          <rdg wit="f1831">will</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['not', 'cease', 'to']">
          <rdg wit="f1818">not cease to</rdg>
          <rdg wit="f1823">not cease to</rdg>
          <rdg wit="fThomas">not cease to</rdg>
          <rdg wit="f1831">not cease to</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['rankle']">
          <rdg wit="f1818">rankle</rdg>
          <rdg wit="fThomas">rankle</rdg>
          <rdg wit="f1831">rankle</rdg>
      </rdgGrp>
      <rdgGrp n="['rankle,']">
          <rdg wit="f1823">rankle,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['shall', 'ascend', 'my']">
          <rdg wit="f1818">shall ascend my</rdg>
          <rdg wit="f1823">shall ascend my</rdg>
          <rdg wit="fThomas">shall ascend my</rdg>
          <rdg wit="f1831">shall ascend my</rdg>
          <rdg wit="fMS">&lt;lb n="c57-0187__main__16"/&gt;shall ascend my</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['funeral']">
          <rdg wit="f1818">funeral</rdg>
          <rdg wit="f1823">funeral</rdg>
          <rdg wit="fThomas">funeral</rdg>
          <rdg wit="f1831">funeral</rdg>
      </rdgGrp>
  </app>
  ```

- [x] ```xml
  <app>
      <rdgGrp n="['and']">
          <rdg wit="f1818">and</rdg>
          <rdg wit="f1823">and</rdg>
          <rdg wit="fThomas">and</rdg>
          <rdg wit="f1831">and</rdg>
          <rdg wit="fMS">&amp;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['exult', 'in', 'the', 'agony', 'of', 'the', 'torturing', 'flames.']">
          <rdg wit="f1818">exult in the agony of the torturing flames.</rdg>
          <rdg wit="f1823">exult in the agony of the torturing flames.</rdg>
          <rdg wit="fThomas">exult in the agony of the torturing flames.</rdg>
          <rdg wit="f1831">exult in the agony of the torturing flames.</rdg>
      </rdgGrp>
  </app>
  ```

- [ ] 
 
 ```xml
  <app>
      <rdgGrp n="['you', 'were']">
          <rdg wit="f1818">You were</rdg>
          <rdg wit="f1823">You were</rdg>
          <rdg wit="fThomas">You were</rdg>
          <rdg wit="f1831">You were</rdg>
          <rdg wit="fMS">You were</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['hereafter']">
          <rdg wit="f1818">hereafter</rdg>
          <rdg wit="f1823">hereafter</rdg>
          <rdg wit="fThomas">hereafter</rdg>
          <rdg wit="f1831">hereafter</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 2023-07-05 ebb: there's a larger transposition problem with "hereafter" in the MS to correct.


- [x] ```xml
  <app>
      <rdgGrp n="['over', 'the', 'frightful', 'catalogue']">
          <rdg wit="f1818">over the frightful catalogue</rdg>
          <rdg wit="f1823">over the frightful catalogue</rdg>
          <rdg wit="fThomas">over the frightful catalogue</rdg>
          <rdg wit="f1831">over the frightful catalogue</rdg>
          <rdg wit="fMS">over the frightful &lt;w ana="start"/&gt;cata&lt;lb n="c57-0184__main__33"/&gt;logue&lt;w ana="end"/&gt;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['of', 'my']">
          <rdg wit="f1818">of my</rdg>
          <rdg wit="f1823">of my</rdg>
          <rdg wit="fThomas">of my</rdg>
          <rdg wit="f1831">of my</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['deeds,']">
          <rdg wit="f1818">deeds,</rdg>
          <rdg wit="f1823">deeds,</rdg>
          <rdg wit="fThomas">deeds,</rdg>
      </rdgGrp>
      <rdgGrp n="['sins,']">
          <rdg wit="f1831">sins,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] 2023-07-05 ebb: Adjust alignment to show where MS sentence breaks missing in other witnesses (otherwise identical apps)

- [x] 2023-07-05 ebb: Try to line up the witnesses as identical here: (space by `<lb/>`)

```xml
	<app>
		<rdgGrp n="['and discoveries.']">
			<rdg wit="fMS">&amp;&lt;lb n="c57-0180__main__22"/&gt;discoveries.</rdg>
		</rdgGrp>
		<rdgGrp n="['and', 'discoveries.']">
			<rdg wit="f1818">and discoveries.</rdg>
			<rdg wit="f1823">and discoveries.</rdg>
			<rdg wit="fThomas">and discoveries.</rdg>
			<rdg wit="f1831">and discoveries.</rdg>
		</rdgGrp>
	</app>
```

- [x] 2023-07-05 ebb: Adjust longer alignment (transposition issue) re  "what comment can I make on death of this glorious creature" passage
- [x] 2023-07-05 ebb: Add `\n` before `&` in MS to try to line up identical witnesses here:
 
 ```xml
 <app>
		<rdgGrp n="['uncouth and']">
			<rdg wit="fMS">&lt;w ana="start"/&gt;un&lt;lb n="c57-0181__main__25"/&gt;couth&lt;w
				ana="end"/&gt;&amp;</rdg>
		</rdgGrp>
		<rdgGrp n="['uncouth', 'and']">
			<rdg wit="f1818">uncouth and</rdg>
			<rdg wit="f1823">uncouth and</rdg>
			<rdg wit="fThomas">uncouth and</rdg>
			<rdg wit="f1831">uncouth and</rdg>
		</rdgGrp>
	</app>
```	
- [x] 2023-07-05 ebb: Unify in one app the hand-like-mummy passage around MS: "appeared &lt;lb n="c57-0181__main__28"/&gt;like those of the mummies for
				to nothing &lt;lb n="c57-0181__main__29"/&gt;else can I compare its" "texture"
				
- [x] 2023-07-05 ebb: Correct false alignment around "to" here:

```xml
<app>
		<rdgGrp n="['involuntarily', 'while', 'i', 'called', 'on', 'him']">
			<rdg wit="fMS">&lt;w ana="start"/&gt;involun&lt;lb
				n="c57-0181__main__35"/&gt;tarily&lt;w ana="end"/&gt; while I called on him</rdg>
		</rdgGrp>
		<rdgGrp
			n="['involuntarily,', 'and', 'endeavoured', 'to', 'recollect', 'what', 'were', 'my', 'duties', 'with', 'regard']">
			<rdg wit="f1818">involuntarily, and endeavoured to recollect what were my duties with
				regard</rdg>
			<rdg wit="f1823">involuntarily, and endeavoured to recollect what were my duties with
				regard</rdg>
			<rdg wit="fThomas">involuntarily, and endeavoured to recollect what were my duties with
				regard</rdg>
			<rdg wit="f1831">involuntarily, and endeavoured to recollect what were my duties with
				regard</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['to']">
			<rdg wit="f1818">to</rdg>
			<rdg wit="f1823">to</rdg>
			<rdg wit="fThomas">to</rdg>
			<rdg wit="f1831">to</rdg>
			<rdg wit="fMS">to</rdg>
		</rdgGrp>
	</app>
	<app>
		<rdgGrp n="['stay.']">
			<rdg wit="fMS">stay.</rdg>
		</rdgGrp>
		<rdgGrp
			n="['this', 'destroyer.', 'i called on him to stay.&lt;p-end/&gt;', '&lt;p-start/&gt;']">
			<rdg wit="f1818">this destroyer. &lt;longToken&gt;I called on him to stay.&lt;p
				eID="novel1_letter4_div4_p77"/&gt; &lt;/longToken&gt; &lt;p
				sID="novel1_letter4_div4_p78"/&gt;</rdg>
			<rdg wit="f1823">this destroyer. &lt;longToken&gt;I called on him to stay.&lt;p
				eID="novel1_letter4_div4_p77"/&gt; &lt;/longToken&gt; &lt;p
				sID="novel1_letter4_div4_p78"/&gt;</rdg>
			<rdg wit="fThomas">this destroyer. &lt;longToken&gt;I called on him to stay.&lt;p
				eID="novel1_letter4_div4_p77"/&gt;&lt;/longToken&gt; &lt;p
				sID="novel1_letter4_div4_p78"/&gt;</rdg>
			<rdg wit="f1831">this destroyer. &lt;longToken&gt;I called on him to stay.&lt;p
				eID="novel1_letter4_div4_p79"/&gt;&lt;/longToken&gt; &lt;p
				sID="novel1_letter4_div4_p80"/&gt;</rdg>
		</rdgGrp>
	</app>
```

- [x] 2023-07-05 ebb: Unify apps around "scaring" transposition: all witnesses other than MS: "scaring and unearthly" 

- [x] 2023-07-05 ebb: Fix false split alignment, unify apps around MS "completion of the deed" vs. "consummation of the deed" 
- [x] 2023-07-05 ebb: Fix false alignment and organize around MS longToken "power of mischief"
- [x] 2023-07-05 ebb: Tighten alignment around first words of sentence after paragraph break: MS del + "It is not thus" and "Oh! It is not thus"
- [x] 2023-07-05 ebb: Transposition issue: "seek not" vs. "do not seek"

- [x] 2023-07-08 ebb: Fixed fused MS normalized token: 'andseem' (to have a knowledge of my crimes) by setting `<longToken>` around `seem
- [x] 2023-07-05 ebb: Tranposition issue: "craving and ardent" vs. "for ever ardent and craving"
- [x] 2023-07-06 ebb: Fixed with longTokens the passage around fMS: 'to others and now you will not desire my life for my own misery.'
