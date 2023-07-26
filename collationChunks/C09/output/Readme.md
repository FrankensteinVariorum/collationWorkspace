- [x] a long different sentence in 1831. 

  ```xml
  pedantry.<longToken>In a thousand ways he smoothed for me the path of knowledge, and made the most abstruse enquiries clear and facile to my apprehension.</longToken>
  ```

- [x] merge two apps:

  ```xml
  <app>
      <rdgGrp n="['the']">
          <rdg wit="f1818">the</rdg>
          <rdg wit="f1823">the</rdg>
          <rdg wit="fThomas">the</rdg>
          <rdg wit="f1831">the</rdg>
      </rdgGrp>
      <rdgGrp n="['those', 'phænonoma']">
          <rdg wit="fMS">those phænonoma</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['phenomena']">
          <rdg wit="f1823">phenomena</rdg>
          <rdg wit="f1831">phenomena</rdg>
      </rdgGrp>
      <rdgGrp n="['phænomena']">
          <rdg wit="f1818">phænomena</rdg>
          <rdg wit="fThomas">phænomena</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs

  ```xml
  <app>
      <rdgGrp n="['applied', 'to']">
          <rdg wit="fMS">applied to</rdg>
      </rdgGrp>
      <rdgGrp n="['directed', 'their']">
          <rdg wit="f1818">directed their</rdg>
          <rdg wit="f1823">directed their</rdg>
          <rdg wit="fThomas">directed their</rdg>
          <rdg wit="f1831">directed their</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['enquiries']">
          <rdg wit="f1831">enquiries</rdg>
      </rdgGrp>
      <rdgGrp n="['inquiries']">
          <rdg wit="f1818">inquiries</rdg>
          <rdg wit="f1823">inquiries</rdg>
          <rdg wit="fThomas">inquiries</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['towards']">
          <rdg wit="f1818">towards</rdg>
          <rdg wit="f1823">towards</rdg>
          <rdg wit="fThomas">towards</rdg>
          <rdg wit="f1831">towards</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs

  ```xml
  <app>
      <rdgGrp n="['astonishing']">
          <rdg wit="f1818">astonishing</rdg>
          <rdg wit="f1823">astonishing</rdg>
          <rdg wit="fThomas">astonishing</rdg>
          <rdg wit="f1831">astonishing</rdg>
          <rdg wit="fMS">astonishing</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['a']">
          <rdg wit="f1818">a</rdg>
          <rdg wit="f1823">a</rdg>
          <rdg wit="fThomas">a</rdg>
          <rdg wit="f1831">a</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge three apps

  ```xml
  <app>
      <rdgGrp n="['', 'labour', '', '']">
          <rdg wit="fMS">&lt;milestone spanTo="#c56-0038.21" unit="tei:seg"
              xml:id="c56-0038.19"/&gt; labour &lt;anchor xml:id="c56-0038.21"/&gt;&lt;sga-add
              hand="#pbs" place="superlinear" sID="c56-0038__main__d5e7846"/&gt; &lt;metamark
              function="transpose" target="#c56-0038.19"&gt;2&lt;/metamark&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['difficulty']">
          <rdg wit="f1818">difficulty</rdg>
          <rdg wit="f1823">difficulty</rdg>
          <rdg wit="fThomas">difficulty</rdg>
          <rdg wit="f1831">difficulty</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['and']">
          <rdg wit="f1818">and</rdg>
          <rdg wit="f1823">and</rdg>
          <rdg wit="fThomas">and</rdg>
          <rdg wit="f1831">and</rdg>
          <rdg wit="fMS">&lt;sga-add eID="c56-0038__main__d5e7846"/&gt;&amp;&lt;sga-add
              hand="#pbs" place="superlinear" sID="c56-0038__main__d5e7852"/&gt;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['', '', '', 'diffi', 'culty', '.']">
          <rdg wit="fMS">&lt;metamark function="transpose"
              target="#c56-0038.20"&gt;1&lt;/metamark&gt; &lt;sga-add
              eID="c56-0038__main__d5e7852"/&gt; &lt;milestone spanTo="#c56-0038.22"
              unit="tei:seg" xml:id="c56-0038.20"/&gt; diffi &lt;lb
              n="c56-0038__main__10"/&gt;culty &lt;anchor xml:id="c56-0038.22"/&gt;.</rdg>
      </rdgGrp>
      <rdgGrp n="['labour.']">
          <rdg wit="f1818">labour.</rdg>
          <rdg wit="f1823">labour.</rdg>
          <rdg wit="fThomas">labour.</rdg>
          <rdg wit="f1831">labour.</rdg>
      </rdgGrp>
  </app>
  ```

- [x] misalignment: wrapping longToken around del element and `myself` in MS

  ```xml
  <app>
      <rdgGrp n="['&lt;del&gt;unto&lt;/del&gt;']">
          <rdg wit="fMS">&lt;del rend="strikethrough"
              xml:id="c56-0038__main__d5e7879"&gt;unto&lt;/del&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['myself,']">
          <rdg wit="f1823">myself,</rdg>
          <rdg wit="f1831">myself,</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['myself']">
          <rdg wit="f1818">myself</rdg>
          <rdg wit="fThomas">myself</rdg>
          <rdg wit="fMS">myself</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge two apps:

  ```xml
  <app>
      <rdgGrp n="['still']">
          <rdg wit="f1818">still</rdg>
          <rdg wit="f1823">still</rdg>
          <rdg wit="fThomas">still</rdg>
          <rdg wit="f1831">still</rdg>
      </rdgGrp>
      <rdgGrp n="['i', 'still']">
          <rdg wit="fMS">I still</rdg>
      </rdgGrp>
  </app>
  
  <app>
      <rdgGrp n="['i']">
          <rdg wit="f1818">I</rdg>
          <rdg wit="f1823">I</rdg>
          <rdg wit="fThomas">I</rdg>
          <rdg wit="f1831">I</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge these apps:

  ```xml
  <app>
      <rdgGrp n="['hiding-places.']">
          <rdg wit="f1823">hiding-places.</rdg>
          <rdg wit="f1831">hiding-places.</rdg>
      </rdgGrp>
      <rdgGrp n="['most', 'secret']">
          <rdg wit="fMS">&lt;lb n="c56-0040__main__18"/&gt;most secret</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['hiding']">
          <rdg wit="f1818">hiding</rdg>
          <rdg wit="fThomas">hiding</rdg>
          <rdg wit="fMS">hiding</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['places', '&lt;del&gt;. but&lt;/del&gt;']">
          <rdg wit="fMS">places &lt;del rend="strikethrough" xml:id="c56-0040__main__d5e8633"&gt;.
              But&lt;/del&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['places.']">
          <rdg wit="f1818">places.</rdg>
          <rdg wit="fThomas">places.</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['this']">
          <rdg wit="f1818">this</rdg>
          <rdg wit="f1823">this</rdg>
          <rdg wit="fThomas">this</rdg>
          <rdg wit="f1831">this</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['one', 'pursuit.', 'it', 'was', 'indeed']">
          <rdg wit="f1818">one pursuit. It was indeed</rdg>
          <rdg wit="f1823">one pursuit. It was indeed</rdg>
          <rdg wit="fThomas">one pursuit. It was indeed</rdg>
          <rdg wit="f1831">one pursuit. It was indeed</rdg>
          <rdg wit="fMS">one &lt;lb n="c56-0040__main__29"/&gt;pursuit. It was indeed</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['but']">
          <rdg wit="f1818">but</rdg>
          <rdg wit="f1823">but</rdg>
          <rdg wit="fThomas">but</rdg>
          <rdg wit="f1831">but</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['charnel']">
          <rdg wit="f1818">charnel</rdg>
          <rdg wit="fThomas">charnel</rdg>
          <rdg wit="fMS">&lt;lb n="c56-0041__main__4"/&gt;Charnel</rdg>
      </rdgGrp>
      <rdgGrp n="['charnel-houses;']">
          <rdg wit="f1823">charnel-houses;</rdg>
          <rdg wit="f1831">charnel-houses;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['houses']">
          <rdg wit="fMS">houses</rdg>
      </rdgGrp>
      <rdgGrp n="['houses;']">
          <rdg wit="f1818">houses;</rdg>
          <rdg wit="fThomas">houses;</rdg>
      </rdgGrp>
  </app>
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
      <rdgGrp n="['disturbed,']">
          <rdg wit="f1818">disturbed,</rdg>
          <rdg wit="f1823">disturbed,</rdg>
          <rdg wit="fThomas">disturbed,</rdg>
          <rdg wit="f1831">disturbed,</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
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
      <rdgGrp n="['tremendous']">
          <rdg wit="f1818">tremendous</rdg>
          <rdg wit="f1823">tremendous</rdg>
          <rdg wit="fThomas">tremendous</rdg>
          <rdg wit="f1831">tremendous</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['from', 'all']">
          <rdg wit="f1818">from all</rdg>
          <rdg wit="f1823">from all</rdg>
          <rdg wit="fThomas">from all</rdg>
          <rdg wit="f1831">from all</rdg>
          <rdg wit="fMS">&lt;lb n="c56-0041__main__8"/&gt;from all</rdg>
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

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['with', 'loathing']">
          <rdg wit="f1818">with loathing</rdg>
          <rdg wit="f1823">with loathing</rdg>
          <rdg wit="fThomas">with loathing</rdg>
          <rdg wit="f1831">with loathing</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['from', 'my']">
          <rdg wit="f1818">from my</rdg>
          <rdg wit="f1823">from my</rdg>
          <rdg wit="fThomas">from my</rdg>
          <rdg wit="f1831">from my</rdg>
          <rdg wit="fMS">from my</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['withered', 'before', 'my', 'work', 'drew', 'near']">
          <rdg wit="f1818">withered before my work drew near</rdg>
          <rdg wit="f1823">withered before my work drew near</rdg>
          <rdg wit="fThomas">withered before my work drew near</rdg>
          <rdg wit="f1831">withered before my work drew near</rdg>
          <rdg wit="fMS">withered before my work drew &lt;lb n="c56-0044__main__3"/&gt;near</rdg>
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

- [x] Thomas has a long sentence in del and add, which leads to many apps with less than 5 rdgs:

  - wrapping with longToken in 1831:

    ```xml
    <longToken>the fall of a leaf startled me, and I shunned my
        fellow-creatures as if I had been guilty of a crime. Sometimes I grew alarmed at the
        wreck I perceived that I had become; the energy of my purpose alone sustained me: my
        labours would soon end,</longToken>
    ```

  - in 1818:

    ```xml
    <longToken>a disease that I regretted
        the more because I had hitherto en<pb xml:id="F1818_v1_108" n="096"/>joyed most
        excellent health, and had always boasted of the firmness of my nerves.</longToken>
    ```

  - in 1823:

    ```xml
    <longToken>a disease that I regretted the
        more because I had hitherto enjoyed most excellent health, and had always boasted <pb xml:id="F1823_v1_115" n="96"/>of the firmness of my nerves.</longToken>
    ```

  - in MS:

    ```xml
    <longToken>a <del rend="strikethrough" xml:id="c56-0044__main__d5e9438">fever</del> a <w ana="start"/>dis<lb n="c56-0044__main__14"/>ease<w ana="end"/> I regretted  <sga-add hand="#pbs" place="superlinear" sID="c56-0044__main__d5e9448"/>the <sga-add eID="c56-0044__main__d5e9448"/> more because I had  
        <lb n="c56-0044__main__15"/>hitherto enjoyed excellent health &amp;  
        <lb n="c56-0044__main__16"/>
        <del rend="strikethrough" xml:id="c56-0044__main__d5e9455">my nerves</del>
        <del rend="strikethrough" xml:id="c56-0044__main__d5e9458">were fi</del> had always  
        <lb n="c56-0044__main__17"/>boasted of  
        <mod sID="c56-0044__main__d5e9464"/>
        <mdel>my</mdel>
        <sga-add hand="#pbs" place="superlinear" sID="c56-0044__main__d5e9468"/>the <sga-add eID="c56-0044__main__d5e9468"/>
        <mod eID="c56-0044__main__d5e9464"/>  firm <sga-add hand="#pbs" place="intralinear" sID="c56-0044__main__d5e9472"/>ness <sga-add eID="c56-0044__main__d5e9472"/>
        <mod sID="c56-0044__main__d5e9475"/>
        <sga-add place="sublinear" sID="c56-0044__main__d5e9477"/>
        <metamark function="insert">^</metamark>
        <sga-add eID="c56-0044__main__d5e9477"/>
        <sga-add hand="#pbs" place="superlinear" sID="c56-0044__main__d5e9483"/>of my <sga-add eID="c56-0044__main__d5e9483"/>
        <mod eID="c56-0044__main__d5e9475"/>  nerves.</longToken>
    ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['i', 'improved']">
          <rdg wit="f1818">I improved</rdg>
          <rdg wit="f1823">I improved</rdg>
          <rdg wit="fThomas">I improved</rdg>
          <rdg wit="fMS">I improved</rdg>
      </rdgGrp>
      <rdgGrp n="['my', 'progress', 'was', 'rapid.']">
          <rdg wit="f1831">my progress was rapid.</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['rapidly .', '&lt;del&gt;it&lt;/del&gt;']">
          <rdg wit="fMS">&lt;w ana="start"/&gt;rapid&lt;lb n="c56-0032__main__3"/&gt;ly&lt;w
              ana="end"/&gt;. &lt;del rend="strikethrough"
              xml:id="c56-0032__main__d5e6351"&gt;It&lt;/del&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['rapidly.']">
          <rdg wit="f1818">ra&lt;pb xml:id="F1818_v1_092" n="080"/&gt;pidly.</rdg>
          <rdg wit="f1823">ra&lt;pb xml:id="F1823_v1_099" n="80"/&gt;pidly.</rdg>
          <rdg wit="fThomas">ra&lt;pb xml:id="F1818_v1_092" n="080"/&gt;pidly.</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['resolution,']">
          <rdg wit="f1818">resolution,</rdg>
          <rdg wit="f1823">resolution,</rdg>
          <rdg wit="fThomas">resolution,</rdg>
          <rdg wit="fMS">resolution,</rdg>
      </rdgGrp>
      <rdgGrp n="['soon']">
          <rdg wit="f1831">soon</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['now']">
          <rdg wit="f1818">now </rdg>
          <rdg wit="f1823">now </rdg>
          <rdg wit="fThomas">now </rdg>
          <rdg wit="fMS">&lt;sga-add eID="c56-0031__main__d5e6289"/&gt;now</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge these apps:

  ```xml
  <app>
      <rdgGrp n="['', '&lt;del&gt;these&lt;/del&gt;']">
          <rdg wit="fMS">&lt;mod sID="c56-0044__main__d5e9495"/&gt; &lt;del rend="strikethrough"
              xml:id="c56-0044__main__d5e9497"&gt;these&lt;/del&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['incipient', 'disease;']">
          <rdg wit="f1831">incipient disease;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['such']">
          <rdg wit="f1818">such</rdg>
          <rdg wit="f1823">such</rdg>
          <rdg wit="fThomas">such</rdg>
          <rdg wit="fMS">&lt;sga-add hand="#pbs" place="superlinear"
              sID="c56-0044__main__d5e9500"/&gt;such</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['sym', '&lt;del&gt;p&lt;/del&gt;', 'toms']">
          <rdg wit="fMS">&lt;sga-add eID="c56-0044__main__d5e9500"/&gt;&lt;mod
              eID="c56-0044__main__d5e9495"/&gt;&lt;w ana="start"/&gt;sym&lt;lb
              n="c56-0044__main__20"/&gt; &lt;del rend="strikethrough"
              xml:id="c56-0044__main__d5e9508"&gt;p&lt;/del&gt; toms&lt;w ana="end"/&gt;</rdg>
      </rdgGrp>
      <rdgGrp n="['symptoms;']">
          <rdg wit="f1818">symptoms;</rdg>
          <rdg wit="f1823">symptoms;</rdg>
          <rdg wit="fThomas">symptoms;</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs

  ```xml
  <app>
      <rdgGrp
              n="['which', 'procured', 'me', 'great', 'esteem', 'and', 'admiration', 'at', 'the', 'university.', 'when', 'i']">
          <rdg wit="f1818">which procured me great esteem and admiration at the university. When
              I</rdg>
          <rdg wit="f1823">which procured me great esteem and admiration at the university. When
              I</rdg>
          <rdg wit="fThomas">which procured me great esteem and admiration at the university. When
              I</rdg>
          <rdg wit="f1831">which procured me great esteem and admiration at the university. When
              I</rdg>
          <rdg wit="fMS">which &lt;w ana="start"/&gt;pro&lt;lb
              n="c56-0032__main__29"/&gt;cured&lt;w ana="end"/&gt; me great esteem and admiration
              &lt;lb n="c56-0032__main__30"/&gt;at the university. When I</rdg>
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

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['yet']">
          <rdg wit="f1818">yet</rdg>
          <rdg wit="f1823">yet</rdg>
          <rdg wit="fThomas">yet</rdg>
          <rdg wit="f1831">yet</rdg>
          <rdg wit="fMS">&lt;lb n="c56-0033__main__14"/&gt;Yet</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['with']">
          <rdg wit="f1818">with</rdg>
          <rdg wit="f1823">with</rdg>
          <rdg wit="fThomas">with</rdg>
          <rdg wit="f1831">with</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['that', 'i', 'alone', 'should']">
          <rdg wit="f1818">that I alone should</rdg>
          <rdg wit="f1823">that I alone should</rdg>
          <rdg wit="fThomas">that I alone should</rdg>
          <rdg wit="f1831">that I alone should</rdg>
          <rdg wit="fMS">&lt;lb n="c56-0035__main__5"/&gt;that I alone should</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['be', 'reserved', 'to']">
          <rdg wit="f1818">be reserved to</rdg>
          <rdg wit="f1823">be reserved to</rdg>
          <rdg wit="fThomas">be reserved to</rdg>
          <rdg wit="f1831">be reserved to</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['the', 'stages', 'of']">
          <rdg wit="f1818">the stages of</rdg>
          <rdg wit="f1823">the stages of</rdg>
          <rdg wit="fThomas">the stages of</rdg>
          <rdg wit="f1831">the stages of</rdg>
          <rdg wit="fMS">the &lt;lb n="c56-0035__main__13"/&gt;stages of</rdg>
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

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['to', 'be']">
          <rdg wit="f1818">to be</rdg>
          <rdg wit="f1823">to be</rdg>
          <rdg wit="fThomas">to be</rdg>
          <rdg wit="f1831">to be</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['the', 'world,', 'than', 'he']">
          <rdg wit="f1818">the world, than he</rdg>
          <rdg wit="f1823">the world, than he</rdg>
          <rdg wit="fThomas">the world, than he</rdg>
          <rdg wit="f1831">the world, than he</rdg>
          <rdg wit="fMS">the world, than he</rdg>
      </rdgGrp>
  </app>
  ```

- [x] merge two apps:

  ```xml
  <app>
      <rdgGrp n="['theirs.']">
          <rdg wit="f1823">theirs.</rdg>
          <rdg wit="f1831">theirs.</rdg>
      </rdgGrp>
      <rdgGrp n="['their’s.']">
          <rdg wit="f1818">their’s.</rdg>
          <rdg wit="fThomas">their’s.</rdg>
      </rdgGrp>
      <rdgGrp
              n="['thiers', '', '&lt;del&gt;and&lt;/del&gt;', 'pur', 'sueing', '', '&lt;mdel&gt;my&lt;/mdel&gt;']">
          <rdg wit="fMS">&lt;lb n="c56-0039__left_margin__3"/&gt;thiers &lt;anchor
              xml:id="c56-0039.08"/&gt;&lt;sga-add eID="c56-0039__main__d5e8456"/&gt;&lt;mod
              eID="c56-0039__main__d5e8454"/&gt; &lt;del rend="strikethrough"
              xml:id="c56-0039__main__d5e8476"&gt;And&lt;/del&gt; pur &lt;lb
              n="c56-0039__main__28"/&gt;sueing &lt;mod sID="c56-0039__main__d5e8481"/&gt;
              &lt;mdel&gt;my&lt;/mdel&gt;</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['pursuing']">
          <rdg wit="f1818">Pursuing</rdg>
          <rdg wit="f1823">Pursuing</rdg>
          <rdg wit="fThomas">Pursuing</rdg>
          <rdg wit="f1831">Pursuing</rdg>
      </rdgGrp>
  </app>
  ```

- [x] app with less than 5 rdgs:

  ```xml
  <app>
      <rdgGrp n="['i', 'was', 'oppressed', 'by']">
          <rdg wit="f1818">I was oppressed by</rdg>
          <rdg wit="f1823">I was oppressed by</rdg>
          <rdg wit="fThomas">I was oppressed by</rdg>
          <rdg wit="f1831">I was oppressed by</rdg>
      </rdgGrp>
  </app>
  <app>
      <rdgGrp n="['a', 'slow']">
          <rdg wit="f1818">a slow</rdg>
          <rdg wit="f1823">a slow</rdg>
          <rdg wit="fThomas">a slow</rdg>
          <rdg wit="f1831">a slow</rdg>
          <rdg wit="fMS">a slow</rdg>
      </rdgGrp>
  </app>
  ```
**ebb checking**:
- [x] correct 1831 base text error re "repulsivepedantry" (documented on PR)
- [x] Respace/longToken to pull MS token together around ever y:
```xml
	<app>
		<rdgGrp n="['ever', 'y', '']">
			<rdg wit="fMS">ever &lt;sga-add hand="#pbs" place="intralinear"
				sID="c56-0031__main__d5e6151"/&gt;y &lt;sga-add
				eID="c56-0031__main__d5e6151"/&gt;</rdg>
		</rdgGrp>
		<rdgGrp n="['every']">
			<rdg wit="f1818">every</rdg>
			<rdg wit="f1823">every</rdg>
			<rdg wit="fThomas">every</rdg>
			<rdg wit="f1831">every</rdg>
		</rdgGrp>
	</app>
```
- [x] Misalignment of 1831 around "fluctuating and uncertain": extend longToken a little further.
- [x] Watch for two caret passages (strength become)
- [x] Chapter 6 aligned only to paragraph break. Added longToken to include it with "When I found"

  